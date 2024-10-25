import pandas as pd
from features.util import STEP

KEY = 'short upper shadow'
VAL = 21 * STEP
RECALL_DAYS = 2


def execute(stock_df: pd.DataFrame, **kwargs):
    _open = stock_df['open']
    close = stock_df['close']
    high = stock_df['high']

    pst = []
    for idx in _open.index:
        if _open[idx] < close[idx]:
            pst.append(high[idx] / close[idx])

    pst.sort()
    if len(pst) < 10:
        return

    threshold = pst[len(pst) // 10]
    print(f'short upper shadow threshold: {(threshold - 1) * 100:.2f}%')

    indices = []

    for idx in _open.index:
        if _open[idx] < close[idx] and high[idx] < close[idx] * threshold:
            indices.append(idx)

    s = pd.Series([True] * len(indices), index=indices)
    stock_df[KEY] = s.reindex(stock_df.index, fill_value=False)
