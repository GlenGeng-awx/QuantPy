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
        min_price = min(_open[idx], close[idx])
        max_price = max(_open[idx], close[idx])

        if high[idx] > max_price * 1.03 and (high[idx] - max_price) > 1.5 * (max_price - min_price):
            indices.append(idx)

    s = pd.Series([True] * len(indices), index=indices)
    stock_df[KEY] = s.reindex(stock_df.index, fill_value=False)
