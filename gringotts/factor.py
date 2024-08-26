import pandas as pd

from technical.min_max import LOCAL_MAX_PRICE_2ND


# x = 0.382 or 0.5 or 0.618 or 0.786
# n = 100, 60, 40, 10, 5
def belong_to_up_x_percent_in_last_n_days(s: pd.Series, idx, x: float = 0.618, n: int = 100) -> bool:
    upper = s.loc[idx - n:idx].max()
    lower = s.loc[idx - n:idx].min()
    curr = s.loc[idx]
    return curr - lower > (upper - lower) * (1 - x)


def belong_to_down_x_percent_in_last_n_days(s: pd.Series, idx, x: float = 0.5, n: int = 40) -> bool:
    upper = s.loc[idx - n:idx].max()
    lower = s.loc[idx - n:idx].min()
    curr = s.loc[idx]
    return curr - lower < (upper - lower) * x


def is_local_min(s: pd.Series, idx: int) -> bool:
    return s[idx] < s[idx - 1] and s[idx] < s[idx + 1]


def is_local_max(s: pd.Series, idx: int) -> bool:
    return s[idx] > s[idx - 1] and s[idx] > s[idx + 1]


def is_golden_cross(fast: pd.Series, slow: pd.Series, idx: int) -> bool:
    return fast[idx] > slow[idx] and fast[idx - 1] < slow[idx - 1]


def is_death_cross(fast: pd.Series, slow: pd.Series, idx: int) -> bool:
    return fast[idx] < slow[idx] and fast[idx - 1] > slow[idx - 1]


def get_sr_levels_in_last_n_days(stock_df: pd.DataFrame, idx, n=80) -> list:
    beg = idx - n
    end = idx - 10
    condition = stock_df[LOCAL_MAX_PRICE_2ND]

    candidates = stock_df[condition].loc[beg:end]['close'].tolist()
    if len(candidates) == 0:
        return []

    baseline = 0
    results = []

    for sr_level in reversed(candidates):
        if sr_level > baseline:
            results.append(sr_level)
            baseline = sr_level

    return results


def up_thru(s: pd.Series, idx, target) -> bool:
    return s.loc[idx - 1] < target <= s.loc[idx]
