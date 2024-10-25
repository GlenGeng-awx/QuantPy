import pandas as pd
from features.util import STEP, DELTA
from features.f_013_s import yesterday_is_max_of_last_n_days

KEY = 'yesterday max of last 5d'
VAL = 31 * STEP + DELTA


def execute(stock_df: pd.DataFrame, **kwargs):
    yesterday_is_max_of_last_n_days(stock_df, 5, KEY)
