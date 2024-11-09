import pandas as pd
from statistical.ma import MA_5
from features.g_14 import up_touch_ma

KEY = 'up touch ma5'
COLOR = 'green'


def execute(stock_df: pd.DataFrame, **kwargs):
    up_touch_ma(stock_df, MA_5, KEY)
