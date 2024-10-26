import pandas as pd
from technical.volume import VOLUME_REG
from features.util import STEP

KEY = 'normal vol'
VAL = 14 * STEP + 3
RECALL_DAYS = 1


def execute(stock_df: pd.DataFrame, **kwargs):
    volume_reg = stock_df[VOLUME_REG]

    indices = []

    for idx in volume_reg.index:
        if -1 < volume_reg[idx] < 1:
            indices.append(idx)

    s = pd.Series([True] * len(indices), index=indices)
    stock_df[KEY] = s.reindex(stock_df.index, fill_value=False)
