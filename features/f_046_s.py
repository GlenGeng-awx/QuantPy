import pandas as pd
from features.util import STEP, DELTA
from features.f_019_s import vol_decr_n_days

KEY = 'vol decr 1d'
VAL = 46 * STEP + DELTA
RECALL_DAYS = 1


def execute(stock_df: pd.DataFrame, **kwargs):
    vol_decr_n_days(stock_df, 1, KEY)
