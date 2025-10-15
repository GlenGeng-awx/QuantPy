import math
import pandas as pd
from util import get_idx_by_date


def get_diff(stock_df: pd.DataFrame, date: str) -> float:
    max_close = stock_df['close'].max()
    min_close = stock_df['close'].min()

    ratio = math.pow(max_close / min_close, 1 / 20) - 1

    idx = get_idx_by_date(stock_df, date)
    close = stock_df.loc[idx]['close']
    return close * ratio


# date is in format of '20210101' or ('20210101', 'open')
def get_date(date):
    if type(date) is tuple:
        date, _ = date
    return date


# date is in format of '20210101' or ('20210101', 'open')
def get_price_key(date):
    if type(date) is tuple:
        _, price_key = date
    else:
        price_key = 'close'
    return price_key
