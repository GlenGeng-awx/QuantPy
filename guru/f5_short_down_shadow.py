import pandas as pd
from guru.util import _pick_rolling_10pst

KEY = 'short down shadow'


def calculate_hits(stock_df: pd.DataFrame) -> list:
    _open, close, low = stock_df['open'], stock_df['close'], stock_df['low']

    down_shadows = []
    for idx in stock_df.index:
        bottom = min(_open[idx], close[idx])
        down_shadow = (bottom - low[idx]) / bottom
        down_shadows.append((down_shadow, idx))

    return _pick_rolling_10pst(stock_df, down_shadows, KEY)
