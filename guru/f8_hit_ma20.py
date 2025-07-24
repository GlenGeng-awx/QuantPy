import pandas as pd
from statistical.ma import MA_20
from guru.f8_hit_ma import _calculate_hits

KEY = 'hit ma20'


def calculate_hits(stock_df: pd.DataFrame) -> list:
    prices = stock_df[MA_20].dropna()
    dates = [stock_df.loc[idx]['Date'] for idx in prices.index]
    return _calculate_hits(stock_df, (dates, prices), 0.01)
