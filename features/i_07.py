import pandas as pd
from technical.volume import VOLUME

KEY = 'vol max of last 5d'
COLOR = 'green'


def vol_is_max_of_last_n_day(stock_df: pd.DataFrame, n: int, output_key):
    volume = stock_df[VOLUME]

    indices = []

    for idx in volume.index[n:]:
        if volume[idx] == volume.loc[idx - n + 1:idx].max():
            indices.append(idx)

    s = pd.Series([True] * len(indices), index=indices)
    stock_df[output_key] = s.reindex(stock_df.index, fill_value=False)


def execute(stock_df: pd.DataFrame, **kwargs):
    vol_is_max_of_last_n_day(stock_df, 5, KEY)
