import pandas as pd
from guru.util import _pick_rolling_n_pst_reversed

KEY = 'will spike'
SZ = 15


def calculate_hits(stock_df: pd.DataFrame) -> list:
    close = stock_df['close']

    spike_psts = []

    for idx in stock_df.index[:-SZ]:
        if close[idx] >= close[idx + SZ]:
            spike_psts.append((None, idx))
            continue
        spike_pst = (close[idx + SZ] - close[idx]) / close[idx]
        spike_psts.append((spike_pst, idx))

    return _pick_rolling_n_pst_reversed(stock_df, spike_psts, KEY, n=0.15, rolling_size=100)
