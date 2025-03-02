import pandas as pd

"""
    complex_shape_noop

    fake red bar       / fake green bar
    up engulfing       / down engulfing
    up harami          / down harami
    up gap             / down gap
"""


def complex_shape_noop(_stock_df: pd.DataFrame, _idx: int) -> bool:
    return True


def fake_red_bar(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['fake red bar'][idx]


def fake_green_bar(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['fake green bar'][idx]


def up_engulfing(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['up engulfing'][idx]


def down_engulfing(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['down engulfing'][idx]


def up_harami(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['up harami'][idx]


def down_harami(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['down harami'][idx]


def up_gap(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['up gap'][idx]


def down_gap(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['down gap'][idx]


operators = [
    complex_shape_noop,

    fake_red_bar,
    fake_green_bar,

    up_engulfing,
    down_engulfing,

    up_harami,
    down_harami,

    up_gap,
    down_gap,
]
