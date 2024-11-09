import pandas as pd
from features.l_21 import price_incr_n_days

KEY = 'low incr 5d'
COLOR = 'red'


def execute(stock_df: pd.DataFrame, **kwargs):
    price_incr_n_days(stock_df, 5, 'low', KEY)
