import pandas as pd
from guru.util import _pick_rolling_n_pst_reversed

KEY = 'long green range'


def calculate_hits(stock_df: pd.DataFrame) -> list:
    _open, close = stock_df['open'], stock_df['close']
    high, low = stock_df['high'], stock_df['low']

    green_ranges = []
    for idx in stock_df.index:
        if close[idx] > _open[idx]:
            green_ranges.append((None, idx))
            continue
        green_range = (high[idx] - low[idx]) / low[idx]
        green_ranges.append((green_range, idx))

    return _pick_rolling_n_pst_reversed(stock_df, green_ranges, KEY)
