import pandas as pd
from technical.volume import VOLUME_REG
from features.util import STEP

KEY = 'high volume'
VAL = 14 * STEP


def execute(stock_df: pd.DataFrame, **kwargs):
    volume_reg = stock_df[VOLUME_REG]

    indices = []

    for idx in volume_reg.index:
        if volume_reg[idx] > 1:
            indices.append(idx)

    s = pd.Series([True] * len(indices), index=indices)
    stock_df[KEY] = s.reindex(stock_df.index, fill_value=False)
