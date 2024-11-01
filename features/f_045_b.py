import pandas as pd
from features.common import STEP
from features.f_013_b import yesterday_is_min_of_last_n_days

KEY = 'yesterday min of last 120d'
VAL = 45 * STEP
RECALL_DAYS = 5


def execute(stock_df: pd.DataFrame, **kwargs):
    yesterday_is_min_of_last_n_days(stock_df, 120, KEY)
