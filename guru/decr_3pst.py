import pandas as pd

KEY = 'decr 3pst'


def calculate_hits(stock_df: pd.DataFrame) -> list:
    dates = stock_df['Date']
    close = stock_df['close']

    hits = []

    for idx in stock_df.index[1:]:
        if close[idx] <= close[idx - 1] * 0.97:
            hits.append(dates[idx])

    return hits
