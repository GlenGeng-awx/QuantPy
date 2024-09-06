import pandas as pd
from statistical.rsi import RSI_14
from features.util import STEP, DELTA

KEY = 'rsi below 30'
VAL = 7 * STEP + DELTA


def execute(stock_df: pd.DataFrame, **kwargs):
    rsi_14 = stock_df[RSI_14]
    stock_df[KEY] = rsi_14 < 30
