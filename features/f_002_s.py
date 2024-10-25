import pandas as pd
from statistical.ma import MA_5
from features.util import STEP, DELTA
from features.f_001_s import down_thru_ma

KEY = 'down thru ma5'
VAL = 2 * STEP + DELTA
RECALL_DAYS = 3


def execute(stock_df: pd.DataFrame, **kwargs):
    down_thru_ma(stock_df, MA_5, KEY)
