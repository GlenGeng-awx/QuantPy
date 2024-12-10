import pandas as pd
from statistical.ema import EMA_12
from features.g_13 import down_touch_ma

KEY = 'down touch ema12'
COLOR = 'red'


def execute(stock_df: pd.DataFrame, **kwargs):
    down_touch_ma(stock_df, EMA_12, KEY)
