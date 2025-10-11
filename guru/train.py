import pandas as pd
import json
from datetime import datetime
from util import get_idx_by_date, shrink_date_str, touch_file
from guru import factors, targets

MIN_HITS = 4
CORRECT_RATIO = 0.70


def get_file_name(stock_name: str, stock_df: pd.DataFrame, train_mode: str) -> str:
    version = shrink_date_str(stock_df['Date'].iloc[-1])
    return f'{train_mode}/{stock_name}.{version}.txt'


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


def _pick(total_num, up_hit, down_hit) -> bool:
    if (up_hit + down_hit) / total_num >= CORRECT_RATIO:
        return True
    return False


def select_impl(stock_df: pd.DataFrame, stock_name: str, context: dict, train_mode: str,
                keys: list, dates: set):
    # print(f'Selecting with keys: {keys} and dates: {dates}')
    total_num, up_hit, down_hit = 0, 0, 0

    for date in dates:
        idx = get_idx_by_date(stock_df, date)
        if not (idx in stock_df.index[200:-15]):
            continue
        total_num += 1

        if date in context.get(targets[0].KEY, set()) or date in context.get(targets[1].KEY, set()):
            down_hit += 1
        elif date in context.get(targets[2].KEY, set()) or date in context.get(targets[3].KEY, set()):
            up_hit += 1

    if _pick(total_num, up_hit, down_hit):
        file_name = get_file_name(stock_name, stock_df, train_mode)
        with open(file_name, 'a') as fd:
            fd.write(f'{json.dumps(keys)}\ttotal {total_num}, up {up_hit}, down {down_hit}\n')
        print(f'Found a selection: {keys} with {total_num} total, {up_hit} up hits, {down_hit} down hits')


def select(stock_df: pd.DataFrame, stock_name: str, context: dict, train_mode: str,
           i: int, keys: list, curr_dates: set, target_dates: set):
    # fail fast
    if len(curr_dates.intersection(target_dates)) < MIN_HITS:
        return

    # we are done
    if i == len(factors):
        select_impl(stock_df, stock_name, context, train_mode, keys, curr_dates)
        return

    keys = keys.copy()

    # not pick i
    select(stock_df, stock_name, context, train_mode, i + 1, keys, curr_dates, target_dates)

    # pick i
    key = factors[i].KEY

    keys.append(key)
    curr_dates = context.get(key, set()).intersection(curr_dates)

    select(stock_df, stock_name, context, train_mode, i + 1, keys, curr_dates, target_dates)


def get_target_dates(context: dict) -> set:
    dates = set()
    for target in targets:
        dates |= set(context.get(target.KEY, []))
    return dates


def train(stock_df: pd.DataFrame, stock_name: str, context: dict, train_mode: str) -> None:
    file_name = get_file_name(stock_name, stock_df, train_mode)
    touch_file(file_name)

    target_dates = get_target_dates(context)
    context = interpolate_context(stock_df, context)

    start_time = datetime.now()
    select(stock_df, stock_name, context, train_mode, 0, [], set(stock_df['Date'].to_list()), target_dates)
    print(f'Training completed for {stock_name} in {(datetime.now() - start_time).total_seconds()} seconds')
