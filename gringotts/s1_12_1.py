import pandas as pd

from .strategy import up_thru_sr_level_and_retrace_and_bounce_back

"""
up thru sr levels, retrace and bounds back
"""


class S1U12V1:
    def __init__(self, stock_df: pd.DataFrame):
        self.stock_df = stock_df
        self.name = f'{__class__.__name__} - up thru sr levels, retrace and bounds back'

    def check_long(self, idx) -> bool:
        return up_thru_sr_level_and_retrace_and_bounce_back(self.stock_df, idx)

    def check_sell(self, _idx) -> bool:
        return False
