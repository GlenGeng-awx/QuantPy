import pandas as pd
from statistical.ma import MA_5
from features.g_04 import down_thru_ma

KEY = 'down thru ma5'
COLOR = 'green'


def execute(stock_df: pd.DataFrame, **kwargs):
    down_thru_ma(stock_df, MA_5, KEY)
