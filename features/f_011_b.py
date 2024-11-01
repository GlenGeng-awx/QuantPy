import pandas as pd
from features.common import STEP

KEY = 'incr top 10% last 3d'
VAL = 11 * STEP
RECALL_DAYS = 3


def get_incr_benchmark(stock_df: pd.DataFrame, sz: int) -> float:
    close = stock_df['close']

    delta = []
    for idx in stock_df.index[sz:]:
        if close[idx] > close[idx - sz]:
            delta.append(close[idx] / close[idx - sz] - 1)

    delta.sort()
    benchmark = delta[-len(delta) // 10]
    print(f'incr top 10% in last {sz}d - benchmark: {benchmark * 100:.2f}%')
    return benchmark


def incr_top_10pst_in_last_n_days(stock_df: pd.DataFrame, n: int, output_key: str):
    benchmark = get_incr_benchmark(stock_df, n)
    close = stock_df['close']

    indices = []

    for idx in close.index[n:]:
        if close[idx] > close[idx - n] * (1 + benchmark):
            indices.append(idx)

    s = pd.Series([True] * len(indices), index=indices)
    stock_df[output_key] = s.reindex(stock_df.index, fill_value=False)


def execute(stock_df: pd.DataFrame, **kwargs):
    incr_top_10pst_in_last_n_days(stock_df, 3, KEY)
