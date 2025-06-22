import pandas as pd
import plotly.graph_objects as go

from core_banking import CORE_BANKING
from util import get_idx_by_date, shrink_date_str
from technical import get_date, get_price_key


def calculate_primary_line(stock_df: pd.DataFrame,
                           calculate_k_fn,
                           calculate_point_fn,
                           date1, date2, prev_len, post_len) -> tuple:
    dates, prices = [], []

    k = calculate_k_fn(stock_df, date1, date2)

    idx1 = get_idx_by_date(stock_df, get_date(date1))
    idx2 = get_idx_by_date(stock_df, get_date(date2))

    for delta in range(-prev_len, idx2 - idx1):
        point = calculate_point_fn(stock_df, date1, delta, k)
        if point:
            dates.append(point[0])
            prices.append(point[1])

    for delta in range(0, post_len):
        point = calculate_point_fn(stock_df, date2, delta, k)
        if point:
            dates.append(point[0])
            prices.append(point[1])

    return dates, prices, k


def calculate_secondary_line(stock_df: pd.DataFrame,
                             calculate_k_fn,
                             calculate_point_fn,
                             date, prev_len, post_len, date1, date2) -> tuple:
    dates, prices = [], []

    k = calculate_k_fn(stock_df, date1, date2)

    for delta in range(-prev_len, post_len):
        point = calculate_point_fn(stock_df, date, delta, k)
        if point:
            dates.append(point[0])
            prices.append(point[1])

    return dates, prices, k


class Line:
    def __init__(self,
                 stock_df: pd.DataFrame,
                 stock_name: str,
                 line_key,
                 calculate_k_fn, calculate_point_fn):
        self.stock_df = stock_df
        self.stock_name = stock_name

        # list of (dates, prices, k)
        self.primary_lines = []
        self.secondary_lines = []

        self.anchor_dates_ps = []

        dates = stock_df['Date'].apply(shrink_date_str).values
        for line in CORE_BANKING.get(stock_name, {}).get(line_key, []):
            if len(line) == 4:
                date1, date2, _, _ = line
                date1, date2 = get_date(date1), get_date(date2)

                if date1 not in dates or date2 not in dates:
                    continue

                self.primary_lines.append(
                    calculate_primary_line(stock_df, calculate_k_fn, calculate_point_fn, *line))

                self.anchor_dates_ps.extend((line[0], line[1]))

            if len(line) == 5:
                date, _, _, date1, date2 = line
                date, date1, date2 = get_date(date), get_date(date1), get_date(date2)

                if date not in dates or date1 not in dates or date2 not in dates:
                    continue

                self.secondary_lines.append(
                    calculate_secondary_line(stock_df, calculate_k_fn, calculate_point_fn, *line))

                self.anchor_dates_ps.append(line[0])

    def build_graph(self, fig: go.Figure, enable=False):
        anchor_dates, anchor_prices = [], []
        for date in self.anchor_dates_ps:
            anchor_dates.append(get_date(date))

            idx = get_idx_by_date(self.stock_df, get_date(date))
            anchor_prices.append(self.stock_df.loc[idx][get_price_key(date)])

        fig.add_trace(
            go.Scatter(
                name=f'anchor point ps',
                x=anchor_dates, y=anchor_prices,
                mode='markers', marker=dict(size=4, color='black'),
                visible=None if enable and self.stock_df.shape[0] < 300 else 'legendonly',
            )
        )

        for i, (dates, prices, k) in enumerate(self.primary_lines):
            fig.add_trace(
                go.Scatter(
                    name=f'primary line-{i + 1}-{len(dates)}',
                    x=dates, y=prices,
                    mode='lines', line=dict(width=1, color='red', dash='dash'),
                    visible=None if enable else 'legendonly',
                )
            )

        for i, (dates, prices, k) in enumerate(self.secondary_lines):
            fig.add_trace(
                go.Scatter(
                    name=f'secondary line-{i + 1}-{len(dates)}',
                    x=dates, y=prices,
                    mode='lines', line=dict(width=1, color='green', dash='dash'),
                    visible=None if enable else 'legendonly',
                )
            )
