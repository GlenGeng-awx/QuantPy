import pandas as pd
from statistical.ma import MA_5
from features.util import STEP, DELTA

KEY = 'up touch ma5'
VAL = 26 * STEP + DELTA


def execute(stock_df: pd.DataFrame, **kwargs):
    close = stock_df['close']
    high = stock_df['high']
    ma5 = stock_df[MA_5]

    indices = []

    for idx in close.index:
        if close[idx] < ma5[idx] < high[idx] * 1.005:
            indices.append(idx)

    s = pd.Series([True] * len(indices), index=indices)
    stock_df[KEY] = s.reindex(stock_df.index, fill_value=False)
