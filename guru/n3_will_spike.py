import pandas as pd
from guru.util import _pick_rolling_n_pst_reversed
from guru.n0_common import get_key, get_ratio, get_size

TARGET = 'will spike'


def calculate_hits(stock_df: pd.DataFrame, mode: str) -> (str, list):
    sz = get_size()
    close = stock_df['close']

    spike_psts = []

    for idx in stock_df.index[:-sz]:
        if close[idx] >= close[idx + sz]:
            spike_psts.append((None, idx))
            continue
        spike_pst = (close[idx + sz] - close[idx]) / close[idx]
        spike_psts.append((spike_pst, idx))

    key = get_key(TARGET, mode)
    ratio = get_ratio(mode)

    return key, _pick_rolling_n_pst_reversed(stock_df, spike_psts, key, ratio=ratio)
