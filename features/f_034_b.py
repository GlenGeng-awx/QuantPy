import pandas as pd
from features.common import STEP
from features.f_019_b import vol_incr_n_days

KEY = 'vol incr 5d'
VAL = 34 * STEP
RECALL_DAYS = 3


def execute(stock_df: pd.DataFrame, **kwargs):
    vol_incr_n_days(stock_df, 5, KEY)
