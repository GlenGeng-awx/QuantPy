import pandas as pd
from features.util import STEP, DELTA
from features.f_019_s import vol_decr_n_days

KEY = 'vol decr 7d'
VAL = 35 * STEP + DELTA
RECALL_DAYS = 5


def execute(stock_df: pd.DataFrame, **kwargs):
    vol_decr_n_days(stock_df, 7, KEY)
