import pandas as pd
from technical.volume import VOLUME_REG

KEY = 'high vol'
SIZE = 100


def calculate_hits(stock_df: pd.DataFrame) -> list:
    dates = stock_df['Date']
    volume_reg = stock_df[VOLUME_REG]
    volume_rolling_avg = volume_reg.rolling(SIZE).mean()

    hits = []

    for idx in stock_df.index[SIZE:]:
        date, vol, rolling_avg = dates[idx], volume_reg[idx], volume_rolling_avg[idx]

        if vol > rolling_avg * (1 + 0.3):
            hits.append(date)

    return hits
