import pandas as pd

"""
    post_noop

    1 day after up / 1 day after down
    2 day after up / 2 day after down
"""


def post_noop(_stock_df: pd.DataFrame, _idx: int) -> bool:
    return True


def one_day_after_up(stock_df: pd.DataFrame, idx: int) -> bool:
    if idx + 1 not in stock_df.index:
        return False
    return stock_df.loc[idx + 1]['close'] > stock_df.loc[idx]['close']


def two_day_after_up(stock_df: pd.DataFrame, idx: int) -> bool:
    if idx + 2 not in stock_df.index:
        return False
    return stock_df.loc[idx + 2]['close'] > stock_df.loc[idx]['close']


def one_day_after_down(stock_df: pd.DataFrame, idx: int) -> bool:
    if idx + 1 not in stock_df.index:
        return False
    return stock_df.loc[idx + 1]['close'] < stock_df.loc[idx]['close']


def two_day_after_down(stock_df: pd.DataFrame, idx: int) -> bool:
    if idx + 2 not in stock_df.index:
        return False
    return stock_df.loc[idx + 2]['close'] < stock_df.loc[idx]['close']


operators = [
    # post_noop,

    # one_day_after_up,
    two_day_after_up,

    # one_day_after_down,
    two_day_after_down
]
