import pandas as pd
import plotly.graph_objects as go


def calculate_ema(s: pd.Series, period: int, smoother: int = 2) -> pd.Series:
    indices = []
    y = []

    prev_ema = 0
    coefficient = smoother / (1 + period)  # 2 / (1 + n)

    for idx, value in s.items():
        ema = value * coefficient + prev_ema * (1 - coefficient)
        prev_ema = ema

#        print(f'idx={idx}, ema{period}={ema:.3f}')
        indices.append(idx)
        y.append(ema)

    return pd.Series(y, index=indices)


class EMA:
    def __init__(self, fig: go.Figure, stock_df: pd.DataFrame):
        self.fig = fig
        self.stock_df = stock_df

        self.smoother = 2

    def build_graph_impl(self, period: int, color: str):
        ema = calculate_ema(self.stock_df['close'], period)
        ema = ema.iloc[period:]

        x = [self.stock_df.loc[idx]['Date'] for idx in ema.index]

        self.fig.add_trace(
            go.Scatter(
                name=f'EMA-{period}',
                x=x,
                y=ema,
                mode='lines',
                line=dict(width=0.75, color=color),
                visible='legendonly' if period != 20 else None,
            )
        )

    def build_graph(self):
        self.build_graph_impl(5, 'black')
        self.build_graph_impl(10, 'orange')
        self.build_graph_impl(20, 'green')
