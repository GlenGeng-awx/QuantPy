import json
from datetime import datetime
import pandas as pd
import plotly.graph_objects as go

from util import get_next_n_workday, shrink_date_str
from guru import (get_op_by_name, build_op_ctx, filter_indices_by_ops,
                  get_sz, get_hard_loss, get_profits)
from .eval_vix import eval_vix


# return list of ops
def parse_all_ops(stock_name: str, to_date: str):
    all_ops = []
    with open(f'./tmp/{stock_name}.{to_date}.res', 'r') as fd:
        for line in fd:
            record = json.loads(line)
            op_names = record['op_names']
            ops = [get_op_by_name(op_name) for op_name in op_names]
            all_ops.append(ops)
    return all_ops


def predict_ops(stock_df: pd.DataFrame, fig: go.Figure, stock_name, op_ctx, ops) -> bool:
    indices = filter_indices_by_ops(op_ctx, ops)
    if not indices:
        return False

    # rule 1: (-3, -1) or (-1, -1)
    if not any(stock_df.index[-1] <= idx <= stock_df.index[-1] for idx in indices):
        return False

    # rule 2: eval vix
    sz = get_sz()
    hard_loss = get_hard_loss()
    long_profit, short_profit = get_profits(stock_name)

    result = eval_vix(stock_df, indices, sz, long_profit, short_profit, hard_loss)
    vix_tag, total_num, successful_rate = result['vix_tag'], result['total_num'], result['successful_rate']

    if not (total_num >= 3 and successful_rate >= 0.8):
        return False

    # rule 3: valid range
    valid_indices = [idx for idx in indices if idx + sz in stock_df.index]
    if valid_indices[-1] - valid_indices[0] < 60:
        return False

    name = ','.join(op.__name__ for op in ops)
    print(f'{stock_name} {name} ---> {vix_tag}')

    dates = stock_df.loc[indices]['Date'].tolist()
    close = stock_df.loc[indices]['close'].tolist()

    name = '<br>'.join(op.__name__ for op in ops if 'noop' not in op.__name__)
    fig.add_trace(
        go.Scatter(
            name=f'{name}<br>{vix_tag}',
            x=dates, y=close,
            mode='markers', marker=dict(size=10, color='orange'),
        )
    )
    return True


def build_graph(stock_df: pd.DataFrame, fig: go.Figure, stock_name, hit_num):
    # mark the first and last date
    fig.add_vline(x=stock_df.iloc[0]['Date'], line_dash="dash", line_width=1, line_color="black")
    fig.add_vline(x=stock_df.iloc[-1]['Date'], line_dash="dash", line_width=1, line_color="black")

    # mark long/short hint
    sz = get_sz()
    long_profit, short_profit = get_profits(stock_name)

    from_date = stock_df.iloc[-1]['Date']
    to_date = get_next_n_workday(from_date, sz)

    close = stock_df.iloc[-1]['close']
    long_target = close * (1 + long_profit)
    short_target = close * (1 - short_profit)

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


def predict(stock_df: pd.DataFrame, fig: go.Figure, stock_name):
    to_date = shrink_date_str(stock_df.iloc[-1]['Date'])
    op_ctx = build_op_ctx(stock_df)
    print(f'finish build op ctx for {stock_name} at {to_date}')

    start_time = datetime.now()
    all_ops = parse_all_ops(stock_name, to_date)

    hit_num = 0
    for ops in all_ops:
        if predict_ops(stock_df, fig, stock_name, op_ctx, ops):
            hit_num += 1

    print(f'{stock_name} predict finished, cost: {(datetime.now() - start_time).total_seconds()}s')

    if hit_num == 0:
        return

    build_graph(stock_df, fig, stock_name, hit_num)
    fig.show()
