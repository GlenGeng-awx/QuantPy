import pandas as pd

from gringotts.buy_strategy import golden_cross_ma5, ma20_trend_is_down
from gringotts.sell_strategy import hard_loss_gt_5_pst, moving_loss_gt_5_pst, death_cross_ma5

"""
gold cross ma 5
"""


class S1U11V1:
    def __init__(self, stock_df: pd.DataFrame, book, **kwargs):
        self.stock_df = stock_df
        self.book = book

        self.name = f'{__class__.__name__} - gold cross ma 5'

    def check_long(self, idx) -> bool:
        if ma20_trend_is_down(self.stock_df, idx):
            return False

        if not golden_cross_ma5(self.stock_df, idx):
            return False

        return True

    def check_sell(self, idx) -> bool:
        return hard_loss_gt_5_pst(self.stock_df, self.book, idx) \
            or moving_loss_gt_5_pst(self.stock_df, self.book, idx) \
            or death_cross_ma5(self.stock_df, idx)
