import pandas as pd
import plotly.graph_objects as go

from guru import (
    a_high_vol,
    a_low_vol,
    b_incr_3pst,
    b_decr_3pst,
    c_long_up_shadow,
    c_long_down_shadow,
    d_hit_ma20,
    d_hit_ma60,
    d_hit_ma120,
)

factors = [
    a_high_vol,
    a_low_vol,
    b_incr_3pst,
    b_decr_3pst,
    c_long_up_shadow,
    c_long_down_shadow,
    d_hit_ma20,
    d_hit_ma60,
    d_hit_ma120,
]


def calculate(stock_df: pd.DataFrame, fig: go.Figure, row=2, last_n_days=None):
    for i, factor in enumerate(factors):
        dates = factor.calculate_hits(stock_df)

        if last_n_days is not None:
            dates = [date for date in dates if date >= stock_df['Date'].iloc[-last_n_days]]

        fig.add_trace(
            go.Scatter(
                name=factor.KEY,
                x=dates,
                y=[1 * (i + 1)] * len(dates),  # Dummy y values for plotting
                mode='markers', marker=dict(size=4),
            ),
            row=row, col=1
        )
