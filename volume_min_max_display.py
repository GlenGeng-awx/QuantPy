import plotly.graph_objects as go
import pandas as pd
from pandas import Series

from conf import *


class VolumeMinMaxDisplay:
    def __init__(self, fig: go.Figure, stock_df: pd.DataFrame):
        self.fig = fig
        self.stock_df = stock_df

    def add_scatter(self, name, condition: Series, color: str, size: int):
        x = self.stock_df[condition]['Date']
        y = self.stock_df[condition][volume_reg]

        self.fig.add_trace(
            go.Scatter(
                name=name,
                x=x,
                y=y,
                mode='markers',
                marker=dict(
                    color=color,
                    size=size
                )
            ),
            row=2, col=1
        )

    def build_graph(self):
        # step A
        condition = self.stock_df['Date'].apply(lambda _: True)
        self.add_scatter('daily volume', condition, 'blue', 2)

        # step B
        condition = self.stock_df[local_min_volume_2nd]
        self.add_scatter(local_min_volume_2nd, condition, 'black', 2)

        condition = self.stock_df[local_min_volume_3rd]
        self.add_scatter(local_min_volume_3rd, condition, 'black', 4)

        condition = self.stock_df[local_min_volume_4th]
        self.add_scatter(local_min_volume_4th, condition, 'black', 6)

        # step C
        condition1 = (
                self.stock_df[local_max_volume_2nd]
                & (self.stock_df['open'] < self.stock_df['close'])
        )
        self.add_scatter(f'{local_max_volume_2nd} - up', condition1, 'red', 2)

        condition2 = (
                self.stock_df[local_max_volume_3rd]
                & (self.stock_df['open'] < self.stock_df['close'])
        )
        self.add_scatter(f'{local_max_volume_3rd} - up', condition2, 'red', 4)

        condition3 = (
                self.stock_df[local_max_volume_4th]
                & (self.stock_df['open'] < self.stock_df['close'])
        )
        self.add_scatter(f'{local_max_volume_4th} - up', condition3, 'red', 6)

        for date in self.stock_df[condition2 | condition3]['Date']:
            # self.fig.add_vline(x=date, line_width=1, line_dash="dash", line_color='red', row=1, col=1)
            self.fig.add_vline(x=date, line_width=0.5, line_dash="dash", line_color='red')

        # step D
        condition1 = (
                self.stock_df[local_max_volume_2nd]
                & (self.stock_df['open'] > self.stock_df['close'])
        )
        self.add_scatter(f'{local_max_volume_2nd} - down', condition1, 'green', 2)

        condition2 = (
                self.stock_df[local_max_volume_3rd]
                & (self.stock_df['open'] > self.stock_df['close'])
        )
        self.add_scatter(f'{local_max_volume_3rd} - down', condition2, 'green', 4)

        condition3 = (
                self.stock_df[local_max_volume_4th]
                & (self.stock_df['open'] > self.stock_df['close'])
        )
        self.add_scatter(f'{local_max_volume_4th} - down', condition3, 'green', 6)

        for date in self.stock_df[condition2 | condition3]['Date']:
            # self.fig.add_vline(x=date, line_width=1, line_dash="dash", line_color='green', row=1, col=1)
            self.fig.add_vline(x=date, line_width=0.5, line_dash="dash", line_color='green')
