import pandas as pd
from statistical.ma import MA_60
from features.common import STEP
from features.f_001_b import up_thru_ma

KEY = 'up thru ma60'
VAL = 29 * STEP
RECALL_DAYS = 5


def execute(stock_df: pd.DataFrame, **kwargs):
    up_thru_ma(stock_df, MA_60, KEY)
