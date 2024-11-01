import pandas as pd
from technical.volume import VOLUME_REG
from features.common import STEP

KEY = 'vol min of last 5d'
VAL = 60 * STEP
RECALL_DAYS = 2


def vol_is_min_of_last_n_day(stock_df: pd.DataFrame, n: int, output_key):
    volume_reg = stock_df[VOLUME_REG]

    indices = []

    for idx in volume_reg.index[n:]:
        if volume_reg[idx] == volume_reg.loc[idx - n + 1:idx].min():
            indices.append(idx)

    s = pd.Series([True] * len(indices), index=indices)
    stock_df[output_key] = s.reindex(stock_df.index, fill_value=False)


def execute(stock_df: pd.DataFrame, **kwargs):
    vol_is_min_of_last_n_day(stock_df, 5, KEY)
