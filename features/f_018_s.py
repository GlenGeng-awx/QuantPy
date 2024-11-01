import pandas as pd
from features.common import STEP, DELTA
from features.f_017_s import get_green_bar_threshold

KEY = 'short green bar'
VAL = 18 * STEP + DELTA
RECALL_DAYS = 2


def execute(stock_df: pd.DataFrame, **kwargs):
    short_threshold, _ = get_green_bar_threshold(stock_df)
    if short_threshold is None:
        return

    _open = stock_df['open']
    close = stock_df['close']
    indices = []

    for idx in _open.index:
        if close[idx] <= _open[idx] <= close[idx] * short_threshold:
            indices.append(idx)

    s = pd.Series([True] * len(indices), index=indices)
    stock_df[KEY] = s.reindex(stock_df.index, fill_value=False)
