import pandas as pd
from features.common import STEP, DELTA
from features.f_060_s import vol_is_max_of_last_n_day

KEY = 'vol max of last 10d'
VAL = 61 * STEP + DELTA
RECALL_DAYS = 3


def execute(stock_df: pd.DataFrame, **kwargs):
    vol_is_max_of_last_n_day(stock_df, 10, KEY)
