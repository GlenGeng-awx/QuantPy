import pandas as pd

KEY = 'incr 3d'


def calculate_hits(stock_df: pd.DataFrame) -> list:
    dates = stock_df['Date']
    close = stock_df['close']

    hits = []

    for idx in stock_df.index[2:]:
        if close[idx - 2] < close[idx - 1] < close[idx]:
            hits.append(dates[idx])

    return hits
