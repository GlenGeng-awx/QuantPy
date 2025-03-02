import pandas as pd
from features.k_44 import get_decr_benchmark

KEY = 'decr bottom 10% last 3d'
COLOR = 'green'


def decr_bottom_10pst_in_last_n_days(stock_df: pd.DataFrame, n: int, output_key: str):
    _, bottom = get_decr_benchmark(stock_df, n)
    close = stock_df['close']

    indices = []

    for idx in close.index[n:]:
        if close[idx - n] * (1 - bottom) < close[idx] < close[idx - n]:
            indices.append(idx)

    s = pd.Series([True] * len(indices), index=indices)
    stock_df[output_key] = s.reindex(stock_df.index, fill_value=False)


def execute(stock_df: pd.DataFrame, **kwargs):
    decr_bottom_10pst_in_last_n_days(stock_df, 3, KEY)
