import json
import pandas as pd
from datetime import datetime

from util import shrink_date_str
from guru import (total_ops, build_op_ctx, filter_indices_by_ops,
                  get_sz, get_hard_loss, get_profits)
from .eval_vix import eval_vix


def train_ops(stock_df: pd.DataFrame, stock_name, fd, op_ctx: dict, ops: list):
    indices = filter_indices_by_ops(op_ctx, ops)
    if not indices:
        return

    sz = get_sz()
    hard_loss = get_hard_loss()
    long_profit, short_profit = get_profits(stock_name)

    # eval vix
    result = eval_vix(stock_df, indices, sz, long_profit, short_profit, hard_loss)
    total_num, successful_rate = result['total_num'], result['successful_rate']

    if not (total_num >= 2 and successful_rate >= 0.8):
        return

    record = json.dumps({
        'stock_name': stock_name,
        'op_names': [op.__name__ for op in ops],
        'result': result,
    })

    print(record)
    fd.write(record + '\n')


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
    to_date = shrink_date_str(stock_df.iloc[-1]['Date'])
    op_ctx = build_op_ctx(stock_df)
    print(f'finish build op ctx for {stock_name} at {to_date}')

    start_time = datetime.now()
    with open(f'./tmp/{stock_name}.{to_date}.res', 'w') as fd:
        train_impl(stock_df,
                   stock_name,
                   op_ctx,
                   [],
                   total_ops,
                   fd)

    end_time = datetime.now()
    time_cost = (end_time - start_time).total_seconds()
    print(f'{stock_name} train finished, cost: {time_cost}s')
