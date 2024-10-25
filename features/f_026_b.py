import pandas as pd
from statistical.ma import MA_5
from features.util import STEP
from features.f_025_b import down_touch_ma

KEY = 'down touch ma5'
VAL = 26 * STEP
RECALL_DAYS = 1


def execute(stock_df: pd.DataFrame, **kwargs):
    down_touch_ma(stock_df, MA_5, KEY)
