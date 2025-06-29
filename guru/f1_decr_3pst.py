import pandas as pd
from guru.util import _pick_rolling_n_pst_reversed

KEY = 'decr 3pst'


def calculate_hits(stock_df: pd.DataFrame) -> list:
    close = stock_df['close']

    decr_psts = []

    for idx in stock_df.index[1:]:
        if close[idx] >= close[idx - 1]:
            decr_psts.append((None, idx))
            continue
        decr_pst = (close[idx - 1] - close[idx]) / close[idx - 1]
        decr_psts.append((decr_pst, idx))

    return _pick_rolling_n_pst_reversed(stock_df, decr_psts, KEY)
