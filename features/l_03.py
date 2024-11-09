import pandas as pd
from technical.volume import VOLUME_REG

KEY = 'vol incr 3d'
COLOR = 'red'


def vol_incr_n_days(stock_df: pd.DataFrame, n: int, key: str):
    volume_reg = stock_df[VOLUME_REG]

    indices = []

    for idx in volume_reg.index[n:]:
        if all(volume_reg[idx - i] > volume_reg[idx - i - 1] for i in range(n)):
            indices.append(idx)

    s = pd.Series([True] * len(indices), index=indices)
    stock_df[key] = s.reindex(stock_df.index, fill_value=False)


def execute(stock_df: pd.DataFrame, **kwargs):
    vol_incr_n_days(stock_df, 3, KEY)
