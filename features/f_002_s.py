import pandas as pd
from statistical.ma import MA_5
from features import STEP, DELTA

KEY = 'below ma5'
VAL = 2 * STEP + DELTA


def execute(stock_df: pd.DataFrame, **kwargs):
    close = stock_df['close']
    ma5 = stock_df[MA_5]

    stock_df[KEY] = close < ma5
