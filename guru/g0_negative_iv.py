import pandas as pd
from guru.util import _pick_rolling_n_pst_reversed

KEY = 'negative iv'
SZ = 15


def calculate_hits(stock_df: pd.DataFrame) -> list:
    close = stock_df['close']

    negative_ivs = []

    for idx in stock_df.index[:-SZ]:
        min_close = stock_df.loc[idx:idx + SZ]['close'].min()
        negative_iv = (close[idx] - min_close) / close[idx]
        negative_ivs.append((negative_iv, idx))

    return _pick_rolling_n_pst_reversed(stock_df, negative_ivs, KEY, n=0.1, rolling_size=100)
