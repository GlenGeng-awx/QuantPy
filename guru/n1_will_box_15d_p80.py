import pandas as pd
from guru.util import _pick_rolling_n_pst

KEY = 'will box 15d p80'
SZ = 15


def calculate_hits(stock_df: pd.DataFrame) -> list:
    close = stock_df['close']

    box_psts = []

    for idx in stock_df.index[:-SZ]:
        max_close = close.loc[idx:idx + SZ].max()
        min_close = close.loc[idx:idx + SZ].min()
        box_pst = (max_close - min_close) / min_close
        box_psts.append((box_pst, idx))

    return _pick_rolling_n_pst(stock_df, box_psts, KEY, n=0.2)
