import pandas as pd
from guru.util import _pick_rolling_n_pst_reversed

KEY = 'positive iv'
SZ = 15


def calculate_hits(stock_df: pd.DataFrame) -> list:
    close = stock_df['close']

    positive_ivs = []

    for idx in stock_df.index[:-SZ]:
        max_close = stock_df.loc[idx:idx + SZ]['close'].max()
        positive_iv = (max_close - close[idx]) / close[idx]
        positive_ivs.append((positive_iv, idx))

    return _pick_rolling_n_pst_reversed(stock_df, positive_ivs, KEY, n=0.1, rolling_size=100)
