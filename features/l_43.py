import pandas as pd
from features.l_41 import baseline_incr_n_days

KEY = 'baseline incr 3d'
COLOR = 'red'


def execute(stock_df: pd.DataFrame, **kwargs):
    baseline_incr_n_days(stock_df, 3, KEY)
