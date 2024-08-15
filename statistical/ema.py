import pandas as pd
import plotly.graph_objects as go

EMA_5 = 'ema_5'
EMA_10 = 'ema_10'
EMA_12 = 'ema_12'
EMA_20 = 'ema_20'
EMA_26 = 'ema_26'


def calculate_ema(s: pd.Series, period: int, smoother: int = 2) -> pd.Series:
    y = []

    coefficient = smoother / (1 + period)  # 2 / (1 + n)
    prev_ema = s.iloc[:period].mean()

    for pos in range(len(s)):
        if pos < period:
            y.append(prev_ema)
            continue

        ema = s.iloc[pos] * coefficient + prev_ema * (1 - coefficient)
        prev_ema = ema

        y.append(ema)

    return pd.Series(y, index=s.index)


class EMA:
    def __init__(self, stock_df: pd.DataFrame):
        self.stock_df = stock_df
        self.smoother = 2

        stock_df[EMA_5] = calculate_ema(stock_df['close'], 5)
        stock_df[EMA_12] = calculate_ema(stock_df['close'], 12)
        stock_df[EMA_10] = calculate_ema(stock_df['close'], 10)
        stock_df[EMA_20] = calculate_ema(stock_df['close'], 20)
        stock_df[EMA_26] = calculate_ema(stock_df['close'], 26)

    def _build_graph(self, fig: go.Figure, ema_type: str, color: str, enable=False):
        ema = self.stock_df[ema_type]
        dates = self.stock_df.loc[ema.index]['Date']

        fig.add_trace(
            go.Scatter(
                name=f'{ema_type.replace("_", "-").upper()}',
                x=dates,
                y=ema,
                mode='lines',
                line=dict(width=0.75, color=color),
                visible=None if enable else 'legendonly',
            )
        )

    def build_graph(self, fig: go.Figure, enable=False):
        self._build_graph(fig, EMA_5, 'black')  # always disable
        self._build_graph(fig, EMA_10, 'orange', enable)
        self._build_graph(fig, EMA_12, 'blue')
        self._build_graph(fig, EMA_20, 'green')
        self._build_graph(fig, EMA_26, 'purple')
