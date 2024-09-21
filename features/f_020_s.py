import pandas as pd
from features.util import STEP, DELTA

KEY = 'price decr 5d'
VAL = 20 * STEP + DELTA


def execute(stock_df: pd.DataFrame, **kwargs):
    close = stock_df['close']

    indices = []

    for idx in close.index[4:]:
        if close[idx] < close[idx - 1] < close[idx - 2] < close[idx - 3] < close[idx - 4]:
            indices.append(idx)

    s = pd.Series([True] * len(indices), index=indices)
    stock_df[KEY] = s.reindex(stock_df.index, fill_value=False)
