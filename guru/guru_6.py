import pandas as pd

"""
    statistic_noop

    trend switch up   / trend switch down
    bband pst gt 0.85 / bband pst lt 0.15
    rsi above 70      / rsi below 30
    macd golden cross / macd death cross
"""


def statistic_noop(_stock_df: pd.DataFrame, _idx: int) -> bool:
    return True


def trend_switch_up(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['trend switch up'][idx]


def trend_switch_down(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['trend switch down'][idx]


def bband_pst_gt_0_85(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['bband pst gt 0.85'][idx]


def bband_pst_lt_0_15(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['bband pst lt 0.15'][idx]


def rsi_above_70(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['rsi above 70'][idx]


def rsi_below_30(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['rsi below 30'][idx]


def macd_golden_cross(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['macd golden cross'][idx]


def macd_death_cross(stock_df: pd.DataFrame, idx: int) -> bool:
    return stock_df['macd death cross'][idx]


operators = [
    statistic_noop,

    trend_switch_up,
    trend_switch_down,

    bband_pst_gt_0_85,
    bband_pst_lt_0_15,

    rsi_above_70,
    rsi_below_30,

    macd_golden_cross,
    macd_death_cross
]
