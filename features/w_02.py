import pandas as pd
from features.w_01 import weekday_is_n

KEY = 'Tuesday'
COLOR = 'red'


def execute(stock_df: pd.DataFrame, **kwargs):
    weekday_is_n(stock_df, 1, KEY)
