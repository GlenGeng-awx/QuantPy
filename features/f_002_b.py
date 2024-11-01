import pandas as pd
from statistical.ma import MA_5
from features.common import STEP
from features.f_001_b import up_thru_ma

KEY = 'up thru ma5'
VAL = 2 * STEP
RECALL_DAYS = 3


def execute(stock_df: pd.DataFrame, **kwargs):
    up_thru_ma(stock_df, MA_5, KEY)
