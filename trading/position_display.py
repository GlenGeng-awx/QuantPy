import pandas as pd
import plotly.graph_objects as go
from guru import build_params
from util import get_idx_by_date, get_next_n_workday
from .position import POSITION


class PositionDisplay:
    def __init__(self, stock_df: pd.DataFrame, stock_name: str):
        self.stock_df = stock_df
        self.stock_name = stock_name

    def build_graph(self, fig: go.Figure, enable: bool):
        if not enable:
            return

        date = POSITION.get(self.stock_name, None)
        if date is None:
            return
        if date > self.stock_df.iloc[-1]['Date']:
            print(f'position {self.stock_name} {date} is out of range')
            return

        idx = get_idx_by_date(self.stock_df, date)
        close = self.stock_df.loc[idx]['close']

        # mark open position
        fig.add_trace(
            go.Scatter(
                name='position', x=[date], y=[close],
                mode='markers', marker=dict(color='blue', size=6),
                visible=None,
            ),
            row=1, col=1,
        )

        params = build_params(self.stock_df.loc[idx - 400:idx])
        sz = params['sz']
        to_date = get_next_n_workday(date, sz)
        long_profit, short_profit = params['long_profit'], params['short_profit']

        # mark long/short prediction
        long_target = close * (1 + long_profit)
        short_target = close * (1 - short_profit)

        fig.add_trace(
            go.Scatter(
                name='long hint', x=[date, to_date], y=[long_target, long_target],
                mode='lines', line=dict(width=2, color='red', dash='dot'),
                visible=None,
            ),
            row=1, col=1,
        )

        fig.add_trace(
            go.Scatter(
                name='short hint', x=[date, to_date], y=[short_target, short_target],
                mode='lines', line=dict(width=2, color='green', dash='dot'),
                visible=None,
            ),
            row=1, col=1,
        )

        # update title
        fig.update_layout(
            title=fig.layout.title.text + f'<br>L {long_profit:.1%}, S {short_profit:.1%}'
        )
