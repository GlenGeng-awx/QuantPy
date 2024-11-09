import pandas as pd
from features.k_23 import incr_top_10pst_in_last_n_days

KEY = 'incr top 10% today'
COLOR = 'red'


def execute(stock_df: pd.DataFrame, **kwargs):
    incr_top_10pst_in_last_n_days(stock_df, 1, KEY)
