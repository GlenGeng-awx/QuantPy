import pandas as pd

from statistical.bband import BBAND_PST, BBAND_PST_MA5
from statistical.rsi import RSI_14

from technical.volume import VOLUME_REG, VOLUME_MA_5
from technical.min_max import LOCAL_MIN_PRICE_2ND
from statistical.ma import MA_20, MA_5

from gringotts.sell_strategy import hard_loss_gt_5_pst, moving_loss_gt_5_pst
from gringotts.factor import *

"""
bband_pst gold cross bband_pst_ma5
"""


class S1U10V1:
    def __init__(self, stock_df: pd.DataFrame, book, **kwargs):
        self.stock_df = stock_df
        self.book = book

        self.bband_pst = self.stock_df[BBAND_PST]
        self.bband_pst_ma5 = self.stock_df[BBAND_PST_MA5]

        self.rsi = self.stock_df[RSI_14]

        self.volume = self.stock_df[VOLUME_REG]
        self.volume_ma5 = self.stock_df[VOLUME_MA_5]

        self.close = self.stock_df['close']
        self.ma5 = self.stock_df[MA_5]
        self.ma20 = self.stock_df[MA_20]

        self.name = f'{__class__.__name__} - bband_pst gold cross bband_pst_ma5'

    def check_long(self, idx) -> bool:
        price_incr_10_pst = (self.close[idx] - self.close[idx - 1]) / self.close[idx - 1] > 0.1
        return price_incr_10_pst

    def check_long_1(self, idx) -> bool:
        return False

    def check_long_2(self, idx) -> bool:
        return False

    def check_long_3(self, idx) -> bool:
        prev_4day_below_ma5 = self.close[idx - 4] < self.ma5[idx - 4]
        prev_3day_below_ma5 = self.close[idx - 3] < self.ma5[idx - 3]
        prev_2day_below_ma5 = self.close[idx - 2] < self.ma5[idx - 2]

        prev_1day_golden_cross = is_golden_cross(self.close, self.ma5, idx - 1)

        above_ma5 = self.close[idx] > self.ma5[idx]

        return prev_4day_below_ma5 and prev_3day_below_ma5 and prev_2day_below_ma5 \
            and prev_1day_golden_cross and above_ma5

    def check_long_4(self, idx) -> bool:
        return False

    def check_sell(self, idx) -> bool:
        return (self.close[idx] - self.close[idx - 1]) / self.close[idx - 1] < -0.1

    def check_sell_1(self, idx) -> bool:
        return False

    def check_sell_2(self, idx) -> bool:
        return False

    def check_sell_3(self, idx) -> bool:
        prev_4day_above_ma5 = self.close[idx - 4] > self.ma5[idx - 4]
        prev_3day_above_ma5 = self.close[idx - 3] > self.ma5[idx - 3]
        prev_2day_above_ma5 = self.close[idx - 2] > self.ma5[idx - 2]

        prev_1day_death_cross = is_death_cross(self.close, self.ma5, idx - 1)

        below_ma5 = self.close[idx] < self.ma5[idx]

        return prev_4day_above_ma5 and prev_3day_above_ma5 and prev_2day_above_ma5 \
            and prev_1day_death_cross and below_ma5

    def check_sell_4(self, idx) -> bool:
        return False
