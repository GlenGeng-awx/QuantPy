import pandas as pd
from features.util import STEP, DELTA
from features.f_020_s import close_decr_n_days

KEY = 'close decr 5d'
VAL = 36 * STEP + DELTA
RECALL_DAYS = 3


def execute(stock_df: pd.DataFrame, **kwargs):
    close_decr_n_days(stock_df, 5, KEY)
