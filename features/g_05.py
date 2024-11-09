import pandas as pd
from statistical.ma import MA_60
from features.g_03 import up_thru_ma

KEY = 'up thru ma60'
COLOR = 'red'


def execute(stock_df: pd.DataFrame, **kwargs):
    up_thru_ma(stock_df, MA_60, KEY)
