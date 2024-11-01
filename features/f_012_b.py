import pandas as pd
from features.common import STEP
from features.f_011_b import incr_top_10pst_in_last_n_days

KEY = 'incr top 10% last 10d'
VAL = 12 * STEP
RECALL_DAYS = 5


def execute(stock_df: pd.DataFrame, **kwargs):
    incr_top_10pst_in_last_n_days(stock_df, 10, KEY)
