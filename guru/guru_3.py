import pandas as pd

"""
    ma_noop

    up thru ma5      / down thru ma5
    up thru ma20     / down thru ma20
    up thru ma60     / down thru ma60
    up thru ma120    / down thru ma120

    down touch ma5   / up touch ma5
    down touch ma20  / up touch ma20
    down touch ma60  / up touch ma60
    down touch ma120 / up touch ma120

    up thru ema5     / down thru ema5
    up thru ema10    / down thru ema10
    up thru ema12    / down thru ema12
    up thru ema20    / down thru ema20
    up thru ema26    / down thru ema26

    down touch ema5  / up touch ema5
    down touch ema10 / up touch ema10
    down touch ema12 / up touch ema12
    down touch ema20 / up touch ema20
    down touch ema26 / up touch ema26
"""


def ma_noop(_stock_df: pd.DataFrame, _idx: int) -> bool:
    return True


def up_thru_ma5(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['up thru ma5'][idx]


def up_thru_ma20(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['up thru ma20'][idx]


def up_thru_ma60(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['up thru ma60'][idx]


def up_thru_ma120(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['up thru ma120'][idx]


def down_thru_ma5(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['down thru ma5'][idx]


def down_thru_ma20(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['down thru ma20'][idx]


def down_thru_ma60(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['down thru ma60'][idx]


def down_thru_ma120(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['down thru ma120'][idx]


def up_touch_ma5(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['up touch ma5'][idx]


def up_touch_ma20(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['up touch ma20'][idx]


def up_touch_ma60(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['up touch ma60'][idx]


def up_touch_ma120(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['up touch ma120'][idx]


def down_touch_ma5(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['down touch ma5'][idx]


def down_touch_ma20(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['down touch ma20'][idx]


def down_touch_ma60(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['down touch ma60'][idx]


def down_touch_ma120(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['down touch ma120'][idx]


def up_thru_ema5(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['up thru ema5'][idx]


def up_thru_ema10(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['up thru ema10'][idx]


def up_thru_ema12(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['up thru ema12'][idx]


def up_thru_ema20(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['up thru ema20'][idx]


def up_thru_ema26(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['up thru ema26'][idx]


def down_thru_ema5(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['down thru ema5'][idx]


def down_thru_ema10(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['down thru ema10'][idx]


def down_thru_ema12(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['down thru ema12'][idx]


def down_thru_ema20(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['down thru ema20'][idx]


def down_thru_ema26(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['down thru ema26'][idx]


def up_touch_ema5(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['up touch ema5'][idx]


def up_touch_ema10(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['up touch ema10'][idx]


def up_touch_ema12(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['up touch ema12'][idx]


def up_touch_ema20(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['up touch ema20'][idx]


def up_touch_ema26(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['up touch ema26'][idx]


def down_touch_ema5(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['down touch ema5'][idx]


def down_touch_ema10(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['down touch ema10'][idx]


def down_touch_ema12(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['down touch ema12'][idx]


def down_touch_ema20(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['down touch ema20'][idx]


def down_touch_ema26(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['down touch ema26'][idx]


operators = [
    ma_noop,

    up_thru_ma5,
    up_thru_ma20,
    up_thru_ma60,
    up_thru_ma120,

    down_thru_ma5,
    down_thru_ma20,
    down_thru_ma60,
    down_thru_ma120,

    up_touch_ma5,
    up_touch_ma20,
    up_touch_ma60,
    up_touch_ma120,

    down_touch_ma5,
    down_touch_ma20,
    down_touch_ma60,
    down_touch_ma120,

    up_thru_ema5,
    up_thru_ema10,
    up_thru_ema12,
    up_thru_ema20,
    up_thru_ema26,

    down_thru_ema5,
    down_thru_ema10,
    down_thru_ema12,
    down_thru_ema20,
    down_thru_ema26,

    up_touch_ema5,
    up_touch_ema10,
    up_touch_ema12,
    up_touch_ema20,
    up_touch_ema26,

    down_touch_ema5,
    down_touch_ema10,
    down_touch_ema12,
    down_touch_ema20,
    down_touch_ema26,
]
