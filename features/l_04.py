import pandas as pd
from technical.volume import VOLUME

KEY = 'vol decr 3d'
COLOR = 'green'


def vol_decr_n_days(stock_df: pd.DataFrame, n: int, key: str):
    volume = stock_df[VOLUME]

    indices = []

    for idx in volume.index[n:]:
        if all(volume[idx - i] < volume[idx - i - 1] for i in range(n)):
            indices.append(idx)

    s = pd.Series([True] * len(indices), index=indices)
    stock_df[key] = s.reindex(stock_df.index, fill_value=False)


def execute(stock_df: pd.DataFrame, **kwargs):
    vol_decr_n_days(stock_df, 3, KEY)
