import pandas as pd
import plotly.graph_objects as go
from guru import get_index, eval_ops

from guru import (
    guru_1,  # sr level
    guru_2,  # ma
    guru_3,  # shape
    guru_4,  # vol
    guru_5,  # statistic
    guru_6,  # yesterday min max
    guru_7,  # price
    guru_9,  # post
)


def get_op(op_name):
    total_ops = guru_1.operators \
                + guru_2.operators \
                + guru_3.operators \
                + guru_4.operators \
                + guru_5.operators \
                + guru_6.operators \
                + guru_7.operators \
                + guru_9.operators

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


def predict_ops(stock_df: pd.DataFrame, fig: go.Figure, from_idx, to_idx, ops) -> bool:
    indices = []

    for idx in get_index(stock_df, from_idx, to_idx):
        if filter_idx(stock_df, idx, ops):
            indices.append(idx)

    if not indices:
        return False

    if indices[-1] < stock_df.index[-10]:
        return False

    # if not (stock_df.index[-20] < indices[-1] < stock_df.index[-10]):
    #     return False

    name = ','.join(op.__name__ for op in ops)
    pnl_tag, color = eval_ops(stock_df, indices, name)

    if pnl_tag is None:
        return False

    print(f'{name} ---> {pnl_tag}')

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
    hit = False
    all_ops = parse_all_ops(stock_name)

    for ops in all_ops:
        hit |= predict_ops(stock_df, fig, from_idx, to_idx, ops)

    if hit:
        fig.show()
