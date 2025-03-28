import pandas as pd
from features.k_15 import get_below_sr_level_min

KEY = 'down to sr level min'
COLOR = 'green'


def execute(stock_df: pd.DataFrame, **kwargs):
    close = stock_df['close']

    indices = []

    for idx in close.index[1:]:
        below_sr_level_min = get_below_sr_level_min(stock_df, idx)
        if below_sr_level_min is None:
            continue

        if close[idx - 1] > close[idx] and close[idx] < below_sr_level_min * 1.03:
            indices.append(idx)

    s = pd.Series([True] * len(indices), index=indices)
    stock_df[KEY] = s.reindex(stock_df.index, fill_value=False)
