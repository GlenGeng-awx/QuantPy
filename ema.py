import pandas as pd
import plotly.graph_objects as go


class EMA:
    def __init__(self, fig: go.Figure, stock_df: pd.DataFrame):
        self.fig = fig
        self.stock_df = stock_df

        self.smoother = 2

    def calculate_ema(self, period: int):
        coefficient = self.smoother / (1 + period)

        x = []
        y = []

        prev_ema = 0

        length = self.stock_df.shape[0]
        for pos in range(period, length):
            row = self.stock_df.iloc[pos]
            date, close = row['Date'], row['close']

            ema = close * coefficient + prev_ema * (1 - coefficient)

            x.append(date)
            y.append(ema)

            prev_ema = ema

        return x, y

    def build_graph_impl(self, period: int, color: str):
        x, y = self.calculate_ema(period)

        self.fig.add_trace(
            go.Scatter(
                name=f'EMA-{period}',
                x=x,
                y=y,
                mode='lines',
                line=dict(width=0.75, color=color),
                visible='legendonly',
            )
        )

    def build_graph(self):
        self.build_graph_impl(5, 'black')
        self.build_graph_impl(10, 'orange')
        self.build_graph_impl(20, 'green')
