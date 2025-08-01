import pandas as pd
from statistical.ma import MA_60
from guru.g2_up_thru_ma import _calculate_hits

KEY = 'up thru ma60'


def calculate_hits(stock_df: pd.DataFrame) -> list:
    prices = stock_df[MA_60].dropna()
    dates = [stock_df.loc[idx]['Date'] for idx in prices.index]
    return _calculate_hits(stock_df, (dates, prices))
