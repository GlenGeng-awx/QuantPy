import copy
from gringotts.strategy import *

SWITCHES = [
    'ma20_trend_switch_to_up',                                  # 0
    'ma20_trend_is_not_down',                                   # 1
    'golden_cross_ma20',                                        # 2
    'golden_cross_ma5',                                         # 3
    'long_term_not_in_bottom',                                  # 4
    'short_term_not_in_bottom',                                 # 5
    'rsi_in_strong_up',                                         # 6
    'bband_pst_ma5_in_strong_up',                               # 7
    'up_thru_sr_levels',                                        # 8
    'up_thru_sr_level_and_retrace_and_bounce_back',             # 9
]


def enumerate_switches(size: int) -> list[list]:
    if size == 0:
        return [[]]

    switches_part1 = enumerate_switches(size - 1)
    switches_part2 = copy.deepcopy(switches_part1)

    for switch in switches_part1:
        switch.append(False)

    for switch in switches_part2:
        switch.append(True)

    return switches_part1 + switches_part2


class TinyModel:
    def __init__(self, stock_df: pd.DataFrame, switches: list[bool]):
        self.stock_df = stock_df
        self.switches = switches

        self.name = f'{__class__.__name__} - giant - {switches}'

    def check_long(self, idx) -> bool:
        if self.switches[0] and not ma20_trend_switch_to_up(self.stock_df, idx):
            return False

        if self.switches[1] and ma20_trend_is_down(self.stock_df, idx):
            return False

        if self.switches[2] and not golden_cross_ma20(self.stock_df, idx):
            return False

        if self.switches[3] and not golden_cross_ma5(self.stock_df, idx):
            return False

        if self.switches[4] and not long_term_not_in_bottom(self.stock_df, idx):
            return False

        if self.switches[5] and not short_term_not_in_bottom(self.stock_df, idx):
            return False

        if self.switches[6] and not rsi_in_strong_up(self.stock_df, idx):
            return False

        if self.switches[7] and not bband_pst_ma5_in_strong_up(self.stock_df, idx):
            return False

        if self.switches[8] and not up_thru_sr_levels(self.stock_df, idx):
            return False

        if self.switches[9] and not up_thru_sr_level_and_retrace_and_bounce_back(self.stock_df, idx):
            return False

        return True

    def check_sell(self, idx) -> bool:
        return False


if __name__ == '__main__':
    switches = [False, True, True, True, False, False, False, False, False, False]

    for idx, enable in enumerate(switches):
        if enable:
            print(f'{SWITCHES[idx]}: {enable}')
