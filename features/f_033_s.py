import pandas as pd
from features.util import STEP, DELTA
from features.f_011_s import decr_top_10pst_in_last_n_days

KEY = 'decr top 10% last 5d'
VAL = 33 * STEP + DELTA
RECALL_DAYS = 4


def execute(stock_df: pd.DataFrame, **kwargs):
    decr_top_10pst_in_last_n_days(stock_df, 5, KEY)
