import pandas as pd
from margins import MARGINS

from guru import (
    guru_1,  # structure
    guru_2,  # sr level min/max
    guru_3,  # ma/ema
    guru_4,  # simple shape
    guru_5,  # complex shape
    guru_6,  # vol
    guru_7,  # statistic
    guru_8,  # yesterday min max
    guru_9,  # price
    guru_a,  # weekday
    guru_b,  # post
    guru_c,  # baseline
)

total_ops = [
    guru_1.operators,
    guru_2.operators,
    guru_3.operators,
    guru_4.operators,
    guru_5.operators,
    guru_6.operators,
    guru_7.operators,
    guru_8.operators,
    guru_9.operators,
    guru_a.operators,
    guru_b.operators,
    guru_c.operators,
]

flatten_ops = [op for ops in total_ops for op in ops]


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
        if len(hits) <= 1:
            return []
    return sorted(list(hits))


def get_op_by_name(op_name):
    for op in flatten_ops:
        if op.__name__ == op_name:
            return op
    raise ValueError(f'op_name: {op_name} not found')


# conf
def get_sz() -> int:
    return 20


def get_hard_loss() -> float:
    return 1.0  # 0.015


def get_profits(stock_name: str) -> (float, float):
    sz = get_sz()
    long_profit = min(MARGINS[stock_name][str(sz)]['incr'] * 0.9, 0.35)
    short_profit = min(MARGINS[stock_name][str(sz)]['decr'] * 0.9, 0.25)
    return long_profit, short_profit
