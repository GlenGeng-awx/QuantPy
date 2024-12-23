import pandas as pd
from datetime import datetime

from d2_margins import MARGINS
from guru import total_ops, build_op_ctx, filter_indices_by_ops
from .eval_vix import eval_vix


# return (pnl_tag, color)
def eval_indices(stock_df: pd.DataFrame, stock_name, indices: list):
    sz = 15
    hard_loss = 1.0  # 0.015

    long_profit = min(MARGINS[stock_name][str(sz)]['incr'] * 0.9, 0.30)
    short_profit = min(MARGINS[stock_name][str(sz)]['decr'] * 0.9, 0.20)

    # eval vix
    vix_tag, total_num, successful_rate, _, _ = eval_vix(stock_df, indices, sz, long_profit, short_profit, hard_loss)

    if total_num >= 2 and successful_rate >= 0.8:
        return vix_tag
    else:
        return None


def train_ops(stock_df: pd.DataFrame, stock_name, fd, op_ctx: dict, ops) -> bool:
    indices = filter_indices_by_ops(op_ctx, ops)
    if not indices:
        return False

    vix_tag = eval_indices(stock_df, stock_name, indices)
    if vix_tag is None:
        return False

    name = ','.join(op.__name__ for op in ops)
    print(f'{stock_name} {name} ---> {vix_tag}')
    fd.write(f'{name}\t{vix_tag}\n')
    fd.flush()
    return True


def train_impl(stock_df: pd.DataFrame,
               stock_name: str,
               op_ctx: dict,
               ops: list,
               remaining_operators: list[list],
               fd):
    if remaining_operators:
        assert len(ops) + len(remaining_operators) == len(total_ops)

        if ops:
            # fail fast
            indices = filter_indices_by_ops(op_ctx, ops)
            if not indices:
                return

        operators = remaining_operators[0]
        for op in operators:
            train_impl(stock_df,
                       stock_name,
                       op_ctx,
                       ops + [op],
                       remaining_operators[1:],
                       fd)
    else:
        assert len(ops) == len(total_ops)

        # required feature 1
        if ops[0].__name__ == 'structure_noop' \
                and ops[1].__name__ == 'sr_level_noop' \
                and ops[2].__name__ == 'ma_noop':
            return

        # required feature 2
        if ops[3].__name__ == 'simple_shape_noop' \
                and ops[4].__name__ == 'complex_shape_noop':
            return

        train_ops(stock_df,
                  stock_name,
                  fd,
                  op_ctx,
                  ops)


def train(stock_df: pd.DataFrame, stock_name):
    op_ctx = build_op_ctx(stock_df)
    print(f'finish build op ctx for {stock_name}')

    start_time = datetime.now()
    with open(f'./tmp/{stock_name}.res', 'w') as fd:
        train_impl(stock_df,
                   stock_name,
                   op_ctx,
                   [],
                   total_ops,
                   fd)

    end_time = datetime.now()
    time_cost = (end_time - start_time).total_seconds()
    print(f'{stock_name} train finished, cost: {time_cost}s')
