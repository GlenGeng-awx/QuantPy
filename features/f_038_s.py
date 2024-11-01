import pandas as pd
from features.common import STEP, DELTA

KEY = 'real green bar'
VAL = 38 * STEP + DELTA
RECALL_DAYS = 1


def execute(stock_df: pd.DataFrame, **kwargs):
    _open = stock_df['open']
    close = stock_df['close']

    indices = []

    for idx in close.index[1:]:
        if close[idx - 1] > close[idx] and _open[idx] > close[idx]:
            indices.append(idx)

    s = pd.Series([True] * len(indices), index=indices)
    stock_df[KEY] = s.reindex(stock_df.index, fill_value=False)
