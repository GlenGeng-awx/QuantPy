import pandas as pd

from .strategy import long_term_not_in_bottom, short_term_not_in_bottom, ma20_trend_is_down, up_thru_sr_levels

"""
up thru sr levels
"""


class S1U12:
    def __init__(self, stock_df: pd.DataFrame):
        self.stock_df = stock_df
        self.name = f'{__class__.__name__} - up thru sr levels'

    def check_long(self, idx) -> bool:
        if not (long_term_not_in_bottom(self.stock_df, idx) and short_term_not_in_bottom(self.stock_df, idx)):
            return False

        if ma20_trend_is_down(self.stock_df, idx):
            return False

        return up_thru_sr_levels(self.stock_df, idx)

    def check_sell(self, _idx) -> bool:
        return False
