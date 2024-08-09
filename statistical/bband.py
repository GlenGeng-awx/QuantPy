import pandas as pd
import plotly.graph_objects as go

BBAND_MID = 'bband_mid'
BBAND_UP = 'bband_up'
BBAND_DOWN = 'bband_down'


def calculate_bband(stock_df: pd.DataFrame, n: int = 20, k: int = 2):
    indices = []
    y = []
    y_up = []
    y_down = []

    length = stock_df.shape[0]
    for pos in range(length):
        row = stock_df.iloc[pos]
        idx, close = row.name, row['close']

        if pos < n:
            continue

        # [from_pos, to_pos]
        from_pos = pos - n + 1
        to_pos = pos + 1

        mean = stock_df.iloc[from_pos:to_pos]['close'].mean()
        std = stock_df.iloc[from_pos:to_pos]['close'].std()

        up = mean + k * std
        down = mean - k * std

        indices.append(idx)
        y.append(mean)
        y_up.append(up)
        y_down.append(down)

    stock_df[BBAND_MID] = pd.Series(y, index=indices)
    stock_df[BBAND_UP] = pd.Series(y_up, index=indices)
    stock_df[BBAND_DOWN] = pd.Series(y_down, index=indices)


class BBand:
    def __init__(self, stock_df: pd.DataFrame, n: int = 20, k: int = 2):
        self.stock_df = stock_df
        self.n = n
        self.k = k

        calculate_bband(stock_df, n, k)

    def _build_graph(self, fig, bband_type: str, color: str, enable=False):
        y = self.stock_df[bband_type].dropna()
        dates = self.stock_df.loc[y.index]['Date']

        fig.add_trace(
            go.Scatter(
                name=f'{bband_type.replace("_", "-").upper()}',
                x=dates,
                y=y,
                mode='lines',
                line=dict(width=0.75, color=color),
                visible=None if enable else 'legendonly',
            )
        )

    def build_graph(self, fig: go.Figure, enable=False):
        self._build_graph(fig, BBAND_UP, 'red', enable)
        self._build_graph(fig, BBAND_MID, 'black', enable)
        self._build_graph(fig, BBAND_DOWN, 'green', enable)
