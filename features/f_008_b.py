import pandas as pd
from statistical.macd import MACD_DIF, MACD_DEA
from features.util import STEP

KEY = 'macd golden cross'
VAL = 8 * STEP
RECALL_DAYS = 3


def execute(stock_df: pd.DataFrame, **kwargs):
    dif = stock_df[MACD_DIF]
    dea = stock_df[MACD_DEA]

    indices = []
    for idx in dif.index[1:]:
        if dif[idx] > dea[idx] and dif[idx - 1] < dea[idx - 1]:
            indices.append(idx)

    s = pd.Series([True] * len(indices), index=indices)
    stock_df[KEY] = s.reindex(stock_df.index, fill_value=False)
