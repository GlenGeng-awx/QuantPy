import pandas as pd
from guru.util import _pick_rolling_n_pst_reversed
from guru.n0_common import get_key, get_ratio, get_size

TARGET = 'will crash'


def calculate_hits(stock_df: pd.DataFrame, mode: str) -> (str, list):
    sz = get_size()
    close = stock_df['close']

    crash_psts = []

    for idx in stock_df.index[:-sz]:
        if close[idx] <= close[idx + sz]:
            crash_psts.append((None, idx))
            continue
        crash_pst = (close[idx] - close[idx + sz]) / close[idx]
        crash_psts.append((crash_pst, idx))

    key = get_key(TARGET, mode)
    ratio = get_ratio(mode)

    return key, _pick_rolling_n_pst_reversed(stock_df, crash_psts, key, ratio=ratio)
