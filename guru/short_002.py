import pandas as pd
from .short_000 import check_short

NAME = 'incr top 10% last 10d'
COLOR = 'black'
TYPE = 'short'


def check(stock_df: pd.DataFrame, idx: int) -> bool:
    conditions = ['incr top 10% last 10d']
    return check_short(stock_df, idx, conditions)
