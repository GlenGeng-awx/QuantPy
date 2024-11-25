import pandas as pd

"""
    yesterday_min_max_noop

    yesterday min of last 5d   / yesterday max of last 5d
    yesterday min of last 10d  / yesterday max of last 10d
    yesterday min of last 20d  / yesterday max of last 20d
    yesterday min of last 60d  / yesterday max of last 60d
    yesterday min of last 120d / yesterday max of last 120d
"""


def yesterday_min_max_noop(_stock_df: pd.DataFrame, _idx: int) -> bool:
    return True


def yesterday_min_of_last_5d(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['yesterday min of last 5d'][idx]


def yesterday_max_of_last_5d(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['yesterday max of last 5d'][idx]


def yesterday_min_of_last_10d(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['yesterday min of last 10d'][idx]


def yesterday_max_of_last_10d(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['yesterday max of last 10d'][idx]


def yesterday_min_of_last_20d(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['yesterday min of last 20d'][idx]


def yesterday_max_of_last_20d(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['yesterday max of last 20d'][idx]


def yesterday_min_of_last_60d(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['yesterday min of last 60d'][idx]


def yesterday_max_of_last_60d(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['yesterday max of last 60d'][idx]


def yesterday_min_of_last_120d(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['yesterday min of last 120d'][idx]


def yesterday_max_of_last_120d(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['yesterday max of last 120d'][idx]


operators = [
    yesterday_min_max_noop,

    yesterday_min_of_last_5d,
    yesterday_max_of_last_5d,

    yesterday_min_of_last_10d,
    yesterday_max_of_last_10d,

    yesterday_min_of_last_20d,
    yesterday_max_of_last_20d,

    yesterday_min_of_last_60d,
    yesterday_max_of_last_60d,

    yesterday_min_of_last_120d,
    yesterday_max_of_last_120d,
]
