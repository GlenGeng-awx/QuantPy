import pandas as pd
import plotly.graph_objects as go

from .ema import calculate_ema


#
# rs = rsi / (1 - rsi)
#
# rsi 0.8, rs is 8/2
# rsi 0.7, rs is 7/3
# rsi 0.3, rs is 3/7
# rsi 0.2, rs is 2/8
#
class RSI:
    def __init__(self, fig: go.Figure, stock_df: pd.DataFrame):
        self.fig = fig
        self.stock_df = stock_df

        self.smoother = 1

    def calculate_rsi(self, period: int):
        delta = self.stock_df['close'].diff()

        gain = delta.where(delta > 0, 0)
        loss = -delta.where(delta < 0, 0)

        gain_ema = calculate_ema(gain, period - 1, self.smoother)
        loss_ema = calculate_ema(loss, period - 1, self.smoother)

        rs = gain_ema / loss_ema
        rsi = (1 - 1 / (1 + rs)) * 100

        return rsi

    def build_graph_impl(self, period: int, color: str, enable=False):
        rsi = self.calculate_rsi(period)
        x = [self.stock_df.loc[idx]['Date'] for idx in rsi.index]

        self.fig.add_trace(
            go.Scatter(
                name=f'RSI-{period}',
                x=x,
                y=rsi,
                mode='lines',
                line=dict(width=0.75, color=color),
                visible=None if enable else 'legendonly',
            ),
            row=2, col=1
        )

    def build_graph(self, enable=False):
        if not enable:
            return

        self.build_graph_impl(14, 'black', True)
        self.build_graph_impl(21, 'orange')

        self.fig.add_hline(y=80, line_dash='dot', line_color='red', row=2, col=1)
        self.fig.add_hline(y=70, line_dash='dot', line_color='red', row=2, col=1)

        self.fig.add_hline(y=30, line_dash='dot', line_color='green', row=2, col=1)
        self.fig.add_hline(y=20, line_dash='dot', line_color='green', row=2, col=1)
