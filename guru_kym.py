import pandas as pd
import numpy as np
import plotly.graph_objects as go
from base_engine import BaseEngine
from preload_conf import *
from conf import *
from util import shrink_date_str, get_idx_by_date, touch_file
from guru_predict import load_prediction
from guru_wizard import PREDICT_MODE, valid_dates
from x_financial_statements import Financial_Statements


def is_x(cell):
    return 'X' in cell


def is_just_x(cell):
    return 'X______' in cell


def recall(cell):
    return is_x(cell)


def negative(cell):
    return is_just_x(cell)


def positive(cell):
    return is_x(cell) and not is_just_x(cell)


def is_target(cell):
    return 'U' in cell or 'D' in cell


def display_stock(stock_name, hit_dates: list):
    if not hit_dates:
        return

    spectrum = [
        (period_1y(), args_1y_guru()),
        (period_4y(), args_4y()),
    ]

    for (from_date, to_date, interval), args in spectrum:
        base_engine = BaseEngine(stock_name, from_date, to_date, interval)
        base_engine.build_graph(**args)

        stock_df, fig = base_engine.stock_df, base_engine.fig

        y = []
        for date in hit_dates:
            idx = get_idx_by_date(stock_df, date)
            y.append(stock_df['close'].loc[idx])

        fig.add_trace(
            go.Scatter(
                name='hit', x=hit_dates, y=y,
                mode='markers',
                marker=dict(color='red', size=8, symbol='star'),
            ),
            row=1, col=1,
        )

        fig.show()


def build_report(target_dates: list, predict_mode: str) -> dict:
    kym_report = {}

    # load predictions
    prediction = load_prediction(predict_mode)

    for stock_name in ALL:
        kym_report[stock_name] = {}
        hit_dates = []

        (from_date, to_date, interval), args = period_1y(), args_1y_guru()

        base_engine = BaseEngine(stock_name, from_date, to_date, interval)
        base_engine.build_graph(**args)

        # load context
        stock_df, context = base_engine.stock_df, base_engine.context

        for date in target_dates:
            if date not in stock_df['Date'].apply(shrink_date_str).values:
                print(f'kym {stock_name} {date} is out of range')
                continue

            idx = get_idx_by_date(stock_df, date)
            close = stock_df['close'].loc[idx]
            min_close = stock_df['close'].loc[idx:idx + 15].min()
            max_close = stock_df['close'].loc[idx:idx + 15].max()

            # predict
            cell = 'X' if date in prediction.get(stock_name, []) else '_'

            # Up
            for key in ['will spike', 'will shoot up']:
                hits = [shrink_date_str(d) for d in context.get(key, [])]
                cell += 'U' if date in hits else '_'

            cell += 'U' if max_close / close - 1 > 0.1 else '_'

            # Down
            for key in ['will crash', 'will shoot down']:
                hits = [shrink_date_str(d) for d in context.get(key, [])]
                cell += 'D' if date in hits else '_'

            cell += 'D' if 1 - min_close / close > 0.1 else '_'

            # FS
            cell += 'F' if date in Financial_Statements.get(stock_name, []) else '_'

            kym_report[stock_name][date] = cell

            if positive(cell):
                hit_dates.append(date)

        display_stock(stock_name, hit_dates)

    return kym_report


def build_df(kym_report: dict) -> pd.DataFrame:
    kym_df = pd.DataFrame(kym_report).T

    nature_rates = []
    model_rates = []

    for date in kym_df.columns:
        count_all = kym_df[date].notna().sum()
        count_target = kym_df[date].dropna().apply(is_target).sum()
        nature_rate = count_target / count_all if count_all > 0 else 0

        count_hit = kym_df[date].dropna().apply(is_x).sum()
        count_fail = kym_df[date].dropna().apply(is_just_x).sum()
        model_rate = (1 - count_fail / count_hit) if count_hit > 0 else 0

        nature_rates.append(f'{nature_rate:.2f}/{count_all}')
        model_rates.append(f'{model_rate:.2f}/{count_hit}')

    kym_df.loc['nature_rates'] = nature_rates
    kym_df.loc['model_rates'] = model_rates
    return kym_df


def kym(kym_df: pd.DataFrame, predict_mode: str):
    nature_rates = []
    nature_hits = []

    model_rates = []
    model_hits = []

    for date in kym_df.columns[:-6]:
        nature_rate, nature_hit = kym_df.loc['nature_rates'][date].split('/')
        nature_rate, nature_hit = float(nature_rate), int(nature_hit)

        nature_rates.append(nature_rate)
        nature_hits.append(nature_hit)

        model_rate, model_hit = kym_df.loc['model_rates'][date].split('/')
        model_rate, model_hit = float(model_rate), int(model_hit)

        model_rates.append(model_rate)
        model_hits.append(model_hit)

    # 自然准确率 均值/方差
    nature_rates_avg = np.array(nature_rates).mean()
    nature_rates_std = np.array(nature_rates).std()

    # 模型准确率 均值/方差 (剔除零信号)
    filtered_rates = []
    for rate, hit in zip(model_rates, model_hits):
        if hit != 0:
            filtered_rates.append(rate)

    filtered_rates = np.array(filtered_rates)
    model_rates_avg = filtered_rates.mean()
    model_rates_std = filtered_rates.std()

    # 平均信号数
    model_hits_avg = np.array(model_hits).mean()

    # 零信号 天数
    zero_hit_days = model_hits.count(0)

    # 零准确率 天数 - 严重劣势
    # 显著劣势 天数
    # 显著优势 天数
    # 劣势 天数
    # 优势 天数
    zero_accuracy_days = 0

    significant_loss_days = 0
    significant_gain_days = 0

    loss_days = 0
    gain_days = 0

    for model_rate, model_hit, nature_rate in zip(model_rates, model_hits, nature_rates):
        if model_hit == 0:
            continue

        if model_rate == 0:
            zero_accuracy_days += 1

        if model_rate < nature_rate:
            loss_days += 1
        if model_rate < nature_rate - 0.05:
            significant_loss_days += 1

        if model_rate > nature_rate:
            gain_days += 1
        if model_rate > nature_rate + 0.05:
            significant_gain_days += 1

    with open('_kym/summary', 'a') as fd:
        print(f'KYM Report for {predict_mode}\n', file=fd)

        kym_df.loc[['nature_rates', 'model_rates']].to_csv(fd, mode='a', sep='\t')

        print('', file=fd)
        print(f'评估天数 : {len(model_hits)}', file=fd)
        print(f'自然准确率 mean: {nature_rates_avg:.2%}, std: {nature_rates_std:.2%}', file=fd)

        print(f'模型准确率 mean: {model_rates_avg:.2%}, std: {model_rates_std:.2%}', file=fd)
        print(f'准确率提升: {model_rates_avg - nature_rates_avg:.2%}', file=fd)
        print(f'平均信号数: {model_hits_avg:.2f}', file=fd)

        print(f'零信号 days: {zero_hit_days}, ratio: {zero_hit_days / len(model_hits):.2%}', file=fd)
        print(f'零准确率 days: {zero_accuracy_days}, ratio: {zero_accuracy_days / len(model_hits):.2%}', file=fd)

        print(f'显著 劣势 days: {significant_loss_days}, ratio: {significant_loss_days / len(model_hits):.2%}', file=fd)
        print(f'显著 优势 days: {significant_gain_days}, ratio: {significant_gain_days / len(model_hits):.2%}', file=fd)
        print(f'劣势 days: {loss_days}, ratio: {loss_days / len(model_hits):.2%}', file=fd)
        print(f'优势 days: {gain_days}, ratio: {gain_days / len(model_hits):.2%}', file=fd)
        print('\n--------------------\n', file=fd)


if __name__ == '__main__':
    target_dates_ = valid_dates[:65]
    touch_file('_kym/summary')

    for predict_mode_ in PREDICT_MODE:
        output_file = f'_kym/{predict_mode_}.csv'

        kym_report_ = build_report(target_dates_, predict_mode_)
        kym_df_ = build_df(kym_report_)

        print(kym_df_)
        kym_df_.to_csv(output_file)

        kym_df_ = pd.read_csv(output_file, index_col=0)
        kym(kym_df_, predict_mode_)
