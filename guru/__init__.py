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
    # long_004, short_004,        # up thru ma5           / down thru ma5
    long_005, short_005,        # up thru ma20          / down thru ma20
    long_006, short_006,        # up thru ma60          / down thru ma60
)

STRATEGY = [
    long_001, long_002, long_003, long_005, long_006,
    short_001, short_002, short_003, short_005, short_006,
]


def execute_strategy(stock_df: pd.DataFrame, from_idx, to_idx, strategy) -> tuple:
    indices = []
    for idx in get_index(stock_df, from_idx, to_idx):
        if strategy.check(stock_df, idx):
            indices.append(idx)

    if not indices:
        return strategy.NAME, strategy.COLOR, None, None, None

    dates = stock_df.loc[indices]['Date'].tolist()
    close = stock_df.loc[indices]['close'].tolist()

    return strategy.NAME, strategy.COLOR, dates, close, indices


def get_pnl_tag(stock_df: pd.DataFrame, indices, strategy) -> str:
    if strategy.TYPE == 'long':
        return '<br>'.join(eval_long(stock_df, indices, strategy.NAME))
    elif strategy.TYPE == 'short':
        return '<br>'.join(eval_short(stock_df, indices, strategy.NAME))
    else:
        return ''


def plot_strategy(stock_df: pd.DataFrame, fig: go.Figure, from_idx, to_idx, strategy) -> bool:
    name, color, dates, close, indices = execute_strategy(stock_df, from_idx, to_idx, strategy)
    if not indices:
        return False

    pnl_tag = get_pnl_tag(stock_df, indices, strategy)

    fig.add_trace(
        go.Scatter(
            name=f'{name}<br>{pnl_tag}',
            x=dates, y=close,
            mode='markers', marker=dict(size=10, color=color),
            # visible='legendonly',
        )
    )
    return True
