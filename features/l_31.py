import pandas as pd
from features.l_21 import price_incr_n_days

KEY = 'high incr 1d'
COLOR = 'red'


def execute(stock_df: pd.DataFrame, **kwargs):
    price_incr_n_days(stock_df, 1, 'high', KEY)
