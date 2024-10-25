import pandas as pd
from features.util import STEP, DELTA
from features.f_019_s import vol_decr_n_days

KEY = 'vol decr 5d'
VAL = 34 * STEP + DELTA


def execute(stock_df: pd.DataFrame, **kwargs):
    vol_decr_n_days(stock_df, 5, KEY)
