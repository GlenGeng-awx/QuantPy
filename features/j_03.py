import pandas as pd
from statistical.bband import BBAND_PST

KEY = 'bband pst gt 0.85'
COLOR = 'red'


def execute(stock_df: pd.DataFrame, **kwargs):
    bband_pst = stock_df[BBAND_PST]
    stock_df[KEY] = bband_pst > 0.85
