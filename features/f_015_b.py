import pandas as pd
from features.util import STEP

KEY = 'incr +8 pst'
VAL = 15 * STEP


def execute(stock_df: pd.DataFrame, **kwargs):
    close = stock_df['close']

    indices = []

    for idx in close.index[1:]:
        if close.loc[idx] >= close.loc[idx - 1] * 1.08:
            indices.append(idx)

    s = pd.Series([True] * len(indices), index=indices)
    stock_df[KEY] = s.reindex(stock_df.index, fill_value=False)
