import pandas as pd
from features.util import STEP

KEY = 'long red bar'
VAL = 17 * STEP


def execute(stock_df: pd.DataFrame, **kwargs):
    _open = stock_df['open']
    close = stock_df['close']

    indices = []

    for idx in _open.index:
        if _open[idx] * 1.05 <= close[idx]:
            indices.append(idx)

    s = pd.Series([True] * len(indices), index=indices)
    stock_df[KEY] = s.reindex(stock_df.index, fill_value=False)
