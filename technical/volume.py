import pandas as pd
import plotly.graph_objects as go

VOLUME = 'volume'
VOLUME_REG = 'volume_reg'

VOLUME_MA_5 = 'volume_ma_5'
VOLUME_MA_15 = 'volume_ma_15'
VOLUME_MA_30 = 'volume_ma_30'
VOLUME_MA_60 = 'volume_ma_60'


class Volume:
    def __init__(self, stock_df: pd.DataFrame):
        self.stock_df = stock_df

        volume = stock_df[VOLUME]

        stock_df[VOLUME_MA_5] = volume.rolling(window=5).mean()
        stock_df[VOLUME_MA_15] = volume.rolling(window=15).mean()
        stock_df[VOLUME_MA_30] = volume.rolling(window=30).mean()
        stock_df[VOLUME_MA_60] = volume.rolling(window=60).mean()

    def add_volume_ma(self, fig: go.Figure, ma_type: str,
                      color: str, size: float, enable_ma=(False, 2)):
        enable, row = enable_ma
        fig.add_trace(
            go.Scatter(
                name=ma_type,
                x=self.stock_df['Date'],
                y=self.stock_df[ma_type],
                mode='lines',
                line=dict(width=size, color=color),
                visible=None if enable else 'legendonly',
            ),
            row=row, col=1
        )

    def build_graph(self,
                    fig: go.Figure,
                    enable_volume=(False, 2),
                    ):
        enable, row = enable_volume
        if not enable:
            return

        fig.add_trace(
            go.Bar(
                name=VOLUME,
                x=self.stock_df['Date'],
                y=self.stock_df[VOLUME],
                marker_color='blue',
                opacity=0.5,
            ),
            row=row, col=1
        )

        self.add_volume_ma(fig, VOLUME_MA_5, 'black', 1, (False, row))
        self.add_volume_ma(fig, VOLUME_MA_15, 'black', 1, (False, row))
        self.add_volume_ma(fig, VOLUME_MA_30, 'black', 1, (False, row))
        self.add_volume_ma(fig, VOLUME_MA_60, 'black', 1, (False, row))
