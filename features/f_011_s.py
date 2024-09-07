import pandas as pd
from features.util import STEP, DELTA

KEY = 'decr 10 pst in last 3d'
VAL = 11 * STEP + DELTA


def execute(stock_df: pd.DataFrame, **kwargs):
    close = stock_df['close']

    indices = []

    for idx in close.index[3:]:
        if close[idx] < close[idx - 3] * 0.9:
            indices.append(idx)

    s = pd.Series([True] * len(indices), index=indices)
    stock_df[KEY] = s.reindex(stock_df.index, fill_value=False)
