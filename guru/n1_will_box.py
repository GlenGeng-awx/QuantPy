import pandas as pd
from guru.util import _pick_rolling_n_pst
from guru.n0_common import get_key, get_size, get_ratio

TARGET = 'will box'


def calculate_hits(stock_df: pd.DataFrame, mode: str) -> (str, list):
    sz = get_size()
    close = stock_df['close']

    box_psts = []

    for idx in stock_df.index[:-sz]:
        max_close = close.loc[idx:idx + sz].max()
        min_close = close.loc[idx:idx + sz].min()
        box_pst = (max_close - min_close) / min_close
        box_psts.append((box_pst, idx))

    key = get_key(TARGET, mode)
    ratio = get_ratio(mode)

    return key, _pick_rolling_n_pst(stock_df, box_psts, key, ratio=ratio)
