import pandas as pd
import plotly.graph_objects as go

from guru import factors


def _calculate(stock_df: pd.DataFrame) -> dict:
    context = {}

    for factor in factors:
        dates = factor.calculate_hits(stock_df)
        context[factor.KEY] = dates

    return context


def plot(stock_df: pd.DataFrame, fig: go.Figure, row=2, display_last_n_days=None) -> dict:
    context = _calculate(stock_df)

    for i, (key, dates) in enumerate(context.items()):
        if display_last_n_days is not None:
            dates = [date for date in dates if date >= stock_df['Date'].iloc[-display_last_n_days]]

        fig.add_trace(
            go.Scatter(
                name=key,
                x=dates,
                y=[1 * (i + 1)] * len(dates),  # Dummy y values for plotting
                mode='markers', marker=dict(size=4),
            ),
            row=row, col=1
        )

    if display_last_n_days is not None:
        fig.add_vline(
            x=stock_df['Date'].iloc[-display_last_n_days],
            line=dict(color='black', width=0.5, dash='dash'),
            row=row, col=1
        )

    return context
