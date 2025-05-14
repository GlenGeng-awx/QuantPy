import pandas as pd
import plotly.graph_objects as go

from technical.line import Line
from util import get_idx_by_date, shrink_date_str

MARGIN = 0.01


def _hit(target_price, price):
    return target_price * (1 - MARGIN) <= price <= target_price * (1 + MARGIN)


def calculate_hits(stock_df: pd.DataFrame, lines: list) -> list:
    hits = []

    for dates, prices, _ in lines:
        for date, price in zip(dates, prices):
            idx = get_idx_by_date(stock_df, shrink_date_str(date))
            high, low, close = stock_df.loc[idx]['high'], stock_df.loc[idx]['low'], stock_df.loc[idx]['close']

            if _hit(price, high):
                hits.append((date, high))
            if _hit(price, low):
                hits.append((date, low))
            if _hit(price, close):
                hits.append((date, close))

    return sorted(list(set(hits)), key=lambda x: x[0])


class HitLine:
    def __init__(self, stock_df: pd.DataFrame, line: Line):
        # list of (date, price, k)
        lines = line.line.primary_lines + line.line.secondary_lines

        # list of (date, price)
        self.line_hits = calculate_hits(stock_df, lines)

    def build_graph(self, fig: go.Figure, enable=False):
        fig.add_trace(
            go.Scatter(
                name=f'hit line',
                x=[date for date, _ in self.line_hits],
                y=[price for _, price in self.line_hits],
                mode='markers', marker=dict(color='DarkCyan', size=4),
                visible=None if enable else 'legendonly',
            )
        )
