import pandas as pd
from statistical.bband import BBAND_PST
from features import STEP

KEY = 'bband pst gt 0.85'
VAL = 6 * STEP


def execute(stock_df: pd.DataFrame, **kwargs):
    bband_pst = stock_df[BBAND_PST]
    stock_df[KEY] = bband_pst > 0.85
