import pandas as pd
from statistical.ema import EMA_12
from features.g_14 import up_touch_ma

KEY = 'up touch ema12'
COLOR = 'green'


def execute(stock_df: pd.DataFrame, **kwargs):
    up_touch_ma(stock_df, EMA_12, KEY)
