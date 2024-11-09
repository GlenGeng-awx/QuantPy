import pandas as pd

KEY = 'fake red bar'
COLOR = 'red'


def execute(stock_df: pd.DataFrame, **kwargs):
    _open = stock_df['open']
    close = stock_df['close']

    indices = []

    for idx in close.index[1:]:
        if _open[idx] < close[idx] < close[idx - 1]:
            indices.append(idx)

    s = pd.Series([True] * len(indices), index=indices)
    stock_df[KEY] = s.reindex(stock_df.index, fill_value=False)
