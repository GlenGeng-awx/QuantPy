import pandas as pd
import plotly.graph_objects as go

from .ema import EMA


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
        ema_calculator = EMA(None, self.stock_df)
        ema_calculator.calculate_ema()

        macd = ema_fast - ema_slow
        signal_line = macd.ewm(span=signal, adjust=False).mean()

        histogram = macd - signal_line

        return macd, signal_line, histogram

    def build_graph_impl(self, slow: int, fast: int, signal: int):
        macd, signal_line, histogram = self.calculate_macd(slow, fast, signal)

        self.stock_df['macd'] = macd
        self.stock_df['signal_line'] = signal_line
        self.stock_df['histogram'] = histogram

    def build_graph(self):
        self.build_graph_impl(26, 12, 9)