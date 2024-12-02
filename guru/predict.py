import pandas as pd
import plotly.graph_objects as go

from d2_margins import MARGINS
from guru import get_index, total_ops
from .holding_long import eval_long
from .holding_short import eval_short


def get_op(op_name):
    for op in total_ops:
        if op.__name__ == op_name:
            return op
    raise ValueError(f'op_name: {op_name} not found')


# return list of ops
def parse_all_ops(stock_name: str):
    all_ops = []
    with open(f'./tmp/{stock_name}.res', 'r') as fd:
        for line in fd:
            op_names = line.split('\t')[0].split(',')
            ops = [get_op(op_name) for op_name in op_names]
            all_ops.append(ops)
    return all_ops


def filter_idx(stock_df: pd.DataFrame, idx: int, ops: list) -> bool:
    for op in ops:
        if not op(stock_df, idx):
            return False
    return True


# return (pnl_tag, color)
def eval_ops(stock_df: pd.DataFrame, stock_name, indices: list) -> tuple:
    long_profit = min(MARGINS[stock_name]['15']['incr'], 0.10)
    short_profit = min(MARGINS[stock_name]['15']['decr'], 0.10)

    if indices[-1] - indices[0] < 10:
        return None, None

    # eval long
    long_results = eval_long(stock_df, indices)

    if any(hit_num >= 2 and total_pnl / hit_num >= long_profit for (_, hit_num, total_pnl) in long_results):
        pnl_tag = '<br>'.join(tag for (tag, _, _) in long_results)
        color = 'orange'
        return pnl_tag, color

    # eval short
    short_results = eval_short(stock_df, indices)

    if any(hit_num >= 2 and total_pnl / hit_num >= short_profit for (_, hit_num, total_pnl) in short_results):
        pnl_tag = '<br>'.join(tag for (tag, _, _) in short_results)
        color = 'black'
        return pnl_tag, color

    return None, None


def predict_ops(stock_df: pd.DataFrame, fig: go.Figure, stock_name, from_idx, to_idx, ops) -> bool:
    indices = []

    for idx in get_index(stock_df, from_idx, to_idx):
        if filter_idx(stock_df, idx, ops):
            indices.append(idx)

    if not indices:
        return False

    if not any(stock_df.index[-5] <= idx <= stock_df.index[-1] for idx in indices):
        return False

    pnl_tag, color = eval_ops(stock_df, stock_name, indices)

    if pnl_tag is None:
        return False

    name = ','.join(op.__name__ for op in ops)
    print(f'{stock_name} {name} ---> {pnl_tag}')

    dates = stock_df.loc[indices]['Date'].tolist()
    close = stock_df.loc[indices]['close'].tolist()

    name = '<br>'.join(op.__name__ for op in ops if 'noop' not in op.__name__)
    fig.add_trace(
        go.Scatter(
            name=f'{name}<br>{pnl_tag}',
            x=dates, y=close,
            mode='markers', marker=dict(size=10, color=color),
            # visible='legendonly',
        )
    )
    return True


def predict(stock_df: pd.DataFrame, fig: go.Figure, stock_name, from_idx, to_idx):
    all_ops = parse_all_ops(stock_name)

    hit = False
    for ops in all_ops:
        hit |= predict_ops(stock_df, fig, stock_name, from_idx, to_idx, ops)

    if hit:
        fig.show()
