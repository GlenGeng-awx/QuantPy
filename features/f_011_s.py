import pandas as pd
from features.util import STEP, DELTA

KEY = 'decr top 10% last 3d'
VAL = 11 * STEP + DELTA
RECALL_DAYS = 3


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


def decr_top_10pst_in_last_n_days(stock_df: pd.DataFrame, n: int, output_key: str):
    benchmark = get_decr_benchmark(stock_df, n)
    close = stock_df['close']

    indices = []

    for idx in close.index[n:]:
        if close[idx] < close[idx - n] * (1 - benchmark):
            indices.append(idx)

    s = pd.Series([True] * len(indices), index=indices)
    stock_df[output_key] = s.reindex(stock_df.index, fill_value=False)


def execute(stock_df: pd.DataFrame, **kwargs):
    decr_top_10pst_in_last_n_days(stock_df, 3, KEY)
