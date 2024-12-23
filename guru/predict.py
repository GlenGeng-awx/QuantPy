from datetime import datetime
import pandas as pd
import plotly.graph_objects as go

import util
from d2_margins import MARGINS
from guru import get_op_by_name, build_op_ctx, filter_indices_by_ops
from .eval_vix import eval_vix


# return list of ops
def parse_all_ops(stock_name: str):
    all_ops = []
    with open(f'./tmp/{stock_name}.res', 'r') as fd:
        for line in fd:
            op_names = line.split('\t')[0].split(',')
            ops = [get_op_by_name(op_name) for op_name in op_names]
            all_ops.append(ops)
    return all_ops


def get_sz() -> int:
    return 15


def get_profits(stock_name: str, sz: int) -> (float, float):
    long_profit = min(MARGINS[stock_name][str(sz)]['incr'] * 0.9, 0.30)
    short_profit = min(MARGINS[stock_name][str(sz)]['decr'] * 0.9, 0.20)
    return long_profit, short_profit


# return (pnl_tag, color)
def eval_indices(stock_df: pd.DataFrame, stock_name, indices: list) -> tuple:
    sz = get_sz()
    hard_loss = 1.0  # 0.015

    long_profit, short_profit = get_profits(stock_name, sz)

    # valid range
    valid_indices = [idx for idx in indices if idx + sz in stock_df.index]
    if valid_indices[-1] - valid_indices[0] < 60:
        return None, None

    # eval vix
    vix_tag, total_num, successful_rate, _, _ = eval_vix(stock_df, indices, sz, long_profit, short_profit, hard_loss)

    if total_num >= 3 and successful_rate >= 0.8:
        return vix_tag, 'orange'
    else:
        return None, None


def predict_ops(stock_df: pd.DataFrame, fig: go.Figure, stock_name, op_ctx, ops) -> bool:
    indices = filter_indices_by_ops(op_ctx, ops)
    if not indices:
        return False

    # (-3, -1) or (-1, -1)
    if not any(stock_df.index[-1] <= idx <= stock_df.index[-1] for idx in indices):
        return False

    vix_tag, color = eval_indices(stock_df, stock_name, indices)
    if vix_tag is None:
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
            mode='markers', marker=dict(size=10, color=color),
            # visible='legendonly',
        )
    )
    return True


def predict(stock_df: pd.DataFrame, fig: go.Figure, stock_name):
    start_time = datetime.now()
    op_ctx = build_op_ctx(stock_df)
    print(f'finish build op ctx for {stock_name}')

    all_ops = parse_all_ops(stock_name)

    hit_num = 0
    for ops in all_ops:
        if predict_ops(stock_df, fig, stock_name, op_ctx, ops):
            hit_num += 1

    print(f'{stock_name} predict finished, cost: {(datetime.now() - start_time).total_seconds()}s')

    if hit_num == 0:
        return

    # mark the first and last date
    fig.add_vline(x=stock_df.iloc[0]['Date'], line_dash="dash", line_width=1, line_color="black")
    fig.add_vline(x=stock_df.iloc[-1]['Date'], line_dash="dash", line_width=1, line_color="black")

    # mark long/short hint
    sz = get_sz()

    from_date = stock_df.iloc[-1]['Date']
    to_date = util.get_next_n_workday(from_date, sz)

    long_profit, short_profit = get_profits(stock_name, sz)
    close = stock_df.iloc[-1]['close']

    fig.add_trace(
        go.Scatter(
            name='long hint',
            x=[from_date, to_date],
            y=[close * (1 + long_profit), close * (1 + long_profit)],
            mode='lines',
            line=dict(width=4, color='red', dash='dot'),
        ),
        row=1, col=1,
    )
    fig.add_trace(
        go.Scatter(
            name='short hint',
            x=[from_date, to_date],
            y=[close * (1 - short_profit), close * (1 - short_profit)],
            mode='lines',
            line=dict(width=4, color='green', dash='dot'),
        ),
        row=1, col=1,
    )

    # update title
    fig.update_layout(
        title=fig.layout.title.text + f'<br>HIT {hit_num} --> L {long_profit:.1%}, S {short_profit:.1%}'
    )
    fig.show()
