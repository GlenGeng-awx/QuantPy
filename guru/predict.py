import json
from datetime import datetime
import pandas as pd
import plotly.graph_objects as go

from util import get_next_n_workday, shrink_date_str, touch
from guru import get_op_by_name, build_op_ctx, build_params, filter_indices
from .eval_vix import filter_short, filter_long
import features


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


def predict_ops(stock_df: pd.DataFrame, params: dict, fig: go.Figure, stock_name, op_ctx, ops: list) -> int:
    indices = filter_indices(stock_df, op_ctx, ops)
    if not indices:
        return 0

    long_result = filter_long(stock_df, indices, params)
    short_result = filter_short(stock_df, indices, params)
    if long_result:
        tag = long_result['long_tag']
        ret = 1
    elif short_result:
        tag = short_result['short_tag']
        ret = -1
    else:
        return 0

    name = ','.join(op.__name__ for op in ops)
    print(f'{stock_name} {name} ---> {tag}')

    tags = [op.__name__ for op in ops] + [tag]
    fig.add_trace(
        go.Scatter(
            name='<br>'.join(tag for tag in tags if 'noop' not in tag),
            x=stock_df.loc[indices]['Date'],
            y=stock_df.loc[indices]['close'],
            mode='markers', marker=dict(size=10, color='orange'),
        )
    )
    return ret


def build_graph(stock_df: pd.DataFrame, params: dict, fig: go.Figure, long_num, short_num):
    # mark the first and last date
    fig.add_vline(x=stock_df.iloc[0]['Date'], line_dash="dash", line_width=1, line_color="black")
    fig.add_vline(x=stock_df.iloc[-1]['Date'], line_dash="dash", line_width=0.25, line_color="black")

    # mark long/short hint
    sz = params['sz']
    long_profit, short_profit = params['long_profit'], params['short_profit']

    from_date = stock_df.iloc[-1]['Date']
    to_date = get_next_n_workday(from_date, sz)

    from_close = stock_df.iloc[-1]['close']
    long_target = from_close * (1 + long_profit)
    short_target = from_close * (1 - short_profit)

    fig.add_trace(
        go.Scatter(
            name='long hint', x=[from_date, to_date], y=[long_target, long_target],
            mode='lines', line=dict(width=2, color='red', dash='solid'),
        ),
        row=1, col=1,
    )
    fig.add_trace(
        go.Scatter(
            name='short hint', x=[from_date, to_date], y=[short_target, short_target],
            mode='lines', line=dict(width=2, color='green', dash='solid'),
        ),
        row=1, col=1,
    )

    # update title
    fig.update_layout(
        title=fig.layout.title.text + f'<br>Long {long_num} Short {short_num} --> L {long_profit:.1%}, S {short_profit:.1%}'
    )


def predict(stock_df: pd.DataFrame, fig: go.Figure, stock_name):
    to_date = shrink_date_str(stock_df.iloc[-1]['Date'])

    all_ops = parse_all_ops(stock_name, to_date)
    if not all_ops:
        return

    stock_df = features.calculate_feature(stock_df, stock_name, False)
    params = build_params(stock_df)
    op_ctx = build_op_ctx(stock_df)
    print(f'finish build op ctx for {stock_name} at {to_date}')

    start_time = datetime.now()
    long_num, short_num = 0, 0
    for ops in all_ops:
        ret = predict_ops(stock_df, params, fig, stock_name, op_ctx, ops)
        if ret == 1:
            long_num += 1
        if ret == -1:
            short_num += 1

    time_cost = (datetime.now() - start_time).total_seconds()
    print(f'----> {stock_name} predict finished, cost: {time_cost}s')

    if long_num + short_num == 0:
        return

    touch(f'./bak/{stock_name}${to_date}${long_num}${short_num}')

    build_graph(stock_df, params, fig, long_num, short_num)
    features.plot_feature(stock_df, fig)
    fig.show()
