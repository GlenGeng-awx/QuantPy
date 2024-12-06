import pandas as pd
from datetime import datetime

from d2_margins import MARGINS
from guru import get_index, flatten_ops, total_ops
from .holding_long import eval_long
from .holding_short import eval_short


def build_train_ctx(stock_df: pd.DataFrame, from_idx, to_idx) -> dict:
    train_ctx = {}

    for op in flatten_ops:
        hits = set()
        for idx in get_index(stock_df, from_idx, to_idx):
            if op(stock_df, idx):
                hits.add(idx)
        train_ctx[op.__name__] = hits

    return train_ctx


def filter_ops(train_ctx: dict, ops: list) -> list:
    hits = train_ctx[ops[0].__name__]
    for op in ops[1:]:
        if 'noop' in op.__name__:
            continue
        hits = hits.intersection(train_ctx[op.__name__])
        if len(hits) <= 1:
            return []
    return sorted(list(hits))


# return (pnl_tag, color)
def eval_ops(stock_df: pd.DataFrame, stock_name, indices: list) -> tuple:
    long_profit = min(MARGINS[stock_name]['15']['incr'], 0.15)
    short_profit = min(MARGINS[stock_name]['15']['decr'], 0.15)

    # eval long
    long_results = eval_long(stock_df, indices)

    if any(hit_num >= 2 and total_pnl >= long_profit * hit_num for (_, hit_num, total_pnl) in long_results):
        pnl_tag = '<br>'.join(tag for (tag, _, _) in long_results)
        color = 'orange'
        return pnl_tag, color

    # eval short
    short_results = eval_short(stock_df, indices)

    if any(hit_num >= 2 and total_pnl >= short_profit * hit_num for (_, hit_num, total_pnl) in short_results):
        pnl_tag = '<br>'.join(tag for (tag, _, _) in short_results)
        color = 'black'
        return pnl_tag, color

    return None, None


def train_ops(stock_df: pd.DataFrame, stock_name, fd, train_ctx: dict, ops) -> bool:
    indices = filter_ops(train_ctx, ops)
    if not indices:
        return False

    pnl_tag, color = eval_ops(stock_df, stock_name, indices)
    if pnl_tag is None:
        return False

    name = ','.join(op.__name__ for op in ops)
    print(f'{stock_name} {name} ---> {pnl_tag}')
    fd.write(f'{name}\t{pnl_tag}\n')
    fd.flush()
    return True


def train_impl(stock_df: pd.DataFrame,
               stock_name: str,
               train_ctx: dict,
               ops: list,
               remaining_operators: list[list],
               fd):
    if remaining_operators:
        assert len(ops) + len(remaining_operators) == len(total_ops)

        if ops:
            indices = filter_ops(train_ctx, ops)
            if not indices:
                return

        operators = remaining_operators[0]
        for op in operators:
            train_impl(stock_df,
                       stock_name,
                       train_ctx,
                       ops + [op],
                       remaining_operators[1:],
                       fd)
    else:
        assert len(ops) == len(total_ops)

        train_ops(stock_df,
                  stock_name,
                  fd,
                  train_ctx,
                  ops)


def train(stock_df: pd.DataFrame, stock_name, from_idx, to_idx):
    train_ctx = build_train_ctx(stock_df, from_idx, to_idx)
    print(f'finish build train ctx for {stock_name}')

    start_time = datetime.now()
    with open(f'./tmp/{stock_name}.res', 'w') as fd:
        train_impl(stock_df,
                   stock_name,
                   train_ctx,
                   [],
                   total_ops,
                   fd)

    end_time = datetime.now()
    time_cost = (end_time - start_time).total_seconds()
    print(f'{stock_name} train finished, cost: {time_cost}s')
