import pandas as pd
import plotly.graph_objects as go
from technical.volume import VOLUME_REG

SIZE = 100


def calculate_hits(stock_df: pd.DataFrame, volume_avg: pd.Series) -> (list, list):
    dates = stock_df['Date']
    volume_reg = stock_df[VOLUME_REG]

    low_hits, high_hits = [], []

    for idx in stock_df.index[SIZE:]:
        date, vol, vol_avg = dates[idx], volume_reg[idx], volume_avg[idx]

        if vol < vol_avg * (1 - 0.3):
            low_hits.append((date, vol))

        if vol > vol_avg * (1 + 0.7):
            high_hits.append((date, vol))

    return low_hits, high_hits


class HitVolume:
    def __init__(self, stock_df: pd.DataFrame):
        self.stock_df = stock_df
        self.vol_avg_100 = stock_df[VOLUME_REG].rolling(SIZE).mean()

        # list of (date, vol)
        self.low_hits, self.high_hits = calculate_hits(stock_df, self.vol_avg_100)

    def build_graph(self, fig: go.Figure, enable_hit_low_vol=(False, 2), enable_hit_high_vol=(False, 2),
                     guru_start_date='2000-01-01', guru_end_date='2099-12-31'):
        self.low_hits = [
            (date, vol) for date, vol in self.low_hits if guru_start_date <= date <= guru_end_date
        ]
        self.high_hits = [
            (date, vol) for date, vol in self.high_hits if guru_start_date <= date <= guru_end_date
        ]

        enable, row = enable_hit_low_vol

        fig.add_trace(
            go.Scatter(
                name='hit low vol',
                x=[date for date, _ in self.low_hits],
                y=[vol for _, vol in self.low_hits],
                mode='markers', marker=dict(color='purple', size=4),
                visible=None if enable else 'legendonly',
            ),
            row=row, col=1
        )

        enable, row = enable_hit_high_vol

        fig.add_trace(
            go.Scatter(
                name='hit high vol',
                x=[date for date, _ in self.high_hits],
                y=[vol for _, vol in self.high_hits],
                mode='markers', marker=dict(color='brown', size=4),
                visible=None if enable else 'legendonly',
            ),
            row=row, col=1
        )

        fig.add_trace(
            go.Scatter(
                name='volume_avg_100',
                x=self.stock_df['Date'],
                y=self.vol_avg_100,
                mode='lines',
                line=dict(width=0.75, color='black'),
                visible='legendonly',
            ),
            row=row, col=1
        )
