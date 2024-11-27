import pandas as pd

"""
    sr_level_noop

    ----------------------
    up to sr level min
    down to sr level min

    up away sr level min
    down away sr level min

    up thru sr level min
    down thru sr level min

    ----------------------
    up to sr level max
    down to sr level max

    up away sr level max
    down away sr level max

    up thru sr level max
    down thru sr level max
"""


def sr_level_noop(_stock_df: pd.DataFrame, _idx: int) -> bool:
    return True


def up_to_sr_level_min(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['up to sr level min'].loc[idx]


def down_to_sr_level_min(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['down to sr level min'].loc[idx]


def up_away_sr_level_min(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['up away sr level min'].loc[idx]


def down_away_sr_level_min(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['down away sr level min'].loc[idx]


def up_thru_sr_level_min(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['up thru sr level min'].loc[idx]


def down_thru_sr_level_min(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['down thru sr level min'].loc[idx]


def up_to_sr_level_max(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['up to sr level max'].loc[idx]


def down_to_sr_level_max(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['down to sr level max'].loc[idx]


def up_away_sr_level_max(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['up away sr level max'].loc[idx]


def down_away_sr_level_max(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['down away sr level max'].loc[idx]


def up_thru_sr_level_max(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['up thru sr level max'].loc[idx]


def down_thru_sr_level_max(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['down thru sr level max'].loc[idx]


operators = [
    sr_level_noop,

    up_to_sr_level_min,
    down_to_sr_level_min,

    up_away_sr_level_min,
    down_away_sr_level_min,

    up_thru_sr_level_min,
    down_thru_sr_level_min,

    up_to_sr_level_max,
    down_to_sr_level_max,

    up_away_sr_level_max,
    down_away_sr_level_max,

    up_thru_sr_level_max,
    down_thru_sr_level_max,
]
