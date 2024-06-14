import plotly.graph_objects as go
import pandas as pd
from conf import *


class PriceTrendDisplay:
    def __init__(self, fig: go.Figure, stock_df: pd.DataFrame):
        self.fig = fig
        self.stock_df = stock_df

    def add_line(self, filter_column: str, display_column: str, color: str, size: int, name=None):
        condition = self.stock_df[filter_column]
        x = self.stock_df[condition]['Date']
        y = self.stock_df[condition][display_column]

        self.fig.add_trace(
            go.Scatter(
                name=name if name else filter_column,
                x=x,
                y=y,
                mode='markers+lines',
                marker=dict(
                    color=color,
                    size=size
                ),
                line=dict(dash="dot"),
            ),
            row=1, col=1,
        )

    def build_graph(self):
        self.add_line(local_max_price_3rd, 'high', 'red', 5, 'price_upper_bound')
        self.add_line(local_min_price_3rd, 'low', 'green', 5, 'price_lower_bound')

        # self.add_line(local_max_price_3rd_quasi, 'high', 'blue', 5)
        # self.add_line(local_min_price_3rd_quasi, 'low', 'black', 5)
