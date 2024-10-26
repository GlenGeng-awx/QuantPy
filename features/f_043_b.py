import pandas as pd
from features.util import STEP
from features.f_042_b import price_incr

KEY = 'high incr'
VAL = 43 * STEP
RECALL_DAYS = 1


def execute(stock_df: pd.DataFrame, **kwargs):
    price_incr(stock_df, 'high', KEY)
