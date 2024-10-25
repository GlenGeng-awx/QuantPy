import pandas as pd
from statistical.ma import MA_60
from features.util import STEP, DELTA
from features.f_001_s import down_thru_ma

KEY = 'down thru ma60'
VAL = 29 * STEP + DELTA
RECALL_DAYS = 5


def execute(stock_df: pd.DataFrame, **kwargs):
    down_thru_ma(stock_df, MA_60, KEY)
