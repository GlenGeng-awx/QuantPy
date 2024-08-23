import pandas as pd

from .trend import MA_20_TREND

"""
MA_20_TREND switch
"""


class S1U9:
    def __init__(self, stock_df: pd.DataFrame):
        self.stock_df = stock_df
        self.name = f'{__class__.__name__} - MA_20_TREND switch'

    def check(self, idx) -> bool:
        return self.stock_df.loc[idx - 1][MA_20_TREND] != 'up' \
            and self.stock_df.loc[idx][MA_20_TREND] == 'up'
