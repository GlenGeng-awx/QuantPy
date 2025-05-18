import pandas as pd
import plotly.graph_objects as go

from technical.line_expo import LineExpo
from guru.hit_line import calculate_hits


class HitLineExpo:
    def __init__(self, stock_df: pd.DataFrame, line_expo: LineExpo):
        # list of (date, price, k)
        lines_expo = line_expo.line.primary_lines + line_expo.line.secondary_lines
        lines_expo = [(date, price) for date, price, _ in lines_expo]

        # list of (date, price)
        self.lines_expo_hits = calculate_hits(stock_df, lines_expo, 0.01)

    def build_graph(self, fig: go.Figure, enable=False,
                    guru_start_date='2000-01-01', guru_end_date='2099-12-31'):
        self.lines_expo_hits = [
            (date, price) for date, price in self.lines_expo_hits if guru_start_date <= date <= guru_end_date
        ]
        fig.add_trace(
            go.Scatter(
                name=f'hit line expo',
                x=[date for date, _ in self.lines_expo_hits],
                y=[price for _, price in self.lines_expo_hits],
                mode='markers', marker=dict(color='Cyan', size=4),
                visible=None if enable else 'legendonly',
            )
        )
