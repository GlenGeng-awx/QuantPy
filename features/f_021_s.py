import pandas as pd
from features.util import STEP, DELTA

KEY = 'short lower shadow'
VAL = 21 * STEP + DELTA


def execute(stock_df: pd.DataFrame, **kwargs):
    _open = stock_df['open']
    close = stock_df['close']
    low = stock_df['low']

    pst = []
    for idx in _open.index:
        if _open[idx] > close[idx]:
            pst.append(close[idx] / low[idx])

    pst.sort()
    if len(pst) < 10:
        return

    threshold = pst[len(pst) // 10]
    print(f'short lower shadow threshold: {(threshold - 1) * 100:.2f}%')

    indices = []

    for idx in _open.index:
        if _open[idx] > close[idx] and low[idx] * threshold > close[idx]:
            indices.append(idx)

    s = pd.Series([True] * len(indices), index=indices)
    stock_df[KEY] = s.reindex(stock_df.index, fill_value=False)
