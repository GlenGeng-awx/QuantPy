import pandas as pd
from features.common import STEP
from features.f_057_b import baseline_incr_n_days

KEY = 'baseline incr 5d'
VAL = 59 * STEP
RECALL_DAYS = 3


def execute(stock_df: pd.DataFrame, **kwargs):
    baseline_incr_n_days(stock_df, 5, KEY)
