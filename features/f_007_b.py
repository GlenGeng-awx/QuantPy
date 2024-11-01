import pandas as pd
from statistical.rsi import RSI_14
from features.common import STEP

KEY = 'rsi above 70'
VAL = 7 * STEP
RECALL_DAYS = 3


def execute(stock_df: pd.DataFrame, **kwargs):
    rsi_14 = stock_df[RSI_14]
    stock_df[KEY] = rsi_14 > 70
