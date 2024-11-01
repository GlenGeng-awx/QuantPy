import pandas as pd
from features.common import STEP, DELTA
from features.f_013_s import yesterday_is_max_of_last_n_days

KEY = 'yesterday max of last 60d'
VAL = 44 * STEP + DELTA
RECALL_DAYS = 4


def execute(stock_df: pd.DataFrame, **kwargs):
    yesterday_is_max_of_last_n_days(stock_df, 60, KEY)
