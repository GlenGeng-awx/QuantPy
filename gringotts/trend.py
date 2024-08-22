import pandas as pd
import plotly.graph_objects as go

from statistical.ma import MA_20

MA_20_TREND = f'{MA_20}_trend'


class Trend:
    def __init__(self, stock_df: pd.DataFrame):
        self.ma20_trend = TrendImpl(stock_df, MA_20, MA_20_TREND)

    def build_graph(self, fig: go.Figure):
        self.ma20_trend.build_graph(fig, enable=True)


def calculate_trend(s: pd.Series):
    trend = []
    indices = []

    index = s.dropna().index
    for idx in index[40:]:
        indices.append(idx)

        if s.loc[idx] < s.loc[idx - 3:idx - 1].min():
            trend.append('down')
        elif s.loc[idx] > s.loc[idx - 3:idx - 1].max():
            trend.append('up')
        else:
            trend.append('swing')

    return pd.Series(trend, index=indices)


class TrendImpl:
    def __init__(self, stock_df: pd.DataFrame, ma_type: str, ma_trend: str):
        self.stock_df = stock_df

        self.ma_type = ma_type
        self.ma_trend = ma_trend

        self.stock_df[self.ma_trend] = calculate_trend(self.stock_df[self.ma_type])

    def build_graph(self, fig: go.Figure, enable=False):
        index = self.stock_df[self.stock_df[self.ma_trend] == 'up'].index
        x = self.stock_df.loc[index]['Date']
        y = self.stock_df.loc[index][self.ma_type]

        fig.add_trace(
            go.Scatter(
                name=f'{self.ma_trend} - up',
                x=x,
                y=y,
                mode="markers",
                marker=dict(size=2, color='red'),
                visible=None if enable else 'legendonly',
            )
        )

        index = self.stock_df[self.stock_df[self.ma_trend] == 'down'].index
        x = self.stock_df.loc[index]['Date']
        y = self.stock_df.loc[index][self.ma_type]

        fig.add_trace(
            go.Scatter(
                name=f'{self.ma_trend} - down',
                x=x,
                y=y,
                mode="markers",
                marker=dict(size=2, color='green'),
                visible=None if enable else 'legendonly',
            )
        )

        index = self.stock_df[self.stock_df[self.ma_trend] == 'swing'].index
        x = self.stock_df.loc[index]['Date']
        y = self.stock_df.loc[index][self.ma_type]

        fig.add_trace(
            go.Scatter(
                name=f'{self.ma_trend} - swing',
                x=x,
                y=y,
                mode="markers",
                marker=dict(size=2, color='black'),
                visible='legendonly',
            )
        )
