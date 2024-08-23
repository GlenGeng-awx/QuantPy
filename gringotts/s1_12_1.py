import pandas as pd
import plotly.graph_objects as go

from .trend import MA_20_TREND
from .factor import belong_to_up_x_percent_in_last_n_days, get_sr_levels_in_last_n_days, up_thru, is_local_min
from .book import Book

"""
up thru sr levels, retrace and bounds back
"""


class S1U12V1:
    def __init__(self, stock_df: pd.DataFrame):
        self.stock_df = stock_df

        self.book = Book(stock_df, max_hard_loss=0.05, max_moving_loss=0.05)
        self.analyze()

    def analyze(self):
        for idx in self.stock_df.index[30:]:
            # retrace
            if not is_local_min(self.stock_df['close'], idx - 1):
                continue

            # up thru sr levels and bounds back
            sr_levels = get_sr_levels_in_last_n_days(self.stock_df, idx, 60)
            print(f'{self.stock_df.loc[idx]["Date"]}\tsr_level: {sr_levels}')

            hit = False

            for sr_level in sr_levels:
                step1 = False

                for n in range(1, 10):
                    if up_thru(self.stock_df['close'], idx - n, sr_level):
                        step1 = True
                        break

                if step1:
                    if self.stock_df['close'][idx - 1] > sr_level:
                        hit = True
                        break

            if hit:
                self.book.plot_buy(idx)

    def show(self, fig: go.Figure):
        fig = go.Figure(fig)

        title = f'{fig.layout.title.text} - {__name__} - up thru sr levels, retrace and bounds back'
        fig.update_layout(title=title)

        self.book.build_graph(fig)
        fig.show()
