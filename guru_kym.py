import pandas as pd
import json
from base_engine import BaseEngine
from preload_conf import *
from conf import *
from util import shrink_date_str, get_idx_by_date
from guru_predict import load_prediction
from guru_wizard import PREDICT_MODE, VALID_DATES
from financial_statements import Financial_Statements


def is_x(cell):
    return 'X' in cell


def is_just_x(cell):
    return 'X______' in cell


def is_target(cell):
    return 'U' in cell or 'D' in cell


def get_summary_file():
    return '_kym/_summary'


def get_txt_file(stock_name: str):
    return f'_kym/{stock_name}.txt'


# kym_report: date -> predict_mode -> cell
def build_report(stock_name: str, target_dates: list) -> pd.DataFrame:
    kym_report = {}

    (from_date, to_date, interval), args = period_1y(), args_1y_guru()

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

        # Up
        for key in ['will spike', 'will shoot up', 'will spike p80', 'will shoot up p80']:
            hits = [shrink_date_str(d) for d in context.get(key, [])]
            cell += 'U' if date in hits else '_'

        # Down
        for key in ['will crash', 'will shoot down', 'will crash p80', 'will shoot down p80']:
            hits = [shrink_date_str(d) for d in context.get(key, [])]
            cell += 'D' if date in hits else '_'

        # FS
        cell += 'F' if date in Financial_Statements.get(stock_name, []) else '_'

        # Predict
        for predict_mode in PREDICT_MODE:
            prediction = load_prediction(predict_mode)
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

        count_hit = model_results.apply(is_x).sum()
        count_fail = model_results.apply(is_just_x).sum()
        model_rate = (1 - count_fail / count_hit) if count_hit > 0 else 0

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
def filter_predict_modes(stock_name: str) -> list:
    summary = json.load(open(get_summary_file(), 'r'))
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
    summary_ = {}

    for stock_name_ in ALL:
        kym_df_ = build_report(stock_name_, target_dates_)
        kym_df_, ranking_ = summarize(kym_df_)

        summary_[stock_name_] = ranking_
        print(kym_df_, file=open(get_txt_file(stock_name_), 'w'))

    print(json.dumps(summary_, indent=2), file=open(get_summary_file(), 'w'))

    for stock_name_ in ALL:
        predict_modes_ = filter_predict_modes(stock_name_)
        print(stock_name_, predict_modes_)
