import pandas as pd
from features.util import STEP
from features.f_057_b import baseline_incr_n_days

KEY = 'baseline incr 3d'
VAL = 58 * STEP
RECALL_DAYS = 2


def execute(stock_df: pd.DataFrame, **kwargs):
    baseline_incr_n_days(stock_df, 3, KEY)
