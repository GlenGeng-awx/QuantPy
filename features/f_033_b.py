import pandas as pd
from features.util import STEP
from features.f_011_b import incr_top_10pst_in_last_n_days

KEY = 'incr top 10% last 5d'
VAL = 33 * STEP
RECALL_DAYS = 4


def execute(stock_df: pd.DataFrame, **kwargs):
    incr_top_10pst_in_last_n_days(stock_df, 5, KEY)
