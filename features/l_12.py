import pandas as pd
from features.l_14 import close_decr_n_days

KEY = 'close decr 1d'
COLOR = 'green'


def execute(stock_df: pd.DataFrame, **kwargs):
    close_decr_n_days(stock_df, 1, KEY)
