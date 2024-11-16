import pandas as pd
from .long_000 import check_long

NAME = 'long green bar'
COLOR = 'orange'
TYPE = 'long'


def check(stock_df: pd.DataFrame, idx: int) -> bool:
    conditions = ['long green bar', 'real green bar']
    return check_long(stock_df, idx, conditions)
