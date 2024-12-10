import pandas as pd
from statistical.ema import EMA_10
from features.g_13 import down_touch_ma

KEY = 'down touch ema10'
COLOR = 'red'


def execute(stock_df: pd.DataFrame, **kwargs):
    down_touch_ma(stock_df, EMA_10, KEY)
