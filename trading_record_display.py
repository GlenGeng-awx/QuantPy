import plotly.graph_objects as go
from trading_record import TRADING_RECORDS


class TradingRecordDisplay:
    def __init__(self, fig: go.Figure, stock_name: str, interval: str, visible: bool = False):
        self.fig = fig
        self.stock_name = stock_name
        self.interval = interval
        self.visible = visible

    def add_scatter(self, category: str, color: str, size: int):
        records = TRADING_RECORDS.get(self.stock_name, [])

        x = [record[0] for record in records if record[1] == category]  # date
        y = [record[2] for record in records if record[1] == category]  # price

        if len(x) == 0:
            return

        if self.interval == '1h':
            x = [date + ' 10:30:00-04:00' for date in x]

        self.fig.add_trace(
            go.Scatter(
                name=category,
                x=x,
                y=y,
                mode='markers',
                marker=dict(
                    color=color,
                    size=size
                ),
                visible='legendonly' if not self.visible else None,
            ),
            row=1, col=1,
        )

    def build_graph(self):
        self.add_scatter('buy', 'red', 4)
        self.add_scatter('sell', 'green', 4)
        self.add_scatter('short', 'black', 4)
