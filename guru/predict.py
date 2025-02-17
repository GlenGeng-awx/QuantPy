import json
import os
from datetime import datetime
import pandas as pd
import plotly.graph_objects as go

from util import get_next_n_workday, shrink_date_str
from guru import (get_op_by_name, build_op_ctx, filter_indices_by_ops,
                  get_sz, get_hard_loss, get_profits)
from .eval_vix import eval_vix

AS_OF = -5


def parse_cross_ops(to_date: str) -> dict:
    file_name = f'bak/cross_vix.{to_date}.res'
    if not os.path.exists(file_name):
        print(f'{file_name} not exists')
        return {}

    cross_ops = {}
    with open(file_name, 'r') as fd:
        for line in fd:
            record = json.loads(line)

            op_names = record['op_names']
            ops = tuple([get_op_by_name(op_name) for op_name in op_names])

            total_num, hit_num = record['total_num'], len(record['hits'])
            long_num, short_num = record['long_num'], record['short_num']
            cross_tag = f'X{hit_num}, T{total_num}, {(long_num + short_num) / total_num:.0%}, L{long_num}, S{short_num}'

            cross_ops[ops] = cross_tag
    return cross_ops


# return list of ops
def parse_all_ops(stock_name: str, to_date: str) -> list[list]:
    all_ops = []
    with open(f'./tmp/{stock_name}.{to_date}.res', 'r') as fd:
        for line in fd:
            record = json.loads(line)
            op_names = record['op_names']
            ops = [get_op_by_name(op_name) for op_name in op_names]
            all_ops.append(ops)
    return all_ops


def predict_ops(stock_df: pd.DataFrame, fig: go.Figure, stock_name, op_ctx, ops: list, cross_ops: dict) -> bool:
    indices = filter_indices_by_ops(op_ctx, ops)
    if not indices:
        return False

    if not any(stock_df.index[AS_OF] == idx for idx in indices):
        return False

    # eval vix
    sz = get_sz()
    hard_loss = get_hard_loss()
    long_profit, short_profit = get_profits(stock_name)

    result = eval_vix(stock_df, indices, sz, long_profit, short_profit, hard_loss)
    vix_tag, total_num, successful_rate = result['vix_tag'], result['total_num'], result['successful_rate']

    def rule_1() -> bool:
        if not (total_num >= 3 and successful_rate >= 0.8):
            return False

        valid_indices = [idx for idx in indices if idx + sz in stock_df.index]
        if valid_indices[-1] - valid_indices[0] < 60:
            return False

        return True

    def rule_2() -> bool:
        if not (total_num >= 2 and successful_rate >= 0.8):
            return False

        if tuple(ops) not in cross_ops:
            return False

        return True

    if not (rule_1() or rule_2()):
        return False

    name = ','.join(op.__name__ for op in ops)
    print(f'{stock_name} {name} ---> {vix_tag}')

    dates = stock_df.loc[indices]['Date'].tolist()
    close = stock_df.loc[indices]['close'].tolist()

    tags = [op.__name__ for op in ops] + [vix_tag] + [cross_ops.get(tuple(ops), 'cross_noop')]
    fig.add_trace(
        go.Scatter(
            name='<br>'.join(tag for tag in tags if 'noop' not in tag),
            x=dates, y=close,
            mode='markers', marker=dict(size=10, color='orange'),
        )
    )
    return True


def build_graph(stock_df: pd.DataFrame, fig: go.Figure, stock_name, hit_num):
    # mark the first and last date
    fig.add_vline(x=stock_df.iloc[0]['Date'], line_dash="dash", line_width=1, line_color="black")
    fig.add_vline(x=stock_df.iloc[AS_OF]['Date'], line_dash="dash", line_width=0.25, line_color="black")

    # mark long/short hint
    sz = get_sz()
    long_profit, short_profit = get_profits(stock_name)

    from_date = stock_df.iloc[AS_OF]['Date']
    to_date = get_next_n_workday(from_date, sz)

    from_close = stock_df.iloc[AS_OF]['close']
    long_target = from_close * (1 + long_profit)
    short_target = from_close * (1 - short_profit)

    fig.add_trace(
        go.Scatter(
            name='long hint', x=[from_date, to_date], y=[long_target, long_target],
            mode='lines', line=dict(width=4, color='red', dash='dot'),
        ),
        row=1, col=1,
    )
    fig.add_trace(
        go.Scatter(
            name='short hint', x=[from_date, to_date], y=[short_target, short_target],
            mode='lines', line=dict(width=4, color='green', dash='dot'),
        ),
        row=1, col=1,
    )

    # update title
    fig.update_layout(
        title=fig.layout.title.text + f'<br>HIT {hit_num} --> L {long_profit:.1%}, S {short_profit:.1%}'
    )


def predict(stock_df: pd.DataFrame, fig: go.Figure, stock_name, show: bool = False) -> bool:
    to_date = shrink_date_str(stock_df.iloc[-1]['Date'])
    op_ctx = build_op_ctx(stock_df)
    print(f'finish build op ctx for {stock_name} at {to_date}')

    start_time = datetime.now()
    all_ops = parse_all_ops(stock_name, to_date)
    cross_ops = parse_cross_ops(to_date)

    hit_num = 0
    for ops in all_ops:
        if predict_ops(stock_df, fig, stock_name, op_ctx, ops, cross_ops):
            hit_num += 1

    print(f'{stock_name} predict finished, cost: {(datetime.now() - start_time).total_seconds()}s')

    if hit_num == 0:
        return False

    if show:
        build_graph(stock_df, fig, stock_name, hit_num)
        fig.show()
    return True
