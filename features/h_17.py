import pandas as pd
from features.h_15 import yesterday_is_min_of_last_n_days

KEY = 'yesterday min of last 60d'
COLOR = 'red'


def execute(stock_df: pd.DataFrame, **kwargs):
    yesterday_is_min_of_last_n_days(stock_df, 60, KEY)
