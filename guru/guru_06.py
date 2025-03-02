import pandas as pd

"""
    vol_noop

    extreme high vol      / extreme low vol
    high vol / normal vol / low vol

    vol min of last 5d    / vol max of last 5d
    vol min of last 10d   / vol max of last 10d

    vol incr 3d           / vol decr 3d
    vol incr 5d           / vol decr 5d
"""


def vol_noop(_stock_df: pd.DataFrame, _idx: int) -> bool:
    return True


def extreme_high_vol(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['extreme high vol'][idx]


def extreme_low_vol(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['extreme low vol'][idx]


def high_vol(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['high vol'][idx]


def normal_vol(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['normal vol'][idx]


def low_vol(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['low vol'][idx]


def vol_min_of_last_5d(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['vol min of last 5d'][idx]


def vol_max_of_last_5d(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['vol max of last 5d'][idx]


def vol_min_of_last_10d(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['vol min of last 10d'][idx]


def vol_max_of_last_10d(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['vol max of last 10d'][idx]


def vol_incr_3d(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['vol incr 3d'][idx]


def vol_decr_3d(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['vol decr 3d'][idx]


def vol_incr_5d(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['vol incr 5d'][idx]


def vol_decr_5d(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['vol decr 5d'][idx]


operators = [
    vol_noop,

    extreme_high_vol,
    extreme_low_vol,

    high_vol,
    normal_vol,
    low_vol,

    vol_min_of_last_5d,
    vol_max_of_last_5d,

    vol_min_of_last_10d,
    vol_max_of_last_10d,

    vol_incr_3d,
    vol_decr_3d,

    vol_incr_5d,
    vol_decr_5d,
]
