import pandas as pd

KEY = 'long upper shadow'
COLOR = 'green'


def get_upper_shadow_threshold(stock_df: pd.DataFrame) -> (float, float):
    _open = stock_df['open']
    close = stock_df['close']
    high = stock_df['high']

    pst = []
    for idx in _open.index:
        max_price = max(_open[idx], close[idx])
        pst.append(high[idx] / max_price)

    pst.sort()
    if len(pst) < 10:
        return None, None

    short_threshold = pst[len(pst) // 10]
    long_threshold = pst[-len(pst) // 10]

    print(f'short upper shadow threshold: {(short_threshold - 1) * 100:.2f}%')
    print(f'long upper shadow threshold: {(long_threshold - 1) * 100:.2f}%')
    return short_threshold, long_threshold


def execute(stock_df: pd.DataFrame, **kwargs):
    _, long_threshold = get_upper_shadow_threshold(stock_df)
    if long_threshold is None:
        return

    _open = stock_df['open']
    close = stock_df['close']
    high = stock_df['high']
    indices = []

    for idx in _open.index:
        max_price = max(_open[idx], close[idx])

        if max_price * long_threshold < high[idx]:
            indices.append(idx)

    s = pd.Series([True] * len(indices), index=indices)
    stock_df[KEY] = s.reindex(stock_df.index, fill_value=False)
