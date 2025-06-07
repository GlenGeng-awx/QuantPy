import pandas as pd
import plotly.graph_objects as go
from guru import (
    high_vol, low_vol, incr_3pst, decr_3pst,
    hit_ma20, hit_ma60, hit_ma120
)

factors = [
    high_vol,
    low_vol,
    incr_3pst,
    decr_3pst,
    hit_ma20,
    hit_ma60,
    hit_ma120,
]


def calculate(stock_df: pd.DataFrame, fig: go.Figure, row=2):
    for i, factor in enumerate(factors):
        dates = factor.calculate_hits(stock_df)
        fig.add_trace(
            go.Scatter(
                name=factor.KEY,
                x=dates,
                y=[1 * (i + 1)] * len(dates),  # Dummy y values for plotting
                mode='markers', marker=dict(size=4),
            ),
            row=row, col=1
        )
