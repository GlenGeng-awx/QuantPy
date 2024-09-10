import pandas as pd
from features.util import STEP

KEY = 'incr 20 pst in last 10d'
VAL = 12 * STEP


def execute(stock_df: pd.DataFrame, **kwargs):
    close = stock_df['close']

    indices = []

    for idx in close.index[10:]:
        if close[idx] > close[idx - 10] * 1.2:
            indices.append(idx)

    s = pd.Series([True] * len(indices), index=indices)
    stock_df[KEY] = s.reindex(stock_df.index, fill_value=False)