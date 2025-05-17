import pandas as pd
import plotly.graph_objects as go

from statistical.ma import MA_20, MA_60, MA_120
from guru.hit_line import calculate_hits


class _HitMA:
    def __init__(self, stock_df: pd.DataFrame, ma_type: str):
        ma = stock_df[ma_type].dropna()
        ma_dates = [stock_df.loc[idx]['Date'] for idx in ma.index]

        self.ma_type = ma_type
        self.ma_hits = calculate_hits(stock_df, [(ma_dates, ma)], 0.01)

    def build_graph(self, fig: go.Figure, color: str, enable=False):
        fig.add_trace(
            go.Scatter(
                name=f'hit {self.ma_type.replace("_", "")}',
                x=[date for date, _ in self.ma_hits],
                y=[price for _, price in self.ma_hits],
                mode='markers', marker=dict(color=color, size=4),
                visible=None if enable else 'legendonly',
            )
        )


class HitMA:
    def __init__(self, stock_df: pd.DataFrame):
        self.ma_20 = _HitMA(stock_df, MA_20)
        self.ma_60 = _HitMA(stock_df, MA_60)
        self.ma_120 = _HitMA(stock_df, MA_120)

    def build_graph(self, fig: go.Figure,
                    enable_hit_ma20=False, enable_hit_ma60=False, enable_hit_ma120=False):
        self.ma_20.build_graph(fig, 'Fuchsia', enable_hit_ma20)
        self.ma_60.build_graph(fig, 'FireBrick', enable_hit_ma60)
        self.ma_120.build_graph(fig, 'DarkViolet', enable_hit_ma120)
