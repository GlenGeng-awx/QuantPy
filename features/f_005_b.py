import pandas as pd
from technical.volume import VOLUME_REG
from features import STEP

KEY = 'up with high vol'
VAL = 5 * STEP


def execute(stock_df: pd.DataFrame, **kwargs):
    close = stock_df['close']
    volume_reg = stock_df[VOLUME_REG]

    indices = []

    for idx in volume_reg.index[1:]:
        if volume_reg[idx] > 2 and close[idx] > close[idx - 1]:
            indices.append(idx)

    s = pd.Series([True] * len(indices), index=indices)
    stock_df[KEY] = s.reindex(stock_df.index, fill_value=False)
