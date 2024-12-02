import pandas as pd
from technical.sr_level import SR_LEVEL_MIN, SR_LEVEL_MAX
from technical.min_max import LOCAL_MIN_PRICE_3RD, LOCAL_MAX_PRICE_3RD

"""
    primary features: sr level min/max OR local min/max 3rd
    -------------------------------------------------------

    ascend sr level min, in last 20 ~ 30
    ascend sr level max, in last 20 ~ 30

    ascend local min 3rd, in last 20 ~ 30
    ascend local max 3rd, in last 20 ~ 30

    descend sr level min, in last 20 ~ 30
    descend sr level max, in last 20 ~ 30

    descend local min 3rd, in last 20 ~ 30
    descend local max 3rd, in last 20 ~ 30
"""


# def sr_level_min_or_min_3rd(stock_df: pd.DataFrame, idx: int) -> bool:
#     df = stock_df.loc[idx - 30:idx - 20]
#     return df[SR_LEVEL_MIN].any() or df[LOCAL_MIN_PRICE_3RD].any()


# def sr_level_max_or_max_3rd(stock_df: pd.DataFrame, idx: int) -> bool:
#     df = stock_df.loc[idx - 30:idx - 20]
#     return df[SR_LEVEL_MAX].any() or df[LOCAL_MAX_PRICE_3RD].any()


def _ascend_impl(stock_df: pd.DataFrame, idx: int, key: str) -> bool:
    df0 = stock_df.loc[idx - 30:idx - 20]
    if not df0[key].any():
        return False

    df1 = stock_df.loc[:idx - 20]
    df2 = df1[df1[key]]['close']
    return len(df2) >= 2 and df2.iloc[-2] < df2.iloc[-1]


def ascend_sr_level_min(stock_df: pd.DataFrame, idx: int) -> bool:
    return _ascend_impl(stock_df, idx, SR_LEVEL_MIN)


def ascend_sr_level_max(stock_df: pd.DataFrame, idx: int) -> bool:
    return _ascend_impl(stock_df, idx, SR_LEVEL_MAX)


def ascend_local_min_3rd(stock_df: pd.DataFrame, idx: int) -> bool:
    return _ascend_impl(stock_df, idx, LOCAL_MIN_PRICE_3RD)


def ascend_local_max_3rd(stock_df: pd.DataFrame, idx: int) -> bool:
    return _ascend_impl(stock_df, idx, LOCAL_MAX_PRICE_3RD)


def _descend_impl(stock_df: pd.DataFrame, idx: int, key: str) -> bool:
    df0 = stock_df.loc[idx - 30:idx - 20]
    if not df0[key].any():
        return False

    df1 = stock_df.loc[:idx - 20]
    df2 = df1[df1[key]]['close']
    return len(df2) >= 2 and df2.iloc[-2] > df2.iloc[-1]


def descend_sr_level_min(stock_df: pd.DataFrame, idx: int) -> bool:
    return _descend_impl(stock_df, idx, SR_LEVEL_MIN)


def descend_sr_level_max(stock_df: pd.DataFrame, idx: int) -> bool:
    return _descend_impl(stock_df, idx, SR_LEVEL_MAX)


def descend_local_min_3rd(stock_df: pd.DataFrame, idx: int) -> bool:
    return _descend_impl(stock_df, idx, LOCAL_MIN_PRICE_3RD)


def descend_local_max_3rd(stock_df: pd.DataFrame, idx: int) -> bool:
    return _descend_impl(stock_df, idx, LOCAL_MAX_PRICE_3RD)


operators = [
    ascend_sr_level_min,
    ascend_sr_level_max,
    ascend_local_min_3rd,
    ascend_local_max_3rd,

    descend_sr_level_min,
    descend_sr_level_max,
    descend_local_min_3rd,
    descend_local_max_3rd
]
