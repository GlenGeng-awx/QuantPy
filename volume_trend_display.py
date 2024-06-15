import plotly.graph_objects as go
import pandas as pd
from conf import volume_ma_5, volume_ma_15, volume_ma_30, volume_ma_60


class VolumeTrendDisplay:
    def __init__(self, fig: go.Figure, stock_df: pd.DataFrame):
        self.fig = fig
        self.stock_df = stock_df

    def add_ma(self, column, color: str, size: float):
        self.fig.add_trace(
            go.Scatter(
                name=column,
                x=self.stock_df['Date'],
                y=self.stock_df[column],
                mode='lines',
                line=dict(width=size, color=color),
            ),
            row=2, col=1
        )

    def build_graph(self):
        self.add_ma(volume_ma_5, 'blue', 0.5)
        # self.add_ma(volume_ma_15, 'red', 0.5)
        # self.add_ma(volume_ma_30, 'grey', 0.5)
        # self.add_ma(volume_ma_60, 'green', 0.5)
