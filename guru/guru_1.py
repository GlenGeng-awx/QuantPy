import pandas as pd
from technical.sr_level import SR_LEVEL_MIN, SR_LEVEL_MAX
from technical.min_max import LOCAL_MIN_PRICE_3RD, LOCAL_MAX_PRICE_3RD

"""
    primary features: sr level min/max OR local min/max 3rd
    -------------------------------------------------------
    structure_noop

     ascend sr level min or local min 3rd, in last 20 ~ 30
       flat sr level min or local min 3rd, in last 20 ~ 30
    descend sr level min or local min 3rd, in last 20 ~ 30

     ascend sr level max or local max 3rd, in last 20 ~ 30
       flat sr level max or local max 3rd, in last 20 ~ 30
    descend sr level max or local max 3rd, in last 20 ~ 30
"""


def structure_noop(_stock_df: pd.DataFrame, _idx: int) -> bool:
    return True


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
