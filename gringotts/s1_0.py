import pandas as pd

from .trend import MA_20_TREND
from .common import LONG, SHORT

"""
Long-only strategy.
"""


class S1U0:
    def __init__(self, stock_df: pd.DataFrame):
        self.stock_df = stock_df
        self.initial_drop = 30

        self.money_pool = 10_000 * 1_000

        self.hard_loss_threshold = 0.05 * self.money_pool
        self.moving_loss_threshold = 0.10

        self.position = 0
        self.cost = 0
        self.revenue = 0
        self.gross_baseline = 0

        self.buy_indices = []
        self.buy_prices = []

        self.sell_indices = []
        self.sell_prices = []

        for idx in self.stock_df.index[self.initial_drop:]:
            self._analyze_per_day(idx)

        self.stock_df[LONG] = pd.Series(self.buy_prices, index=self.buy_indices)
        self.stock_df[SHORT] = pd.Series(self.sell_prices, index=self.sell_indices)

    def _analyze_per_day(self, idx):
        row = self.stock_df.loc[idx]

        if self.cost == 0:
            if self.stock_df.loc[idx - 1:idx][MA_20_TREND].tolist() == ['down', 'up']:
                self.position = self.money_pool // row['close']
                self.cost = self.position * row['close']

                print(f'buy with {row["close"]:.2f} at {row["Date"]}, position={self.position}, cost={self.cost:.2f}')
                self.buy_indices.append(idx)
                self.buy_prices.append(row['close'])
        else:
            gross = self.position * row['close']
            self.gross_baseline = max(self.gross_baseline, gross)

            hit = False

            if self.gross_baseline - gross > self.gross_baseline * self.moving_loss_threshold:
                print(f'---> moving loss hit')
                hit = True

            if self.cost - gross > self.hard_loss_threshold:
                print(f'---> hard loss hit')
                hit = True

            if row[MA_20_TREND] != 'up':
                print(f'---> trend switch hit')
                hit = True

            if hit:
                per_revenue = gross - self.cost
                self.revenue += per_revenue

                print(f'sell with {row["close"]} at {row["Date"]}, '
                      f'cost={self.cost:.2f}, gross={gross:.2f}, '
                      f'per_revenue={per_revenue:.2f}, {per_revenue / self.cost * 100:.2f}%, '
                      f'total_revenue={self.revenue:.2f}, {self.revenue / self.money_pool * 100:.2f}%.\n\n')

                self.cost = 0
                self.position = 0
                self.gross_baseline = 0

                self.sell_indices.append(idx)
                self.sell_prices.append(row['close'])
