import pandas as pd
from statistical.ma import MA_60
from features.util import STEP
from features.f_025_b import down_touch_ma

KEY = 'down touch ma60'
VAL = 30 * STEP


def execute(stock_df: pd.DataFrame, **kwargs):
    down_touch_ma(stock_df, MA_60, KEY)
