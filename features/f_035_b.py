import pandas as pd
from features.util import STEP
from features.f_019_b import vol_incr_n_days

KEY = 'vol incr 7d'
VAL = 35 * STEP


def execute(stock_df: pd.DataFrame, **kwargs):
    vol_incr_n_days(stock_df, 7, KEY)
