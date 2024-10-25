import pandas as pd
from features.util import STEP, DELTA
from features.f_020_s import price_decr_n_days

KEY = 'price decr 7d'
VAL = 37 * STEP + DELTA
RECALL_DAYS = 5


def execute(stock_df: pd.DataFrame, **kwargs):
    price_decr_n_days(stock_df, 7, KEY)
