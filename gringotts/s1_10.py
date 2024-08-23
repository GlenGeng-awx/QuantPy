import pandas as pd

from statistical.bband import BBAND_PST_MA5
from statistical.rsi import RSI_14

from .trend import MA_20_TREND
from .factor import belong_to_up_x_percent_in_last_n_days

"""
rsi and bband is in strong uptrend
"""


class S1U10:
    def __init__(self, stock_df: pd.DataFrame):
        self.stock_df = stock_df
        self.name = f'{__class__.__name__} - rsi and bband is in strong uptrend'

    def check(self, idx) -> bool:
        # long term not in bottom
        if not belong_to_up_x_percent_in_last_n_days(self.stock_df['close'], idx, 0.786, 100):
            return False

        # short term not in bottom
        if not belong_to_up_x_percent_in_last_n_days(self.stock_df['close'], idx, 0.786, 10):
            return False

        if self.stock_df.loc[idx][MA_20_TREND] == 'down':
            return False

        if self.stock_df.loc[idx][RSI_14] < 65:
            return False

        if self.stock_df.loc[idx][BBAND_PST_MA5] < 0.8:
            return False

        return True
