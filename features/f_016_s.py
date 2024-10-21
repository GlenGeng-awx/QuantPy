import pandas as pd
from features.util import STEP, DELTA

KEY = 'long upper shadow'
VAL = 16 * STEP + DELTA


def execute(stock_df: pd.DataFrame, **kwargs):
    _open = stock_df['open']
    close = stock_df['close']
    high = stock_df['high']

    pst = []
    for idx in _open.index:
        max_price = max(_open[idx], close[idx])
        pst.append(high[idx] / max_price)

    pst.sort()
    if len(pst) < 10:
        return

    threshold = pst[-len(pst) // 10]
    print(f'long upper shadow threshold: {(threshold - 1) * 100:.2f}%')

    indices = []

    for idx in _open.index:
        max_price = max(_open[idx], close[idx])

        if max_price * threshold < high[idx]:
            indices.append(idx)

    s = pd.Series([True] * len(indices), index=indices)
    stock_df[KEY] = s.reindex(stock_df.index, fill_value=False)
