import pandas as pd
from technical.volume import VOLUME_REG

KEY = 'vol incr 5d'


def calculate_hits(stock_df: pd.DataFrame) -> list:
    dates = stock_df['Date']
    vol = stock_df[VOLUME_REG]

    hits = []

    for idx in stock_df.index[5:]:
        if vol[idx - 5] < vol[idx - 4] < vol[idx - 3] < vol[idx - 2] < vol[idx - 1] < vol[idx]:
            hits.append(dates[idx])

    return hits
