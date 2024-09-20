import pandas as pd
from features.util import STEP

KEY = 'short lower shadow'
VAL = 21 * STEP


def execute(stock_df: pd.DataFrame, **kwargs):
    _open = stock_df['open']
    close = stock_df['close']
    low = stock_df['low']

    indices = []

    for idx in _open.index:
        if low[idx] * 1.005 > min(_open[idx], close[idx]):
            indices.append(idx)

    s = pd.Series([True] * len(indices), index=indices)
    stock_df[KEY] = s.reindex(stock_df.index, fill_value=False)
