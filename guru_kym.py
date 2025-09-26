import pandas as pd
import numpy as np
import plotly.graph_objects as go
from multiprocessing import Pool
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

        # display_stock(stock_name, hit_dates)

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


def model_score(
        model_acc,          # 模型准确率
        model_std,          # 模型标准差
        nature_acc,         # 自然准确率
        nature_std,         # 自然标准差
        avg_signal,         # 平均信号数
        zero_signal_ratio,  # 零信号天数占比
        zero_acc_ratio,     # 0%准确率天数占比
        loss_ratio,         # 劣势天数（< baseline）占比
        strong_loss_ratio,  # 显著劣势（< baseline-0.05）占比
        gain_ratio,         # 优势天数（> baseline）占比
        strong_gain_ratio,  # 显著优势（> baseline+0.05）占比
):
    # 1. 准确率提升（最多40分）：每提高1%得4分，提升10%及以上满分
    score = 40
    acc_improve = max(0, model_acc - nature_acc)
    acc_score = min(score, acc_improve / 0.10 * score)

    # 2. 标准差奖励（最多20分）：标准差≤3×基线满分，≥6×基线0分，线性评分
    score = 20
    std_low, std_high = nature_std * 3, nature_std * 6
    if model_std <= std_low:
        std_score = score
    elif model_std >= std_high:
        std_score = 0
    else:
        std_score = (std_high - model_std) / (std_high - std_low) * score

    # 3. 平均信号（最多5分）：5~10之间满分，超出或不足每1扣2分，最小0分
    score = 5
    if 5 <= avg_signal <= 10:
        avg_signal_score = score
    elif avg_signal < 5:
        avg_signal_score = max(0, score - (5 - avg_signal) * 2)
    else:  # avg_signal > 10
        avg_signal_score = max(0, score - (avg_signal - 10) * 2)

    # 4. 零信号惩罚（最多5分）：每1%零信号天数扣1分，5%以上0分
    score = 5
    zero_signal_score = max(0, score - zero_signal_ratio * 100)

    # 5. 0%准确率惩罚（最多10分）：每1%占比扣1分，10%以上0分
    score = 10
    zero_acc_score = max(0, score - zero_acc_ratio * 100)

    # 6. 劣势天数惩罚（最多4分）：≥50%全扣完，线性递减
    score = 4
    loss_score = max(0, score - loss_ratio / 0.5 * score)

    # 7. 显著劣势天数惩罚（最多6分）：≥30%全扣完，线性递减
    score = 6
    strong_loss_score = max(0, score - strong_loss_ratio / 0.3 * score)

    # 8. 优势天数奖励（最多4分）：≥70%满分，线性递增
    score = 4
    gain_score = min(score, gain_ratio / 0.7 * score)

    # 9. 显著优势天数奖励（最多6分）：≥50%满分，线性递增
    score = 6
    strong_gain_score = min(score, strong_gain_ratio / 0.5 * score)

    detail = {
        'acc_score': acc_score,
        'std_score': std_score,
        'avg_signal_score': avg_signal_score,
        'zero_signal_score': zero_signal_score,
        'zero_acc_score': zero_acc_score,
        'loss_score': loss_score,
        'strong_loss_score': strong_loss_score,
        'gain_score': gain_score,
        'strong_gain_score': strong_gain_score,
    }

    total = round(sum(detail.values()), 2)
    detail = {key: float(round(value, 2)) for key, value in detail.items()}

    return total, detail


def kym(kym_df: pd.DataFrame, predict_mode: str) -> (float, tuple):
    nature_rates = []
    nature_signals = []

    model_rates = []
    model_signals = []

    for date in kym_df.columns[-75:-15]:
        nature_rate, nature_signal = kym_df.loc['nature_rates'][date].split('/')
        nature_rate, nature_signal = float(nature_rate), int(nature_signal)

        nature_rates.append(nature_rate)
        nature_signals.append(nature_signal)

        model_rate, model_signal = kym_df.loc['model_rates'][date].split('/')
        model_rate, model_signal = float(model_rate), int(model_signal)

        model_rates.append(model_rate)
        model_signals.append(model_signal)

    # 自然准确率 均值/方差
    nature_acc = np.array(nature_rates).mean()
    nature_std = np.array(nature_rates).std()

    # 模型准确率 均值/方差 (剔除零信号)
    filtered_rates = []
    for rate, signal in zip(model_rates, model_signals):
        if signal != 0:
            filtered_rates.append(rate)

    model_acc = np.array(filtered_rates).mean()
    model_std = np.array(filtered_rates).std()

    # 平均信号数
    avg_signal = np.array(model_signals).mean()

    # 零信号 天数
    zero_signal_days = model_signals.count(0)

    # 有效天数（非零信号天数），所有相关比率均以此为分母
    valid_days = len(model_signals) - zero_signal_days

    # 零准确率 天数 - 严重劣势
    # 显著劣势 天数
    # 显著优势 天数
    # 劣势 天数
    # 优势 天数
    zero_acc_days = 0

    strong_loss_days = 0
    strong_gain_days = 0

    loss_days = 0
    gain_days = 0

    for model_rate, model_signal, nature_rate in zip(model_rates, model_signals, nature_rates):
        if model_signal == 0:
            continue

        if model_rate == 0:
            zero_acc_days += 1

        if model_rate < nature_rate:
            loss_days += 1
        if model_rate < nature_rate - 0.05:
            strong_loss_days += 1

        if model_rate > nature_rate:
            gain_days += 1
        if model_rate > nature_rate + 0.05:
            strong_gain_days += 1

    score, detail = model_score(
        model_acc=model_acc,
        model_std=model_std,
        nature_acc=nature_acc,
        nature_std=nature_std,
        avg_signal=avg_signal,
        zero_signal_ratio=zero_signal_days / len(model_signals),
        zero_acc_ratio=zero_acc_days / valid_days,
        loss_ratio=loss_days / valid_days,
        strong_loss_ratio=strong_loss_days / valid_days,
        gain_ratio=gain_days / valid_days,
        strong_gain_ratio=strong_gain_days / valid_days,
    )

    with open('_kym/summary', 'a') as fd:
        print(f'KYM Report for {predict_mode}\n', file=fd)

        kym_df.loc[['nature_rates', 'model_rates']].to_csv(fd, mode='a', sep='\t')

        print('', file=fd)
        print(f'自然准确率 mean: {nature_acc:.2%}, std: {nature_std:.2%}', file=fd)
        print(f'评估天数: {len(model_signals)}，有效天数: {valid_days}', file=fd)

        print(f'模型准确率 mean: {model_acc:.2%}, std: {model_std:.2%}', file=fd)
        print(f'准确率提升: {model_acc - nature_acc:.2%}', file=fd)
        print(f'平均信号数: {avg_signal:.2f}', file=fd)

        print(f'零信号 days: {zero_signal_days}, ratio: {zero_signal_days / len(model_signals):.2%}', file=fd)
        print(f'零准确率 days: {zero_acc_days}, ratio: {zero_acc_days / valid_days:.2%}', file=fd)

        print(f'显著 劣势 days: {strong_loss_days}, ratio: {strong_loss_days / valid_days:.2%}', file=fd)
        print(f'显著 优势 days: {strong_gain_days}, ratio: {strong_gain_days / valid_days:.2%}', file=fd)
        print(f'劣势 days: {loss_days}, ratio: {loss_days / valid_days:.2%}', file=fd)
        print(f'优势 days: {gain_days}, ratio: {gain_days / valid_days:.2%}', file=fd)
        print(f'得分 {score} with detail {detail}', file=fd)
        print('\n--------------------\n', file=fd)

    return score, detail


def preprocess(predict_mode: str):
    target_dates = valid_dates

    kym_report = build_report(target_dates, predict_mode)
    kym_df = build_df(kym_report)

    output_file = f'_kym/{predict_mode}.csv'
    kym_df.to_csv(output_file)


if __name__ == '__main__':
    with Pool(processes=12) as pool:
        pool.map(preprocess, PREDICT_MODE)

    touch_file('_kym/summary')
    rank = []

    for predict_mode_ in PREDICT_MODE:
        output_file_ = f'_kym/{predict_mode_}.csv'
        kym_df_ = pd.read_csv(output_file_, index_col=0)

        score_, detail_ = kym(kym_df_, predict_mode_)
        rank.append((predict_mode_, score_, detail_))

    print('KYM Rank:')
    rank.sort(key=lambda x: x[1], reverse=True)
    for mode, score_, detail_ in rank:
        print(f'{mode}\t score:{score_}, detail: {detail_}')
