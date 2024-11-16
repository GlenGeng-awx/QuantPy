import pandas as pd
from .long_000 import check_long

NAME = 'long lower shadow'
COLOR = 'orange'
TYPE = 'long'


def check(stock_df: pd.DataFrame, idx: int) -> bool:
    conditions = ['long lower shadow']
    return check_long(stock_df, idx, conditions)
