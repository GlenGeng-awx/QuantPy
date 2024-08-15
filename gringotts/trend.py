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

        self._setup_trend(index[1])

        for idx in index[2:]:
            self.indices.append(idx)
            row = self.stock_df.loc[idx]

            if self.up_baseline:
                if self._is_still_in_up_trend(idx):
                    self.trend.append('up')
                    self.up_baseline = max(self.up_baseline, row[self.ma_type])
                else:
                    self.trend.append('down')
                    self._transition_to_down_trend(idx)
            else:
                if self._is_still_in_down_trend(idx):
                    self.trend.append('down')
                    self.down_baseline = min(self.down_baseline, row[self.ma_type])
                else:
                    self.trend.append('up')
                    self._transition_to_up_trend(idx)

        return pd.Series(self.trend, index=self.indices)

    def _setup_trend(self, idx):
        self.indices.append(idx)

        row = self.stock_df.loc[idx]
        prev_row = self.stock_df.loc[idx - 1]

        if row[self.ma_type] >= prev_row[self.ma_type]:
            self._transition_to_up_trend(idx)
            self.trend.append('up')
        else:
            self._transition_to_down_trend(idx)
            self.trend.append('down')

    def _transition_to_up_trend(self, idx):
        self.down_baseline = None
        self.up_baseline = self.stock_df.loc[idx][self.ma_type]

    def _transition_to_down_trend(self, idx):
        self.up_baseline = None
        self.down_baseline = self.stock_df.loc[idx][self.ma_type]

    def _is_still_in_up_trend(self, idx) -> bool:
        row = self.stock_df.loc[idx]
        prev_row = self.stock_df.loc[idx - 1]

        if row[self.ma_type] >= prev_row[self.ma_type]:
            return True

        if row[self.ma_type] > self.up_baseline * (1 - self.alpha):
            print(f'hit up_baseline at {self.stock_df.loc[idx]["Date"]}')
            return True

        return False

    def _is_still_in_down_trend(self, idx) -> bool:
        row = self.stock_df.loc[idx]
        prev_row = self.stock_df.loc[idx - 1]

        if row[self.ma_type] <= prev_row[self.ma_type]:
            return True

        if row[self.ma_type] < self.down_baseline * (1 + self.alpha):
            print(f'hit down_baseline at {self.stock_df.loc[idx]["Date"]}')
            return True

        return False

    def build_graph(self, fig: go.Figure):
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
            )
        )


class Trend:
    def __init__(self, stock_df: pd.DataFrame):
        self.ma20_trend = TrendImpl(stock_df, MA_20, MA_20_TREND, 0.008)
        self.ema26_trend = TrendImpl(stock_df, EMA_26, EMA_26_TREND, 0.005)

    def build_graph(self, fig: go.Figure):
        self.ma20_trend.build_graph(fig)
        self.ema26_trend.build_graph(fig)
