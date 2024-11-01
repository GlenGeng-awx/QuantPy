import pandas as pd
from features.common import STEP, DELTA
from features.f_042_s import price_decr_n_days

KEY = 'high decr 1d'
VAL = 43 * STEP + DELTA
RECALL_DAYS = 1


def execute(stock_df: pd.DataFrame, **kwargs):
    price_decr_n_days(stock_df, 1, 'high', KEY)
