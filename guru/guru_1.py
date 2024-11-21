import pandas as pd
from technical.sr_level import SR_LEVEL_MIN, SR_LEVEL_MAX
from technical.min_max import LOCAL_MIN_PRICE_3RD, LOCAL_MAX_PRICE_3RD

"""
    primary features: sr level min/max
    ----------------------------------

    sr level min + local min 3rd, in last 20 ~ 27
    sr level max + local max 3rd, in last 20 ~ 27

    up to sr level,     in last 3d
    down to sr level,   in last 3d

    up away sr level,   in last 3d
    down away sr level, in last 3d

    up thru sr level,   in last 3d
    down thru sr level, in last 3d
"""


def sr_min_plus_min_3rd(stock_df: pd.DataFrame, idx: int) -> bool:
    df = stock_df.loc[idx - 27:idx - 20]
    return df[SR_LEVEL_MIN].any() and df[LOCAL_MIN_PRICE_3RD].any()


def sr_max_plus_max_3rd(stock_df: pd.DataFrame, idx: int) -> bool:
    df = stock_df.loc[idx - 27:idx - 20]
    return df[SR_LEVEL_MAX].any() and df[LOCAL_MAX_PRICE_3RD].any()


def up_to_sr_level(stock_df: pd.DataFrame, idx: int) -> bool:
    df = stock_df.loc[idx - 3:idx]
    return df['up to sr level'].any()


def down_to_sr_level(stock_df: pd.DataFrame, idx: int) -> bool:
    df = stock_df.loc[idx - 3:idx]
    return df['down to sr level'].any()


def up_away_sr_level(stock_df: pd.DataFrame, idx: int) -> bool:
    df = stock_df.loc[idx - 3:idx]
    return df['up away sr level'].any()


def down_away_sr_level(stock_df: pd.DataFrame, idx: int) -> bool:
    df = stock_df.loc[idx - 3:idx]
    return df['down away sr level'].any()


def up_thru_sr_level(stock_df: pd.DataFrame, idx: int) -> bool:
    df = stock_df.loc[idx - 3:idx]
    return df['up thru sr level'].any()


def down_thru_sr_level(stock_df: pd.DataFrame, idx: int) -> bool:
    df = stock_df.loc[idx - 3:idx]
    return df['down thru sr level'].any()


operators = [
    sr_min_plus_min_3rd,
    sr_max_plus_max_3rd,

    up_to_sr_level,
    down_to_sr_level,

    up_away_sr_level,
    down_away_sr_level,

    up_thru_sr_level,
    down_thru_sr_level
]
