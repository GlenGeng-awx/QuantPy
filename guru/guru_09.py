import pandas as pd

"""
    incr_decr_top_10pst_noop

    incr top 10% today    / decr top 10% today
    incr top 10% last 3d  / decr top 10% last 3d
    incr top 10% last 5d  / decr top 10% last 5d
    incr top 10% last 10d / decr top 10% last 10d
    incr top 10% last 15d / decr top 10% last 15d
    incr top 10% last 20d / decr top 10% last 20d
"""


def incr_decr_top_10pst_noop(_stock_df: pd.DataFrame, _idx: int) -> bool:
    return True


def incr_top_10pst_today(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['incr top 10% today'][idx]


def decr_top_10pst_today(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['decr top 10% today'][idx]


def incr_top_10pst_last_3d(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['incr top 10% last 3d'][idx]


def decr_top_10pst_last_3d(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['decr top 10% last 3d'][idx]


def incr_top_10pst_last_5d(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['incr top 10% last 5d'][idx]


def decr_top_10pst_last_5d(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['decr top 10% last 5d'][idx]


def incr_top_10pst_last_10d(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['incr top 10% last 10d'][idx]


def decr_top_10pst_last_10d(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['decr top 10% last 10d'][idx]


def incr_top_10pst_last_15d(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['incr top 10% last 15d'][idx]


def decr_top_10pst_last_15d(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['decr top 10% last 15d'][idx]


def incr_top_10pst_last_20d(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['incr top 10% last 20d'][idx]


def decr_top_10pst_last_20d(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['decr top 10% last 20d'][idx]


operators = [
    incr_decr_top_10pst_noop,

    incr_top_10pst_today,
    decr_top_10pst_today,

    incr_top_10pst_last_3d,
    decr_top_10pst_last_3d,

    incr_top_10pst_last_5d,
    decr_top_10pst_last_5d,

    incr_top_10pst_last_10d,
    decr_top_10pst_last_10d,

    incr_top_10pst_last_15d,
    decr_top_10pst_last_15d,

    incr_top_10pst_last_20d,
    decr_top_10pst_last_20d,
]
