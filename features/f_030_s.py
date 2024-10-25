import pandas as pd
from statistical.ma import MA_60
from features.util import STEP, DELTA
from features.f_025_s import up_touch_ma

KEY = 'up touch ma60'
VAL = 30 * STEP + DELTA
RECALL_DAYS = 3


def execute(stock_df: pd.DataFrame, **kwargs):
    up_touch_ma(stock_df, MA_60, KEY)
