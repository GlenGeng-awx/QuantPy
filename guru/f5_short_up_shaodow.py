import pandas as pd
from guru.util import _pick_rolling_n_pst

KEY = 'short up shadow'


def calculate_hits(stock_df: pd.DataFrame) -> list:
    _open, close, high = stock_df['open'], stock_df['close'], stock_df['high']

    up_shadows = []
    for idx in stock_df.index:
        top = max(_open[idx], close[idx])
        up_shadow = (high[idx] - top) / top
        up_shadows.append((up_shadow, idx))

    return _pick_rolling_n_pst(stock_df, up_shadows, KEY)
