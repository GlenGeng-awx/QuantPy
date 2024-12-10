import pandas as pd
from statistical.ema import EMA_12
from features.g_03 import up_thru_ma

KEY = 'up thru ema12'
COLOR = 'red'


def execute(stock_df: pd.DataFrame, **kwargs):
    up_thru_ma(stock_df, EMA_12, KEY)
