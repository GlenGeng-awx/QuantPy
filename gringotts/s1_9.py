import pandas as pd

from .trend import MA_20_TREND
from .strategy import ma20_trend_switch_to_up

"""
MA_20_TREND switch
"""


class S1U9:
    def __init__(self, stock_df: pd.DataFrame):
        self.stock_df = stock_df
        self.name = f'{__class__.__name__} - MA_20_TREND switch'

    def check_long(self, idx) -> bool:
        return ma20_trend_switch_to_up(self.stock_df, idx)

    def check_sell(self, idx) -> bool:
        return self.stock_df.loc[idx][MA_20_TREND] != 'up'
