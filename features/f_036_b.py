import pandas as pd
from features.util import STEP
from features.f_020_b import close_incr_n_days

KEY = 'close incr 5d'
VAL = 36 * STEP
RECALL_DAYS = 3


def execute(stock_df: pd.DataFrame, **kwargs):
    close_incr_n_days(stock_df, 5, KEY)
