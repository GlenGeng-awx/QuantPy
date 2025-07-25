import pandas as pd
from technical.volume import VOLUME_REG
from guru.util import _pick_rolling_n_pst


# sz: 3/5/10/15
def _calculate_hits(stock_df: pd.DataFrame, sz: int, key: str) -> list:
    vol = stock_df[VOLUME_REG]

    box_psts = []

    for idx in stock_df.index[sz:]:
        max_close = vol.loc[idx - sz + 1:idx].max()
        min_close = vol.loc[idx - sz + 1:idx].min()
        box_pst = (max_close - min_close) / min_close
        box_psts.append((box_pst, idx))

    return _pick_rolling_n_pst(stock_df, box_psts, key)
