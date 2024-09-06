import pandas as pd

from gringotts.buy_strategy import ma20_trend_switch_to_up
from gringotts.sell_strategy import ma20_trend_not_up, hard_loss_gt_5_pst, moving_loss_gt_5_pst

"""
MA_20_TREND switch
"""


class S1U9:
    def __init__(self, stock_df: pd.DataFrame, book, **kwargs):
        self.stock_df = stock_df
        self.book = book

        self.name = f'{__class__.__name__} - MA_20_TREND switch'

    def check_long(self, idx) -> bool:
        return ma20_trend_switch_to_up(self.stock_df, idx)

    def check_sell(self, idx) -> bool:
        return hard_loss_gt_5_pst(self.stock_df, self.book, idx) \
            or moving_loss_gt_5_pst(self.stock_df, self.book, idx) \
            or ma20_trend_not_up(self.stock_df, idx)
