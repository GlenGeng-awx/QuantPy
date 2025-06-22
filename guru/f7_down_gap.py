import pandas as pd
from guru.util import _pick_rolling_n_pst_reversed

KEY = 'down gap'


def calculate_hits(stock_df: pd.DataFrame) -> list:
    close, high, low = stock_df['close'], stock_df['high'], stock_df['low']

    down_gaps = []
    for idx in stock_df.index[1:]:
        if high[idx] >= low[idx - 1]:
            down_gaps.append((None, idx))
            continue
        down_gap = (low[idx - 1] - high[idx]) / close[idx - 1]
        down_gaps.append((down_gap, idx))

    return _pick_rolling_n_pst_reversed(stock_df, down_gaps, KEY, n=0.3)
