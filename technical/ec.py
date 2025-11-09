import pandas as pd
import plotly.graph_objects as go

from earnings_call import Earnings_Call
from util import get_idx_by_date, shrink_date_str
from technical import get_diff


class EC:
    def __init__(self, stock_df: pd.DataFrame, stock_name: str):
        self.stock_df = stock_df
        self.stock_name = stock_name

        all_dates = stock_df['Date'].apply(shrink_date_str).values
        self.dates = [date for date in Earnings_Call.get(stock_name, []) if date in all_dates]

    def build_graph(self, fig: go.Figure, enable=False):
        x, y = [], []

        for date in self.dates:
            idx = get_idx_by_date(self.stock_df, date)
            close = self.stock_df.loc[idx]['close']
            diff = get_diff(self.stock_df, date)

            x.extend([date, date, None])
            y.extend([close - diff, close + diff, None])

        fig.add_trace(
            go.Scatter(
                name='EC', x=x, y=y,
                mode='lines', line=dict(width=2, color='blue', dash='dot'),
                visible=None if enable else 'legendonly',
            )
        )
