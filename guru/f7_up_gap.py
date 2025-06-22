import pandas as pd
from guru.util import _pick_rolling_n_pst_reversed

KEY = 'up gap'


def calculate_hits(stock_df: pd.DataFrame) -> list:
    close, high, low = stock_df['close'], stock_df['high'], stock_df['low']

    up_gaps = []
    for idx in stock_df.index[1:]:
        if low[idx] <= high[idx - 1]:
            up_gaps.append((None, idx))
            continue
        up_gap = (low[idx] - high[idx - 1]) / close[idx - 1]
        up_gaps.append((up_gap, idx))

    return _pick_rolling_n_pst_reversed(stock_df, up_gaps, KEY, n=0.3)
