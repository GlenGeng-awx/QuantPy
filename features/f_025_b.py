import pandas as pd
from statistical.ma import MA_20
from features.util import STEP

KEY = 'down touch ma20'
VAL = 25 * STEP


def execute(stock_df: pd.DataFrame, **kwargs):
    close = stock_df['close']
    low = stock_df['low']
    ma20 = stock_df[MA_20]

    indices = []

    for idx in close.index:
        if close[idx] > ma20[idx] and ma20[idx] * 1.005 > low[idx]:
            indices.append(idx)

    s = pd.Series([True] * len(indices), index=indices)
    stock_df[KEY] = s.reindex(stock_df.index, fill_value=False)
