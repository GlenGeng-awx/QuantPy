import pandas as pd
from features.common import STEP
from features.f_016_b import get_lower_shadow_threshold

KEY = 'short lower shadow'
VAL = 21 * STEP
RECALL_DAYS = 2


def execute(stock_df: pd.DataFrame, **kwargs):
    short_threshold, _ = get_lower_shadow_threshold(stock_df)
    if short_threshold is None:
        return

    _open = stock_df['open']
    close = stock_df['close']
    low = stock_df['low']
    indices = []

    for idx in _open.index:
        min_price = min(_open[idx], close[idx])

        if low[idx] * short_threshold > min_price:
            indices.append(idx)

    s = pd.Series([True] * len(indices), index=indices)
    stock_df[KEY] = s.reindex(stock_df.index, fill_value=False)
