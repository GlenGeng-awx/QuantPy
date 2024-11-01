import pandas as pd
from features.common import STEP
from features.f_060_b import vol_is_min_of_last_n_day

KEY = 'vol min of last 10d'
VAL = 61 * STEP
RECALL_DAYS = 3


def execute(stock_df: pd.DataFrame, **kwargs):
    vol_is_min_of_last_n_day(stock_df, 10, KEY)
