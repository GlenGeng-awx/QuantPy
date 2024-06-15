import plotly.graph_objects as go
import pandas as pd
from conf import *


class PriceMinMaxDisplay:
    def __init__(self, fig: go.Figure, stock_df: pd.DataFrame):
        self.fig = fig
        self.stock_df = stock_df

    def add_scatter(self, filter_column: str, display_column: str, color: str, size: int):
        condition = self.stock_df[filter_column]
        x = self.stock_df[condition]['Date']
        y = self.stock_df[condition][display_column]

        self.fig.add_trace(
            go.Scatter(
                name=filter_column,
                x=x,
                y=y,
                mode='markers',
                marker=dict(
                    color=color,
                    size=size
                )
            ),
            row=1, col=1,
        )

    def build_graph(self):
        self.add_scatter(local_max_price_1st, high_k, 'red', 2)
        self.add_scatter(local_max_price_2nd, high_k, 'red', 4)
        self.add_scatter(local_max_price_3rd, high_k, 'red', 6)
        self.add_scatter(local_max_price_4th, high_k, 'red', 8)

        self.add_scatter(local_min_price_1st, low_k, 'green', 2)
        self.add_scatter(local_min_price_2nd, low_k, 'green', 4)
        self.add_scatter(local_min_price_3rd, low_k, 'green', 6)
        self.add_scatter(local_min_price_4th, low_k, 'green', 8)

        self.add_scatter(range_max_price_15, high_k, 'black', 2)
        self.add_scatter(range_max_price_30, high_k, 'black', 4)

        self.add_scatter(range_min_price_15, low_k, 'black', 2)
        self.add_scatter(range_min_price_30, low_k, 'black', 4)
