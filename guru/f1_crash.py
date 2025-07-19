import pandas as pd
from guru.util import _pick_rolling_n_pst_reversed


# sz: 1/3/5/10/15
def _calculate_hits(stock_df: pd.DataFrame, sz: int, key: str) -> list:
    close = stock_df['close']

    decr_psts = []

    for idx in stock_df.index[sz:]:
        if close[idx] >= close[idx - sz]:
            decr_psts.append((None, idx))
            continue
        decr_pst = (close[idx - sz] - close[idx]) / close[idx - sz]
        decr_psts.append((decr_pst, idx))

    return _pick_rolling_n_pst_reversed(stock_df, decr_psts, key)
