import pandas as pd
from features.k_62 import decr_bottom_10pst_in_last_n_days

KEY = 'decr bottom 10% last 20d'
COLOR = 'green'


def execute(stock_df: pd.DataFrame, **kwargs):
    decr_bottom_10pst_in_last_n_days(stock_df, 20, KEY)
