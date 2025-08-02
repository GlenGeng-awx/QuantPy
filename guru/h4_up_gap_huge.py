import pandas as pd

KEY = 'up gap huge'


def calculate_hits(stock_df: pd.DataFrame) -> list:
    dates = stock_df['Date']
    high, low, close = stock_df['high'], stock_df['low'], stock_df['close']

    up_gaps = []

    for idx in stock_df.index[1:]:
        if low[idx] > high[idx - 1] and (low[idx] - high[idx - 1]) / close[idx - 1] > 0.01:
            up_gaps.append(dates[idx])

    return up_gaps
