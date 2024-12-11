import pandas as pd

"""
    simple_shape_noop

    real red bar       / real green bar
    fake red bar       / fake green bar

    long red bar       / long green bar
    short red bar      / short green bar

    long lower shadow  / long upper shadow
    short lower shadow / short upper shadow
"""


def simple_shape_noop(_stock_df: pd.DataFrame, _idx: int) -> bool:
    return True


def real_red_bar(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['real red bar'][idx]


def real_green_bar(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['real green bar'][idx]


def fake_red_bar(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['fake red bar'][idx]


def fake_green_bar(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['fake green bar'][idx]


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


operators = [
    simple_shape_noop,

    # real_red_bar,
    # real_green_bar,

    fake_red_bar,
    fake_green_bar,

    long_red_bar,
    long_green_bar,

    short_red_bar,
    short_green_bar,

    long_lower_shadow,
    long_upper_shadow,

    short_lower_shadow,
    short_upper_shadow,
]
