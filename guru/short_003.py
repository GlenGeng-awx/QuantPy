import pandas as pd
from .short_000 import check_short

NAME = 'long upper shadow'
COLOR = 'black'
TYPE = 'short'


def check(stock_df: pd.DataFrame, idx: int) -> bool:
    conditions = ['long upper shadow']
    return check_short(stock_df, idx, conditions)
