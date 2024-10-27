import pandas as pd
from features.util import STEP
from features.f_042_b import price_incr_n_days

KEY = 'low incr 5d'
VAL = 52 * STEP
RECALL_DAYS = 3


def execute(stock_df: pd.DataFrame, **kwargs):
    price_incr_n_days(stock_df, 5, 'low', KEY)
