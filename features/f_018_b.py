import pandas as pd
from features.util import STEP
from features.f_017_b import get_red_bar_threshold

KEY = 'short red bar'
VAL = 18 * STEP
RECALL_DAYS = 2


def execute(stock_df: pd.DataFrame, **kwargs):
    short_threshold, _ = get_red_bar_threshold(stock_df)
    if short_threshold is None:
        return

    _open = stock_df['open']
    close = stock_df['close']
    indices = []

    for idx in _open.index:
        if _open[idx] <= close[idx] <= _open[idx] * short_threshold:
            indices.append(idx)

    s = pd.Series([True] * len(indices), index=indices)
    stock_df[KEY] = s.reindex(stock_df.index, fill_value=False)
