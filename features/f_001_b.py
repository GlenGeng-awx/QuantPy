import pandas as pd
from statistical.ma import MA_20
from features.util import STEP

KEY = 'up thru ma20'
VAL = 1 * STEP


def up_thru_ma(stock_df: pd.DataFrame, ma_key: str, output_key: str):
    close = stock_df['close']
    ma = stock_df[ma_key]

    indices = []

    for idx in close.index[1:]:
        if close[idx - 1] < ma[idx - 1] and close[idx] > ma[idx]:
            indices.append(idx)

    s = pd.Series([True] * len(indices), index=indices)
    stock_df[output_key] = s.reindex(stock_df.index, fill_value=False)


def execute(stock_df: pd.DataFrame, **kwargs):
    up_thru_ma(stock_df, MA_20, KEY)
