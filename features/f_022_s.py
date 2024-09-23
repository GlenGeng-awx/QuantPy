import pandas as pd
from features.util import STEP, DELTA
from features.f_022_b import get_above_sr_level

KEY = 'down away sr level'
VAL = 22 * STEP + DELTA


def execute(stock_df: pd.DataFrame, **kwargs):
    close = stock_df['close']

    indices = []

    for idx in close.index[1:]:
        above_sr_level = get_above_sr_level(stock_df, idx)
        if above_sr_level is None:
            continue

        if close[idx] < close[idx - 1] and close[idx] * 1.05 > above_sr_level:
            indices.append(idx)

    s = pd.Series([True] * len(indices), index=indices)
    stock_df[KEY] = s.reindex(stock_df.index, fill_value=False)
