import pandas as pd
from statistical.trend import MA_20_TREND
from features.util import STEP, DELTA

KEY = 'trend switch down'
VAL = 4 * STEP + DELTA
RECALL_DAYS = 5


def execute(stock_df: pd.DataFrame, **kwargs):
    ma20_trend = stock_df[MA_20_TREND]

    indices = []

    for idx in ma20_trend.index[2:]:
        if ma20_trend[idx] == 'down' and ma20_trend[idx - 1] != 'down':
            indices.append(idx)

    s = pd.Series([True] * len(indices), index=indices)
    stock_df[KEY] = s.reindex(stock_df.index, fill_value=False)
