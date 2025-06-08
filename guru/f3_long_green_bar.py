import pandas as pd
from guru.util import _pick_10pst

KEY = 'long green bar'


def calculate_hits(stock_df: pd.DataFrame) -> list:
    _open, close = stock_df['open'], stock_df['close']

    green_bars = []
    for idx in stock_df.index:
        if close[idx] > _open[idx]:
            continue
        green_bar = (_open[idx] - close[idx]) / _open[idx]
        green_bars.append((green_bar, idx))

    return _pick_10pst(stock_df, green_bars)
