import pandas as pd
import plotly.graph_objects as go

from core_banking import CORE_BANKING
from util import get_idx_by_date, shrink_date_str, get_next_n_workday
from technical import get_date, get_price_key


# date is in format of '2021-01-01' or ('2021-01-01', 'open')
def calculate_neck_line(stock_df: pd.DataFrame, date, prev_len, post_len) -> tuple:
    idx = get_idx_by_date(stock_df, get_date(date))
    price = stock_df.loc[idx][get_price_key(date)]

    dates, prices = [], []

    for delta in range(-prev_len, post_len):
        target_x = idx + delta

        if not stock_df.index[0] <= target_x <= stock_df.index[-1] + 10:
            continue

        if target_x in stock_df.index:
            target_date = stock_df.loc[target_x]['Date']
        else:
            diff = target_x - stock_df.index[-1]
            last_date = stock_df['Date'].iloc[-1]

            target_date = get_next_n_workday(last_date, diff)

        dates.append(target_date)
        prices.append(price)

    return dates, prices


class NeckLine:
    def __init__(self, stock_df: pd.DataFrame, stock_name: str):
        self.stock_df = stock_df
        self.stock_name = stock_name

        # list of (dates, prices)
        self.neck_lines = []
        # list of (date, price_key)
        self.anchors = []

        dates = stock_df['Date'].apply(shrink_date_str).values
        for line in CORE_BANKING.get(stock_name, {}).get('neck_lines', []):
            date, _, _ = line
            if get_date(date) not in dates:
                continue

            self.neck_lines.append(calculate_neck_line(stock_df, *line))
            self.anchors.append(date)

    def build_graph(self, fig: go.Figure, enable=False):
        anchor_dates, anchor_prices = [], []
        for date in self.anchors:
            anchor_dates.append(get_date(date))

            idx = get_idx_by_date(self.stock_df, get_date(date))
            anchor_prices.append(self.stock_df.loc[idx][get_price_key(date)])

        fig.add_trace(
            go.Scatter(
                name=f'anchor point neck',
                x=anchor_dates, y=anchor_prices,
                mode='markers', marker=dict(size=4, color='blue'),
                visible='legendonly',
            )
        )

        # sort by price
        self.neck_lines.sort(key=lambda x: x[1][0], reverse=True)

        for i, (dates, prices) in enumerate(self.neck_lines):
            ratio = 0
            if i < len(self.neck_lines) - 1:
                current_price = prices[0]
                below_price = self.neck_lines[i + 1][1][0]
                ratio = current_price / below_price - 1

            fig.add_trace(
                go.Scatter(
                    name=f'neck line-{i + 1}-{ratio:.1%}',
                    x=dates, y=prices,
                    mode='lines', line=dict(width=0.9, color='black', dash='dash'),
                    visible=None if enable else 'legendonly',
                )
            )
