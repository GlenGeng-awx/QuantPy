import pandas as pd
from features.util import STEP, DELTA
from features.f_041_s import price_decr

KEY = 'low decr'
VAL = 42 * STEP + DELTA
RECALL_DAYS = 1


def execute(stock_df: pd.DataFrame, **kwargs):
    price_decr(stock_df, 'low', KEY)
