from statistical.ma import MA_20, MA_5
from statistical.rsi import RSI_14
from statistical.bband import BBAND_PST_MA5

from .trend import MA_20_TREND
from .factor import *


def ma20_trend_switch_to_up(stock_df: pd.DataFrame, idx) -> bool:
    ma20_trend = stock_df[MA_20_TREND]
    return ma20_trend.loc[idx - 1] != 'up' and ma20_trend.loc[idx] == 'up'


def ma20_trend_is_down(stock_df: pd.DataFrame, idx) -> bool:
    ma20_trend = stock_df[MA_20_TREND]
    return ma20_trend.loc[idx] == 'down'


def golden_cross_ma20(stock_df: pd.DataFrame, idx) -> bool:
    return is_golden_cross(stock_df['close'], stock_df[MA_20], idx)


def golden_cross_ma5(stock_df: pd.DataFrame, idx) -> bool:
    return is_golden_cross(stock_df['close'], stock_df[MA_5], idx)


def long_term_not_in_bottom(stock_df: pd.DataFrame, idx) -> bool:
    return belong_to_up_x_percent_in_last_n_days(stock_df['close'], idx, 0.786, 100)


def short_term_not_in_bottom(stock_df: pd.DataFrame, idx) -> bool:
    return belong_to_up_x_percent_in_last_n_days(stock_df['close'], idx, 0.786, 10)


def rsi_in_strong_up(stock_df: pd.DataFrame, idx) -> bool:
    rsi = stock_df[RSI_14]
    return rsi.loc[idx] > 65


def bband_pst_ma5_in_strong_up(stock_df: pd.DataFrame, idx) -> bool:
    bband_pst_ma5 = stock_df[BBAND_PST_MA5]
    return bband_pst_ma5.loc[idx] > 0.8


def up_thru_sr_levels(stock_df: pd.DataFrame, idx) -> bool:
    sr_levels = get_sr_levels_in_last_n_days(stock_df, idx, 60)
    # print(f'\t{stock_df.loc[idx]["Date"]}\tsr_level: {sr_levels}')
    return any(up_thru(stock_df['close'], idx, sr_level) for sr_level in sr_levels)


def up_thru_sr_level_and_retrace_and_bounce_back(stock_df, idx) -> bool:
    sr_levels = get_sr_levels_in_last_n_days(stock_df, idx, 60)
    # print(f'\t{stock_df.loc[idx]["Date"]}\tsr_level: {sr_levels}')

    for sr_level in sr_levels:
        step1 = False
        step2 = False

        for n in range(1, 10):
            if up_thru(stock_df['close'], idx - n, sr_level):
                step1 = True

        if is_local_min(stock_df['close'], idx - 1) \
                and stock_df['close'][idx - 1] > sr_level:
            step2 = True

        if step1 and step2:
            return True

    return False
