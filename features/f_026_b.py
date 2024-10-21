import pandas as pd
from statistical.ma import MA_5
from features.util import STEP

KEY = 'down touch ma5'
VAL = 26 * STEP


def execute(stock_df: pd.DataFrame, **kwargs):
    close = stock_df['close']
    low = stock_df['low']
    ma5 = stock_df[MA_5]

    indices = []

    for idx in close.index:
        if close[idx] > ma5[idx] and ma5[idx] * 1.005 > low[idx]:
            indices.append(idx)

    s = pd.Series([True] * len(indices), index=indices)
    stock_df[KEY] = s.reindex(stock_df.index, fill_value=False)
