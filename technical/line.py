import pandas as pd
import plotly.graph_objects as go

from trading.core_banking import CORE_BANKING
from util import get_idx_by_date, shrink_date_str


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
    idx1 = get_idx_by_date(stock_df, date1)
    idx2 = get_idx_by_date(stock_df, date2)

    for delta in range(-prev_len, idx2 - idx1):
        point = _calculate_point(stock_df, date1, delta, k)
        if point:
            dates.append(point[0])
            prices.append(point[1])

    for delta in range(0, post_len):
        point = _calculate_point(stock_df, date2, delta, k)
        if point:
            dates.append(point[0])
            prices.append(point[1])

    return dates, prices, k


def calculate_secondary_line(stock_df: pd.DataFrame, date, prev_len, post_len, date1, date2) -> tuple:
    dates, prices = [], []

    k = _calculate_k(stock_df, date1, date2)

    for delta in range(-prev_len, post_len):
        point = _calculate_point(stock_df, date, delta, k)
        if point:
            dates.append(point[0])
            prices.append(point[1])

    return dates, prices, k


def calculate_neck_line(stock_df: pd.DataFrame, date, prev_len, post_len) -> tuple:
    idx = get_idx_by_date(stock_df, date)
    price = stock_df.loc[idx]['close']

    dates, prices = [], []

    for delta in range(-prev_len, post_len):
        if idx + delta not in stock_df.index:
            continue
        dates.append(stock_df.loc[idx + delta]['Date'])
        prices.append(price)

    return dates, prices


class Line:
    def __init__(self, stock_df: pd.DataFrame, stock_name: str):
        self.stock_df = stock_df
        self.stock_name = stock_name

        self.primary_lines = []
        self.secondary_lines = []
        self.anchor_dates_ps = []

        self.neck_lines = []
        self.anchor_dates_n = []

        dates = stock_df['Date'].apply(shrink_date_str).values
        for line in CORE_BANKING.get(stock_name, {}).get('lines', []):
            if len(line) == 4:
                date1, date2, _, _ = line
                if date1 not in dates or date2 not in dates:
                    continue

                self.primary_lines.append(calculate_primary_line(stock_df, *line))
                self.anchor_dates_ps.extend((line[0], line[1]))

            elif len(line) == 5:
                date, _, _, date1, date2 = line
                if date not in dates or date1 not in dates or date2 not in dates:
                    continue

                self.secondary_lines.append(calculate_secondary_line(stock_df, *line))
                self.anchor_dates_ps.append(line[0])

            elif len(line) == 3:
                date, _, _ = line
                if date not in dates:
                    continue

                self.neck_lines.append(calculate_neck_line(stock_df, *line))
                self.anchor_dates_n.append(line[0])

            else:
                raise Exception(f'invalid line {line}')

    def build_graph(self, fig: go.Figure, enable=False):
        anchor_prices_ps = []
        for date in self.anchor_dates_ps:
            idx = get_idx_by_date(self.stock_df, date)
            anchor_prices_ps.append(self.stock_df.loc[idx]['close'])

        anchor_prices_n = []
        for date in self.anchor_dates_n:
            idx = get_idx_by_date(self.stock_df, date)
            anchor_prices_n.append(self.stock_df.loc[idx]['close'])

        fig.add_trace(
            go.Scatter(
                name=f'anchor point ps',
                x=self.anchor_dates_ps,
                y=anchor_prices_ps,
                mode='markers',
                marker=dict(size=5, color='black'),
                visible=None if enable else 'legendonly',
            )
        )

        fig.add_trace(
            go.Scatter(
                name=f'anchor point n',
                x=self.anchor_dates_n,
                y=anchor_prices_n,
                mode='markers',
                marker=dict(size=5, color='blue'),
                visible='legendonly',
            )
        )

        for i, (dates, prices, k) in enumerate(self.primary_lines):
            fig.add_trace(
                go.Scatter(
                    name=f'primary line-{i + 1}',
                    x=dates,
                    y=prices,
                    mode='lines',
                    line=dict(width=1, color='red', dash='dash'),
                    visible=None if enable else 'legendonly',
                )
            )

        for i, (dates, prices, k) in enumerate(self.secondary_lines):
            fig.add_trace(
                go.Scatter(
                    name=f'secondary line-{i + 1}',
                    x=dates,
                    y=prices,
                    mode='lines',
                    line=dict(width=1, color='green', dash='dash'),
                    visible=None if enable else 'legendonly',
                )
            )

        self.neck_lines.sort(key=lambda x: x[1][0], reverse=True)
        for i, (dates, prices) in enumerate(self.neck_lines):
            fig.add_trace(
                go.Scatter(
                    name=f'neck line-{i + 1}',
                    x=dates,
                    y=prices,
                    mode='lines',
                    line=dict(width=1.25, color='black', dash='dash'),
                    visible=None if enable else 'legendonly',
                )
            )
