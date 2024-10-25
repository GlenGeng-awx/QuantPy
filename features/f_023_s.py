import pandas as pd
from features.util import STEP, DELTA
from features.f_023_b import get_below_sr_level

KEY = 'down to sr level'
VAL = 23 * STEP + DELTA
RECALL_DAYS = 2


def execute(stock_df: pd.DataFrame, **kwargs):
    close = stock_df['close']

    indices = []

    for idx in close.index[1:]:
        below_sr_level = get_below_sr_level(stock_df, idx)
        if below_sr_level is None:
            continue

        if close[idx - 1] > close[idx] and close[idx] < below_sr_level * 1.03:
            indices.append(idx)

    s = pd.Series([True] * len(indices), index=indices)
    stock_df[KEY] = s.reindex(stock_df.index, fill_value=False)
