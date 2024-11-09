import pandas as pd
from statistical.ma import MA_60
from features.g_04 import down_thru_ma

KEY = 'down thru ma60'
COLOR = 'green'


def execute(stock_df: pd.DataFrame, **kwargs):
    down_thru_ma(stock_df, MA_60, KEY)
