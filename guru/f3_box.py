import pandas as pd
from guru.util import _pick_rolling_n_pst


# sz: 5/10/15
def _calculate_hits(stock_df: pd.DataFrame, sz: int, key: str) -> list:
    close = stock_df['close']

    box_psts = []

    for idx in stock_df.index[sz:]:
        max_close = close.loc[idx - sz + 1:idx].max()
        min_close = close.loc[idx - sz + 1:idx].min()
        box_pst = (max_close - min_close) / min_close
        box_psts.append((box_pst, idx))

    return _pick_rolling_n_pst(stock_df, box_psts, key)
