import pandas as pd
from .short_000 import check_short

NAME = 'long red bar'
COLOR = 'black'
TYPE = 'short'


def check(stock_df: pd.DataFrame, idx: int) -> bool:
    conditions = ['long red bar', 'real red bar']
    return check_short(stock_df, idx, conditions)
