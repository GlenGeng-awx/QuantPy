import pandas as pd
from features.util import STEP, DELTA

KEY = 'decr +8 pst'
VAL = 15 * STEP + DELTA


def execute(stock_df: pd.DataFrame, **kwargs):
    close = stock_df['close']

    indices = []

    for idx in close.index[1:]:
        if close.loc[idx] <= close.loc[idx - 1] * 0.92:
            indices.append(idx)

    s = pd.Series([True] * len(indices), index=indices)
    stock_df[KEY] = s.reindex(stock_df.index, fill_value=False)
