import pandas as pd
import plotly.graph_objects as go

from core_banking import CORE_BANKING
from util import get_idx_by_date, shrink_date_str, get_next_n_workday


# price_key: high, low, close, open
def calculate_neck_line(stock_df: pd.DataFrame, date, price_key, prev_len, post_len) -> tuple:
    idx = get_idx_by_date(stock_df, date)
    price = stock_df.loc[idx][price_key]

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
            date, price_key, _, _ = line
            if date not in dates:
                continue

            self.neck_lines.append(calculate_neck_line(stock_df, *line))
            self.anchors.append((date, price_key))

    def build_graph(self, fig: go.Figure, enable=False):
        anchor_dates = []
        anchor_prices = []
        for date, price_key in self.anchors:
            anchor_dates.append(date)
            idx = get_idx_by_date(self.stock_df, date)
            anchor_prices.append(self.stock_df.loc[idx][price_key])

        fig.add_trace(
            go.Scatter(
                name=f'anchor point n',
                x=anchor_dates,
                y=anchor_prices,
                mode='markers',
                marker=dict(size=4, color='blue'),
                visible=None if enable else 'legendonly',
            )
        )

        # sort by price
        self.neck_lines.sort(key=lambda x: x[1][0], reverse=True)

        for i, (dates, prices) in enumerate(self.neck_lines):
            fig.add_trace(
                go.Scatter(
                    name=f'neck line-{i + 1}',
                    x=dates,
                    y=prices,
                    mode='lines',
                    line=dict(width=0.9, color='black', dash='dash'),
                    visible=None if enable else 'legendonly',
                )
            )
