import pandas as pd
from technical.min_max import LOCAL_MAX_PRICE_2ND

KEY = 'up thru r level'
COLOR = 'red'


def get_resistance_levels_in_last_n_days(stock_df: pd.DataFrame, idx, n=80) -> list:
    beg = idx - n
    end = idx - 10
    condition = stock_df[LOCAL_MAX_PRICE_2ND]

    candidates = stock_df[condition].loc[beg:end]['close'].tolist()
    if len(candidates) == 0:
        return []

    baseline = 0
    results = []

    for r_level in reversed(candidates):
        if r_level > baseline:
            results.append(r_level)
            baseline = r_level

    return results


def execute(stock_df: pd.DataFrame, **kwargs):
    close = stock_df['close']

    indices = []
    for idx in close.index:
        r_levels = get_resistance_levels_in_last_n_days(stock_df, idx, 60)

        if any(close[idx - 1] < r_level <= close[idx] for r_level in r_levels):
            indices.append(idx)

    s = pd.Series([True] * len(indices), index=indices)
    stock_df[KEY] = s.reindex(stock_df.index, fill_value=False)
