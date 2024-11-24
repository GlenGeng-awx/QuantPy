import plotly.graph_objects as go
from .position import POSITION


class PositionDisplay:
    def __init__(self, stock_name: str):
        self.stock_name = stock_name

    def build_graph_impl(self, fig: go.Figure, enable: bool, category: str, color: str, size: int):
        records = POSITION.get(self.stock_name, [])

        x = [record[0] for record in records if record[1] == category]  # date
        y = [record[2] for record in records if record[1] == category]  # price

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
        self.build_graph_impl(fig, enable, 'long', 'red', 10)
        self.build_graph_impl(fig, enable, 'short', 'green', 10)
