import math

import pandas as pd
import plotly.graph_objects as go

from util import get_idx_by_date, shrink_date_str
from technical import Anchor
from technical.primary_line import calculate_k, calculate_point
from core_banking import CORE_BANKING


def calculate_secondary_line(stock_df: pd.DataFrame,
                             anchor: Anchor, prev_len, post_len, anchor1: Anchor, anchor2: Anchor) -> tuple:
    dates, prices = [], []

    k = calculate_k(stock_df, anchor1, anchor2)

    if post_len is None:
        idx = get_idx_by_date(stock_df, anchor.date)
        post_len = stock_df.index[-1] - idx + 10

    for delta in range(-prev_len, post_len):
        point = calculate_point(stock_df, anchor, delta, k)
        if point:
            dates.append(point[0])
            prices.append(point[1])

    return dates, prices, k


class SecondaryLine:
    def __init__(self, stock_df: pd.DataFrame, stock_name: str):
        self.stock_df = stock_df
        self.stock_name = stock_name

        # list of (dates, prices, k)
        self.secondary_lines = []
        self.anchor_dates = []

        dates = stock_df['Date'].apply(shrink_date_str).values
        for line in CORE_BANKING.get(stock_name, {}).get('lines', []):
            if len(line) == 5:
                anchor = Anchor.of(line[0])
                anchor1, anchor2 = Anchor.of(line[3]), Anchor.of(line[4])

                if anchor.date not in dates or anchor1.date not in dates or anchor2.date not in dates:
                    continue

                secondary_line = calculate_secondary_line(stock_df, anchor, line[1], line[2], anchor1, anchor2)
                self.secondary_lines.append(secondary_line)
                self.anchor_dates.append(anchor)

    def build_graph(self, fig: go.Figure, enable=False):
        anchor_dates, anchor_prices = [], []
        for anchor in self.anchor_dates:
            anchor_dates.append(anchor.date)

            idx = get_idx_by_date(self.stock_df, anchor.date)
            anchor_prices.append(self.stock_df.loc[idx][anchor.price_key])

        fig.add_trace(
            go.Scatter(
                name=f'anchor point s',
                x=anchor_dates, y=anchor_prices,
                mode='markers', marker=dict(size=4, color='black'),
                visible=None if enable else 'legendonly',
            )
        )

        for i, (dates, prices, k) in enumerate(self.secondary_lines):
            ratio = f'{math.pow(k, 250) - 1:.1%}'

            fig.add_trace(
                go.Scatter(
                    name=f's line-{i + 1} {len(dates)}d {ratio}',
                    x=dates, y=prices,
                    mode='lines', line=dict(width=1, color='green', dash='dash'),
                    visible=None if enable else 'legendonly',
                )
            )
