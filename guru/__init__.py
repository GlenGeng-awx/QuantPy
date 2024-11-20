import pandas as pd
import plotly.graph_objects as go

from .holding_long import eval_long
from .holding_short import eval_short

from guru import (
    guru_1,         # sr level
    guru_2,         # ma
    guru_3,         # shape
    guru_4,         # volume
    guru_5,         # post check
)


def get_index(stock_df: pd.DataFrame, from_idx, to_idx) -> pd.Series:
    if from_idx is not None and to_idx is not None:
        return stock_df.index[from_idx:to_idx]

    if from_idx is not None and to_idx is None:
        return stock_df.index[from_idx:]

    if from_idx is None and to_idx is not None:
        return stock_df.index[:to_idx]

    if from_idx is None and to_idx is None:
        return stock_df.index


def filter_index(stock_df: pd.DataFrame, idx: int, ops: list) -> bool:
    for op in ops:
        if not op(stock_df, idx):
            return False
    return True


def execute_ops(stock_df: pd.DataFrame, fig: go.Figure, from_idx, to_idx, ops) -> bool:
    indices = []

    for idx in get_index(stock_df, from_idx, to_idx):
        if filter_index(stock_df, idx, ops):
            indices.append(idx)

    if not indices:
        return False

    name = ','.join(op.__name__ for op in ops)

    long_results = eval_long(stock_df, indices, name)
    enable_long = all(hit_num >= 3 and total_pnl / hit_num >= 0.20 for (_, hit_num, total_pnl) in long_results)

    short_results = eval_short(stock_df, indices, name)
    enable_short = all(hit_num >= 3 and total_pnl / hit_num >= 0.20 for (_, hit_num, total_pnl) in short_results)

    if not enable_long and not enable_short:
        return False

    dates = stock_df.loc[indices]['Date'].tolist()
    close = stock_df.loc[indices]['close'].tolist()

    pnl_tag = ''
    color = ''

    if enable_long:
        pnl_tag = '<br>'.join(tag for (tag, _, _) in long_results)
        color = 'orange'

    if enable_short:
        pnl_tag = '<br>'.join(tag for (tag, _, _) in short_results)
        color = 'black'

    print(f'{name} ---> {pnl_tag}')

    name = '<br>'.join(op.__name__ for op in ops)

    # fig.add_trace(
    #     go.Scatter(
    #         name=f'{name}<br>{pnl_tag}',
    #         x=dates, y=close,
    #         mode='markers', marker=dict(size=10, color=color),
    #         visible='legendonly',
    #     )
    # )

    return True


def train(stock_df: pd.DataFrame, fig: go.Figure, from_idx, to_idx) -> bool:
    hit = False

    for op1 in guru_1.operators:
        for op2 in guru_2.operators:
            for op3 in guru_3.operators:
                for op4 in guru_4.operators:
                    for op5 in guru_5.operators:
                        if execute_ops(stock_df, fig, from_idx, to_idx, [op1, op2, op3, op4, op5]):
                            hit = True

    return hit
