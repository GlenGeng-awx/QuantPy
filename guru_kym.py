import pandas as pd
import json
from base_engine import BaseEngine
from preload_conf import *
from conf import *
from util import shrink_date_str
from guru_predict import load_prediction
from guru_wizard import PREDICT_MODE, VALID_DATES
from guru import models, n0_common, BOX, TREND
from financial_statements import Financial_Statements


def is_hit(cell):
    return 'X' in cell


def is_target(cell):
    return 'H' in cell


def is_success(cell):
    return is_hit(cell) and is_target(cell)


def get_summary_file(model_name: str):
    return f'{model_name}/_kym/_summary'


def get_stock_file(stock_name: str, model_name: str):
    return f'{model_name}/_kym/{stock_name}.txt'


# kym_report: date -> predict_mode -> cell
def build_report(stock_name: str, target_dates: list, model_name: str) -> pd.DataFrame:
    kym_report = {}

    to_date = target_dates[-1]
    (from_date, to_date, interval), args = period_predict(to_date), args_1y_guru()

    base_engine = BaseEngine(stock_name, from_date, to_date, interval)
    base_engine.build_graph(**args)

    # load context
    stock_df, context = base_engine.stock_df, base_engine.context

    for date in target_dates:
        if date not in stock_df['Date'].apply(shrink_date_str).values:
            print(f'kym {stock_name} {date} is out of range')
            continue

        kym_report[date] = {}

        cell = ''

        # Target
        for target in models[model_name]:
            for mode in [n0_common.TRAIN, n0_common.RECALL]:
                key = n0_common.get_key(target.TARGET, mode)
                dates = [shrink_date_str(d) for d in context.get(key, [])]
                cell += 'H' if date in dates else '_'

        # FS
        cell += 'F' if date in Financial_Statements.get(stock_name, []) else '_'

        # Predict
        for predict_mode in PREDICT_MODE:
            prediction = load_prediction(predict_mode, model_name)
            hit = 'X' if date in prediction.get(stock_name, []) else '_'
            kym_report[date][predict_mode] = hit + cell

    return pd.DataFrame(kym_report).T


def summarize(kym_df: pd.DataFrame):
    nature_rates = []
    model_rates = []
    ranking = []

    for predict_mode in kym_df.columns:
        # ignore last 15d, total 85d
        model_results = kym_df[predict_mode].iloc[-100:-15].dropna()

        count_all = model_results.count()
        count_target = model_results.apply(is_target).sum()
        nature_rate = count_target / count_all if count_all > 0 else 0

        count_hit = model_results.apply(is_hit).sum()
        count_success = model_results.apply(is_success).sum()
        model_rate = count_success / count_hit if count_hit > 0 else 0

        nature_rates.append(f'{nature_rate:.2f}/{count_all}')
        model_rates.append(f'{model_rate:.2f}/{count_hit}')
        ranking.append((model_rate, count_hit, nature_rate, count_all, predict_mode))

    kym_df.loc['nature_rates'] = nature_rates
    kym_df.loc['model_rates'] = model_rates

    ranking.sort(key=lambda x: (-x[0], -x[1]))

    ranking = [
        f'{predict_mode} {model_rate:.2f} {count_hit} {nature_rate:.2f} {count_all}'
        for model_rate, count_hit, nature_rate, count_all, predict_mode in ranking
    ]

    return kym_df, ranking


# return list of (predict_mode, model_rate, count_hit, nature_rate, count_all)
def filter_predict_modes(stock_name: str, model_name: str) -> list:
    summary_file = get_summary_file(model_name)
    summary = json.load(open(summary_file, 'r'))
    records = summary.get(stock_name, [])

    predict_modes = []

    for record in records:
        predict_mode, model_rate, count_hit, nature_rate, count_all = record.split()

        model_rate, count_hit = float(model_rate), int(count_hit)
        nature_rate, count_all = float(nature_rate), int(count_all)

        if model_rate >= 0.5 and model_rate > nature_rate:
            predict_modes.append((predict_mode, model_rate, count_hit, nature_rate, count_all))

    return predict_modes


if __name__ == '__main__':
    target_dates_ = VALID_DATES
    model_name_ = BOX
    # model_name_ = TREND
    summary_ = {}

    for stock_name_ in ALL:
        kym_df_ = build_report(stock_name_, target_dates_, model_name_)
        kym_df_, ranking_ = summarize(kym_df_)

        summary_[stock_name_] = ranking_
        print(kym_df_, file=open(get_stock_file(stock_name_, model_name_), 'w'))

    print(json.dumps(summary_, indent=2), file=open(get_summary_file(model_name_), 'w'))

    for stock_name_ in ALL:
        predict_modes_ = filter_predict_modes(stock_name_, model_name_)
        print(stock_name_, predict_modes_)
