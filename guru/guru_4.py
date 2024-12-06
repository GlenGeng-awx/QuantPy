import pandas as pd

"""
    shape_noop

    long red bar       / long green bar
    short red bar      / short green bar

    long lower shadow  / long upper shadow
    short lower shadow / short upper shadow

    up engulfing       / down engulfing
    up harami          / down harami
    up gap             / down gap
"""


def shape_noop(_stock_df: pd.DataFrame, _idx: int) -> bool:
    return True


def long_red_bar(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['long red bar'][idx]


def long_green_bar(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['long green bar'][idx]


def short_red_bar(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['short red bar'][idx]


def short_green_bar(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['short green bar'][idx]


def long_lower_shadow(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['long lower shadow'][idx]


def long_upper_shadow(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['long upper shadow'][idx]


def short_lower_shadow(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['short lower shadow'][idx]


def short_upper_shadow(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['short upper shadow'][idx]


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
    shape_noop,

    long_red_bar,
    long_green_bar,

    short_red_bar,
    short_green_bar,

    long_lower_shadow,
    long_upper_shadow,

    short_lower_shadow,
    short_upper_shadow,

    up_engulfing,
    down_engulfing,

    up_harami,
    down_harami,

    up_gap,
    down_gap,
]
