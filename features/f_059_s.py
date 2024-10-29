import pandas as pd
from features.util import STEP, DELTA
from features.f_057_s import baseline_decr_n_days

KEY = 'baseline decr 5d'
VAL = 59 * STEP + DELTA
RECALL_DAYS = 3


def execute(stock_df: pd.DataFrame, **kwargs):
    baseline_decr_n_days(stock_df, 5, KEY)
