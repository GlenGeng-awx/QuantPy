import pandas as pd
from features.common import STEP
from features.f_019_b import vol_incr_n_days

KEY = 'vol incr 1d'
VAL = 46 * STEP
RECALL_DAYS = 1


def execute(stock_df: pd.DataFrame, **kwargs):
    vol_incr_n_days(stock_df, 1, KEY)
