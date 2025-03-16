import json
import pandas as pd
from datetime import datetime

from util import shrink_date_str
from guru import total_ops, build_op_ctx, build_params, filter_indices
from .eval_vix import filter_long, filter_short
import features


def print_result(stock_name, ops, result, fd):
    record = json.dumps({
        'stock_name': stock_name,
        'op_names': [op.__name__ for op in ops],
        'result': result,
    })

    print(record)
    fd.write(record + '\n')


def train_ops(stock_df: pd.DataFrame, stock_name, params: dict, fd, op_ctx: dict, ops: list):
    indices = filter_indices(stock_df, op_ctx, ops)
    if not indices:
        return

    long_result = filter_long(stock_df, indices, params)
    if long_result is not None:
        print_result(stock_name, ops, long_result, fd)

    short_result = filter_short(stock_df, indices, params)
    if short_result is not None:
        print_result(stock_name, ops, short_result, fd)


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
            indices = filter_indices(stock_df, op_ctx, ops)
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
