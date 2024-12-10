import pandas as pd
from technical.sr_level import SR_LEVEL_MIN, SR_LEVEL_MAX
from technical.min_max import LOCAL_MIN_PRICE_3RD, LOCAL_MAX_PRICE_3RD

"""
    structure_noop

     ascend sr_level_min or local_min_3rd, in last 20 ~ 30
       flat sr_level_min or local_min_3rd, in last 20 ~ 30
    descend sr_level_min or local_min_3rd, in last 20 ~ 30

     ascend sr_level_max or local_max_3rd, in last 20 ~ 30
       flat sr_level_max or local_max_3rd, in last 20 ~ 30
    descend sr_level_max or local_max_3rd, in last 20 ~ 30
"""


def structure_noop(_stock_df: pd.DataFrame, _idx: int) -> bool:
    return True


def _ascend_impl(stock_df: pd.DataFrame, idx: int, key: str) -> bool:
    df0 = stock_df.loc[idx - 30:idx - 20]
    if not df0[key].any():
        return False

    df1 = stock_df.loc[:idx - 20]
    df2 = df1[df1[key]]['close']
    return len(df2) >= 2 and df2.iloc[-2] * 1.03 < df2.iloc[-1]


def _flat_impl(stock_df: pd.DataFrame, idx: int, key: str) -> bool:
    df0 = stock_df.loc[idx - 30:idx - 20]
    if not df0[key].any():
        return False

    df1 = stock_df.loc[:idx - 20]
    df2 = df1[df1[key]]['close']
    return len(df2) >= 2 and df2.iloc[-2] * 0.97 < df2.iloc[-1] < df2.iloc[-2] * 1.03


def _descend_impl(stock_df: pd.DataFrame, idx: int, key: str) -> bool:
    df0 = stock_df.loc[idx - 30:idx - 20]
    if not df0[key].any():
        return False

    df1 = stock_df.loc[:idx - 20]
    df2 = df1[df1[key]]['close']
    return len(df2) >= 2 and df2.iloc[-2] > df2.iloc[-1] * 1.03


def ascend_sr_min_or_min_3rd(stock_df: pd.DataFrame, idx: int) -> bool:
    return _ascend_impl(stock_df, idx, SR_LEVEL_MIN) \
        or _ascend_impl(stock_df, idx, LOCAL_MIN_PRICE_3RD)


def flat_sr_min_or_min_3rd(stock_df: pd.DataFrame, idx: int) -> bool:
    return _flat_impl(stock_df, idx, SR_LEVEL_MIN) \
        or _flat_impl(stock_df, idx, LOCAL_MIN_PRICE_3RD)


def descend_sr_min_or_min_3rd(stock_df: pd.DataFrame, idx: int) -> bool:
    return _descend_impl(stock_df, idx, SR_LEVEL_MIN) \
        or _descend_impl(stock_df, idx, LOCAL_MIN_PRICE_3RD)


def ascend_sr_max_or_max_3rd(stock_df: pd.DataFrame, idx: int) -> bool:
    return _ascend_impl(stock_df, idx, SR_LEVEL_MAX) \
        or _ascend_impl(stock_df, idx, LOCAL_MAX_PRICE_3RD)


def flat_sr_max_or_max_3rd(stock_df: pd.DataFrame, idx: int) -> bool:
    return _flat_impl(stock_df, idx, SR_LEVEL_MAX) \
        or _flat_impl(stock_df, idx, LOCAL_MAX_PRICE_3RD)


def descend_sr_max_or_max_3rd(stock_df: pd.DataFrame, idx: int) -> bool:
    return _descend_impl(stock_df, idx, SR_LEVEL_MAX) \
        or _descend_impl(stock_df, idx, LOCAL_MAX_PRICE_3RD)


operators = [
    structure_noop,

    ascend_sr_min_or_min_3rd,
    flat_sr_min_or_min_3rd,
    descend_sr_min_or_min_3rd,

    ascend_sr_max_or_max_3rd,
    flat_sr_max_or_max_3rd,
    descend_sr_max_or_max_3rd,
]
