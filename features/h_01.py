import pandas as pd

KEY = 'yesterday is local min'
COLOR = 'red'


def execute(stock_df: pd.DataFrame, **kwargs):
    close = stock_df['close']

    indices = []

    for idx in stock_df.index[2:]:
        if close[idx - 1] < close[idx - 2] and close[idx - 1] < close[idx]:
            indices.append(idx)

    s = pd.Series([True] * len(indices), index=indices)
    stock_df[KEY] = s.reindex(stock_df.index, fill_value=False)
