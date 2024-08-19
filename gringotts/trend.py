import pandas as pd
import plotly.graph_objects as go

from statistical.ma import MA_20
from statistical.ema import EMA_26

MA_20_TREND = f'{MA_20}_trend'
EMA_26_TREND = f'{EMA_26}_trend'


class TrendImpl:
    def __init__(self, stock_df: pd.DataFrame, ma_type: str, ma_trend: str, alpha: float = 0.02):
        self.stock_df = stock_df

        self.ma_type = ma_type
        self.ma_trend = ma_trend
        self.alpha = alpha
        # self.alpha = 0.0

        self.indices = []
        self.trend = []

        self.up_baseline = None
        self.down_baseline = None

        self.stock_df[self.ma_trend] = self.calculate_trend()

    def calculate_trend(self):
        index = self.stock_df[self.ma_type].dropna().index

        trend = []
        indices = []

        for idx in index[40:]:
            if self.stock_df[self.ma_type].loc[idx] < self.stock_df[self.ma_type].loc[idx-30:idx-1].min():
                trend.append('down')
                indices.append(idx)

            if self.stock_df[self.ma_type].loc[idx] > self.stock_df[self.ma_type].loc[idx-30:idx-1].max():
                trend.append('up')
                indices.append(idx)

        return pd.Series(trend, index=indices)

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
                marker=dict(size=3, color='red'),
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
                marker=dict(size=3, color='green'),
                visible=None if enable else 'legendonly',
            )
        )


class Trend:
    def __init__(self, stock_df: pd.DataFrame):
        self.ma20_trend = TrendImpl(stock_df, MA_20, MA_20_TREND, 0.008)
        self.ema26_trend = TrendImpl(stock_df, EMA_26, EMA_26_TREND, 0.005)

    def build_graph(self, fig: go.Figure):
        self.ma20_trend.build_graph(fig, enable=True)
        self.ema26_trend.build_graph(fig)
