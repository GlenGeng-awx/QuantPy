import pandas as pd
import plotly.graph_objects as go

from util import local_max, local_min

VOLUME_REG = 'volume_reg'

VOLUME_MA_5 = 'volume_ma_5'
VOLUME_MA_15 = 'volume_ma_15'
VOLUME_MA_30 = 'volume_ma_30'
VOLUME_MA_60 = 'volume_ma_60'

LOCAL_MAX_VOLUME_1ST = 'local_max_volume_1st'
LOCAL_MAX_VOLUME_2ND = 'local_max_volume_2nd'
LOCAL_MAX_VOLUME_3RD = 'local_max_volume_3rd'
LOCAL_MAX_VOLUME_4TH = 'local_max_volume_4th'

LOCAL_MIN_VOLUME_1ST = 'local_min_volume_1st'
LOCAL_MIN_VOLUME_2ND = 'local_min_volume_2nd'
LOCAL_MIN_VOLUME_3RD = 'local_min_volume_3rd'
LOCAL_MIN_VOLUME_4TH = 'local_min_volume_4th'


class Volume:
    def __init__(self, stock_df: pd.DataFrame):
        self.stock_df = stock_df

        volume = stock_df['volume']
        print(f'volume mean: {volume.mean()}, volume std: {volume.std()}')

        # step 1
        stock_df[VOLUME_REG] = (volume - volume.mean()) / volume.std()

        # step 2
        stock_df[VOLUME_MA_5] = stock_df[VOLUME_REG].rolling(window=5).mean()
        stock_df[VOLUME_MA_15] = stock_df[VOLUME_REG].rolling(window=15).mean()
        stock_df[VOLUME_MA_30] = stock_df[VOLUME_REG].rolling(window=30).mean()
        stock_df[VOLUME_MA_60] = stock_df[VOLUME_REG].rolling(window=60).mean()

        # step 3
        stock_df[VOLUME_REG] = stock_df[VOLUME_REG].apply(lambda v: 4 + (v - 4) / 6 if v > 4 else v)

        # step 4
        # local max volume analysis
        stock_df[LOCAL_MAX_VOLUME_1ST] = local_max(stock_df, VOLUME_REG).reindex(stock_df.index, fill_value=False)
        stock_df[LOCAL_MAX_VOLUME_2ND] = local_max(stock_df[stock_df[LOCAL_MAX_VOLUME_1ST]], VOLUME_REG).reindex(stock_df.index, fill_value=False)
        stock_df[LOCAL_MAX_VOLUME_3RD] = local_max(stock_df[stock_df[LOCAL_MAX_VOLUME_2ND]], VOLUME_REG).reindex(stock_df.index, fill_value=False)
        stock_df[LOCAL_MAX_VOLUME_4TH] = local_max(stock_df[stock_df[LOCAL_MAX_VOLUME_3RD]], VOLUME_REG).reindex(stock_df.index, fill_value=False)

        # local min volume analysis
        stock_df[LOCAL_MIN_VOLUME_1ST] = local_min(stock_df, VOLUME_REG).reindex(stock_df.index, fill_value=False)
        stock_df[LOCAL_MIN_VOLUME_2ND] = local_min(stock_df[stock_df[LOCAL_MIN_VOLUME_1ST]], VOLUME_REG).reindex(stock_df.index, fill_value=False)
        stock_df[LOCAL_MIN_VOLUME_3RD] = local_min(stock_df[stock_df[LOCAL_MIN_VOLUME_2ND]], VOLUME_REG).reindex(stock_df.index, fill_value=False)
        stock_df[LOCAL_MIN_VOLUME_4TH] = local_min(stock_df[stock_df[LOCAL_MIN_VOLUME_3RD]], VOLUME_REG).reindex(stock_df.index, fill_value=False)

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
                    enable_volume_raw=(False, 2),
                    enable_volume_reg=(False, 2)
                    ):
        enable, row = enable_volume_reg
        if enable:
            fig.add_trace(
                go.Bar(
                    name=VOLUME_REG,
                    x=self.stock_df['Date'],
                    y=self.stock_df[VOLUME_REG],
                    marker_color='blue',
                    opacity=0.5,
                    # visible='legendonly',
                ),
                row=row, col=1
            )

            self.add_volume_ma(fig, VOLUME_MA_5, 'black', 1, (True, 2))
            self.add_volume_ma(fig, VOLUME_MA_15, 'black', 1)
            self.add_volume_ma(fig, VOLUME_MA_30, 'black', 1)
            self.add_volume_ma(fig, VOLUME_MA_60, 'black', 1)

        enable, row = enable_volume_raw
        if enable:
            fig.add_trace(
                go.Bar(
                    name="volume",
                    x=self.stock_df['Date'],
                    y=self.stock_df['volume'],
                    marker_color='blue',
                    opacity=0.5,
                ),
                row=row, col=1
            )
