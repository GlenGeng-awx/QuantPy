import pandas as pd
from statistical.ema import EMA_20
from features.g_13 import down_touch_ma

KEY = 'down touch ema20'
COLOR = 'red'


def execute(stock_df: pd.DataFrame, **kwargs):
    down_touch_ma(stock_df, EMA_20, KEY)