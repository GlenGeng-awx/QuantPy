import pandas as pd
from guru.util import _pick_rolling_n_pst_reversed

KEY = 'will shoot down p80'
SZ = 15


def calculate_hits(stock_df: pd.DataFrame) -> list:
    close = stock_df['close']

    shoot_down_psts = []

    for idx in stock_df.index[:-SZ]:
        min_close = stock_df.loc[idx:idx + SZ]['close'].min()
        shoot_down_pst = (close[idx] - min_close) / close[idx]
        shoot_down_psts.append((shoot_down_pst, idx))

    return _pick_rolling_n_pst_reversed(stock_df, shoot_down_psts, KEY, n=0.2)
