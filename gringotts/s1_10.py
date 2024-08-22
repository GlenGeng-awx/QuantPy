import pandas as pd

from statistical.bband import BBAND_PST_MA5
from statistical.rsi import RSI_14

from .trend import MA_20_TREND
from .factor import belong_to_up_x_percent_in_last_n_days
from .book import Book

"""
rsi and bband is in strong uptrend
"""


class S1U10:
    def __init__(self, stock_df: pd.DataFrame):
        self.stock_df = stock_df

        self.book = Book(stock_df, max_hard_loss=0.05, max_moving_loss=0.05)
        self.analyze()

    def analyze(self):
        for idx in self.stock_df.index[30:]:
            # long term not in bottom
            if not belong_to_up_x_percent_in_last_n_days(self.stock_df['close'], idx, 0.786, 100):
                continue

            # short term not in bottom
            if not belong_to_up_x_percent_in_last_n_days(self.stock_df['close'], idx, 0.786, 10):
                continue

            if self.stock_df.loc[idx][MA_20_TREND] == 'down':
                continue

            if self.stock_df.loc[idx][RSI_14] < 65:
                continue

            if self.stock_df.loc[idx][BBAND_PST_MA5] < 0.8:
                continue

            self.book.plot_buy(idx)
