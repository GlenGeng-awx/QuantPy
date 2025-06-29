import pandas as pd

KEY = 'up gap'


def calculate_hits(stock_df: pd.DataFrame) -> list:
    dates = stock_df['Date']
    high, low = stock_df['high'], stock_df['low']

    up_gaps = []

    for idx in stock_df.index[1:]:
        if low[idx] > high[idx - 1]:
            up_gaps.append(dates[idx])

    return up_gaps
