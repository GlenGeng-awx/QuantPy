import pandas as pd
import plotly.graph_objects as go


def calculate_ema(s: pd.Series, period: int, smoother: int = 2) -> pd.Series:
    indices = []
    y = []

    coefficient = smoother / (1 + period)  # 2 / (1 + n)
    prev_ema = s.iloc[:period].mean()

    for idx, value in s.iloc[:period].items():
        indices.append(idx)
        y.append(prev_ema)

    for idx, value in s[period:].items():
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

    def build_graph_impl(self, period: int, color: str, enable=False):
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
                visible=None if enable else 'legendonly',
            )
        )

    def build_graph(self, enable=False):
        self.build_graph_impl(5, 'black')   # always disable
        self.build_graph_impl(10, 'orange', enable)
        self.build_graph_impl(20, 'green', enable)
