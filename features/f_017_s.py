import pandas as pd
from features.util import STEP, DELTA

KEY = 'long green bar'
VAL = 17 * STEP + DELTA


def execute(stock_df: pd.DataFrame, **kwargs):
    _open = stock_df['open']
    close = stock_df['close']

    indices = []

    for idx in _open.index:
        if close[idx] * 1.05 <= _open[idx]:
            indices.append(idx)

    s = pd.Series([True] * len(indices), index=indices)
    stock_df[KEY] = s.reindex(stock_df.index, fill_value=False)
