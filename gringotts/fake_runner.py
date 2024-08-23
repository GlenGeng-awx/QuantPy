import pandas as pd
import plotly.graph_objects as go

from .book import Book


class FakeRunner:
    def __init__(self, stock_df: pd.DataFrame, strategy):
        self.stock_df = stock_df
        self.strategy = strategy(stock_df)

        self.book = Book(stock_df, max_hard_loss=0.05, max_moving_loss=0.05)
        self.run()

    def run(self):
        for idx in self.stock_df.index[30:]:
            if self.strategy.check_long(idx):
                self.book.plot_buy(idx)

    def show(self, fig: go.Figure):
        # clone before use
        fig = go.Figure(fig)
        self.book.build_graph(fig)

        title = fig.layout.title.text
        strategy_name = self.strategy.name
        fig.update_layout(title=f'{title} - {strategy_name}')

        fig.show()
