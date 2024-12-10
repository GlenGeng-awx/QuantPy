import pandas as pd
from statistical.ema import EMA_5
from features.g_13 import down_touch_ma

KEY = 'down touch ema5'
COLOR = 'red'


def execute(stock_df: pd.DataFrame, **kwargs):
    down_touch_ma(stock_df, EMA_5, KEY)
