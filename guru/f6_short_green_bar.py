import pandas as pd
from guru.util import _pick_rolling_n_pst

KEY = 'short green bar'


def calculate_hits(stock_df: pd.DataFrame) -> list:
    _open, close = stock_df['open'], stock_df['close']

    green_bars = []
    for idx in stock_df.index:
        if close[idx] > _open[idx]:
            green_bars.append((None, idx))
            continue
        green_bar = (_open[idx] - close[idx]) / _open[idx]
        green_bars.append((green_bar, idx))

    return _pick_rolling_n_pst(stock_df, green_bars, KEY)
