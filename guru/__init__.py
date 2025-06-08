import pandas as pd
import plotly.graph_objects as go

from guru import (
    f0_high_vol,
    f0_low_vol,
    f1_incr_3pst,
    f1_decr_3pst,
    f2_long_up_shadow,
    f2_long_down_shadow,
    f3_long_red_bar,
    f3_long_green_bar,
    f4_hit_ma20,
    f4_hit_ma60,
    f4_hit_ma120,
)

factors = [
    f0_high_vol,
    f0_low_vol,
    f1_incr_3pst,
    f1_decr_3pst,
    f2_long_up_shadow,
    f2_long_down_shadow,
    f3_long_red_bar,
    f3_long_green_bar,
    f4_hit_ma20,
    f4_hit_ma60,
    f4_hit_ma120,
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

    if last_n_days is not None:
        fig.add_vline(
            x=stock_df['Date'].iloc[-last_n_days],
            line=dict(color='black', width=0.5, dash='dash'),
            row=row, col=1
        )
