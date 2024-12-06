import pandas as pd

"""
    weekday_noop

    Monday
    Tuesday
    Wednesday
    Thursday
    Friday
"""


def weekday_noop(_stock_df: pd.DataFrame, _idx: int) -> bool:
    return True


def monday(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['Monday'][idx]


def tuesday(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['Tuesday'][idx]


def wednesday(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['Wednesday'][idx]


def thursday(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['Thursday'][idx]


def friday(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['Friday'][idx]


operators = [
    weekday_noop,

    monday,
    tuesday,
    wednesday,
    thursday,
    friday,
]
