import pandas as pd
from statistical.ma import MA_20
from features.util import STEP, DELTA

KEY = 'down thru ma20'
VAL = 1 * STEP + DELTA


def execute(stock_df: pd.DataFrame, **kwargs):
    close = stock_df['close']
    ma20 = stock_df[MA_20]

    indices = []

    for idx in close.index[1:]:
        if close[idx - 1] > ma20[idx - 1] and close[idx] < ma20[idx]:
            indices.append(idx)

    s = pd.Series([True] * len(indices), index=indices)
    stock_df[KEY] = s.reindex(stock_df.index, fill_value=False)
