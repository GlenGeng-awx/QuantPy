import pandas as pd
from statistical.ema import EMA_10
from features.g_04 import down_thru_ma

KEY = 'down thru ema10'
COLOR = 'green'


def execute(stock_df: pd.DataFrame, **kwargs):
    down_thru_ma(stock_df, EMA_10, KEY)
