import pandas as pd
from features.k_61 import incr_bottom_10pst_in_last_n_days

KEY = 'incr bottom 10% last 5d'
COLOR = 'red'


def execute(stock_df: pd.DataFrame, **kwargs):
    incr_bottom_10pst_in_last_n_days(stock_df, 5, KEY)
