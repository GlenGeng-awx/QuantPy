import pandas as pd
from statistical.ma import MA_5
from features.common import STEP, DELTA
from features.f_025_s import up_touch_ma

KEY = 'up touch ma5'
VAL = 26 * STEP + DELTA
RECALL_DAYS = 1


def execute(stock_df: pd.DataFrame, **kwargs):
    up_touch_ma(stock_df, MA_5, KEY)
