import pandas as pd
from statistical.ema import EMA_26
from features.g_14 import up_touch_ma

KEY = 'up touch ema26'
COLOR = 'green'


def execute(stock_df: pd.DataFrame, **kwargs):
    up_touch_ma(stock_df, EMA_26, KEY)
