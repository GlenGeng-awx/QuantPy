import pandas as pd
import plotly.graph_objects as go

from .ema import calculate_ema


# 先行計算出快速線(n日EMA)與慢速線(m日EMA,n<m)。
# 以此兩個數值，再計算兩者間的「差離值」(DIF)，
# 再計算DIF之x日EMA，此即DEA
# 最後再計算DIF與DEA的差值乘以2，即為MACD柱狀圖(Histogram)
class MACD:
    def __init__(self,
                 fig: go.Figure, stock_df: pd.DataFrame,
                 slow: int = 26, fast: int = 12, signal: int = 9):
        self.fig = fig
        self.stock_df = stock_df

        self.slow = slow
        self.fast = fast
        self.signal = signal

    def calculate_macd(self):
        fast_ema = calculate_ema(self.stock_df['close'], self.fast)
        slow_ema = calculate_ema(self.stock_df['close'], self.slow)

        dif = fast_ema - slow_ema
        dea = calculate_ema(dif, self.signal)

        histogram = (dif - dea) * 2

        return dif, dea, histogram

    def build_graph(self, enable=False):
        if not enable:
            return

        dif, dea, histogram = self.calculate_macd()

        dif = dif.iloc[self.slow:]
        dea = dea.iloc[self.slow:]
        histogram = histogram.iloc[self.slow:]

        x = [self.stock_df.loc[idx]['Date'] for idx in dif.index]

        self.fig.add_trace(
            go.Scatter(
                name='DIF',
                x=x,
                y=dif,
                mode='lines',
                line=dict(width=0.75, color='black'),
            ),
            row=2, col=1
        )

        self.fig.add_trace(
            go.Scatter(
                name='DEA',
                x=x,
                y=dea,
                mode='lines',
                line=dict(width=0.75, color='red'),
            ),
            row=2, col=1
        )

        red_bar = histogram[histogram >= 0]

        self.fig.add_trace(
            go.Bar(
                name='Histogram - Red',
                x=[self.stock_df.loc[idx]['Date'] for idx in red_bar.index],
                y=red_bar,
                marker_color='red',
                opacity=0.5,
            ),
            row=2, col=1
        )

        green_bar = histogram[histogram < 0]

        self.fig.add_trace(
            go.Bar(
                name='Histogram - Green',
                x=[self.stock_df.loc[idx]['Date'] for idx in green_bar.index],
                y=green_bar,
                marker_color='green',
                opacity=0.5,
            ),
            row=2, col=1
        )
