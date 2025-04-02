import pandas as pd
import plotly.graph_objects as go

MA_5 = 'ma_5'
MA_20 = 'ma_20'
MA_60 = 'ma_60'
MA_120 = 'ma_120'


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
        stock_df[MA_20] = calculate_ma(stock_df['close'], 20)
        stock_df[MA_60] = calculate_ma(stock_df['close'], 60)
        stock_df[MA_120] = calculate_ma(stock_df['close'], 120)

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

    def build_graph(self, fig: go.Figure, enable=False):
        last_close = self.stock_df['close'].iloc[-1]

        last_ma20 = self.stock_df[MA_20].iloc[-1]
        last_ma60 = self.stock_df[MA_60].iloc[-1]
        last_ma120 = self.stock_df[MA_120].iloc[-1]

        min_diff = min(abs(last_close - last_ma20), abs(last_close - last_ma60), abs(last_close - last_ma120))

        self._build_graph(fig, MA_5, 'red')
        self._build_graph(fig, MA_20, 'orange', enable=enable and abs(last_close - last_ma20) == min_diff)
        self._build_graph(fig, MA_60, 'black', enable=enable and abs(last_close - last_ma60) == min_diff)
        self._build_graph(fig, MA_120, 'blue', enable=enable and abs(last_close - last_ma120) == min_diff)
