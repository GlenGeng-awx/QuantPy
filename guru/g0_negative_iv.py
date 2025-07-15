import pandas as pd
from guru.util import _pick_rolling_n_pst_reversed

KEY = 'negative iv'
SZ = 15


def calculate_hits(stock_df: pd.DataFrame) -> list:
    close = stock_df['close']

    negative_ivs = []

    for idx in stock_df.index[:-SZ]:
        if close[idx] <= close[idx + SZ]:
            negative_ivs.append((None, idx))
            continue
        negative_iv = (close[idx] - close[idx + SZ]) / close[idx]
        negative_ivs.append((negative_iv, idx))

    return _pick_rolling_n_pst_reversed(stock_df, negative_ivs, KEY, n=0.15, rolling_size=100)
