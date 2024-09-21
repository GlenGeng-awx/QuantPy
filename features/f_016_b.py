import pandas as pd
from features.util import STEP

KEY = 'long lower shadow'
VAL = 16 * STEP


def execute(stock_df: pd.DataFrame, **kwargs):
    _open = stock_df['open']
    close = stock_df['close']
    low = stock_df['low']

    indices = []

    for idx in _open.index:
        min_price = min(_open[idx], close[idx])
        max_price = max(_open[idx], close[idx])

        if low[idx] * 1.03 < min_price and (min_price - low[idx]) > 1.5 * (max_price - min_price):
            indices.append(idx)

    s = pd.Series([True] * len(indices), index=indices)
    stock_df[KEY] = s.reindex(stock_df.index, fill_value=False)
