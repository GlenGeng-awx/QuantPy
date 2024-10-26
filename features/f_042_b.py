import pandas as pd
from features.util import STEP
from features.f_041_b import price_incr

KEY = 'low incr'
VAL = 42 * STEP
RECALL_DAYS = 1


def execute(stock_df: pd.DataFrame, **kwargs):
    price_incr(stock_df, 'low', KEY)
