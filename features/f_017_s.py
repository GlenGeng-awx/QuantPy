import pandas as pd
from features.common import STEP, DELTA

KEY = 'long green bar'
VAL = 17 * STEP + DELTA
RECALL_DAYS = 2


def get_green_bar_threshold(stock_df: pd.DataFrame) -> (float, float):
    _open = stock_df['open']
    close = stock_df['close']

    pst = []
    for idx in _open.index:
        if _open[idx] > close[idx]:
            pst.append(_open[idx] / close[idx])

    pst.sort()
    if len(pst) < 10:
        return None, None

    short_threshold = pst[len(pst) // 10]
    long_threshold = pst[-len(pst) // 10]

    print(f'short green bar threshold: {(short_threshold - 1) * 100:.2f}%')
    print(f'long green bar threshold: {(long_threshold - 1) * 100:.2f}%')
    return short_threshold, long_threshold


def execute(stock_df: pd.DataFrame, **kwargs):
    _, long_threshold = get_green_bar_threshold(stock_df)
    if long_threshold is None:
        return

    _open = stock_df['open']
    close = stock_df['close']
    indices = []

    for idx in _open.index:
        if close[idx] * long_threshold <= _open[idx]:
            indices.append(idx)

    s = pd.Series([True] * len(indices), index=indices)
    stock_df[KEY] = s.reindex(stock_df.index, fill_value=False)
