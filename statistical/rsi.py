import pandas as pd
import plotly.graph_objects as go

from .ema import calculate_ema

RSI_14 = 'rsi_14'
RSI_21 = 'rsi_21'


#
# rs = rsi / (1 - rsi)
#
# rsi 0.8, rs is 8/2
# rsi 0.7, rs is 7/3
# rsi 0.3, rs is 3/7
# rsi 0.2, rs is 2/8
#
def calculate_rsi(stock_df: pd.DataFrame, period: int, smoother: int = 1) -> pd.Series:
    delta = stock_df['close'].diff()

    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)

    gain_ema = calculate_ema(gain, period - 1, smoother)
    loss_ema = calculate_ema(loss, period - 1, smoother)

    rs = gain_ema / loss_ema
    rsi = (1 - 1 / (1 + rs)) * 100

    return rsi


class RSI:
    def __init__(self, stock_df: pd.DataFrame):
        self.stock_df = stock_df
        self.smoother = 1

        stock_df[RSI_14] = calculate_rsi(stock_df, 14, self.smoother)
        stock_df[RSI_21] = calculate_rsi(stock_df, 21, self.smoother)

    def _build_graph(self, fig: go.Figure, rsi_type: str, color: str, enable=False):
        rsi = self.stock_df[rsi_type]
        dates = self.stock_df.loc[rsi.index]['Date']

        fig.add_trace(
            go.Scatter(
                name=f'{rsi_type.replace("_", "-").upper()}',
                x=dates,
                y=rsi,
                mode='lines',
                line=dict(width=0.75, color=color),
                visible=None if enable else 'legendonly',
            ),
            row=2, col=1
        )

    def build_graph(self, fig: go.Figure, enable=False):
        if not enable:
            return

        self._build_graph(fig, RSI_14, 'black', True)
        self._build_graph(fig, RSI_21, 'orange')

        fig.add_hline(y=80, line_dash='dot', line_color='red', row=2, col=1)
        fig.add_hline(y=70, line_dash='dot', line_color='red', row=2, col=1)

        fig.add_hline(y=30, line_dash='dot', line_color='green', row=2, col=1)
        fig.add_hline(y=20, line_dash='dot', line_color='green', row=2, col=1)
