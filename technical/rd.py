import pandas as pd
import plotly.graph_objects as go
from technical.volume import VOLUME

SZ = 40


def _select_bound(pst: list) -> (float, float):
    if len(pst) < 10:
        return None, None
    pst.sort()
    reserved = len(pst) // 10

    short_bound, long_bound = pst[reserved], pst[-reserved]
    return short_bound, long_bound


def get_upper_shadow_bound(stock_df: pd.DataFrame) -> (float, float):
    _open, close, high = stock_df['open'], stock_df['close'], stock_df['high']

    pst = []
    for idx in stock_df.index:
        max_price = max(_open[idx], close[idx])
        pst.append(high[idx] / max_price)
    return _select_bound(pst)


def get_lower_shadow_bound(stock_df: pd.DataFrame) -> (float, float):
    _open, close, low = stock_df['open'], stock_df['close'], stock_df['low']

    pst = []
    for idx in stock_df.index:
        min_price = min(_open[idx], close[idx])
        pst.append(min_price / low[idx])
    return _select_bound(pst)


def filter_up_rd(stock_df: pd.DataFrame, long_upper_shadow_bound: float) -> list:
    volume = stock_df[VOLUME]
    _open, close, high = stock_df['open'], stock_df['close'], stock_df['high']

    indices = []
    for idx in stock_df.index[SZ:]:
        max_price = max(_open[idx], close[idx])
        pst = high[idx] / max_price

        if _open[idx] > high[idx - 1] \
                and high[idx] == high.loc[idx - SZ:idx].max() \
                and volume[idx] == volume.loc[idx - SZ:idx].max() \
                and pst > long_upper_shadow_bound:
            indices.append(idx)
    return indices


def filter_down_rd(stock_df: pd.DataFrame, long_lower_shadow_bound: float) -> list:
    volume = stock_df[VOLUME]
    _open, close, low = stock_df['open'], stock_df['close'], stock_df['low']

    indices = []
    for idx in stock_df.index[SZ:]:
        min_price = min(_open[idx], close[idx])
        pst = min_price / low[idx]

        if _open[idx] < low[idx - 1] \
                and low[idx] == low.loc[idx - SZ:idx].min() \
                and volume[idx] == volume.loc[idx - SZ:idx].max() \
                and pst > long_lower_shadow_bound:
            indices.append(idx)
    return indices


class RD:
    def __init__(self, stock_df: pd.DataFrame, stock_name: str):
        self.stock_df = stock_df
        self.stock_name = stock_name

        _, long_lower_shadow_bound = get_lower_shadow_bound(stock_df)
        _, long_upper_shadow_bound = get_upper_shadow_bound(stock_df)

        print(f'long upper shadow of {stock_name}: {(long_lower_shadow_bound - 1) * 100:.2f}%')
        print(f'long lower shadow of {stock_name}: {(long_upper_shadow_bound - 1) * 100:.2f}%')

        self.up_rd = filter_up_rd(stock_df, long_upper_shadow_bound)
        self.down_rd = filter_down_rd(stock_df, long_lower_shadow_bound)

        print(f'up rd {stock_name}: {self.up_rd}')
        print(f'down rd {stock_name}: {self.down_rd}')

    def build_graph(self, fig: go.Figure, enable=False):
        fig.add_trace(
            go.Scatter(
                name='up rd',
                x=self.stock_df['Date'].loc[self.up_rd],
                y=self.stock_df['high'].loc[self.up_rd],
                text='RD',
                mode='text', textfont=dict(color="green", size=11),
                visible=None if enable else 'legendonly',
            )
        )

        fig.add_trace(
            go.Scatter(
                name='down rd',
                x=self.stock_df['Date'].loc[self.down_rd],
                y=self.stock_df['low'].loc[self.down_rd],
                text='RD',
                mode='text', textfont=dict(color="red", size=11),
                visible=None if enable else 'legendonly',
            )
        )
