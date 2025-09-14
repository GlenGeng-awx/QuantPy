import pandas as pd
import plotly.graph_objects as go

MA_5 = 'ma_5'
MA_10 = 'ma_10'
MA_20 = 'ma_20'
MA_60 = 'ma_60'
MA_120 = 'ma_120'
MA_200 = 'ma_200'
MA_250 = 'ma_250'


def calculate_ma(s: pd.Series, period: int) -> pd.Series:
    indices = []
    y = []

    for idx in s.index[period:]:
        indices.append(idx)

        # [idx - period + 1, idx]
        mean = s.loc[idx - period + 1:idx].mean()
        y.append(mean)

    return pd.Series(y, index=indices)


class MA:
    def __init__(self, stock_df: pd.DataFrame):
        self.stock_df = stock_df

        stock_df[MA_5] = calculate_ma(stock_df['close'], 5)
        stock_df[MA_10] = calculate_ma(stock_df['close'], 10)
        stock_df[MA_20] = calculate_ma(stock_df['close'], 20)
        stock_df[MA_60] = calculate_ma(stock_df['close'], 60)
        stock_df[MA_120] = calculate_ma(stock_df['close'], 120)
        stock_df[MA_200] = calculate_ma(stock_df['close'], 200)
        stock_df[MA_250] = calculate_ma(stock_df['close'], 250)

    def _build_graph(self, fig: go.Figure, ma_type: str, color: str, enable=False):
        ma = self.stock_df[ma_type].dropna()
        dates = self.stock_df.loc[ma.index]['Date']

        fig.add_trace(
            go.Scatter(
                name=f'{ma_type.replace("_", "-").upper()}',
                x=dates,
                y=ma,
                mode='lines',
                line=dict(width=0.75, color=color),
                visible=None if enable else 'legendonly',
            )
        )

    # 5/10/20/60/120/200/250
    def build_graph(self, fig: go.Figure, enable_ma=(False, False, False, False, False, False, False)):
        enable_ma5, enable_ma10, enable_ma20, enable_ma60 = enable_ma[:4]
        enable_ma120, enable_ma200, enable_ma250 = enable_ma[4:]

        self._build_graph(fig, MA_5, 'red', enable=enable_ma5)
        self._build_graph(fig, MA_10, 'green', enable=enable_ma10)
        self._build_graph(fig, MA_20, 'orange', enable=enable_ma20)
        self._build_graph(fig, MA_60, 'black', enable=enable_ma60)
        self._build_graph(fig, MA_120, 'blue', enable=enable_ma120)
        self._build_graph(fig, MA_200, 'purple', enable=enable_ma200)
        self._build_graph(fig, MA_250, 'brown', enable=enable_ma250)
