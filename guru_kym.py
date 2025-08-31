import pandas as pd
import plotly.graph_objects as go
from base_engine import BaseEngine
from preload_conf import *
from conf import *
from util import shrink_date_str, get_idx_by_date
from guru_train import valid_dates
from guru_predict import load_prediction
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


def show(stock_name, hit_dates: list):
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


def kym():
    target_dates = valid_dates

    # step 1
    kym_report = {}

    # load predictions
    prediction = load_prediction()

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

        show(stock_name, hit_dates)

    # step 2
    kym_df = pd.DataFrame(kym_report).T

    correct_rates = []

    for date in kym_df.columns:
        count_all = kym_df[date].dropna().apply(is_x).sum()
        count_fail = kym_df[date].dropna().apply(is_just_x).sum()

        correct_rate = (1 - count_fail / count_all) if count_all > 0 else None
        correct_rates.append(f'{correct_rate:.2f}/{count_all}')

    kym_df.loc['correct_rates'] = correct_rates

    print(kym_df)


if __name__ == '__main__':
    kym()
