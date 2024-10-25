import pandas as pd
from features.util import STEP
from features.f_013_b import yesterday_is_min_of_last_n_days

KEY = 'yesterday min of last 5d'
VAL = 31 * STEP


def execute(stock_df: pd.DataFrame, **kwargs):
    yesterday_is_min_of_last_n_days(stock_df, 5, KEY)
