import pandas as pd
from statistical.ma import MA_20
from features.util import STEP, DELTA

KEY = 'up touch ma20'
VAL = 25 * STEP + DELTA


def execute(stock_df: pd.DataFrame, **kwargs):
    close = stock_df['close']
    high = stock_df['high']
    ma20 = stock_df[MA_20]

    indices = []

    for idx in close.index:
        if close[idx] < ma20[idx] < high[idx] * 1.005:
            indices.append(idx)

    s = pd.Series([True] * len(indices), index=indices)
    stock_df[KEY] = s.reindex(stock_df.index, fill_value=False)
