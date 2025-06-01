import pandas as pd
import plotly.graph_objects as go

from trading.core_banking import CORE_BANKING
from util import get_idx_by_date, shrink_date_str, get_next_n_workday


def calculate_primary_line(stock_df: pd.DataFrame,
                           calculate_k_fn, calculate_point_fn,
                           date1, date2, prev_len, post_len) -> tuple:
    dates, prices = [], []

    k = calculate_k_fn(stock_df, date1, date2)
    idx1 = get_idx_by_date(stock_df, date1)
    idx2 = get_idx_by_date(stock_df, date2)

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
                             calculate_k_fn, calculate_point_fn,
                             date, prev_len, post_len, date1, date2) -> tuple:
    dates, prices = [], []

    k = calculate_k_fn(stock_df, date1, date2)

    for delta in range(-prev_len, post_len):
        point = calculate_point_fn(stock_df, date, delta, k)
        if point:
            dates.append(point[0])
            prices.append(point[1])

    return dates, prices, k


class _Line:
    def __init__(self, stock_df: pd.DataFrame, stock_name: str,
                 key, calculate_k_fn, calculate_point_fn):
        self.stock_df = stock_df
        self.stock_name = stock_name

        # list of (dates, prices, k)
        self.primary_lines = []
        self.secondary_lines = []

        self.anchor_dates_ps = []

        dates = stock_df['Date'].apply(shrink_date_str).values
        for line in CORE_BANKING.get(stock_name, {}).get(key, []):
            if len(line) == 4:
                date1, date2, _, _ = line
                if date1 not in dates or date2 not in dates:
                    continue

                self.primary_lines.append(
                    calculate_primary_line(stock_df, calculate_k_fn, calculate_point_fn, *line))

                self.anchor_dates_ps.extend((line[0], line[1]))

            if len(line) == 5:
                date, _, _, date1, date2 = line
                if date not in dates or date1 not in dates or date2 not in dates:
                    continue

                self.secondary_lines.append(
                    calculate_secondary_line(stock_df, calculate_k_fn, calculate_point_fn, *line))

                self.anchor_dates_ps.append(line[0])

    def build_graph(self, fig: go.Figure, enable=False):
        anchor_prices = []
        for date in self.anchor_dates_ps:
            idx = get_idx_by_date(self.stock_df, date)
            anchor_prices.append(self.stock_df.loc[idx]['close'])

        fig.add_trace(
            go.Scatter(
                name=f'anchor point ps',
                x=self.anchor_dates_ps,
                y=anchor_prices,
                mode='markers',
                marker=dict(size=4, color='black'),
                visible=None if enable and self.stock_df.shape[0] < 300 else 'legendonly',
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

    if target_x > stock_df.index[-1] + 10 or target_x < stock_df.index[0]:
        return ()

    if target_x in stock_df.index:
        target_date = stock_df.loc[target_x]['Date']
    else:
        diff = target_x - stock_df.index[-1]
        last_date = stock_df['Date'].iloc[-1]
        target_date = get_next_n_workday(last_date, diff)

    return target_date, target_y


class Line:
    def __init__(self, stock_df: pd.DataFrame, stock_name: str):
        self.line = _Line(
            stock_df, stock_name,
            'lines',
            _calculate_k,
            _calculate_point
        )

    def build_graph(self, fig: go.Figure, enable=False):
        self.line.build_graph(fig, enable)
