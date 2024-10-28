import pandas as pd
from features.util import STEP, DELTA
from features.f_042_s import price_decr_n_days

KEY = 'high decr 5d'
VAL = 56 * STEP + DELTA
RECALL_DAYS = 3


def execute(stock_df: pd.DataFrame, **kwargs):
    price_decr_n_days(stock_df, 5, 'high', KEY)