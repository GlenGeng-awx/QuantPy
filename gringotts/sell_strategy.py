import pandas as pd

from statistical.ma import MA_20, MA_5

from gringotts.trend import MA_20_TREND
from gringotts.factor import is_death_cross


def hard_loss_gt_3_pst(stock_df: pd.DataFrame, book, idx: int) -> bool:
    return book.get_hard_loss_pst() > 3


def hard_loss_gt_5_pst(stock_df: pd.DataFrame, book, idx: int) -> bool:
    return book.get_hard_loss_pst() > 5


def hard_loss_gt_7_pst(stock_df: pd.DataFrame, book, idx: int) -> bool:
    return book.get_hard_loss_pst() > 7


def moving_loss_gt_3_pst(stock_df: pd.DataFrame, book, idx: int) -> bool:
    return book.get_moving_loss_pst() > 3


def moving_loss_gt_5_pst(stock_df: pd.DataFrame, book, idx: int) -> bool:
    return book.get_moving_loss_pst() > 5


def moving_loss_gt_10_pst(stock_df: pd.DataFrame, book, idx: int) -> bool:
    return book.get_moving_loss_pst() > 10


def ma20_trend_not_up(stock_df: pd.DataFrame, idx) -> bool:
    ma20_trend = stock_df[MA_20_TREND]
    return ma20_trend.loc[idx] != 'up'


def death_cross_ma20(stock_df: pd.DataFrame, idx) -> bool:
    return is_death_cross(stock_df['close'], stock_df[MA_20], idx)


def death_cross_ma5(stock_df: pd.DataFrame, idx) -> bool:
    return is_death_cross(stock_df['close'], stock_df[MA_5], idx)
