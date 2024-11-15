import pandas as pd
import plotly.graph_objects as go

from .util import get_index
from .holding_long import eval_long
from .holding_short import eval_short

from guru import (
    # sr level & min max 3rd
    long_001, short_001,        # long green bar        / long red bar
    long_002, short_002,        # decr top 10% last 10d / incr top 10% last 10d
    long_003, short_003,        # long lower shadow     / long upper shadow
    long_004, short_004,        # up thru ma5           / down thru ma5
    long_005, short_005,        # up thru ma20          / down thru ma20
)

STRATEGY = [
    long_001, long_002, long_003, long_004, long_005,
    short_001, short_002, short_003, short_004, short_005,
]


def _execute_strategy(stock_df: pd.DataFrame, from_idx, to_idx, strategy) -> tuple:
    indices = []
    for idx in get_index(stock_df, from_idx, to_idx):
        if strategy.check(stock_df, idx):
            indices.append(idx)

    if not indices:
        return strategy.NAME, strategy.COLOR, None, None, 0, 0

    dates = stock_df.loc[indices]['Date'].tolist()
    close = stock_df.loc[indices]['close'].tolist()

    if strategy.TYPE == 'long':
        hit_num, total_pnl = eval_long(stock_df, indices, strategy.NAME)
    else:
        hit_num, total_pnl = eval_short(stock_df, indices, strategy.NAME)

    return strategy.NAME, strategy.COLOR, dates, close, hit_num, total_pnl


def plot_strategy(stock_df: pd.DataFrame, fig: go.Figure, from_idx, to_idx, strategy) -> bool:
    name, color, dates, close, hit_num, total_pnl = _execute_strategy(stock_df, from_idx, to_idx, strategy)

    if not dates:
        return False

    fig.add_trace(
        go.Scatter(
            name=f'{name}, {hit_num}, {total_pnl:.2%}',
            x=dates, y=close,
            mode='markers', marker=dict(size=10, color=color),
            # visible='legendonly',
        )
    )
    return True
