import pandas as pd
import plotly.graph_objects as go

from util import local_max, local_min

LOCAL_MAX_PRICE_1ST = 'local_max_price_1st'
LOCAL_MAX_PRICE_2ND = 'local_max_price_2nd'
LOCAL_MAX_PRICE_3RD = 'local_max_price_3rd'
LOCAL_MAX_PRICE_4TH = 'local_max_price_4th'

LOCAL_MIN_PRICE_1ST = 'local_min_price_1st'
LOCAL_MIN_PRICE_2ND = 'local_min_price_2nd'
LOCAL_MIN_PRICE_3RD = 'local_min_price_3rd'
LOCAL_MIN_PRICE_4TH = 'local_min_price_4th'


class MinMax:
    def __init__(self, stock_df: pd.DataFrame):
        self.stock_df = stock_df

        # local max price
        stock_df[LOCAL_MAX_PRICE_1ST] = local_max(stock_df).reindex(stock_df.index, fill_value=False)
        stock_df[LOCAL_MAX_PRICE_2ND] = local_max(stock_df[stock_df[LOCAL_MAX_PRICE_1ST]]).reindex(stock_df.index, fill_value=False)
        stock_df[LOCAL_MAX_PRICE_3RD] = local_max(stock_df[stock_df[LOCAL_MAX_PRICE_2ND]]).reindex(stock_df.index, fill_value=False)
        stock_df[LOCAL_MAX_PRICE_4TH] = local_max(stock_df[stock_df[LOCAL_MAX_PRICE_3RD]]).reindex(stock_df.index, fill_value=False)

        # local min price
        stock_df[LOCAL_MIN_PRICE_1ST] = local_min(stock_df).reindex(stock_df.index, fill_value=False)
        stock_df[LOCAL_MIN_PRICE_2ND] = local_min(stock_df[stock_df[LOCAL_MIN_PRICE_1ST]]).reindex(stock_df.index, fill_value=False)
        stock_df[LOCAL_MIN_PRICE_3RD] = local_min(stock_df[stock_df[LOCAL_MIN_PRICE_2ND]]).reindex(stock_df.index, fill_value=False)
        stock_df[LOCAL_MIN_PRICE_4TH] = local_min(stock_df[stock_df[LOCAL_MIN_PRICE_3RD]]).reindex(stock_df.index, fill_value=False)

    def _build_graph(self, fig: go.Figure, name: str, color: str, size: int, enable=False):
        df = self.stock_df[self.stock_df[name]]

        fig.add_trace(
            go.Scatter(
                name=name,
                x=df['Date'],
                y=df['close'],
                mode='markers',
                marker=dict(
                    color=color,
                    size=size
                ),
                visible=None if enable else 'legendonly',
            ),
            row=1, col=1,
        )

    def build_graph(self, fig: go.Figure, interval, enable=False):
        self._build_graph(fig, LOCAL_MAX_PRICE_1ST, 'red', 3)
        self._build_graph(fig, LOCAL_MIN_PRICE_1ST, 'green', 3)

        self._build_graph(fig, LOCAL_MAX_PRICE_2ND, 'red', 3)
        self._build_graph(fig, LOCAL_MIN_PRICE_2ND, 'green', 3)

        self._build_graph(fig, LOCAL_MAX_PRICE_3RD, 'red', 6,
                          True if enable and interval == '1d' else False)
        self._build_graph(fig, LOCAL_MIN_PRICE_3RD, 'green', 6,
                          True if enable and interval == '1d' else False)

        self._build_graph(fig, LOCAL_MAX_PRICE_4TH, 'red', 8,
                          True if enable and interval == '1d' else False)
        self._build_graph(fig, LOCAL_MIN_PRICE_4TH, 'green', 8,
                          True if enable and interval == '1d' else False)
