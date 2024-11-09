import pandas as pd
from features.l_04 import vol_decr_n_days

KEY = 'vol decr 1d'
COLOR = 'green'


def execute(stock_df: pd.DataFrame, **kwargs):
    vol_decr_n_days(stock_df, 1, KEY)
