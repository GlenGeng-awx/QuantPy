import glob
import pandas as pd
import plotly.graph_objects as go
from guru import build_params
from util import get_idx_by_date, get_next_n_workday


class PositionDisplay:
    def __init__(self, stock_df: pd.DataFrame, stock_name: str):
        self.stock_df = stock_df
        self.stock_name = stock_name

    def build_graph_impl(self, fig: go.Figure, num: int, date: str):
        if date > self.stock_df.iloc[-1]['Date']:
            print(f'position {self.stock_name} {date} is out of range')
            return

        idx = get_idx_by_date(self.stock_df, date)
        close = self.stock_df.loc[idx]['close']

        params = build_params(self.stock_df.loc[idx - 400:idx])
        sz, long_profit, short_profit = params['sz'], params['long_profit'], params['short_profit']

        to_date = get_next_n_workday(date, sz)
        long_target = close * (1 + long_profit)
        short_target = close * (1 - short_profit)

        color = 'orange'
        if self.stock_df.loc[idx:idx + sz]['high'].max() > long_target \
                or self.stock_df.loc[idx:idx + sz]['low'].min() < short_target:
            color = 'black'

        fig.add_trace(
            go.Scatter(
                name=f'position-{num}', x=[date], y=[close],
                mode='markers', marker=dict(color=color, size=8),
                visible=None,
            ),
            row=1, col=1,
        )

        fig.add_trace(
            go.Scatter(
                name=f'long hint-{num}-{long_profit:.1%}',
                x=[date, to_date], y=[long_target, long_target],
                mode='lines', line=dict(width=2, color='red', dash='dot'),
                visible=None,
            ),
            row=1, col=1,
        )

        fig.add_trace(
            go.Scatter(
                name=f'short hint-{num}-{short_profit:.1%}',
                x=[date, to_date], y=[short_target, short_target],
                mode='lines', line=dict(width=2, color='green', dash='dot'),
                visible=None,
            ),
            row=1, col=1,
        )

    def build_graph(self, fig: go.Figure, enable: bool):
        if not enable:
            return

        dates = []
        for filename in glob.glob(f'./bak/{self.stock_name}$*'):
            # from ./bak/JNJ$2025-02-06$4 to (JNJ, 2025-02-06, 4)
            record = filename.split('/')[-1]
            _, to_date, _ = record.split('$')
            dates.append(to_date)

        for (num, date) in enumerate(sorted(dates)):
            self.build_graph_impl(fig, num + 1, date)
