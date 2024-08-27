import pandas as pd

from gringotts.buy_strategy import up_thru_sr_level_and_retrace_and_bounce_back
from gringotts.sell_strategy import hard_loss_gt_5_pst, moving_loss_gt_5_pst

"""
up thru sr levels, retrace and bounds back
"""


class S1U12V1:
    def __init__(self, stock_df: pd.DataFrame, book, **kwargs):
        self.stock_df = stock_df
        self.book = book

        self.name = f'{__class__.__name__} - up thru sr levels, retrace and bounds back'

    def check_long(self, idx) -> bool:
        return up_thru_sr_level_and_retrace_and_bounce_back(self.stock_df, idx)

    def check_sell(self, idx) -> bool:
        return hard_loss_gt_5_pst(self.stock_df, self.book, idx) \
            or moving_loss_gt_5_pst(self.stock_df, self.book, idx)
