import pandas as pd
from .long_000 import check_long

NAME = 'decr top 10% last 10d'
COLOR = 'orange'
TYPE = 'long'


def check(stock_df: pd.DataFrame, idx: int) -> bool:
    conditions = ['decr top 10% last 10d']
    return check_long(stock_df, idx, conditions)
