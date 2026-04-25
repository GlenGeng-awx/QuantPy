import pandas as pd
from technical.volume import VOLUME_REG
from guru.factor import Factor

SIZE = 100


def _high_vol(stock_df: pd.DataFrame) -> list:
    dates = stock_df['Date']
    volume_reg = stock_df[VOLUME_REG]
    volume_rolling_avg = volume_reg.rolling(SIZE).mean()

    hits = []
    for idx in stock_df.index[SIZE:]:
        if volume_reg[idx] > volume_rolling_avg[idx] * 2:
            hits.append(dates[idx])
    return hits


def _low_vol(stock_df: pd.DataFrame) -> list:
    dates = stock_df['Date']
    volume_reg = stock_df[VOLUME_REG]
    volume_rolling_avg = volume_reg.rolling(SIZE).mean()

    hits = []
    for idx in stock_df.index[SIZE:]:
        if volume_reg[idx] < volume_rolling_avg[idx] * 0.5:
            hits.append(dates[idx])
    return hits


def _consecutive(stock_df, ascending):
    dates = stock_df['Date']
    vol = stock_df[VOLUME_REG]
    hits = []
    for idx in stock_df.index[5:]:
        if all((vol[idx - i] < vol[idx - i + 1]) if ascending else (vol[idx - i] > vol[idx - i + 1]) for i in range(5, 0, -1)):
            hits.append(dates[idx])
    return hits


factors = [
    Factor('high vol', 'black', _high_vol),
    Factor('low vol', 'black', _low_vol),
    Factor('vol incr 5d', 'black', lambda df: _consecutive(df, ascending=True)),
    Factor('vol decr 5d', 'black', lambda df: _consecutive(df, ascending=False)),
]
