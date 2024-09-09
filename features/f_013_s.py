import pandas as pd
from features.util import STEP, DELTA

KEY = 'yesterday is max of last 20d'
VAL = 13 * STEP + DELTA


def execute(stock_df: pd.DataFrame, **kwargs):
    close = stock_df['close']

    indices = []

    for idx in close.index[20:]:
        if close.loc[idx - 1] == close.loc[idx - 20:idx].max():
            indices.append(idx)

    s = pd.Series([True] * len(indices), index=indices)
    stock_df[KEY] = s.reindex(stock_df.index, fill_value=False)
