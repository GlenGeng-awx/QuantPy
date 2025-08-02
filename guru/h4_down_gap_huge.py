import pandas as pd

KEY = 'down gap huge'


def calculate_hits(stock_df: pd.DataFrame) -> list:
    dates = stock_df['Date']
    high, low, close = stock_df['high'], stock_df['low'], stock_df['close']

    down_gaps = []

    for idx in stock_df.index[1:]:
        if high[idx] < low[idx - 1] and (low[idx - 1] - high[idx]) / close[idx - 1] > 0.01:
            down_gaps.append(dates[idx])

    return down_gaps
