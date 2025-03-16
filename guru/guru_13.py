import pandas as pd

"""
    baseline_noop

    baseline incr 3d / baseline decr 3d
    baseline incr 5d / baseline decr 5d
"""


def baseline_noop(_stock_df: pd.DataFrame, _idx: int) -> bool:
    return True


def baseline_incr_1d(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['baseline incr 1d'][idx]


def baseline_decr_1d(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['baseline decr 1d'][idx]


def baseline_incr_3d(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['baseline incr 3d'][idx]


def baseline_decr_3d(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['baseline decr 3d'][idx]


def baseline_incr_5d(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['baseline incr 5d'][idx]


def baseline_decr_5d(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['baseline decr 5d'][idx]


operators = [
    baseline_noop,

    # baseline_incr_1d,
    # baseline_decr_1d,

    baseline_incr_3d,
    baseline_decr_3d,

    baseline_incr_5d,
    baseline_decr_5d,
]
