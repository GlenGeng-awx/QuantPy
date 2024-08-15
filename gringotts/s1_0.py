import pandas as pd

from .book import Book
from .trend import MA_20_TREND

"""
Long-only strategy.
"""


class S1U0:
    def __init__(self, stock_df: pd.DataFrame):
        self.stock_df = stock_df
        self.book = Book(stock_df)

        self.initial_drop = 30
        self.hard_loss_threshold = 0.05
        self.moving_loss_threshold = 0.05
        self.gross_baseline = 0

        for idx in self.stock_df.index[self.initial_drop:]:
            self._analyze_per_day(idx)
        self.book.finalize()

    def _analyze_per_day(self, idx):
        self.book.observe(idx)

        if self.book.position == 0:
            if self.stock_df.loc[idx - 1:idx][MA_20_TREND].tolist() == ['down', 'up']:
                self.book.buy(idx)
        else:
            self.gross_baseline = max(self.gross_baseline, self.book.gross)

            hit = False

            if self.gross_baseline - self.book.gross > self.gross_baseline * self.moving_loss_threshold:
                print(f'---> moving loss hit')
                hit = True
            if self.book.inflight_loss_pst > self.hard_loss_threshold:
                print(f'---> hard loss hit')
                hit = True
            if self.stock_df.loc[idx][MA_20_TREND] != 'up':
                print(f'---> trend switch hit')
                hit = True

            if hit:
                self.book.sell(idx)
                self.gross_baseline = 0

