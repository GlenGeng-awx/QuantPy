import pandas as pd
from features.util import STEP, DELTA
from features.f_011_s import get_decr_benchmark

KEY = 'decr top 10% last 10d'
VAL = 12 * STEP + DELTA


def execute(stock_df: pd.DataFrame, **kwargs):
    benchmark = get_decr_benchmark(stock_df, 10)
    close = stock_df['close']

    indices = []

    for idx in close.index[10:]:
        if close[idx] < close[idx - 10] * (1 - benchmark):
            indices.append(idx)

    s = pd.Series([True] * len(indices), index=indices)
    stock_df[KEY] = s.reindex(stock_df.index, fill_value=False)
