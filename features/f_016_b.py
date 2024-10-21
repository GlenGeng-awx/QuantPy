import pandas as pd
from features.util import STEP

KEY = 'long lower shadow'
VAL = 16 * STEP


def execute(stock_df: pd.DataFrame, **kwargs):
    _open = stock_df['open']
    close = stock_df['close']
    low = stock_df['low']

    pst = []
    for idx in _open.index:
        min_price = min(_open[idx], close[idx])
        pst.append(min_price / low[idx])

    pst.sort()
    if len(pst) < 10:
        return

    threshold = pst[-len(pst) // 10]
    print(f'long lower shadow threshold: {(threshold - 1) * 100:.2f}%')

    indices = []

    for idx in _open.index:
        min_price = min(_open[idx], close[idx])

        if low[idx] * threshold < min_price:
            indices.append(idx)

    s = pd.Series([True] * len(indices), index=indices)
    stock_df[KEY] = s.reindex(stock_df.index, fill_value=False)
