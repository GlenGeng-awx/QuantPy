import copy

from gringotts.book import Book
from gringotts.buy_strategy import *
from gringotts.sell_strategy import *

BUY_SWITCHES = [
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

SELL_SWITCHES = [
    'hard_loss_gt_3_pst',                                       # 0
    'hard_loss_gt_5_pst',                                       # 1
    'hard_loss_gt_7_pst',                                       # 2
    'moving_loss_gt_3_pst',                                     # 3
    'moving_loss_gt_5_pst',                                     # 4
    'moving_loss_gt_10_pst',                                    # 5
    'ma20_trend_not_up',                                        # 6
    'death_cross_ma20',                                         # 7
    'death_cross_ma5',                                          # 8
]


def decode_buy_switches(buy_switches: list[bool]) -> list[str]:
    assert len(buy_switches) == len(BUY_SWITCHES)
    results = []
    for idx, enable in enumerate(buy_switches):
        if enable:
            results.append(BUY_SWITCHES[idx])
    return results


def decode_sell_switches(sell_switches: list[bool]) -> list[str]:
    assert len(sell_switches) == len(SELL_SWITCHES)
    results = []
    for idx, enable in enumerate(sell_switches):
        if enable:
            results.append(SELL_SWITCHES[idx])
    return results


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
    def __init__(self,
                 stock_df: pd.DataFrame,
                 book: Book,
                 buy_switches: list[bool],
                 sell_switches: list[bool],
                 **kwargs
                 ):
        self.stock_df = stock_df
        self.book = book   # None if fake runner

        self.buy_switches = buy_switches
        self.sell_switches = sell_switches

        self.name = f'{__class__.__name__} buy {buy_switches} sell {sell_switches}'

    def check_long(self, idx) -> bool:
        if self.buy_switches[0] and not ma20_trend_switch_to_up(self.stock_df, idx):
            return False

        if self.buy_switches[1] and ma20_trend_is_down(self.stock_df, idx):
            return False

        if self.buy_switches[2] and not golden_cross_ma20(self.stock_df, idx):
            return False

        if self.buy_switches[3] and not golden_cross_ma5(self.stock_df, idx):
            return False

        if self.buy_switches[4] and not long_term_not_in_bottom(self.stock_df, idx):
            return False

        if self.buy_switches[5] and not short_term_not_in_bottom(self.stock_df, idx):
            return False

        if self.buy_switches[6] and not rsi_in_strong_up(self.stock_df, idx):
            return False

        if self.buy_switches[7] and not bband_pst_ma5_in_strong_up(self.stock_df, idx):
            return False

        if self.buy_switches[8] and not up_thru_sr_levels(self.stock_df, idx):
            return False

        if self.buy_switches[9] and not up_thru_sr_level_and_retrace_and_bounce_back(self.stock_df, idx):
            return False

        return True

    def check_sell(self, idx) -> bool:
        if self.sell_switches[0] and hard_loss_gt_3_pst(self.stock_df, self.book, idx):
            return True

        if self.sell_switches[1] and hard_loss_gt_5_pst(self.stock_df, self.book, idx):
            return True

        if self.sell_switches[2] and hard_loss_gt_7_pst(self.stock_df, self.book, idx):
            return True

        if self.sell_switches[3] and moving_loss_gt_3_pst(self.stock_df, self.book, idx):
            return True

        if self.sell_switches[4] and moving_loss_gt_5_pst(self.stock_df, self.book, idx):
            return True

        if self.sell_switches[5] and moving_loss_gt_10_pst(self.stock_df, self.book, idx):
            return True

        if self.sell_switches[6] and ma20_trend_not_up(self.stock_df, idx):
            return True

        if self.sell_switches[7] and death_cross_ma20(self.stock_df, idx):
            return True

        if self.sell_switches[8] and death_cross_ma5(self.stock_df, idx):
            return True

        return False


if __name__ == '__main__':
    buy_switches = [False, True, False, False, False, False, True, False, False, True]
    sell_switches = [False, False, False, False, False, True, False, False, False]

    print(f'Buy Switches: {decode_buy_switches(buy_switches)}')
    print(f'Sell Switches: {decode_sell_switches(sell_switches)}')
