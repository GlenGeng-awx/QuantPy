import pandas as pd
from .short_000 import check_short

NAME = 'down thru ma5'
COLOR = 'black'
TYPE = 'short'


def check(stock_df: pd.DataFrame, idx: int) -> bool:
    conditions = ['down thru ma5']
    return check_short(stock_df, idx, conditions)