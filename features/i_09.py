import pandas as pd
from features.i_07 import vol_is_max_of_last_n_day

KEY = 'vol max of last 10d'
COLOR = 'green'


def execute(stock_df: pd.DataFrame, **kwargs):
    vol_is_max_of_last_n_day(stock_df, 10, KEY)
