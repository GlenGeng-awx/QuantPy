import pandas as pd
from guru.util import _pick_rolling_n_pst_reversed

KEY = 'will crash'
SZ = 15


def calculate_hits(stock_df: pd.DataFrame) -> list:
    close = stock_df['close']

    crash_psts = []

    for idx in stock_df.index[:-SZ]:
        if close[idx] <= close[idx + SZ]:
            crash_psts.append((None, idx))
            continue
        crash_pst = (close[idx] - close[idx + SZ]) / close[idx]
        crash_psts.append((crash_pst, idx))

    return _pick_rolling_n_pst_reversed(stock_df, crash_psts, KEY)
