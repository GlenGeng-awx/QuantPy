import pandas as pd
import plotly.graph_objects as go

from d2_margins import MARGINS
from guru import get_op_by_name, build_op_ctx, filter_indices_by_ops
from .eval_long import eval_long
from .eval_short import eval_short


# return list of ops
def parse_all_ops(stock_name: str):
    all_ops = []
    with open(f'./tmp/{stock_name}.res', 'r') as fd:
        for line in fd:
            op_names = line.split('\t')[0].split(',')
            ops = [get_op_by_name(op_name) for op_name in op_names]
            all_ops.append(ops)
    return all_ops


# return (pnl_tag, color)
def eval_indices(stock_df: pd.DataFrame, stock_name, indices: list) -> tuple:
    long_profit = min(MARGINS[stock_name]['15']['incr'] * 0.8, 0.20)
    short_profit = min(MARGINS[stock_name]['15']['decr'] * 0.8, 0.15)

    if indices[-1] - indices[0] < 10:
        return None, None

    # eval long
    pnl_tag, total_num, _, successful_rate = eval_long(stock_df, indices, 15, long_profit, 0.03)
    if total_num >= 4 and successful_rate >= 0.8:
        color = 'orange'
        return pnl_tag, color

    # eval short
    pnl_tag, total_num, _, successful_rate = eval_short(stock_df, indices, 15, short_profit, 0.03)
    if total_num >= 4 and successful_rate >= 0.8:
        color = 'black'
        return pnl_tag, color

    return None, None


def predict_ops(stock_df: pd.DataFrame, fig: go.Figure, stock_name, op_ctx, ops) -> bool:
    indices = filter_indices_by_ops(op_ctx, ops)
    if not indices:
        return False

    #  (-5, -1)
    #  (-3, -3)
    if not any(stock_df.index[-3] <= idx <= stock_df.index[-3] for idx in indices):
        return False

    pnl_tag, color = eval_indices(stock_df, stock_name, indices)

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


def predict(stock_df: pd.DataFrame, fig: go.Figure, stock_name):
    op_ctx = build_op_ctx(stock_df)
    print(f'finish build op ctx for {stock_name}')

    all_ops = parse_all_ops(stock_name)

    hit = False
    for ops in all_ops:
        hit |= predict_ops(stock_df, fig, stock_name, op_ctx, ops)

    if not hit:
        return

    # mark the first and last date
    fig.add_vline(x=stock_df.iloc[0]['Date'], line_dash="dash", line_width=1, line_color="black")
    fig.add_vline(x=stock_df.iloc[-1]['Date'], line_dash="dash", line_width=1, line_color="black")

    fig.show()
