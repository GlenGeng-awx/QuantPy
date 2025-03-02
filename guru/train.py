import json
import pandas as pd
from datetime import datetime

from util import shrink_date_str
from guru import total_ops, build_op_ctx, build_params, filter_indices_by_ops
from .eval_vix import eval_vix
import features


def train_ops(stock_df: pd.DataFrame, stock_name, params: dict, fd, op_ctx: dict, ops: list):
    indices = filter_indices_by_ops(op_ctx, ops)
    if not indices:
        return

    sz = params['sz']
    hard_loss = params['hard_loss']
    long_profit, short_profit = params['long_profit'], params['short_profit']

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

    # print(record)
    fd.write(record + '\n')


def train_impl(stock_df: pd.DataFrame,
               stock_name: str,
               params: dict,
               op_ctx: dict,
               ops: list,
               remaining_operators: list[list],
               fd):
    if remaining_operators:
        assert len(ops) + len(remaining_operators) == len(total_ops)

        # fail fast
        if ops:
            indices = filter_indices_by_ops(op_ctx, ops)
            if not indices:
                return

        operators = remaining_operators[0]
        for op in operators:
            train_impl(stock_df,
                       stock_name,
                       params,
                       op_ctx,
                       ops + [op],
                       remaining_operators[1:],
                       fd)
    else:
        assert len(ops) == len(total_ops)

        # required feature
        if ops[2].__name__ == 'ma_noop':
            return

        train_ops(stock_df,
                  stock_name,
                  params,
                  fd,
                  op_ctx,
                  ops)


def train(stock_df: pd.DataFrame, stock_name):
    to_date = shrink_date_str(stock_df.iloc[-1]['Date'])

    stock_df = features.calculate_feature(stock_df, stock_name)
    params = build_params(stock_df)
    op_ctx = build_op_ctx(stock_df)
    print(f'finish build op ctx for {stock_name} at {to_date}')

    start_time = datetime.now()
    with open(f'./tmp/{stock_name}.{to_date}.res', 'w') as fd:
        train_impl(stock_df,
                   stock_name,
                   params,
                   op_ctx,
                   [],
                   total_ops,
                   fd)

    time_cost = (datetime.now() - start_time).total_seconds()
    print(f'----> {stock_name} train finished, cost: {time_cost}s')
