import json
import pandas as pd
import plotly.graph_objects as go
from base_engine import BaseEngine
from preload_conf import *
from conf import *
from util import shrink_date_str, get_idx_by_date
from guru_train import valid_dates
from x_financial_statements import Financial_Statements


def is_x(cell_):
    return 'X' in cell_


def is_just_x(cell_):
    return 'X______' in cell_


def recall(cell_):
    return is_x(cell_)


def negative(cell_):
    return is_just_x(cell_)


def positive(cell_):
    return is_x(cell_) and not is_just_x(cell_)


def show(stock_name_, hit_dates_: list):
    if not hit_dates_:
        return

    spectrum = [
        (period_4y(), args_4y()),
        (period_1y(), args_1y_guru()),
    ]

    for (from_date_, to_date_, interval_), args_ in spectrum:
        base_engine_ = BaseEngine(stock_name_, from_date_, to_date_, interval_)
        base_engine_.build_graph(**args_)

        stock_df_, fig_ = base_engine_.stock_df, base_engine_.fig

        y = []
        for date_ in hit_dates_:
            idx_ = get_idx_by_date(stock_df_, date_)
            y.append(stock_df_['close'].loc[idx_])

        fig_.add_trace(
            go.Scatter(
                name='hit', x=hit_dates_, y=y,
                mode='markers',
                marker=dict(color='red', size=8, symbol='star'),
            ),
            row=1, col=1,
        )

        fig_.show()


dates = valid_dates

# step 1
kym_report = {}

# load predictions
with open("_predict", "r") as f:
    prediction = json.load(f)

for stock_name in ALL:
    kym_report[stock_name] = {}
    hit_dates = []

    (from_date, to_date, interval), args = period_1y(), args_1y_guru()

    base_engine = BaseEngine(stock_name, from_date, to_date, interval)
    base_engine.build_graph(**args)

    # load context
    stock_df, context = base_engine.stock_df, base_engine.context

    for date in dates:
        idx = get_idx_by_date(stock_df, date)
        close = stock_df['close'].loc[idx]
        min_close = stock_df['close'].loc[idx:idx + 15].min()
        max_close = stock_df['close'].loc[idx:idx + 15].max()

        # predict
        cell = 'X' if date in prediction[stock_name] else '_'

        # up
        for key in ['will spike', 'will shoot up']:
            hits = [shrink_date_str(d) for d in context.get(key, [])]
            cell += 'U' if date in hits else '_'

        cell += 'U' if max_close / close - 1 > 0.1 else '_'

        # down
        for key in ['will crash', 'will shoot down']:
            hits = [shrink_date_str(d) for d in context.get(key, [])]
            cell += 'D' if date in hits else '_'

        cell += 'D' if 1 - min_close / close > 0.1 else '_'

        # fs
        cell += 'F' if date in Financial_Statements.get(stock_name, []) else '_'

        kym_report[stock_name][date] = cell

        if positive(cell):
            hit_dates.append(date)

    show(stock_name, hit_dates)

# step 2
kym_df = pd.DataFrame(kym_report).T

correct_rates = []

for date in kym_df.columns:
    count_all = kym_df[date].apply(is_x).sum()
    count_fail = kym_df[date].apply(is_just_x).sum()

    correct_rate = (1 - count_fail / count_all) if count_all > 0 else None
    correct_rates.append(f'{correct_rate:.2f}/{count_all}')

kym_df.loc['correct_rates'] = correct_rates

print(kym_df)
