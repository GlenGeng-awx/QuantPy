import pandas as pd
import plotly.graph_objects as go

from technical.line import Line
from util import get_idx_by_date, shrink_date_str


def _hit(target_price, price, margin: float):
    return target_price * (1 - margin) <= price <= target_price * (1 + margin)


# lines: list of (dates, prices)
def calculate_hits(stock_df: pd.DataFrame, lines: list, margin) -> list:
    hits = []

    for dates, prices in lines:
        for date, price in zip(dates, prices):
            idx = get_idx_by_date(stock_df, shrink_date_str(date))
            high, low, close = stock_df.loc[idx]['high'], stock_df.loc[idx]['low'], stock_df.loc[idx]['close']

            if _hit(price, high, margin):
                hits.append((date, high))
            if _hit(price, low, margin):
                hits.append((date, low))
            if _hit(price, close, margin):
                hits.append((date, close))

    return sorted(list(set(hits)), key=lambda x: x[0])


class HitLine:
    def __init__(self, stock_df: pd.DataFrame, line: Line):
        # list of (date, price, k)
        lines = line.line.primary_lines + line.line.secondary_lines
        lines = [(date, price) for date, price, _ in lines]

        # list of (date, price)
        self.line_hits = calculate_hits(stock_df, lines, 0.01)

    def build_graph(self, fig: go.Figure, enable=False,
                    guru_start_date='2000-01-01', guru_end_date='2099-12-31'):
        self.line_hits = [
            (date, price) for date, price in self.line_hits if guru_start_date <= date <= guru_end_date
        ]
        fig.add_trace(
            go.Scatter(
                name=f'hit line',
                x=[date for date, _ in self.line_hits],
                y=[price for _, price in self.line_hits],
                mode='markers', marker=dict(color='DarkCyan', size=4),
                visible=None if enable else 'legendonly',
            )
        )
