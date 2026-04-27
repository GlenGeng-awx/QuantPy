import math
import pandas as pd
from typing import NamedTuple
from util import get_idx_by_date


class Anchor(NamedTuple):
    date: str
    price_key: str = 'close'

    @classmethod
    def of(cls, raw):
        if isinstance(raw, tuple):
            return cls(*raw)
        return cls(raw)


def get_diff(stock_df: pd.DataFrame, date: str) -> float:
    max_close = stock_df['close'].max()
    min_close = stock_df['close'].min()

    ratio = math.pow(max_close / min_close, 1 / 20) - 1

    idx = get_idx_by_date(stock_df, date)
    close = stock_df.loc[idx]['close']
    return close * ratio
