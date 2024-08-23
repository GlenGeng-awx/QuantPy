import pandas as pd

from .trend import MA_20_TREND
from .factor import belong_to_up_x_percent_in_last_n_days, get_sr_levels_in_last_n_days, up_thru

"""
up thru sr levels
"""


class S1U12:
    def __init__(self, stock_df: pd.DataFrame):
        self.stock_df = stock_df
        self.name = f'{__class__.__name__} - up thru sr levels'

    def check_long(self, idx) -> bool:
        # long term not in bottom
        if not belong_to_up_x_percent_in_last_n_days(self.stock_df['close'], idx, 0.786, 100):
            return False

        # short term not in bottom
        if not belong_to_up_x_percent_in_last_n_days(self.stock_df['close'], idx, 0.786, 10):
            return False

        if self.stock_df.loc[idx][MA_20_TREND] == 'down':
            return False

        sr_levels = get_sr_levels_in_last_n_days(self.stock_df, idx, 60)
        print(f'{self.stock_df.loc[idx]["Date"]}\tsr_level: {sr_levels}')

        return any(up_thru(self.stock_df['close'], idx, sr_level) for sr_level in sr_levels)

    def check_sell(self, _idx) -> bool:
        return False
