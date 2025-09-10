import pandas as pd
from guru.util import _pick_rolling_n_pst_reversed


# sz: 1/3/5/10/15/20/25/30
def _calculate_hits(stock_df: pd.DataFrame, sz: int, key: str) -> list:
    close = stock_df['close']

    incr_psts = []

    for idx in stock_df.index[sz:]:
        if close[idx] <= close[idx - sz]:
            incr_psts.append((None, idx))
            continue
        incr_pst = (close[idx] - close[idx - sz]) / close[idx - sz]
        incr_psts.append((incr_pst, idx))

    return _pick_rolling_n_pst_reversed(stock_df, incr_psts, key)
