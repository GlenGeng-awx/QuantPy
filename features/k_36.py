import pandas as pd
from features.k_35 import get_below_sr_level_max

KEY = 'down to sr level max'
COLOR = 'green'


def execute(stock_df: pd.DataFrame, **kwargs):
    close = stock_df['close']

    indices = []

    for idx in close.index[1:]:
        below_sr_level_max = get_below_sr_level_max(stock_df, idx)
        if below_sr_level_max is None:
            continue

        if close[idx - 1] > close[idx] and close[idx] < below_sr_level_max * 1.03:
            indices.append(idx)

    s = pd.Series([True] * len(indices), index=indices)
    stock_df[KEY] = s.reindex(stock_df.index, fill_value=False)
