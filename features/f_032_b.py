import pandas as pd
from features.util import STEP
from features.f_013_b import yesterday_is_min_of_last_n_days

KEY = 'yesterday min of last 10d'
VAL = 32 * STEP


def execute(stock_df: pd.DataFrame, **kwargs):
    yesterday_is_min_of_last_n_days(stock_df, 10, KEY)
