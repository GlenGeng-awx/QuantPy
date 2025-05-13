import pandas as pd
import plotly.graph_objects as go

from trading.core_banking import CORE_BANKING
from util import get_idx_by_date, shrink_date_str


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


class NeckLine:
    def __init__(self, stock_df: pd.DataFrame, stock_name: str):
        self.stock_df = stock_df
        self.stock_name = stock_name

        self.neck_lines = []
        self.anchor_dates = []

        dates = stock_df['Date'].apply(shrink_date_str).values
        for line in CORE_BANKING.get(stock_name, {}).get('lines', []):
            if len(line) == 3:
                date, _, _ = line
                if date not in dates:
                    continue

                self.neck_lines.append(calculate_neck_line(stock_df, *line))
                self.anchor_dates.append(line[0])

    def build_graph(self, fig: go.Figure, enable=False):
        anchor_prices = []
        for date in self.anchor_dates:
            idx = get_idx_by_date(self.stock_df, date)
            anchor_prices.append(self.stock_df.loc[idx]['close'])

        fig.add_trace(
            go.Scatter(
                name=f'anchor point n',
                x=self.anchor_dates,
                y=anchor_prices,
                mode='markers',
                marker=dict(size=5, color='blue'),
                visible='legendonly',
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
