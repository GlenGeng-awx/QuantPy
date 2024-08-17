import pandas as pd

LONG = 'long'
SHORT = 'short'


def is_golden_cross(fast: pd.Series, slow: pd.Series, idx: int) -> bool:
    return fast[idx] > slow[idx] and fast[idx - 1] < slow[idx - 1]


def is_death_cross(fast: pd.Series, slow: pd.Series, idx: int) -> bool:
    return fast[idx] < slow[idx] and fast[idx - 1] > slow[idx - 1]


def is_local_min(s: pd.Series, idx: int) -> bool:
    return s[idx] < s[idx - 1] and s[idx] < s[idx + 1]


def is_local_max(s: pd.Series, idx: int) -> bool:
    return s[idx] > s[idx - 1] and s[idx] > s[idx + 1]
