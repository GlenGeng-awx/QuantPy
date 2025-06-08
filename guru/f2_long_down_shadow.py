import pandas as pd
from guru.util import _pick_10pst

KEY = 'long down shadow'


def calculate_hits(stock_df: pd.DataFrame) -> list:
    _open, close, low = stock_df['open'], stock_df['close'], stock_df['low']

    down_shadows = []
    for idx in stock_df.index:
        down_shadow = min(_open[idx], close[idx]) - low[idx]
        down_shadows.append((down_shadow, idx))

    return _pick_10pst(stock_df, down_shadows)
