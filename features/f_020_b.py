import pandas as pd
from features.util import STEP

KEY = 'price incr 3d'
VAL = 20 * STEP


def execute(stock_df: pd.DataFrame, **kwargs):
    close = stock_df['close']
    _open = stock_df['open']

    indices = []

    for idx in close.index[2:]:
        if close[idx] > close[idx - 1] > close[idx - 2]     \
                and (_open[idx] < close[idx])               \
                and (_open[idx - 1] < close[idx - 1])       \
                and (_open[idx - 2] < close[idx - 2]):
            indices.append(idx)

    s = pd.Series([True] * len(indices), index=indices)
    stock_df[KEY] = s.reindex(stock_df.index, fill_value=False)
