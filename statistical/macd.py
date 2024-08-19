import pandas as pd
import plotly.graph_objects as go

from .ema import calculate_ema

MACD_DIF = 'macd_dif'
MACD_DEA = 'macd_dea'
MACD_HISTOGRAM = 'macd_histogram'


# 先行計算出快速線(n日EMA)與慢速線(m日EMA,n<m)。
# 以此兩個數值，再計算兩者間的「差離值」(DIF)，
# 再計算DIF之x日EMA，此即DEA
# 最後再計算DIF與DEA的差值乘以2，即為MACD柱狀圖(Histogram)
def calculate_macd(stock_df: pd.DataFrame, slow: int = 26, fast: int = 12, signal: int = 9):
    fast_ema = calculate_ema(stock_df['close'], fast)
    slow_ema = calculate_ema(stock_df['close'], slow)

    dif = fast_ema - slow_ema
    dea = calculate_ema(dif, signal)

    histogram = (dif - dea) * 2

    stock_df[MACD_DIF] = dif
    stock_df[MACD_DEA] = dea
    stock_df[MACD_HISTOGRAM] = histogram


class MACD:
    def __init__(self, stock_df: pd.DataFrame,
                 slow: int = 26, fast: int = 12, signal: int = 9):
        self.stock_df = stock_df

        self.slow = slow
        self.fast = fast
        self.signal = signal

        calculate_macd(stock_df, slow, fast, signal)

    def build_graph(self, fig: go.Figure, enable_macd=(False, 2)):
        enable, row = enable_macd
        if not enable:
            return

        dif = self.stock_df[MACD_DIF][self.slow:]
        dea = self.stock_df[MACD_DEA][self.slow:]
        dates = self.stock_df.loc[dif.index]['Date']

        fig.add_trace(
            go.Scatter(
                name='DIF',
                x=dates,
                y=dif,
                mode='lines',
                line=dict(width=0.75, color='black'),
            ),
            row=row, col=1
        )

        fig.add_trace(
            go.Scatter(
                name='DEA',
                x=dates,
                y=dea,
                mode='lines',
                line=dict(width=0.75, color='orange'),
            ),
            row=row, col=1
        )

        histogram = self.stock_df[MACD_HISTOGRAM][self.slow:]

        red_bar = histogram[histogram >= 0]
        dates = self.stock_df.loc[red_bar.index]['Date']

        fig.add_trace(
            go.Bar(
                name='Histogram - Red',
                x=dates,
                y=red_bar,
                marker_color='red',
                opacity=0.5,
            ),
            row=row, col=1
        )

        green_bar = histogram[histogram < 0]
        dates = self.stock_df.loc[green_bar.index]['Date']

        fig.add_trace(
            go.Bar(
                name='Histogram - Green',
                x=dates,
                y=green_bar,
                marker_color='green',
                opacity=0.5,
            ),
            row=row, col=1
        )
