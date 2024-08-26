import pandas as pd

from .buy_strategy import (long_term_not_in_bottom, short_term_not_in_bottom,
                           ma20_trend_is_down, rsi_in_strong_up, bband_pst_ma5_in_strong_up)

"""
rsi and bband is in strong uptrend
"""


class S1U10:
    def __init__(self, stock_df: pd.DataFrame):
        self.stock_df = stock_df
        self.name = f'{__class__.__name__} - rsi and bband is in strong uptrend'

    def check_long(self, idx) -> bool:
        if not (long_term_not_in_bottom(self.stock_df, idx) and short_term_not_in_bottom(self.stock_df, idx)):
            return False

        if ma20_trend_is_down(self.stock_df, idx):
            return False

        if not rsi_in_strong_up(self.stock_df, idx):
            return False

        if not bband_pst_ma5_in_strong_up(self.stock_df, idx):
            return False

        return True

    def check_sell(self, _idx) -> bool:
        return False
