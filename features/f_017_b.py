import pandas as pd
from features.util import STEP

KEY = 'long red bar'
VAL = 17 * STEP
RECALL_DAYS = 2


def execute(stock_df: pd.DataFrame, **kwargs):
    _open = stock_df['open']
    close = stock_df['close']

    pst = []
    for idx in _open.index:
        if _open[idx] < close[idx]:
            pst.append(close[idx] / _open[idx])

    pst.sort()
    if len(pst) < 10:
        return

    threshold = pst[-len(pst) // 10]
    print(f'long red bar threshold: {(threshold - 1) * 100:.2f}%')

    indices = []

    for idx in _open.index:
        if _open[idx] * threshold <= close[idx]:
            indices.append(idx)

    s = pd.Series([True] * len(indices), index=indices)
    stock_df[KEY] = s.reindex(stock_df.index, fill_value=False)
