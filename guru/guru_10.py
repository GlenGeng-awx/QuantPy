import pandas as pd

"""
    incr_decr_bottom_10pst_noop

    incr bottom 10% last 3d  / decr bottom 10% last 3d
    incr bottom 10% last 5d  / decr bottom 10% last 5d
    incr bottom 10% last 10d / decr bottom 10% last 10d
    incr bottom 10% last 15d / decr bottom 10% last 15d
    incr bottom 10% last 20d / decr bottom 10% last 20d
"""


def incr_decr_bottom_10pst_noop(_stock_df: pd.DataFrame, _idx: int) -> bool:
    return True


def incr_bottom_10pst_last_3d(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['incr bottom 10% last 3d'][idx]


def decr_bottom_10pst_last_3d(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['decr bottom 10% last 3d'][idx]


def incr_bottom_10pst_last_5d(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['incr bottom 10% last 5d'][idx]


def decr_bottom_10pst_last_5d(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['decr bottom 10% last 5d'][idx]


def incr_bottom_10pst_last_10d(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['incr bottom 10% last 10d'][idx]


def decr_bottom_10pst_last_10d(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['decr bottom 10% last 10d'][idx]


def incr_bottom_10pst_last_15d(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['incr bottom 10% last 15d'][idx]


def decr_bottom_10pst_last_15d(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['decr bottom 10% last 15d'][idx]


def incr_bottom_10pst_last_20d(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['incr bottom 10% last 20d'][idx]


def decr_bottom_10pst_last_20d(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['decr bottom 10% last 20d'][idx]


operators = [
    incr_decr_bottom_10pst_noop,

    incr_bottom_10pst_last_3d,
    decr_bottom_10pst_last_3d,

    incr_bottom_10pst_last_5d,
    decr_bottom_10pst_last_5d,

    incr_bottom_10pst_last_10d,
    decr_bottom_10pst_last_10d,

    incr_bottom_10pst_last_15d,
    decr_bottom_10pst_last_15d,

    incr_bottom_10pst_last_20d,
    decr_bottom_10pst_last_20d,
]
