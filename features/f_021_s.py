import pandas as pd
from features.util import STEP, DELTA

KEY = 'decr with short lower shadow'
VAL = 21 * STEP + DELTA


def execute(stock_df: pd.DataFrame, **kwargs):
    _open = stock_df['open']
    close = stock_df['close']
    low = stock_df['low']

    indices = []

    for idx in _open.index:
        if _open[idx] > close[idx] and low[idx] * 1.005 > close[idx]:
            indices.append(idx)

    s = pd.Series([True] * len(indices), index=indices)
    stock_df[KEY] = s.reindex(stock_df.index, fill_value=False)
