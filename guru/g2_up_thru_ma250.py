import pandas as pd
from statistical.ma import MA_250
from guru.g2_up_thru_ma import _calculate_hits

KEY = 'up thru ma250'


def calculate_hits(stock_df: pd.DataFrame) -> list:
    prices = stock_df[MA_250].dropna()
    dates = [stock_df.loc[idx]['Date'] for idx in prices.index]
    return _calculate_hits(stock_df, (dates, prices))
