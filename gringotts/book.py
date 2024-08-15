import pandas as pd
from .common import LONG, SHORT


class Book:
    def __init__(self, stock_df: pd.DataFrame, money_pool: int = 10_000 * 1_000):
        self.stock_df = stock_df
        self.money_pool = money_pool

        self.position = 0
        self.cost = 0
        self.revenue = 0

        self.gross = 0
        self.inflight_revenue = 0
        self.inflight_loss_pst = 0

        self.buy_indices = []
        self.buy_prices = []

        self.sell_indices = []
        self.sell_prices = []

    def buy(self, idx):
        row = self.stock_df.loc[idx]
        self.position = self.money_pool // row['close']

        self.cost = self.position * row['close']
        self.gross = self.position * row['close']

        self.buy_indices.append(idx)
        self.buy_prices.append(row['close'])

        print(f'buy at {row["Date"]} with price {row["close"]:.2f}\n'
              f'\tposition={self.position}, cost={self.cost:.2f}\n')

    def observe(self, idx):
        if self.position == 0:
            return

        row = self.stock_df.loc[idx]
        self.gross = self.position * row['close']
        self.inflight_revenue = self.gross - self.cost
        self.inflight_loss_pst = (self.cost - self.gross) / self.cost

    def sell(self, idx):
        row = self.stock_df.loc[idx]
        self.revenue += self.inflight_revenue

        print(f'sell at {row["Date"]} with price {row["close"]:.2f}\n'
              f'\tcost={self.cost:.2f}, gross={self.gross:.2f}\n'
              f'\tper_revenue={self.inflight_revenue:.2f}, {self.inflight_revenue / self.cost * 100:.2f}%, '
              f'revenue={self.revenue:.2f}, {self.revenue / self.cost * 100:.2f}%.\n')

        self.position = 0
        self.cost = 0

        self.gross = 0
        self.inflight_revenue = 0
        self.inflight_loss_pst = 0

        self.sell_indices.append(idx)
        self.sell_prices.append(row['close'])

    def finalize(self):
        self.stock_df[LONG] = pd.Series(self.buy_prices, index=self.buy_indices)
        self.stock_df[SHORT] = pd.Series(self.sell_prices, index=self.sell_indices)
