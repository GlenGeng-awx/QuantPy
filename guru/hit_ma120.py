import pandas as pd
from statistical.ma import MA_120
from guru.util import _calculate_hits

KEY = 'hit ma120'


def calculate_hits(stock_df: pd.DataFrame) -> list:
    prices = stock_df[MA_120].dropna()
    dates = [stock_df.loc[idx]['Date'] for idx in prices.index]
    return _calculate_hits(stock_df, (dates, prices), 0.01)
