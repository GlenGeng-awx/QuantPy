import pandas as pd
from statistical.ma import MA_120
from features.g_13 import down_touch_ma

KEY = 'down touch ma120'
COLOR = 'red'


def execute(stock_df: pd.DataFrame, **kwargs):
    down_touch_ma(stock_df, MA_120, KEY)
