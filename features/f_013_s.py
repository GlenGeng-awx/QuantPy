import pandas as pd
from features.common import STEP, DELTA

KEY = 'yesterday max of last 20d'
VAL = 13 * STEP + DELTA
RECALL_DAYS = 3


def yesterday_is_max_of_last_n_days(stock_df: pd.DataFrame, n: int, output_key):
    close = stock_df['close']

    indices = []

    for idx in close.index[n:]:
        if close.loc[idx - 1] == close.loc[idx - n:idx].max():
            indices.append(idx)

    s = pd.Series([True] * len(indices), index=indices)
    stock_df[output_key] = s.reindex(stock_df.index, fill_value=False)


def execute(stock_df: pd.DataFrame, **kwargs):
    yesterday_is_max_of_last_n_days(stock_df, 20, KEY)
