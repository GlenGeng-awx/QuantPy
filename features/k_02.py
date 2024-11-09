import pandas as pd
from technical.min_max import LOCAL_MIN_PRICE_2ND

KEY = 'down thru s level'
COLOR = 'green'


def get_support_levels_in_last_n_days(stock_df: pd.DataFrame, idx, n=80) -> list:
    beg = idx - n
    end = idx - 10
    condition = stock_df[LOCAL_MIN_PRICE_2ND]

    candidates = stock_df[condition].loc[beg:end]['close'].tolist()
    if len(candidates) == 0:
        return []

    baseline = 1_000_000
    results = []

    for s_level in reversed(candidates):
        if s_level < baseline:
            results.append(s_level)
            baseline = s_level

    return results


def execute(stock_df: pd.DataFrame, **kwargs):
    close = stock_df['close']

    indices = []
    for idx in close.index:
        s_levels = get_support_levels_in_last_n_days(stock_df, idx, 60)

        if any(close[idx - 1] >= s_level > close[idx] for s_level in s_levels):
            indices.append(idx)

    s = pd.Series([True] * len(indices), index=indices)
    stock_df[KEY] = s.reindex(stock_df.index, fill_value=False)
