import pandas as pd
from features.l_03 import vol_incr_n_days

KEY = 'vol incr 1d'
COLOR = 'red'


def execute(stock_df: pd.DataFrame, **kwargs):
    vol_incr_n_days(stock_df, 1, KEY)
