import pandas as pd
from technical.volume import VOLUME_REG

KEY = 'normal vol'
COLOR = 'red'


def execute(stock_df: pd.DataFrame, **kwargs):
    volume_reg = stock_df[VOLUME_REG]

    indices = []

    for idx in volume_reg.index:
        if -0.5 < volume_reg[idx] < 0.5:
            indices.append(idx)

    s = pd.Series([True] * len(indices), index=indices)
    stock_df[KEY] = s.reindex(stock_df.index, fill_value=False)
