import pandas as pd

KEY = 'close incr 3d'
COLOR = 'red'


def close_incr_n_days(stock_df: pd.DataFrame, n: int, key: str):
    close = stock_df['close']
    _open = stock_df['open']

    indices = []

    for idx in close.index[n:]:
        if all(close[idx - i] > close[idx - i - 1] for i in range(n)) \
                and all(_open[idx - i] < close[idx - i] for i in range(n)):
            indices.append(idx)

    s = pd.Series([True] * len(indices), index=indices)
    stock_df[key] = s.reindex(stock_df.index, fill_value=False)


def execute(stock_df: pd.DataFrame, **kwargs):
    close_incr_n_days(stock_df, 3, KEY)
