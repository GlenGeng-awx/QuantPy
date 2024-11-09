import pandas as pd
from features.h_16 import yesterday_is_max_of_last_n_days

KEY = 'yesterday max of last 120d'
COLOR = 'green'


def execute(stock_df: pd.DataFrame, **kwargs):
    yesterday_is_max_of_last_n_days(stock_df, 120, KEY)
