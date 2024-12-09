import pandas as pd
from statistical.ma import MA_120
from features.g_03 import up_thru_ma

KEY = 'up thru ma120'
COLOR = 'red'


def execute(stock_df: pd.DataFrame, **kwargs):
    up_thru_ma(stock_df, MA_120, KEY)
