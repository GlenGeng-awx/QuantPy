import pandas as pd
import plotly.graph_objects as go

from .book import Book


class RealRunner:
    def __init__(self, stock_df: pd.DataFrame, strategy):
        self.stock_df = stock_df
        self.strategy = strategy(stock_df)

        # self.book = Book(stock_df, max_hard_loss=0.05, max_moving_loss=0.05)
        self.book = Book(stock_df, max_hard_loss=0.1, max_moving_loss=0.1)
        self.run()

    def run(self):
        for idx in self.stock_df.index[30:]:
            self.book.observe(idx)

            if self.book.position == 0:
                if self.strategy.check(idx):
                    self.book.buy(idx)
            else:
                hit = False

                if self.book.hit_hard_loss():
                    print(f'---> hard loss hit')
                    hit = True

                if self.book.hit_moving_loss():
                    print(f'---> moving loss hit')
                    hit = True

                if hit:
                    self.book.sell(idx)

    def show(self, fig: go.Figure):
        # clone before use
        fig = go.Figure(fig)
        self.book.build_graph(fig, size=7)
        revenue_pst = self.book.revenue / self.book.money_pool * 100

        title = fig.layout.title.text
        strategy_name = self.strategy.name
        fig.update_layout(title=f'{title} - {strategy_name} --> {revenue_pst:.2f}%')

        fig.show()
