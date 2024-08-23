import pandas as pd

from .factor import get_sr_levels_in_last_n_days, up_thru, is_local_min


"""
up thru sr levels, retrace and bounds back
"""


class S1U12V1:
    def __init__(self, stock_df: pd.DataFrame):
        self.stock_df = stock_df
        self.name = f'{__class__.__name__} - up thru sr levels, retrace and bounds back'

    def check_long(self, idx) -> bool:
        # retrace
        if not is_local_min(self.stock_df['close'], idx - 1):
            return False

        # up thru sr levels and bounds back
        sr_levels = get_sr_levels_in_last_n_days(self.stock_df, idx, 60)
        print(f'{self.stock_df.loc[idx]["Date"]}\tsr_level: {sr_levels}')

        hit = False

        for sr_level in sr_levels:
            step1 = False

            for n in range(1, 10):
                if up_thru(self.stock_df['close'], idx - n, sr_level):
                    step1 = True
                    break

            if step1:
                if self.stock_df['close'][idx - 1] > sr_level:
                    hit = True
                    break

        return hit

    def check_sell(self, _idx) -> bool:
        return False
