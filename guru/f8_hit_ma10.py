import pandas as pd
from statistical.ma import MA_10
from guru.util import _calculate_hits

KEY = 'hit ma10'


def calculate_hits(stock_df: pd.DataFrame) -> list:
    prices = stock_df[MA_10].dropna()
    dates = [stock_df.loc[idx]['Date'] for idx in prices.index]
    return _calculate_hits(stock_df, (dates, prices), 0.005)
