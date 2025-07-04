import pandas as pd
from guru.util import _pick_rolling_n_pst_reversed

KEY = 'long red bar'


def calculate_hits(stock_df: pd.DataFrame) -> list:
    _open, close = stock_df['open'], stock_df['close']

    red_bars = []
    for idx in stock_df.index:
        if close[idx] < _open[idx]:
            red_bars.append((None, idx))
            continue
        red_bar = (close[idx] - _open[idx]) / _open[idx]
        red_bars.append((red_bar, idx))

    return _pick_rolling_n_pst_reversed(stock_df, red_bars, KEY)
