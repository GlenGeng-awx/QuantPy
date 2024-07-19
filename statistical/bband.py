import pandas as pd
import plotly.graph_objects as go


class BBand:
    def __init__(self, fig: go.Figure, stock_df: pd.DataFrame, n: int = 20, k: int = 2):
        self.fig = fig
        self.stock_df = stock_df

        self.n = n
        self.k = k

    def calculate_bband(self):
        indices = []
        x = []
        y = []
        y_upper = []
        y_lower = []

        length = self.stock_df.shape[0]
        for pos in range(length):
            row = self.stock_df.iloc[pos]
            idx, date, close = row.name, row['Date'], row['close']

            if pos < self.n:
                continue

            # [from_pos, to_pos]
            from_pos = pos - self.n + 1
            to_pos = pos + 1

            mean = self.stock_df.iloc[from_pos:to_pos]['close'].mean()
            std = self.stock_df.iloc[from_pos:to_pos]['close'].std()

            up = mean + self.k * std
            down = mean - self.k * std

            indices.append(idx)
            x.append(date)
            y.append(mean)
            y_upper.append(up)
            y_lower.append(down)

            # print(f'{date}, mid={mean:.3f}, std={std:.3f}, up={up:.3f}, down={down:.3f}')

        return indices, x, y, y_upper, y_lower

    def build_graph(self, enable=False):
        _, x, y, y_upper, y_lower = self.calculate_bband()

        self.fig.add_trace(
            go.Scatter(
                name=f'BBand - up',
                x=x,
                y=y_upper,
                mode='lines',
                line=dict(width=0.75, color='red'),
                visible=None if enable else 'legendonly',
            )
        )

        self.fig.add_trace(
            go.Scatter(
                name=f'BBand - mid',
                x=x,
                y=y,
                mode='lines',
                line=dict(width=0.75, color='black'),
                visible=None if enable else 'legendonly',
            )
        )

        self.fig.add_trace(
            go.Scatter(
                name=f'BBand - down',
                x=x,
                y=y_lower,
                mode='lines',
                line=dict(width=0.75, color='green'),
                visible=None if enable else 'legendonly',
            )
        )
