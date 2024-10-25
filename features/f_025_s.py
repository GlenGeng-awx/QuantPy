import pandas as pd
from statistical.ma import MA_20
from features.util import STEP, DELTA

KEY = 'up touch ma20'
VAL = 25 * STEP + DELTA
RECALL_DAYS = 2


def up_touch_ma(stock_df: pd.DataFrame, ma_key: str, output_key: str):
    close = stock_df['close']
    high = stock_df['high']
    ma = stock_df[ma_key]

    indices = []

    for idx in close.index:
        if close[idx] < ma[idx] < high[idx] * 1.005:
            indices.append(idx)

    s = pd.Series([True] * len(indices), index=indices)
    stock_df[output_key] = s.reindex(stock_df.index, fill_value=False)


def execute(stock_df: pd.DataFrame, **kwargs):
    up_touch_ma(stock_df, MA_20, KEY)
