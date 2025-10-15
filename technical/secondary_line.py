import pandas as pd
import plotly.graph_objects as go

from util import get_idx_by_date, shrink_date_str
from technical import get_date, get_price_key
from technical.primary_line import calculate_k, calculate_point
from core_banking import CORE_BANKING


def calculate_secondary_line(stock_df: pd.DataFrame,
                             date, prev_len, post_len, date1, date2) -> tuple:
    dates, prices = [], []

    k = calculate_k(stock_df, date1, date2)

    for delta in range(-prev_len, post_len):
        point = calculate_point(stock_df, date, delta, k)
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
                date, _, _, date1, date2 = line
                date, date1, date2 = get_date(date), get_date(date1), get_date(date2)

                if date not in dates or date1 not in dates or date2 not in dates:
                    continue

                secondary_line = calculate_secondary_line(stock_df, *line)
                self.secondary_lines.append(secondary_line)
                self.anchor_dates.append(line[0])

    def build_graph(self, fig: go.Figure, enable=False):
        anchor_dates, anchor_prices = [], []
        for date in self.anchor_dates:
            anchor_dates.append(get_date(date))

            idx = get_idx_by_date(self.stock_df, get_date(date))
            anchor_prices.append(self.stock_df.loc[idx][get_price_key(date)])

        fig.add_trace(
            go.Scatter(
                name=f'anchor point s',
                x=anchor_dates, y=anchor_prices,
                mode='markers', marker=dict(size=4, color='black'),
                visible=None if enable else 'legendonly',
            )
        )

        for i, (dates, prices, k) in enumerate(self.secondary_lines):
            fig.add_trace(
                go.Scatter(
                    name=f's line-{i + 1} {len(dates)}d',
                    x=dates, y=prices,
                    mode='lines', line=dict(width=1, color='green', dash='dash'),
                    visible=None if enable else 'legendonly',
                )
            )
