import pandas as pd
from .long_000 import check_long

NAME = 'up thru ma60'
COLOR = 'orange'
TYPE = 'long'


def check(stock_df: pd.DataFrame, idx: int) -> bool:
    conditions = ['up thru ma60']
    return check_long(stock_df, idx, conditions)
