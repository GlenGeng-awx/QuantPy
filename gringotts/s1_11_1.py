import pandas as pd

from statistical.ma import MA_5

from .strategy import golden_cross_ma5, ma20_trend_is_down


"""
gold cross ma 5
"""


class S1U11V1:
    def __init__(self, stock_df: pd.DataFrame):
        self.stock_df = stock_df
        self.name = f'{__class__.__name__} - gold cross ma 5'

    def check_long(self, idx) -> bool:
        if ma20_trend_is_down(self.stock_df, idx):
            return False

        if not golden_cross_ma5(self.stock_df, idx):
            return False

        return True

    def check_sell(self, idx) -> bool:
        # if is_death_cross(self.stock_df['close'], self.stock_df[MA_5], idx):
        if self.stock_df['close'].loc[idx] < self.stock_df[MA_5].loc[idx] * 0.98:
            return True

        return False
