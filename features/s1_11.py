import pandas as pd

from gringotts.buy_strategy import long_term_not_in_bottom, golden_cross_ma20
from gringotts.sell_strategy import hard_loss_gt_5_pst, moving_loss_gt_5_pst

"""
gold cross ma 20
"""


class S1U11:
    def __init__(self, stock_df: pd.DataFrame, book, **kwargs):
        self.stock_df = stock_df
        self.book = book

        self.name = f'{__class__.__name__} - gold cross ma 20'

    def check_long(self, idx) -> bool:
        if not long_term_not_in_bottom(self.stock_df, idx):
            return False

        if not golden_cross_ma20(self.stock_df, idx):
            return False

        return True

    def check_sell(self, idx) -> bool:
        return hard_loss_gt_5_pst(self.stock_df, self.book, idx) \
            or moving_loss_gt_5_pst(self.stock_df, self.book, idx)
