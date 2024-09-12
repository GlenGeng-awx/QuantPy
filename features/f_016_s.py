import pandas as pd
from features.util import STEP, DELTA

KEY = 'long upper shadow'
VAL = 16 * STEP + DELTA


def execute(stock_df: pd.DataFrame, **kwargs):
    _open = stock_df['open']
    close = stock_df['close']
    high = stock_df['high']

    indices = []

    for idx in _open.index:
        if high[idx] > max(_open[idx], close[idx]) * 1.035:
            indices.append(idx)

    s = pd.Series([True] * len(indices), index=indices)
    stock_df[KEY] = s.reindex(stock_df.index, fill_value=False)
