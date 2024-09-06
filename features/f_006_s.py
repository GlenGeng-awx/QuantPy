import pandas as pd
from statistical.bband import BBAND_PST
from features.util import STEP, DELTA

KEY = 'bband pst lt 0.15'
VAL = 6 * STEP + DELTA


def execute(stock_df: pd.DataFrame, **kwargs):
    bband_pst = stock_df[BBAND_PST]
    stock_df[KEY] = bband_pst < 0.15
