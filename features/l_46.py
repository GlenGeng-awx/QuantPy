import pandas as pd
from features.l_42 import baseline_decr_n_days

KEY = 'baseline decr 5d'
COLOR = 'green'


def execute(stock_df: pd.DataFrame, **kwargs):
    baseline_decr_n_days(stock_df, 5, KEY)
