import pandas as pd
import plotly.graph_objects as go
from guru import get_profits, get_sz
from util import get_idx_by_date, get_next_n_workday
from .position import POSITION


class PositionDisplay:
    def __init__(self, stock_df: pd.DataFrame, stock_name: str):
        self.stock_df = stock_df
        self.stock_name = stock_name

    def build_graph(self, fig: go.Figure, enable: bool):
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
                mode='markers', marker=dict(color='orange', size=10),
                visible='legendonly' if not enable else None,
            ),
            row=1, col=1,
        )

        # mark long/short prediction
        sz = get_sz()
        to_date = get_next_n_workday(date, sz)
        long_profit, short_profit = get_profits(self.stock_name)

        long_target = close * (1 + long_profit)
        short_target = close * (1 - short_profit)

        fig.add_trace(
            go.Scatter(
                name='long hint', x=[date, to_date], y=[long_target, long_target],
                mode='lines', line=dict(width=2, color='red', dash='dot'),
                visible='legendonly' if not enable else None,
            ),
            row=1, col=1,
        )

        fig.add_trace(
            go.Scatter(
                name='short hint', x=[date, to_date], y=[short_target, short_target],
                mode='lines', line=dict(width=2, color='green', dash='dot'),
                visible='legendonly' if not enable else None,
            ),
            row=1, col=1,
        )
