import pandas as pd
from features.util import STEP
from features.f_013_b import yesterday_is_min_of_last_n_days

KEY = 'yesterday min of last 60d'
VAL = 44 * STEP
RECALL_DAYS = 4


def execute(stock_df: pd.DataFrame, **kwargs):
    yesterday_is_min_of_last_n_days(stock_df, 60, KEY)
