import plotly.graph_objects as go
from base_engine import BaseEngine
from preload_conf import *
from conf import *
from util import get_idx_by_date
from guru_predict import load_prediction
from x_position import Call, Put, CLOSED_POSITIONS, ACTIVE_POSITIONS


# predict_dates : [date]
# txn_dates     : [date]
# calls         : [(date, strike_price)]
# puts          : [(date, strike_price)]
def show(stock_name, predict_dates: list, txn_dates: list, calls: list, puts: list):
    if not txn_dates:
        return

    spectrum = [
        # (period_4y(), args_4y()),
        (period_1y(), args_1y_guru()),
    ]

    for (from_date, to_date, interval), args in spectrum:
        base_engine = BaseEngine(stock_name, from_date, to_date, interval)
        base_engine.build_graph(**args)

        stock_df, fig = base_engine.stock_df, base_engine.fig

        y = []
        for date in predict_dates:
            idx = get_idx_by_date(stock_df, date)
            y.append(stock_df['close'].loc[idx])

        fig.add_trace(
            go.Scatter(
                name='predict_dates', x=predict_dates, y=y,
                mode='markers',
                marker=dict(color='blue', size=6, symbol='star'),
                visible='legendonly',
            ),
            row=1, col=1,
        )

        y = []
        for date in txn_dates:
            idx = get_idx_by_date(stock_df, date)
            y.append(stock_df['close'].loc[idx])

        fig.add_trace(
            go.Scatter(
                name='txn_dates', x=txn_dates, y=y,
                mode='markers',
                marker=dict(color='black', size=8, symbol='star'),
            ),
            row=1, col=1,
        )

        fig.add_trace(
            go.Scatter(
                name='calls',
                x=[date for date, _ in calls],
                y=[strike_price for _, strike_price in calls],
                mode='markers',
                marker=dict(color='red', size=8, symbol='star'),
            ),
            row=1, col=1,
        )

        fig.add_trace(
            go.Scatter(
                name='puts',
                x=[date for date, _ in puts],
                y=[strike_price for _, strike_price in puts],
                mode='markers',
                marker=dict(color='green', size=8, symbol='star'),
            ),
            row=1, col=1,
        )

        fig.show()


def kyc():
    prediction = load_prediction()

    for stock_name in ALL:
        predict_dates = prediction.get(stock_name, [])
        txn_dates, calls, puts = [], [], []

        for position in ACTIVE_POSITIONS:
            for record in position.get(stock_name, []):
                direction, strike_date, strike_price, txn_date = record[1], record[2], record[3], record[7]
                txn_dates.append(txn_date)

                if direction == Call:
                    calls.append((strike_date, strike_price))
                elif direction == Put:
                    puts.append((strike_date, strike_price))

        show(stock_name, predict_dates, txn_dates, calls, puts)


if __name__ == '__main__':
    kyc()
