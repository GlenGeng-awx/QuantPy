import pandas as pd
from features.util import STEP

KEY = 'incr 10 pst in last 3d'
VAL = 11 * STEP


def execute(stock_df: pd.DataFrame, **kwargs):
    close = stock_df['close']

    indices = []

    for idx in close.index[3:]:
        if close[idx] > close[idx - 3] * 1.1:
            indices.append(idx)

    s = pd.Series([True] * len(indices), index=indices)
    stock_df[KEY] = s.reindex(stock_df.index, fill_value=False)
