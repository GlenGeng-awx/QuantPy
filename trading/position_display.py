import pandas as pd
import plotly.graph_objects as go
from util import get_idx_by_date
from .position import POSITION


class PositionDisplay:
    def __init__(self, stock_df: pd.DataFrame, stock_name: str):
        self.stock_df = stock_df
        self.stock_name = stock_name

    def build_graph_impl(self, fig: go.Figure, enable: bool, category: str, color: str, size: int):
        x = []
        y = []

        records = POSITION.get(self.stock_name, [])
        for (date, _category) in records:
            if date > self.stock_df.iloc[-1]['Date']:
                print(f'position {self.stock_name} {date} is out of range')
                continue

            if _category == category:
                x.append(date)

                idx = get_idx_by_date(self.stock_df, date)
                close = self.stock_df.loc[idx]['close']

                if category == 'CALL':
                    theta = 1  # 1.05
                    y.append(close * theta)
                elif category == 'PUT':
                    theta = 1  # 0.95
                    y.append(close * theta)
                elif category == 'CLOSE':
                    y.append(close)
                else:
                    raise ValueError(f'Unknown category: {category}')

        if len(x) == 0:
            return

        fig.add_trace(
            go.Scatter(
                name=category, x=x, y=y,
                mode='markers',
                marker=dict(color=color, size=size),
                visible='legendonly' if not enable else None,
            ),
            row=1, col=1,
        )

    def build_graph(self, fig: go.Figure, enable: bool):
        self.build_graph_impl(fig, enable, 'CALL', 'red', 10)
        self.build_graph_impl(fig, enable, 'PUT', 'green', 10)
        self.build_graph_impl(fig, enable, 'CLOSE', 'black', 8)
