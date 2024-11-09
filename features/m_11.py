import pandas as pd

KEY = 'long red bar'
COLOR = 'red'


def get_red_bar_threshold(stock_df: pd.DataFrame) -> (float, float):
    _open = stock_df['open']
    close = stock_df['close']

    pst = []
    for idx in _open.index:
        if _open[idx] < close[idx]:
            pst.append(close[idx] / _open[idx])

    pst.sort()
    if len(pst) < 10:
        return None, None

    short_threshold = pst[len(pst) // 10]
    long_threshold = pst[-len(pst) // 10]

    print(f'short red bar threshold: {(short_threshold - 1) * 100:.2f}%')
    print(f'long red bar threshold: {(long_threshold - 1) * 100:.2f}%')
    return short_threshold, long_threshold


def execute(stock_df: pd.DataFrame, **kwargs):
    _, long_threshold = get_red_bar_threshold(stock_df)
    if long_threshold is None:
        return

    _open = stock_df['open']
    close = stock_df['close']
    indices = []

    for idx in _open.index:
        if _open[idx] * long_threshold <= close[idx]:
            indices.append(idx)

    s = pd.Series([True] * len(indices), index=indices)
    stock_df[KEY] = s.reindex(stock_df.index, fill_value=False)
