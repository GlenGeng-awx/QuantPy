import pandas as pd
import plotly.graph_objects as go

from .ma import MA_20

MA_20_TREND = f'{MA_20}_trend'


def calculate_trend(s: pd.Series):
    trend = []
    indices = []

    for idx in s.dropna().index[5:]:
        indices.append(idx)

        if s.loc[idx] < s.loc[idx - 3:idx - 1].min():
            trend.append('down')
        elif s.loc[idx] > s.loc[idx - 3:idx - 1].max():
            trend.append('up')
        else:
            trend.append('swing')

    return pd.Series(trend, index=indices)


class Trend:
    def __init__(self, stock_df: pd.DataFrame):
        self.stock_df = stock_df

        self.ma_type = MA_20
        self.ma_trend = MA_20_TREND

        self.stock_df[self.ma_trend] = calculate_trend(self.stock_df[self.ma_type])

    def build_graph(self, fig: go.Figure, enable=False):
        index = self.stock_df[self.stock_df[self.ma_trend] == 'up'].index
        x = self.stock_df.loc[index]['Date']
        y = self.stock_df.loc[index][self.ma_type]

        fig.add_trace(
            go.Scatter(
                name=f'{self.ma_trend.upper()} - Up',
                x=x, y=y,
                mode="markers", marker=dict(size=2, color='red'),
                visible=None if enable else 'legendonly',
            )
        )

        index = self.stock_df[self.stock_df[self.ma_trend] == 'down'].index
        x = self.stock_df.loc[index]['Date']
        y = self.stock_df.loc[index][self.ma_type]

        fig.add_trace(
            go.Scatter(
                name=f'{self.ma_trend.upper()} - Down',
                x=x, y=y,
                mode="markers", marker=dict(size=2, color='green'),
                visible=None if enable else 'legendonly',
            )
        )

        index = self.stock_df[self.stock_df[self.ma_trend] == 'swing'].index
        x = self.stock_df.loc[index]['Date']
        y = self.stock_df.loc[index][self.ma_type]

        fig.add_trace(
            go.Scatter(
                name=f'{self.ma_trend} - Swing',
                x=x, y=y,
                mode="markers", marker=dict(size=2, color='black'),
                visible='legendonly',
            )
        )
