import pandas as pd
from features.util import STEP
from features.f_020_b import price_incr_n_days

KEY = 'price incr 7d'
VAL = 37 * STEP


def execute(stock_df: pd.DataFrame, **kwargs):
    price_incr_n_days(stock_df, 7, KEY)
