import pandas as pd
from statistical.ma import MA_120
from features.g_14 import up_touch_ma

KEY = 'up touch ma120'
COLOR = 'green'


def execute(stock_df: pd.DataFrame, **kwargs):
    up_touch_ma(stock_df, MA_120, KEY)
