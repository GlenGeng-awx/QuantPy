import pandas as pd
from statistical.ma import MA_20

KEY = 'up touch ma20'
COLOR = 'green'


def up_touch_ma(stock_df: pd.DataFrame, ma_key: str, output_key: str):
    _open = stock_df['open']
    close = stock_df['close']
    high = stock_df['high']
    ma = stock_df[ma_key]

    indices = []

    for idx in close.index:
        if _open[idx] < ma[idx] < high[idx] * 1.005 and close[idx] < ma[idx]:
            indices.append(idx)

    s = pd.Series([True] * len(indices), index=indices)
    stock_df[output_key] = s.reindex(stock_df.index, fill_value=False)


def execute(stock_df: pd.DataFrame, **kwargs):
    up_touch_ma(stock_df, MA_20, KEY)
