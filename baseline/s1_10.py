import pandas as pd

from gringotts.buy_strategy import (long_term_not_in_bottom, short_term_not_in_bottom,
                                    ma20_trend_is_down, rsi_in_strong_up, bband_pst_ma5_in_strong_up)
from gringotts.sell_strategy import hard_loss_gt_5_pst, moving_loss_gt_5_pst

"""
rsi and bband is in strong uptrend
"""


class S1U10:
    def __init__(self, stock_df: pd.DataFrame, book, **kwargs):
        self.stock_df = stock_df
        self.book = book

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

    def check_sell(self, idx) -> bool:
        return hard_loss_gt_5_pst(self.stock_df, self.book, idx) \
            or moving_loss_gt_5_pst(self.stock_df, self.book, idx)
