import pandas as pd
import plotly.graph_objects as go

from technical.core_banking import CORE_BANKING
from util import get_idx_by_date


def _calculate_k(stock_df: pd.DataFrame, date1, date2) -> float:
    x1 = get_idx_by_date(stock_df, date1)
    y1 = stock_df.loc[x1]['close']

    x2 = get_idx_by_date(stock_df, date2)
    y2 = stock_df.loc[x2]['close']

    k = (y2 - y1) / (x2 - x1)
    return k


def _calculate_point(stock_df: pd.DataFrame, date, delta, k) -> tuple:
    x = get_idx_by_date(stock_df, date)
    y = stock_df.loc[x]['close']

    target_x = x + delta
    target_y = y + k * delta

    if target_x in stock_df.index:
        target_date = stock_df.loc[target_x]['Date']
        return target_date, target_y
    else:
        return ()


def calculate_primary_line(stock_df: pd.DataFrame, date1, date2, prev_len, post_len) -> tuple:
    dates, prices = [], []

    k = _calculate_k(stock_df, date1, date2)

    for delta in range(-prev_len, 0):
        point = _calculate_point(stock_df, date1, delta, k)
        if point:
            dates.append(point[0])
            prices.append(point[1])

    for delta in range(0, post_len):
        point = _calculate_point(stock_df, date2, delta, k)
        if point:
            dates.append(point[0])
            prices.append(point[1])

    return dates, prices


def calculate_secondary_line(stock_df: pd.DataFrame, date, prev_len, post_len, date1, date2) -> tuple:
    dates, prices = [], []

    k = _calculate_k(stock_df, date1, date2)

    for delta in range(-prev_len, post_len):
        point = _calculate_point(stock_df, date, delta, k)
        if point:
            dates.append(point[0])
            prices.append(point[1])

    return dates, prices


class Line:
    def __init__(self, stock_df: pd.DataFrame, stock_name: str):
        self.stock_df = stock_df
        self.stock_name = stock_name

        self.primary_lines = []
        self.secondary_lines = []

        self.anchor_dates = []

        for line in CORE_BANKING.get(stock_name, {}).get('lines', []):
            if len(line) == 4:
                self.primary_lines.append(calculate_primary_line(stock_df, *line))
                self.anchor_dates.extend((line[0], line[1]))
            else:
                self.secondary_lines.append(calculate_secondary_line(stock_df, *line))
                self.anchor_dates.append(line[0])

    def build_graph(self, fig: go.Figure, enable=False):
        for i, (dates, prices) in enumerate(self.primary_lines):
            fig.add_trace(
                go.Scatter(
                    name=f'primary line-{i}',
                    x=dates,
                    y=prices,
                    mode='lines',
                    line=dict(width=1, color='red', dash='dash'),
                    visible=None if enable else 'legendonly',
                )
            )

        for i, (dates, prices) in enumerate(self.secondary_lines):
            fig.add_trace(
                go.Scatter(
                    name=f'secondary line-{i}',
                    x=dates,
                    y=prices,
                    mode='lines',
                    line=dict(width=1, color='green', dash='dash'),
                    visible=None if enable else 'legendonly',
                )
            )

        anchor_prices = []
        for date in self.anchor_dates:
            idx = get_idx_by_date(self.stock_df, date)
            anchor_prices.append(self.stock_df.loc[idx]['close'])

        fig.add_trace(
            go.Scatter(
                name=f'anchor point',
                x=self.anchor_dates,
                y=anchor_prices,
                mode='markers',
                marker=dict(size=5, color='blue'),
                visible=None if enable else 'legendonly',
            )
        )
