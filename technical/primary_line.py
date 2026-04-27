import pandas as pd
import plotly.graph_objects as go
import math

from util import get_idx_by_date, shrink_date_str, get_next_n_workday
from technical import Anchor
from core_banking import CORE_BANKING, MID_TERM


def calculate_k(stock_df: pd.DataFrame, anchor1: Anchor, anchor2: Anchor) -> float:
    x1 = get_idx_by_date(stock_df, anchor1.date)
    y1 = stock_df.loc[x1][anchor1.price_key]

    x2 = get_idx_by_date(stock_df, anchor2.date)
    y2 = stock_df.loc[x2][anchor2.price_key]

    ratio = y2 / y1
    delta = x2 - x1
    k = math.pow(ratio, 1 / delta)
    return k


def calculate_point(stock_df: pd.DataFrame, anchor: Anchor, delta, k) -> tuple:
    x = get_idx_by_date(stock_df, anchor.date)
    y = stock_df.loc[x][anchor.price_key]

    target_x = x + delta
    target_y = y * math.pow(k, delta)

    if not stock_df.index[0] <= target_x <= stock_df.index[-1] + 10:
        return ()

    if target_x in stock_df.index:
        target_date = stock_df.loc[target_x]['Date']
    else:
        diff = target_x - stock_df.index[-1]
        last_date = stock_df['Date'].iloc[-1]

        target_date = get_next_n_workday(last_date, diff)

    return target_date, target_y


def calculate_primary_line(stock_df: pd.DataFrame,
                           anchor1: Anchor, anchor2: Anchor, prev_len, post_len) -> tuple:
    dates, prices = [], []

    k = calculate_k(stock_df, anchor1, anchor2)

    idx1 = get_idx_by_date(stock_df, anchor1.date)
    idx2 = get_idx_by_date(stock_df, anchor2.date)

    for delta in range(-prev_len, idx2 - idx1):
        point = calculate_point(stock_df, anchor1, delta, k)
        if point:
            dates.append(point[0])
            prices.append(point[1])

    if post_len is None:
        post_len = stock_df.index[-1] - idx2 + 10

    for delta in range(0, post_len):
        point = calculate_point(stock_df, anchor2, delta, k)
        if point:
            dates.append(point[0])
            prices.append(point[1])

    return dates, prices, k


class PrimaryLine:
    def __init__(self, stock_df: pd.DataFrame, stock_name: str):
        self.stock_df = stock_df
        self.stock_name = stock_name

        # list of (dates, prices, k)
        self.primary_lines = []
        self.anchor_dates = []

        dates = stock_df['Date'].apply(shrink_date_str).values
        for line in CORE_BANKING.get(stock_name, {}).get('lines', []):
            if len(line) == 4 or (len(line) == 5 and line[4] == MID_TERM):
                anchor1, anchor2 = Anchor.of(line[0]), Anchor.of(line[1])
                if anchor1.date not in dates or anchor2.date not in dates:
                    continue

                primary_line = calculate_primary_line(stock_df, anchor1, anchor2, line[2], line[3])
                self.primary_lines.append(primary_line)
                self.anchor_dates.extend((anchor1, anchor2))

    def build_graph(self, fig: go.Figure, enable=False):
        anchor_dates, anchor_prices = [], []
        for anchor in self.anchor_dates:
            anchor_dates.append(anchor.date)

            idx = get_idx_by_date(self.stock_df, anchor.date)
            anchor_prices.append(self.stock_df.loc[idx][anchor.price_key])

        fig.add_trace(
            go.Scatter(
                name=f'anchor point p',
                x=anchor_dates, y=anchor_prices,
                mode='markers', marker=dict(size=4, color='black'),
                visible=None if enable else 'legendonly',
            )
        )

        for i, (dates, prices, k) in enumerate(self.primary_lines):
            ratio = f'{math.pow(k, 250) - 1:.1%}'

            fig.add_trace(
                go.Scatter(
                    name=f'p line-{i + 1} {len(dates)}d {ratio}',
                    x=dates, y=prices,
                    mode='lines', line=dict(width=1, color='red', dash='dash'),
                    visible=None if enable else 'legendonly',
                )
            )
