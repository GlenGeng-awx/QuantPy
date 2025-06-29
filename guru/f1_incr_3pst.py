import pandas as pd
from guru.util import _pick_rolling_n_pst_reversed

KEY = 'incr 3pst'


def calculate_hits(stock_df: pd.DataFrame) -> list:
    close = stock_df['close']

    incr_psts = []

    for idx in stock_df.index[1:]:
        if close[idx] <= close[idx - 1]:
            incr_psts.append((None, idx))
            continue
        incr_pst = (close[idx] - close[idx - 1]) / close[idx - 1]
        incr_psts.append((incr_pst, idx))

    return _pick_rolling_n_pst_reversed(stock_df, incr_psts, KEY)
