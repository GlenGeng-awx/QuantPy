import pandas as pd
from statistical.ma import MA_60
from features.g_14 import up_touch_ma

KEY = 'up touch ma60'
COLOR = 'green'


def execute(stock_df: pd.DataFrame, **kwargs):
    up_touch_ma(stock_df, MA_60, KEY)
