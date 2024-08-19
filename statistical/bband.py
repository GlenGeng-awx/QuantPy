import pandas as pd
import plotly.graph_objects as go

from .ma import calculate_ma

BBAND_MID = 'bband_mid'
BBAND_UP = 'bband_up'
BBAND_DOWN = 'bband_down'
BBAND_PST = 'bband_pst'
BBAND_PST_MA5 = 'bband_pst_ma5'


def calculate_bband(stock_df: pd.DataFrame, n: int = 20, k: int = 2):
    indices = []
    y = []
    y_up = []
    y_down = []
    y_pst = []

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
        pst = (close - down) / (up - down)

        indices.append(idx)
        y.append(mean)
        y_up.append(up)
        y_down.append(down)
        y_pst.append(pst)

    stock_df[BBAND_MID] = pd.Series(y, index=indices)
    stock_df[BBAND_UP] = pd.Series(y_up, index=indices)
    stock_df[BBAND_DOWN] = pd.Series(y_down, index=indices)
    stock_df[BBAND_PST] = pd.Series(y_pst, index=indices)
    stock_df[BBAND_PST_MA5] = calculate_ma(stock_df[BBAND_PST].dropna(), 5)


class BBand:
    def __init__(self, stock_df: pd.DataFrame, n: int = 20, k: int = 2):
        self.stock_df = stock_df
        self.n = n
        self.k = k

        calculate_bband(stock_df, n, k)

    def _build_graph_4_bband(self, fig, bband_type: str, color: str, enable=False):
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

    def _build_graph_4_bband_pst(self, fig, enable_bband_pst=(False, 2)):
        enable, row = enable_bband_pst
        if not enable:
            return

        bband_pst = self.stock_df[BBAND_PST].dropna()

        fig.add_trace(
            go.Scatter(
                name='%B',
                x=self.stock_df.loc[bband_pst.index]['Date'],
                y=bband_pst,
                mode='lines + markers',
                line=dict(width=0.5, color='blue'),
                marker=dict(size=2, color='blue'),
            ),
            row=row, col=1
        )

        bband_pst_ma5 = self.stock_df[BBAND_PST_MA5].dropna()

        fig.add_trace(
            go.Scatter(
                name='%B MA5',
                x=self.stock_df.loc[bband_pst_ma5.index]['Date'],
                y=bband_pst_ma5,
                mode='lines',
                line=dict(width=0.75, color='red'),
            ),
            row=row, col=1
        )

        fig.add_hline(y=0.15, line_dash='dot', line_color='red', line_width=1, row=row, col=1)
        fig.add_hline(y=0.85, line_dash='dot', line_color='red', line_width=1, row=row, col=1)

    def build_graph(self, fig: go.Figure, enable_bband=False, enable_bband_pst=(False, 2)):
        self._build_graph_4_bband(fig, BBAND_UP, 'red', enable_bband)
        self._build_graph_4_bband(fig, BBAND_MID, 'black', enable=False)
        self._build_graph_4_bband(fig, BBAND_DOWN, 'green', enable_bband)

        self._build_graph_4_bband_pst(fig, enable_bband_pst)
