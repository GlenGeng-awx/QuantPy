import pandas as pd

from .trend import MA_20_TREND
from .factor import belong_to_up_x_percent_in_last_n_days, get_sr_levels_in_last_n_days, up_thru
from .book import Book

"""
up thru sr levels
"""


class S1U12:
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

            sr_levels = get_sr_levels_in_last_n_days(self.stock_df, idx, 60)
            print(f'{self.stock_df.loc[idx]["Date"]}\tsr_level: {sr_levels}')

            if any(up_thru(self.stock_df['close'], idx, sr_level) for sr_level in sr_levels):
                self.book.plot_buy(idx)
