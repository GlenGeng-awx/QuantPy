import pandas as pd
import json
import os.path
from datetime import datetime
from util import get_idx_by_date, shrink_date_str, touch_file
from guru import factors, required_factors, get_target_dates

MIN_HITS = 4
CORRECT_RATIO = 0.70


# model/_train_36m/QQQ.2025-10-21.txt
def get_file_name(stock_name: str, stock_df: pd.DataFrame, train_mode: str) -> str:
    version = shrink_date_str(stock_df['Date'].iloc[-1])
    return f'model/{train_mode}/{stock_name}.{version}.txt'


def _get_sz(key: str) -> int:
    if key not in [factor.KEY for factor in factors]:
        return 1
    if key in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']:
        return 1
    return 3


def interpolate_context(stock_df: pd.DataFrame, context: dict) -> dict:
    interpolated_context = {}
    for key, dates in context.items():
        sz = _get_sz(key)
        filled = set()

        for date in dates:
            idx = get_idx_by_date(stock_df, date)
            for i in range(idx, idx + sz):
                if i in stock_df.index:
                    filled.add(stock_df.loc[i]['Date'])

        interpolated_context[key] = filled
    return interpolated_context


def select_impl(stock_df: pd.DataFrame, stock_name: str, train_mode: str,
                keys: list, curr_dates: set, target_dates: set):
    if len(set(keys).intersection(required_factors)) == 0:
        return

    # print(f'Selecting with keys: {keys} and dates: {dates}')
    total_num, hit_num = 0, 0

    for date in curr_dates:
        idx = get_idx_by_date(stock_df, date)
        if not (idx in stock_df.index[200:-15]):
            continue
        total_num += 1

        if date in target_dates:
            hit_num += 1

    if hit_num / total_num >= CORRECT_RATIO:
        file_name = get_file_name(stock_name, stock_df, train_mode)
        with open(file_name, 'a') as fd:
            fd.write(f'{json.dumps(keys)}\ttotal {total_num}, hit {hit_num}\n')
        print(f'Found a selection for {stock_name}: {keys} with {total_num} total, {hit_num} hits.')


def select(stock_df: pd.DataFrame, stock_name: str, context: dict, train_mode: str,
           i: int, keys: list, curr_dates: set, target_dates: set):
    # fail fast
    if len(curr_dates.intersection(target_dates)) < MIN_HITS:
        return

    # we are done
    if i == len(factors):
        select_impl(stock_df, stock_name, train_mode, keys, curr_dates, target_dates)
        return

    keys = keys.copy()

    # not pick i
    select(stock_df, stock_name, context, train_mode, i + 1, keys, curr_dates, target_dates)

    # pick i
    key = factors[i].KEY

    keys.append(key)
    curr_dates = context.get(key, set()).intersection(curr_dates)

    select(stock_df, stock_name, context, train_mode, i + 1, keys, curr_dates, target_dates)


def train(stock_df: pd.DataFrame, stock_name: str, context: dict, train_mode: str):
    file_name = get_file_name(stock_name, stock_df, train_mode)
    if os.path.exists(file_name):
        print(f'Train file {file_name} exists, skip training for {stock_name} {train_mode}')
        return

    touch_file(file_name)

    target_dates = get_target_dates(context)
    context = interpolate_context(stock_df, context)

    start_time = datetime.now()
    curr_dates = set(stock_df['Date'].to_list())
    select(stock_df, stock_name, context, train_mode, 0, [], curr_dates, target_dates)
    print(f'Train completed for {stock_name} in {(datetime.now() - start_time).total_seconds()} seconds')
