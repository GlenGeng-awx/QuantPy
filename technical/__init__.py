import math
import pandas as pd

from util import get_idx_by_date
from technical.min_max import LOCAL_MAX_PRICE_1ST, LOCAL_MIN_PRICE_1ST


# yaxis_type: 'linear' or 'log'
def get_diff(stock_df: pd.DataFrame, date: str, yaxis_type: str) -> float:
    max_close = stock_df['close'].max()
    min_close = stock_df['close'].min()

    if yaxis_type == 'linear':
        return (max_close - min_close) / 15

    if yaxis_type == 'log':
        ratio = math.pow(max_close / min_close, 1 / 15) - 1

        idx = get_idx_by_date(stock_df, date)
        close = stock_df.loc[idx]['close']
        return close * ratio

    raise ValueError(f'Invalid yaxis_type: {yaxis_type}. Expected "linear" or "log".')


# return (x, y, text)
def plot_tags(stock_df: pd.DataFrame,
              stock_name,
              yaxis_type: str,
              date: str,
              tags: list) -> (str, float, str):
    idx = get_idx_by_date(stock_df, date)
    close = stock_df.loc[idx]['close']

    diff = get_diff(stock_df, date, yaxis_type)

    diff_ = diff
    if len(tags) == 2:
        diff_ = diff * 1.25
    if len(tags) == 3:
        diff_ = diff * 1.75
    elif len(tags) == 4:
        diff_ = diff * 2

    if stock_df.loc[idx][LOCAL_MAX_PRICE_1ST]:
        y = close + diff_ * 0.9
        text = '<br>'.join(reversed(tags))
    elif stock_df.loc[idx][LOCAL_MIN_PRICE_1ST]:
        y = close - diff_
        text = '<br>'.join(tags)
    else:
        print(f'invalid elliott {stock_name} {date} {tags}')
        raise ValueError

    return date, y, text
