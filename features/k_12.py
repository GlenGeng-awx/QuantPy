import pandas as pd
from features.k_11 import get_above_sr_level_min

KEY = 'down away sr level min'
COLOR = 'green'


def execute(stock_df: pd.DataFrame, **kwargs):
    close = stock_df['close']

    indices = []

    for idx in close.index[1:]:
        above_sr_level_min = get_above_sr_level_min(stock_df, idx)
        if above_sr_level_min is None:
            continue

        if close[idx] < close[idx - 1] and close[idx] * 1.03 > above_sr_level_min:
            indices.append(idx)

    s = pd.Series([True] * len(indices), index=indices)
    stock_df[KEY] = s.reindex(stock_df.index, fill_value=False)
