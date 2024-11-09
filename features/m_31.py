import pandas as pd

KEY = 'up engulfing'
COLOR = 'red'


def execute(stock_df: pd.DataFrame, **kwargs):
    _open = stock_df['open']
    close = stock_df['close']
    high = stock_df['high']
    low = stock_df['low']

    indices = []

    for idx in close.index[1:]:
        yesterday_is_down = close[idx - 1] < _open[idx - 1]
        today_is_up = close[idx] > _open[idx]
        today_is_engulfing = close[idx] > high[idx - 1] and _open[idx] < low[idx - 1]

        if yesterday_is_down and today_is_up and today_is_engulfing:
            indices.append(idx)

    s = pd.Series([True] * len(indices), index=indices)
    stock_df[KEY] = s.reindex(stock_df.index, fill_value=False)
