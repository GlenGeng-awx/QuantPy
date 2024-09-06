import pandas as pd
from statistical.ma import MA_20
from features import STEP, DELTA

KEY = 'below ma20'
VAL = 1 * STEP + DELTA


def execute(stock_df: pd.DataFrame, **kwargs):
    close = stock_df['close']
    ma20 = stock_df[MA_20]

    stock_df[KEY] = close < ma20
