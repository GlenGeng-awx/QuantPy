import pandas as pd
from features.util import STEP, DELTA
from features.f_011_s import decr_top_10pst_in_last_n_days

KEY = 'decr top 10% today'
VAL = 15 * STEP + DELTA


def execute(stock_df: pd.DataFrame, **kwargs):
    decr_top_10pst_in_last_n_days(stock_df, 1, KEY)
