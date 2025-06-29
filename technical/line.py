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

        self.anchor_dates_long = []
        self.anchor_dates_short = []

        dates = stock_df['Date'].apply(shrink_date_str).values
        for line in CORE_BANKING.get(stock_name, {}).get(line_key, []):
            if len(line) == 4:
                date1, date2, _, _ = line
                date1, date2 = get_date(date1), get_date(date2)

                if date1 not in dates or date2 not in dates:
                    continue

                primary_line = calculate_primary_line(stock_df, calculate_k_fn, calculate_point_fn, *line)
                self.primary_lines.append(primary_line)

                if len(primary_line[0]) > 200:
                    self.anchor_dates_long.extend((line[0], line[1]))
                else:
                    self.anchor_dates_short.extend((line[0], line[1]))

            if len(line) == 5:
                date, _, _, date1, date2 = line
                date, date1, date2 = get_date(date), get_date(date1), get_date(date2)

                if date not in dates or date1 not in dates or date2 not in dates:
                    continue

                secondary_line = calculate_secondary_line(stock_df, calculate_k_fn, calculate_point_fn, *line)
                self.secondary_lines.append(secondary_line)

                if len(secondary_line[0]) > 200:
                    self.anchor_dates_long.append(line[0])
                else:
                    self.anchor_dates_short.append(line[0])

    def build_graph(self, fig: go.Figure, enable=False):
        anchor_dates_long, anchor_prices_long = [], []
        for date in self.anchor_dates_long:
            anchor_dates_long.append(get_date(date))

            idx = get_idx_by_date(self.stock_df, get_date(date))
            anchor_prices_long.append(self.stock_df.loc[idx][get_price_key(date)])

        anchor_dates_short, anchor_prices_short = [], []
        for date in self.anchor_dates_short:
            anchor_dates_short.append(get_date(date))

            idx = get_idx_by_date(self.stock_df, get_date(date))
            anchor_prices_short.append(self.stock_df.loc[idx][get_price_key(date)])

        fig.add_trace(
            go.Scatter(
                name=f'anchor point long',
                x=anchor_dates_long, y=anchor_prices_long,
                mode='markers', marker=dict(size=4, color='black'),
                visible=None if enable else 'legendonly',
            )
        )

        fig.add_trace(
            go.Scatter(
                name=f'anchor point short',
                x=anchor_dates_short, y=anchor_prices_short,
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
