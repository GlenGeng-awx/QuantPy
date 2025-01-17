import pandas as pd
from features.i_06 import vol_is_min_of_last_n_day

KEY = 'vol min of last 10d'
COLOR = 'red'


def execute(stock_df: pd.DataFrame, **kwargs):
    vol_is_min_of_last_n_day(stock_df, 10, KEY)
