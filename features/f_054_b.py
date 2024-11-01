import pandas as pd
from features.common import STEP
from features.f_042_b import price_incr_n_days

KEY = 'high incr 3d'
VAL = 54 * STEP
RECALL_DAYS = 2


def execute(stock_df: pd.DataFrame, **kwargs):
    price_incr_n_days(stock_df, 3, 'high', KEY)
