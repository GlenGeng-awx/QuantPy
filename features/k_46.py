import pandas as pd
from features.k_44 import decr_top_10pst_in_last_n_days

KEY = 'decr top 10% last 5d'
COLOR = 'green'


def execute(stock_df: pd.DataFrame, **kwargs):
    decr_top_10pst_in_last_n_days(stock_df, 5, KEY)
