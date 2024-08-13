import pandas as pd
import plotly.graph_objects as go

from statistical.bband import BBAND_MID

BBAND_TREND = 'bband_trend'


def calculate_trend(stock_df: pd.DataFrame, initial_drop: int):
    trend = []
    indices = []

    for idx in stock_df.index[initial_drop:]:
        row = stock_df.loc[idx]
        prev_row = stock_df.loc[idx - 1]

        if row[BBAND_MID] > prev_row[BBAND_MID]:
            trend.append('up')
        elif row[BBAND_MID] < prev_row[BBAND_MID]:
            trend.append('down')
        else:
            # today == yesterday
            if trend:
                trend.append(trend[-1])
            else:
                continue

        indices.append(idx)

    stock_df[BBAND_TREND] = pd.Series(trend, index=indices)


class BBandTrend:
    def __init__(self, stock_df: pd.DataFrame):
        self.stock_df = stock_df
        self.initial_drop = 30

        calculate_trend(stock_df, self.initial_drop)

    def build_graph(self, fig: go.Figure):
        index = self.stock_df[self.stock_df[BBAND_TREND] == 'up'].index
        x = self.stock_df.loc[index]['Date']
        y = self.stock_df.loc[index][BBAND_MID]

        fig.add_trace(
            go.Scatter(
                name=f'up trend',
                x=x,
                y=y,
                mode="markers",
                marker=dict(size=2, color='red'),
            )
        )

        index = self.stock_df[self.stock_df[BBAND_TREND] == 'down'].index
        x = self.stock_df.loc[index]['Date']
        y = self.stock_df.loc[index][BBAND_MID]

        fig.add_trace(
            go.Scatter(
                name=f'down trend',
                x=x,
                y=y,
                mode="markers",
                marker=dict(size=2, color='green'),
            )
        )
