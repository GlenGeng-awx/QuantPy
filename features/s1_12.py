import pandas as pd

from gringotts.buy_strategy import long_term_not_in_bottom, short_term_not_in_bottom, ma20_trend_is_down, up_thru_sr_levels
from gringotts.sell_strategy import hard_loss_gt_5_pst, moving_loss_gt_5_pst

"""
up thru sr levels
"""


class S1U12:
    def __init__(self, stock_df: pd.DataFrame, book, **kwargs):
        self.stock_df = stock_df
        self.book = book

        self.name = f'{__class__.__name__} - up thru sr levels'

    def check_long(self, idx) -> bool:
        if not (long_term_not_in_bottom(self.stock_df, idx) and short_term_not_in_bottom(self.stock_df, idx)):
            return False

        if ma20_trend_is_down(self.stock_df, idx):
            return False

        return up_thru_sr_levels(self.stock_df, idx)

    def check_sell(self, idx) -> bool:
        return hard_loss_gt_5_pst(self.stock_df, self.book, idx) \
            or moving_loss_gt_5_pst(self.stock_df, self.book, idx)
