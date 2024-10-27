import pandas as pd
from features.util import STEP
from features.f_020_b import close_incr_n_days

KEY = 'close incr 1d'
VAL = 41 * STEP
RECALL_DAYS = 1


def execute(stock_df: pd.DataFrame, **kwargs):
    close_incr_n_days(stock_df, 1, KEY)
