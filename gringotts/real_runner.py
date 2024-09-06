import pandas as pd
import plotly.graph_objects as go

from .book import Book


class RealRunner:
    def __init__(self, stock_df: pd.DataFrame, strategy, **kwargs):
        self.stock_df = stock_df
        self.book = Book(stock_df)

        self.strategy = strategy(stock_df=stock_df, book=self.book, **kwargs)
        self.run()

    def run(self):
        for idx in self.stock_df.index[30:]:
            self.book.observe(idx)

            if self.book.position == 0:
                if self.strategy.check_long(idx):
                    self.book.buy(idx)
            else:
                if self.strategy.check_sell(idx):
                    self.book.sell(idx)

    def show(self, fig: go.Figure):
        # clone before use
        fig = go.Figure(fig)
        self.book.build_graph(fig, size=7)

        origin_title = fig.layout.title.text
        strategy_name = self.strategy.name
        stat_text = self.book.get_stat_text()

        fig.update_layout(title=f'{origin_title} - real runner - {stat_text}<br>{strategy_name}')
        fig.show()
