import pandas as pd
from features.common import STEP, DELTA
from features.f_042_s import price_decr_n_days

KEY = 'high decr 3d'
VAL = 54 * STEP + DELTA
RECALL_DAYS = 2


def execute(stock_df: pd.DataFrame, **kwargs):
    price_decr_n_days(stock_df, 3, 'high', KEY)
