import pandas as pd
from technical.sr_level import SR_LEVEL_MIN, SR_LEVEL_MAX
from technical.min_max import LOCAL_MIN_PRICE_3RD, LOCAL_MAX_PRICE_3RD

"""
    primary features: sr level min/max OR local min/max 3rd
    -------------------------------------------------------

    sr level min or local min 3rd, in last 20 ~ 30
    sr level max or local max 3rd, in last 20 ~ 30
"""


def sr_level_min_or_min_3rd(stock_df: pd.DataFrame, idx: int) -> bool:
    df = stock_df.loc[idx - 30:idx - 20]
    return df[SR_LEVEL_MIN].any() or df[LOCAL_MIN_PRICE_3RD].any()


def sr_level_max_or_max_3rd(stock_df: pd.DataFrame, idx: int) -> bool:
    df = stock_df.loc[idx - 30:idx - 20]
    return df[SR_LEVEL_MAX].any() or df[LOCAL_MAX_PRICE_3RD].any()


operators = [
    sr_level_min_or_min_3rd,
    sr_level_max_or_max_3rd,
]
