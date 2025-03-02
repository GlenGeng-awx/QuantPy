import pandas as pd
from features.k_62 import decr_bottom_10pst_in_last_n_days

KEY = 'decr bottom 10% last 5d'
COLOR = 'green'


def execute(stock_df: pd.DataFrame, **kwargs):
    decr_bottom_10pst_in_last_n_days(stock_df, 5, KEY)
