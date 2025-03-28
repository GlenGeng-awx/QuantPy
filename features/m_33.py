import pandas as pd

KEY = 'up harami'
COLOR = 'red'


def execute(stock_df: pd.DataFrame, **kwargs):
    _open = stock_df['open']
    close = stock_df['close']

    indices = []

    for idx in close.index[1:]:
        min_of_yesterday = min(_open[idx - 1], close[idx - 1])
        max_of_yesterday = max(_open[idx - 1], close[idx - 1])

        if min_of_yesterday < _open[idx] < close[idx] < max_of_yesterday:
            indices.append(idx)

    s = pd.Series([True] * len(indices), index=indices)
    stock_df[KEY] = s.reindex(stock_df.index, fill_value=False)
