import pandas as pd

"""
    ma_noop

    up thru ma5     / down thru ma5
    up thru ma20    / down thru ma20
    up thru ma60    / down thru ma60

    down touch ma5  / up touch ma5
    down touch ma20 / up touch ma20
    down touch ma60 / up touch ma60
"""


def ma_noop(_stock_df: pd.DataFrame, _idx: int) -> bool:
    return True


def up_thru_ma5(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['up thru ma5'][idx]


def up_thru_ma20(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['up thru ma20'][idx]


def up_thru_ma60(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['up thru ma60'][idx]


def down_thru_ma5(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['down thru ma5'][idx]


def down_thru_ma20(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['down thru ma20'][idx]


def down_thru_ma60(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['down thru ma60'][idx]


def up_touch_ma5(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['up touch ma5'][idx]


def up_touch_ma20(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['up touch ma20'][idx]


def up_touch_ma60(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['up touch ma60'][idx]


def down_touch_ma5(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['down touch ma5'][idx]


def down_touch_ma20(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['down touch ma20'][idx]


def down_touch_ma60(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['down touch ma60'][idx]


operators = [
    ma_noop,

    up_thru_ma5,
    up_thru_ma20,
    up_thru_ma60,

    down_thru_ma5,
    down_thru_ma20,
    down_thru_ma60,

    up_touch_ma5,
    up_touch_ma20,
    up_touch_ma60,

    down_touch_ma5,
    down_touch_ma20,
    down_touch_ma60
]
