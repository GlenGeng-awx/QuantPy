import pandas as pd

from statistical.ma import MA_20, MA_5

from .trend import MA_20_TREND
from .factor import belong_to_up_x_percent_in_last_n_days, is_golden_cross
from .book import Book

"""
gold cross ma 20 - bad
"""


class S1U11:
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

            # MA_20 or MA_5
            if not is_golden_cross(self.stock_df['close'], self.stock_df[MA_20], idx):
                continue

            self.book.plot_buy(idx)
