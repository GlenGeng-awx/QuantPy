import pandas as pd
from features.util import STEP
from features.f_011_b import get_incr_benchmark

KEY = 'incr top 10% today'
VAL = 15 * STEP


def execute(stock_df: pd.DataFrame, **kwargs):
    benchmark = get_incr_benchmark(stock_df, 1)
    close = stock_df['close']

    indices = []

    for idx in close.index[1:]:
        if close.loc[idx] >= close.loc[idx - 1] * (1 + benchmark):
            indices.append(idx)

    s = pd.Series([True] * len(indices), index=indices)
    stock_df[KEY] = s.reindex(stock_df.index, fill_value=False)
