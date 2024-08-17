import pandas as pd

from .book import Book
from .trend import MA_20_TREND

"""
Long-only strategy.
"""


class S1U0:
    def __init__(self, stock_df: pd.DataFrame):
        self.stock_df = stock_df
        self.book = Book(stock_df, max_hard_loss=0.05, max_moving_loss=0.05)

        for idx in self.stock_df.index[30:]:
            self._analyze_per_day(idx)

        self.book.finalize()

    def _analyze_per_day(self, idx):
        self.book.observe(idx)

        if self.book.position == 0:
            if self.stock_df.loc[idx - 1:idx][MA_20_TREND].tolist() == ['down', 'up']:
                self.book.buy(idx)
        else:
            hit = False

            if self.book.hit_moving_loss():
                print(f'---> hit moving loss')
                hit = True
            if self.book.hit_hard_loss():
                print(f'---> hit hard loss hit')
                hit = True
            if self.stock_df.loc[idx][MA_20_TREND] != 'up':
                print(f'---> hit trend switch')
                hit = True

            if hit:
                self.book.sell(idx)
