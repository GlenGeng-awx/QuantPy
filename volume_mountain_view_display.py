import plotly.graph_objects as go
import pandas as pd

from conf import *


class VolumeMountainViewDisplay:
    def __init__(self, fig: go.Figure, stock_df: pd.DataFrame):
        self.fig = fig
        self.stock_df = stock_df

    def build_graph(self):
        condition = (
            self.stock_df[local_max_volume_1st] | self.stock_df[local_min_volume_1st]
            | (self.stock_df[volume_reg] > 2)
        )

        x = self.stock_df[condition]['Date']
        y = self.stock_df[condition][volume_reg]

        self.fig.add_trace(
            go.Scatter(
                name='volume mountain view',
                x=x,
                y=y,
                mode='lines',
                line=dict(width=0.5, color='grey'),
            ),
            row=2, col=1
        )
