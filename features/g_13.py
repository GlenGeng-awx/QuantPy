import pandas as pd
from statistical.ma import MA_20

KEY = 'down touch ma20'
COLOR = 'red'


def down_touch_ma(stock_df: pd.DataFrame, ma_key: str, output_key: str):
    _open = stock_df['open']
    close = stock_df['close']
    low = stock_df['low']
    ma = stock_df[ma_key]

    indices = []

    for idx in close.index:
        if _open[idx] > ma[idx] and close[idx] > ma[idx] and ma[idx] * 1.005 > low[idx]:
            indices.append(idx)

    s = pd.Series([True] * len(indices), index=indices)
    stock_df[output_key] = s.reindex(stock_df.index, fill_value=False)


def execute(stock_df: pd.DataFrame, **kwargs):
    down_touch_ma(stock_df, MA_20, KEY)
