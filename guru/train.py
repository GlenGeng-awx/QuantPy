import pandas as pd
import json
from datetime import datetime
from util import get_idx_by_date
from guru import factors

BIAS = 0.9
RATIO = 0.7
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


def get_15d_10pst_up(stock_df: pd.DataFrame) -> (float, list):
    ups = []
    for idx in stock_df.index:
        if idx + 15 not in stock_df.index:
            continue
        curr_close = stock_df.loc[idx]['close']
        next_close = stock_df.loc[idx + 15]['close']
        if next_close >= curr_close:
            up = next_close / curr_close - 1
            ups.append((up, idx))
    ups.sort(key=lambda x: x[0], reverse=True)

    threshold_pos = int(len(ups) * 0.1) - 1
    threshold_value = ups[threshold_pos][0]
    print(f'15d 10pst up = {threshold_value:.2%}')
    return threshold_value, ups[:threshold_pos + 1]


def get_15d_10pst_down(stock_df: pd.DataFrame) -> (float, list):
    downs = []
    for idx in stock_df.index:
        if idx + 15 not in stock_df.index:
            continue
        curr_close = stock_df.loc[idx]['close']
        next_close = stock_df.loc[idx + 15]['close']
        if next_close <= curr_close:
            down = 1 - next_close / curr_close
            downs.append((down, idx))
    downs.sort(key=lambda x: x[0], reverse=True)

    threshold_pos = int(len(downs) * 0.1) - 1
    threshold_value = downs[threshold_pos][0]
    print(f'15d 10pst down = {threshold_value:.2%}')
    return threshold_value, downs[:threshold_pos + 1]


def select_impl(stock_df: pd.DataFrame, params: dict, keys: list, dates: set):
    # print(f'Selecting with keys: {keys} and dates: {dates}')
    up_pst, down_pst = params['up_pst'] * BIAS, params['down_pst'] * BIAS
    total_num, up_hit, down_hit = 0, 0, 0

    for date in dates:
        idx = get_idx_by_date(stock_df, date)
        if idx + 15 not in stock_df.index:
            continue
        total_num += 1

        curr_close = stock_df.loc[idx]['close']
        max_close = stock_df.loc[idx:idx + 15]['close'].max()
        min_close = stock_df.loc[idx:idx + 15]['close'].min()

        if max_close >= curr_close * (1 + up_pst):
            up_hit += 1
        if min_close <= curr_close * (1 - down_pst):
            down_hit += 1

    if total_num >= HITS and (up_hit + down_hit) / total_num >= RATIO:
        with open(f'tmp/{params["stock_name"]}.txt', 'a') as fd:
            fd.write(f'{json.dumps(keys)}\ttotal {total_num}, up {up_hit}, down {down_hit}\n')
        print(f'Found a selection: {keys} with {total_num} total, {up_hit} up hits, {down_hit} down hits')


def select(stock_df: pd.DataFrame, params: dict, i: int, keys: list, curr_dates: set):
    # fail fast
    if len(curr_dates) < HITS:
        return

    context = params['context']

    # we are done
    if i == len(context):
        select_impl(stock_df, params, keys, curr_dates)
        return

    keys = keys.copy()

    # not pick i
    select(stock_df, params, i + 1, keys, curr_dates)

    # pick i
    key = factors[i].KEY

    keys.append(key)
    curr_dates = context.get(key, set()).intersection(curr_dates)

    select(stock_df, params, i + 1, keys, curr_dates)


def train(stock_df: pd.DataFrame, stock_name: str, context: dict) -> None:
    touch_file(f'tmp/{stock_name}.txt')
    context = interpolate_context(stock_df, context)

    up_pst, _ = get_15d_10pst_up(stock_df)
    down_pst, _ = get_15d_10pst_down(stock_df)

    params = {
        'stock_name': stock_name,
        'context': context,
        'up_pst': up_pst,
        'down_pst': down_pst,
    }

    start_time = datetime.now()
    select(stock_df, params, 0, [], set(stock_df['Date'].to_list()))
    print(f'Training completed for {stock_name} in {(datetime.now() - start_time).total_seconds()} seconds')
