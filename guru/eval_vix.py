import pandas as pd
from guru import HIT_NUM


# (long_tag, total_num, successful_rate, hit_num)
def eval_long(stock_df: pd.DataFrame, indices: list, sz: int, long_profit: float) -> dict:
    total_num, hit_num, successful_rate = 0, 0, 0.0

    for idx in indices:
        if idx + sz not in stock_df.index:
            continue
        total_num += 1

        max_close = stock_df.loc[idx:idx + sz]['close'].max()
        max_profit = max_close / stock_df.loc[idx]['close'] - 1

        if max_profit >= long_profit:
            hit_num += 1

    if total_num != 0:
        successful_rate = hit_num / total_num

    return {
        'long_tag': f'Long {total_num}, {successful_rate:.0%}, {hit_num}',
        'total_num': total_num,
        'successful_rate': successful_rate,
        'hit_num': hit_num,
    }


def filter_long(stock_df: pd.DataFrame, indices: list, param: dict):
    result = eval_long(stock_df, indices, param['sz'], param['long_profit'])
    if result['total_num'] >= HIT_NUM and result['successful_rate'] >= 0.9:
        return result
    return None


# (short_tag, total_num, successful_rate, hit_num)
def eval_short(stock_df: pd.DataFrame, indices: list, sz: int, short_profit: float) -> dict:
    total_num, hit_num, successful_rate = 0, 0, 0.0

    for idx in indices:
        if idx + sz not in stock_df.index:
            continue
        total_num += 1

        min_close = stock_df.loc[idx:idx + sz]['close'].min()
        max_profit = 1 - min_close / stock_df.loc[idx]['close']

        if max_profit >= short_profit:
            hit_num += 1

    if total_num != 0:
        successful_rate = hit_num / total_num

    return {
        'short_tag': f'Short {total_num}, {successful_rate:.0%}, {hit_num}',
        'total_num': total_num,
        'successful_rate': successful_rate,
        'hit_num': hit_num,
    }


def filter_short(stock_df: pd.DataFrame, indices: list, param: dict):
    result = eval_short(stock_df, indices, param['sz'], param['short_profit'])
    if result['total_num'] >= HIT_NUM and result['successful_rate'] >= 0.9:
        return result
    return None
