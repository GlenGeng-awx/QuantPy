import pandas as pd

KEY = 'down gap'


def calculate_hits(stock_df: pd.DataFrame) -> list:
    dates = stock_df['Date']
    high, low = stock_df['high'], stock_df['low']

    down_gaps = []

    for idx in stock_df.index[1:]:
        if high[idx] < low[idx - 1]:
            down_gaps.append(dates[idx])

    return down_gaps
