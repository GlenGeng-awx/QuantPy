import pandas as pd
from features.util import STEP
from features.f_040_0 import weekday_is_n

KEY = 'Thursday'
VAL = 40 * STEP + 3
RECALL_DAYS = 1


def execute(stock_df: pd.DataFrame, **kwargs):
    weekday_is_n(stock_df, 3, KEY)
