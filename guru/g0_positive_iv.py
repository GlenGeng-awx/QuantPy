import pandas as pd
from guru.util import _pick_rolling_n_pst_reversed

KEY = 'positive iv'
SZ = 15


def calculate_hits(stock_df: pd.DataFrame) -> list:
    close = stock_df['close']

    positive_ivs = []

    for idx in stock_df.index[:-SZ]:
        if close[idx] >= close[idx + SZ]:
            positive_ivs.append((None, idx))
            continue
        positive_iv = (close[idx + SZ] - close[idx]) / close[idx]
        positive_ivs.append((positive_iv, idx))

    return _pick_rolling_n_pst_reversed(stock_df, positive_ivs, KEY, n=0.15, rolling_size=100)
