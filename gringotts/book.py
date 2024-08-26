import pandas as pd
import plotly.graph_objects as go


class Book:
    def __init__(self,
                 stock_df: pd.DataFrame,
                 money_pool: int = 10_000 * 1_000,
                 max_hard_loss: float = 0.05,   # 5%
                 max_moving_loss: float = 0.05  # 5%
                 ):
        self.stock_df = stock_df
        self.money_pool = money_pool

        self.max_hard_loss = max_hard_loss
        self.max_moving_loss = max_moving_loss

        # lifetime 1
        self.revenue = 0

        # lifetime 2
        self.position = 0
        self.cost = 0

        # lifetime 3
        self.gross = 0
        self.gross_baseline = 0

        # plot
        self.buy_indices = []
        self.buy_prices = []

        self.sell_indices = []
        self.sell_prices = []

        # stat
        self.positive_count = 0
        self.negative_count = 0

    def plot_buy(self, idx):
        self.buy_indices.append(idx)
        self.buy_prices.append(self.stock_df.loc[idx]['close'])

    def plot_sell(self, idx):
        self.sell_indices.append(idx)
        self.sell_prices.append(self.stock_df.loc[idx]['close'])

    def build_graph(self, fig: go.Figure, size=5):
        fig.add_trace(
            go.Scatter(
                name=f'Long',
                x=self.stock_df.loc[self.buy_indices]['Date'],
                y=self.buy_prices,
                mode="markers",
                marker=dict(size=size, color='black'),
            )
        )

        fig.add_trace(
            go.Scatter(
                name=f'Sell',
                x=self.stock_df.loc[self.sell_indices]['Date'],
                y=self.sell_prices,
                mode="markers",
                marker=dict(size=size, color='purple'),
            )
        )

    def buy(self, idx):
        row = self.stock_df.loc[idx]

        self.position = self.money_pool // row['close']
        self.cost = self.position * row['close']

        self.gross = self.cost
        self.gross_baseline = self.cost

        self.plot_buy(idx)

        print(f'buy at {row["Date"]} with price {row["close"]:.2f}\n'
              f'\tposition={self.position}, cost={self.cost:.2f}\n')

    def sell(self, idx):
        row = self.stock_df.loc[idx]

        inflight_revenue = self.gross - self.cost
        self.revenue += inflight_revenue

        if inflight_revenue > 0:
            self.positive_count += 1
        else:
            self.negative_count += 1

        print(f'sell at {row["Date"]} with price {row["close"]:.2f}\n'
              f'\tcost={self.cost:.2f}, gross={self.gross:.2f}\n'
              f'\tper_revenue={inflight_revenue:.2f}, {inflight_revenue / self.cost * 100:.2f}%, '
              f'revenue={self.revenue:.2f}, {self.revenue / self.cost * 100:.2f}%.\n')

        self.position = 0
        self.cost = 0

        self.gross = 0
        self.gross_baseline = 0

        self.plot_sell(idx)

    def observe(self, idx):
        if self.position == 0:
            return

        row = self.stock_df.loc[idx]

        self.gross = self.position * row['close']
        self.gross_baseline = max(self.gross_baseline, self.gross)

    def hit_hard_loss(self) -> bool:
        return self.cost - self.gross > self.cost * self.max_hard_loss

    def hit_moving_loss(self) -> bool:
        return self.gross_baseline - self.gross > self.gross_baseline * self.max_moving_loss

    def get_stat(self) -> dict:
        return {
            'revenue_pst': self.revenue / self.money_pool * 100,
            'buy_count': len(self.buy_indices),
            'positive_count': self.positive_count,
            'negative_count': self.negative_count
        }
