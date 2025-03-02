import pandas as pd

"""
    price_noop

    close incr 3d         / close decr 3d
    close incr 5d         / close decr 5d

    low incr 3d           / low decr 3d
    low incr 5d           / low decr 5d

    high incr 3d          / high decr 2d
    high incr 5d          / high decr 3d
"""


def price_noop(_stock_df: pd.DataFrame, _idx: int) -> bool:
    return True


def close_incr_3d(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['close incr 3d'][idx]


def close_decr_3d(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['close decr 3d'][idx]


def close_incr_5d(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['close incr 5d'][idx]


def close_decr_5d(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['close decr 5d'][idx]


def low_incr_3d(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['low incr 3d'][idx]


def low_decr_3d(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['low decr 3d'][idx]


def low_incr_5d(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['low incr 5d'][idx]


def low_decr_5d(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['low decr 5d'][idx]


def high_incr_3d(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['high incr 3d'][idx]


def high_decr_3d(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['high decr 3d'][idx]


def high_decr_5d(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['high decr 5d'][idx]


def high_incr_5d(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['high incr 5d'][idx]


operators = [
    price_noop,

    close_incr_3d,
    close_decr_3d,

    close_incr_5d,
    close_decr_5d,

    low_incr_3d,
    low_decr_3d,

    low_incr_5d,
    low_decr_5d,

    high_incr_3d,
    high_decr_3d,

    high_incr_5d,
    high_decr_5d,
]
