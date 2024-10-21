import pandas as pd
from features.util import STEP, DELTA

KEY = 'decr top 10% last 3d'
VAL = 11 * STEP + DELTA


def get_decr_benchmark(stock_df: pd.DataFrame, sz: int) -> float:
    close = stock_df['close']

    delta = []
    for idx in stock_df.index[sz:]:
        if close[idx] < close[idx - sz]:
            delta.append(1 - close[idx] / close[idx - sz])

    delta.sort()
    benchmark = delta[-len(delta) // 10]
    print(f'decr top 10% in last {sz}d - benchmark: {benchmark * 100:.2f}%')
    return benchmark


def execute(stock_df: pd.DataFrame, **kwargs):
    benchmark = get_decr_benchmark(stock_df, 3)
    close = stock_df['close']

    indices = []

    for idx in close.index[3:]:
        if close[idx] < close[idx - 3] * (1 - benchmark):
            indices.append(idx)

    s = pd.Series([True] * len(indices), index=indices)
    stock_df[KEY] = s.reindex(stock_df.index, fill_value=False)
