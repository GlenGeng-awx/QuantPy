import pandas as pd
from features.common import STEP
from features.f_040_0 import weekday_is_n

KEY = 'Tuesday'
VAL = 40 * STEP + 1
RECALL_DAYS = 1


def execute(stock_df: pd.DataFrame, **kwargs):
    weekday_is_n(stock_df, 1, KEY)
