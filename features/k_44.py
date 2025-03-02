import pandas as pd

KEY = 'decr top 10% last 3d'
COLOR = 'green'


def get_decr_benchmark(stock_df: pd.DataFrame, sz: int) -> (float, float):
    close = stock_df['close']

    delta = []
    for idx in stock_df.index[sz:]:
        if close[idx] < close[idx - sz]:
            delta.append(1 - close[idx] / close[idx - sz])

    delta.sort()
    top = delta[-len(delta) // 10]
    bottom = delta[len(delta) // 10]
    print(f'decr (top, bottom) 10% in last {sz}d - top: {top * 100:.2f}%, bottom: {bottom * 100:.2f}%')
    return top, bottom


def decr_top_10pst_in_last_n_days(stock_df: pd.DataFrame, n: int, output_key: str):
    top, _ = get_decr_benchmark(stock_df, n)
    close = stock_df['close']

    indices = []

    for idx in close.index[n:]:
        if close[idx] < close[idx - n] * (1 - top):
            indices.append(idx)

    s = pd.Series([True] * len(indices), index=indices)
    stock_df[output_key] = s.reindex(stock_df.index, fill_value=False)


def execute(stock_df: pd.DataFrame, **kwargs):
    decr_top_10pst_in_last_n_days(stock_df, 3, KEY)
