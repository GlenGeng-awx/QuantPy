import pandas as pd
from features.util import STEP, DELTA
from features.f_016_s import get_upper_shadow_threshold

KEY = 'short upper shadow'
VAL = 21 * STEP + DELTA
RECALL_DAYS = 2


def execute(stock_df: pd.DataFrame, **kwargs):
    short_threshold, _ = get_upper_shadow_threshold(stock_df)
    if short_threshold is None:
        return

    _open = stock_df['open']
    close = stock_df['close']
    high = stock_df['high']
    indices = []

    for idx in _open.index:
        max_price = max(_open[idx], close[idx])

        if high[idx] < max_price * short_threshold:
            indices.append(idx)

    s = pd.Series([True] * len(indices), index=indices)
    stock_df[KEY] = s.reindex(stock_df.index, fill_value=False)