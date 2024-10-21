import pandas as pd
from statistical.ma import MA_5
from features.util import STEP, DELTA

KEY = 'down thru ma5'
VAL = 2 * STEP + DELTA


def execute(stock_df: pd.DataFrame, **kwargs):
    close = stock_df['close']
    ma5 = stock_df[MA_5]

    indices = []

    for idx in close.index[1:]:
        if close[idx - 1] > ma5[idx - 1] and close[idx] < ma5[idx]:
            indices.append(idx)

    s = pd.Series([True] * len(indices), index=indices)
    stock_df[KEY] = s.reindex(stock_df.index, fill_value=False)
