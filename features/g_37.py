import pandas as pd
from statistical.ema import EMA_20
from features.g_03 import up_thru_ma

KEY = 'up thru ema20'
COLOR = 'red'


def execute(stock_df: pd.DataFrame, **kwargs):
    up_thru_ma(stock_df, EMA_20, KEY)
