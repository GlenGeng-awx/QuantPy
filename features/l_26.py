import pandas as pd
from features.l_22 import price_decr_n_days

KEY = 'low decr 5d'
COLOR = 'green'


def execute(stock_df: pd.DataFrame, **kwargs):
    price_decr_n_days(stock_df, 5, 'low', KEY)
