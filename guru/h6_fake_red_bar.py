import pandas as pd

KEY = 'fake red bar'


def calculate_hits(stock_df: pd.DataFrame) -> list:
    dates = stock_df['Date']
    _open, close = stock_df['open'], stock_df['close']

    fake_red_bars = []

    for idx in stock_df.index[1:]:
        if close[idx - 1] > close[idx] > _open[idx]:
            fake_red_bars.append(dates[idx])

    return fake_red_bars
