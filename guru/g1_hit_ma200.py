import pandas as pd
from technical.ma import MA_200
from guru.g1_hit_ma import _calculate_hits

KEY = 'hit ma200'
COLOR = 'black'


def calculate_hits(stock_df: pd.DataFrame) -> list:
    prices = stock_df[MA_200].dropna()
    dates = [stock_df.loc[idx]['Date'] for idx in prices.index]
    return _calculate_hits(stock_df, (dates, prices), 0.005)
