import pandas as pd
from guru.util import _pick_rolling_n_pst_reversed

KEY = 'will shoot up'
SZ = 15


def calculate_hits(stock_df: pd.DataFrame) -> list:
    close = stock_df['close']

    shoot_up_psts = []

    for idx in stock_df.index[:-SZ]:
        max_close = stock_df.loc[idx:idx + SZ]['close'].max()
        shoot_up_pst = (max_close - close[idx]) / close[idx]
        shoot_up_psts.append((shoot_up_pst, idx))

    return _pick_rolling_n_pst_reversed(stock_df, shoot_up_psts, KEY)
