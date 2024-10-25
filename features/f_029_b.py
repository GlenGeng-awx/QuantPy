import pandas as pd
from statistical.ma import MA_60
from features.util import STEP
from features.f_001_b import up_thru_ma

KEY = 'up thru ma60'
VAL = 29 * STEP


def execute(stock_df: pd.DataFrame, **kwargs):
    up_thru_ma(stock_df, MA_60, KEY)
