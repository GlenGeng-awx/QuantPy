import pandas as pd
from datetime import datetime

from d2_margins import MARGINS
from guru import total_ops, build_op_ctx, filter_indices_by_ops
from .eval_long import eval_long
from .eval_short import eval_short


# return (pnl_tag, color)
def eval_ops(stock_df: pd.DataFrame, stock_name, indices: list) -> tuple:
    long_profit = min(MARGINS[stock_name]['15']['incr'] * 0.8, 0.25)
    short_profit = min(MARGINS[stock_name]['15']['decr'] * 0.8, 0.20)

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


def train_ops(stock_df: pd.DataFrame, stock_name, fd, op_ctx: dict, ops) -> bool:
    indices = filter_indices_by_ops(op_ctx, ops)
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
               op_ctx: dict,
               ops: list,
               remaining_operators: list[list],
               fd):
    if remaining_operators:
        assert len(ops) + len(remaining_operators) == len(total_ops)

        if ops:
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
