import pandas as pd
import plotly.graph_objects as go
from technical.volume import VOLUME_REG

SIZE = 100
VOLUME_AVG_100 = 'volume_avg_100'


def calculate_hits(stock_df: pd.DataFrame, vol_avg_100: pd.Series) -> list:
    hits = []
    volume_reg = stock_df[VOLUME_REG]

    for idx in stock_df.index[SIZE:]:
        date = stock_df.loc[idx]['Date']
        vol = volume_reg[idx]
        vol_avg = vol_avg_100[idx]

        if vol_avg * (1 - 0.3) < vol < vol_avg * (1 + 0.7):
            continue

        hits.append((date, vol))

    return hits


class HitVolume:
    def __init__(self, stock_df: pd.DataFrame):
        self.stock_df = stock_df
        self.vol_avg_100 = stock_df[VOLUME_REG].rolling(SIZE).mean()

        self.hits = calculate_hits(stock_df, self.vol_avg_100)

    def build_graph(self, fig: go.Figure, enable_hit_volume=(False, 2)):
        enable, row = enable_hit_volume

        fig.add_trace(
            go.Scatter(
                name='hit volume',
                x=[date for date, _ in self.hits],
                y=[vol for _, vol in self.hits],
                mode='markers', marker=dict(color='purple', size=4),
                visible=None if enable else 'legendonly',
            ),
            row=row, col=1
        )

        fig.add_trace(
            go.Scatter(
                name=VOLUME_AVG_100,
                x=self.stock_df['Date'],
                y=self.vol_avg_100,
                mode='lines',
                line=dict(width=0.75, color='black'),
                visible='legendonly',
            ),
            row=row, col=1
        )
