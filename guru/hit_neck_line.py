import pandas as pd
import plotly.graph_objects as go

from technical.neck_line import NeckLine
from guru.hit_line import calculate_hits


class HitNeckLine:
    def __init__(self, stock_df: pd.DataFrame, neck_line: NeckLine):
        # list of (date, price)
        neck_lines = [(date, price, 'noop') for date, price in neck_line.neck_lines]
        self.neck_line_hits = calculate_hits(stock_df, neck_lines)

    def build_graph(self, fig: go.Figure, enable=False):
        fig.add_trace(
            go.Scatter(
                name=f'hit neck line',
                x=[date for date, _ in self.neck_line_hits],
                y=[price for _, price in self.neck_line_hits],
                mode='markers', marker=dict(color='DarkBlue', size=4),
                visible=None if enable else 'legendonly',
            )
        )
