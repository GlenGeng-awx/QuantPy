import pandas as pd
from features.k_43 import get_incr_benchmark
from features.k_44 import get_decr_benchmark

from guru import (
    guru_01,  # structure
    guru_02,  # sr level min/max
    guru_03,  # ma/ema
    guru_04,  # simple shape
    guru_05,  # complex shape
    guru_06,  # vol
    guru_07,  # statistic
    guru_08,  # yesterday min max
    guru_09,  # incr decr top 10pst
    guru_10,  # incr decr bottom 10pst
    guru_11,  # price
    guru_a,  # weekday
    guru_b,  # post
    guru_c,  # baseline
)

total_ops = [
    guru_01.operators,
    guru_02.operators,
    guru_03.operators,
    guru_04.operators,
    guru_05.operators,
    guru_06.operators,
    guru_07.operators,
    guru_08.operators,
    guru_09.operators,
    guru_10.operators,
    guru_11.operators,
    guru_a.operators,
    guru_b.operators,
    guru_c.operators,
]

flatten_ops = [op for ops in total_ops for op in ops]

HIT_NUM = 2
PERIOD = 200    # 400


def build_op_ctx(stock_df: pd.DataFrame) -> dict:
    op_ctx = {}

    for op in flatten_ops:
        hits = set()
        for idx in stock_df.index:
            if op(stock_df, idx):
                hits.add(idx)
        op_ctx[op.__name__] = hits

    return op_ctx


def filter_indices_by_ops(op_ctx: dict, ops: list) -> list:
    hits = op_ctx[ops[0].__name__]
    for op in ops[1:]:
        if 'noop' in op.__name__:
            continue
        hits = hits.intersection(op_ctx[op.__name__])
    return sorted(list(hits))


def filter_indices(stock_df: pd.DataFrame, op_ctx: dict, ops: list) -> list:
    indices = filter_indices_by_ops(op_ctx, ops)
    if stock_df.index[-1] not in indices:
        return []
    if len(indices) < 1 + HIT_NUM:
        return []
    if indices[-2] - indices[0] < 20:
        return []
    return indices


def get_op_by_name(op_name):
    for op in flatten_ops:
        if op.__name__ == op_name:
            return op
    raise ValueError(f'op_name: {op_name} not found')


def build_params(stock_df: pd.DataFrame) -> dict:
    sz = 21

    long_profit, _ = get_incr_benchmark(stock_df, 20)
    short_profit, _ = get_decr_benchmark(stock_df, 20)

    return {
        'sz': sz,
        'long_profit': long_profit,
        'short_profit': short_profit
    }
