import pandas as pd
from features.l_42 import baseline_decr_n_days

KEY = 'baseline decr 3d'
COLOR = 'green'


def execute(stock_df: pd.DataFrame, **kwargs):
    baseline_decr_n_days(stock_df, 3, KEY)
