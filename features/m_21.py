import pandas as pd

KEY = 'long lower shadow'
COLOR = 'red'


def get_lower_shadow_threshold(stock_df: pd.DataFrame) -> (float, float):
    _open = stock_df['open']
    close = stock_df['close']
    low = stock_df['low']

    pst = []
    for idx in _open.index:
        min_price = min(_open[idx], close[idx])
        pst.append(min_price / low[idx])

    pst.sort()
    if len(pst) < 10:
        return None, None

    short_threshold = pst[len(pst) // 10]
    long_threshold = pst[-len(pst) // 10]

    print(f'short lower shadow threshold: {(short_threshold - 1) * 100:.2f}%')
    print(f'long lower shadow threshold: {(long_threshold - 1) * 100:.2f}%')
    return short_threshold, long_threshold


def execute(stock_df: pd.DataFrame, **kwargs):
    _, long_threshold = get_lower_shadow_threshold(stock_df)
    if long_threshold is None:
        return

    _open = stock_df['open']
    close = stock_df['close']
    low = stock_df['low']

    indices = []

    for idx in _open.index:
        min_price = min(_open[idx], close[idx])

        if low[idx] * long_threshold < min_price:
            indices.append(idx)

    s = pd.Series([True] * len(indices), index=indices)
    stock_df[KEY] = s.reindex(stock_df.index, fill_value=False)
