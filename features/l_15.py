import pandas as pd
from features.l_13 import close_incr_n_days

KEY = 'close incr 5d'
COLOR = 'red'


def execute(stock_df: pd.DataFrame, **kwargs):
    close_incr_n_days(stock_df, 5, KEY)
