import pandas as pd
import json
from datetime import datetime
from util import get_idx_by_date
from guru import factors, targets

HITS = 4


def touch_file(filename: str):
    with open(filename, 'w'):
        pass


def interpolate_context(stock_df: pd.DataFrame, context: dict) -> dict:
    interpolated_context = {}
    for key, dates in context.items():
        filled = set()
        for date in dates:
            idx = get_idx_by_date(stock_df, date)
            for i in range(idx, idx + 3):
                if i in stock_df.index:
                    filled.add(stock_df.loc[i]['Date'])
        interpolated_context[key] = filled
    return interpolated_context


def pick(total_num, up_hit, down_hit) -> bool:
    if total_num < HITS:
        return False
    ratio = (up_hit + down_hit) / total_num

    if total_num == 4 and ratio == 1:
        return True
    if total_num == 5 and ratio >= 0.8:
        return True
    if 6 <= total_num <= 10 and ratio >= 0.7:
        return True
    if total_num >= 11 and ratio >= 0.6:
        return True

    return False


def select_impl(stock_df: pd.DataFrame, stock_name: str, context: dict, keys: list, dates: set):
    # print(f'Selecting with keys: {keys} and dates: {dates}')
    total_num, up_hit, down_hit = 0, 0, 0

    for date in dates:
        idx = get_idx_by_date(stock_df, date)
        if idx + 15 not in stock_df.index:
            continue
        total_num += 1

        negative_iv, positive_iv = targets
        if date in context.get(positive_iv.KEY, set()):
            up_hit += 1
        elif date in context.get(negative_iv.KEY, set()):
            down_hit += 1

    if pick(total_num, up_hit, down_hit):
        with open(f'tmp/{stock_name}.txt', 'a') as fd:
            fd.write(f'{json.dumps(keys)}\ttotal {total_num}, up {up_hit}, down {down_hit}\n')
        print(f'Found a selection: {keys} with {total_num} total, {up_hit} up hits, {down_hit} down hits')


def select(stock_df: pd.DataFrame, stock_name: str, context: dict, i: int, keys: list, curr_dates: set):
    # fail fast
    if len(curr_dates) < HITS:
        return

    # we are done
    if i == len(factors):
        select_impl(stock_df, stock_name, context, keys, curr_dates)
        return

    keys = keys.copy()

    # not pick i
    select(stock_df, stock_name, context, i + 1, keys, curr_dates)

    # pick i
    key = factors[i].KEY

    keys.append(key)
    curr_dates = context.get(key, set()).intersection(curr_dates)

    select(stock_df, stock_name, context, i + 1, keys, curr_dates)


def train(stock_df: pd.DataFrame, stock_name: str, context: dict) -> None:
    touch_file(f'tmp/{stock_name}.txt')
    context = interpolate_context(stock_df, context)

    start_time = datetime.now()
    select(stock_df, stock_name, context, 0, [], set(stock_df['Date'].to_list()))
    print(f'Training completed for {stock_name} in {(datetime.now() - start_time).total_seconds()} seconds')
