import pandas as pd
from features.common import STEP, DELTA
from features.f_020_s import close_decr_n_days

KEY = 'close decr 1d'
VAL = 41 * STEP + DELTA
RECALL_DAYS = 1


def execute(stock_df: pd.DataFrame, **kwargs):
    close_decr_n_days(stock_df, 1, KEY)
