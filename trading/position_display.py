import glob
import pandas as pd
import plotly.graph_objects as go
from guru import build_params, PERIOD
from util import get_idx_by_date, get_next_n_workday


class PositionDisplay:
    def __init__(self, stock_df: pd.DataFrame, stock_name: str):
        self.stock_df = stock_df
        self.stock_name = stock_name

    def build_graph_impl(self, fig: go.Figure, date: str, long_num: int, short_num: int):
        if date > self.stock_df.iloc[-1]['Date']:
            print(f'position {self.stock_name} {date} is out of range')
            return

        idx = get_idx_by_date(self.stock_df, date)
        close = self.stock_df.loc[idx]['close']

        params = build_params(self.stock_df.loc[idx - PERIOD:idx])
        sz, long_profit, short_profit = params['sz'], params['long_profit'], params['short_profit']

        to_date = get_next_n_workday(date, sz)
        long_target = close * (1 + long_profit)
        short_target = close * (1 - short_profit)

        if long_num > short_num:
            color = 'orange'
        else:
            color = 'black'

        marker_sz = 5
        if max(long_num, short_num) >= 5:
            marker_sz = 10

        fig.add_trace(
            go.Scatter(
                name=f'L{long_num},S{short_num}', x=[date], y=[close],
                mode='markers', marker=dict(color=color, size=marker_sz),
                visible=None,
            ),
            row=1, col=1,
        )

        min_price = self.stock_df.loc[idx:idx + sz]['low'].min()
        max_price = self.stock_df.loc[idx:idx + sz]['high'].max()

        if min_price > short_target and max_price < long_target and idx + sz < self.stock_df.index[-1]:
            return

        fig.add_trace(
            go.Scatter(
                name=f'long hint-{long_profit:.1%}',
                x=[date, to_date], y=[long_target, long_target],
                mode='lines', line=dict(width=1, color='red', dash='solid'),
                visible=None,
            ),
            row=1, col=1,
        )

        fig.add_trace(
            go.Scatter(
                name=f'short hint-{short_profit:.1%}',
                x=[date, to_date], y=[short_target, short_target],
                mode='lines', line=dict(width=1, color='green', dash='solid'),
                visible=None,
            ),
            row=1, col=1,
        )

    def build_graph(self, fig: go.Figure, enable: bool):
        if not enable:
            return

        dates = []
        for filename in glob.glob(f'./bak/{self.stock_name}$*'):
            # from ./bak/JNJ$2025-02-06$4$0 to (JNJ, 2025-02-06, 4, 0)
            record = filename.split('/')[-1]
            _, to_date, long_num, short_num = record.split('$')
            dates.append((to_date, int(long_num), int(short_num)))

        for (date, long_num, short_num) in sorted(dates):
            self.build_graph_impl(fig, date, long_num, short_num)
