import pandas as pd
from statistical.rsi import RSI_14

KEY = 'rsi above 70'
COLOR = 'red'


def execute(stock_df: pd.DataFrame, **kwargs):
    rsi_14 = stock_df[RSI_14]
    stock_df[KEY] = rsi_14 > 70
