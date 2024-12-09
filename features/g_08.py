import pandas as pd
from statistical.ma import MA_120
from features.g_04 import down_thru_ma

KEY = 'down thru ma120'
COLOR = 'green'


def execute(stock_df: pd.DataFrame, **kwargs):
    down_thru_ma(stock_df, MA_120, KEY)
