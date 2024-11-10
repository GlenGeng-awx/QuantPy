import pandas as pd
import plotly.graph_objects as go
from multiprocessing import Process
from conf import *
from technical.min_max import LOCAL_MAX_PRICE_3RD, LOCAL_MIN_PRICE_3RD
from technical.sr_level import SR_LEVEL_MIN, SR_LEVEL_MAX
from d1_preload import preload

FROM = 27  # 27, 30, 35
TO = 20


def check_long(stock_df: pd.DataFrame, idx: int) -> bool:
    conditions = ['long green bar', 'decr top 10% last 5d']
    # conditions = ['decr top 10% last 5d']
    if not any(stock_df.loc[idx][condition] for condition in conditions):
        return False

    stock_df = stock_df.loc[idx - FROM:idx - TO]
    return stock_df[SR_LEVEL_MIN].any() and stock_df[LOCAL_MIN_PRICE_3RD].any()


def check_short(stock_df: pd.DataFrame, idx: int) -> bool:
    conditions = ['long red bar', 'incr top 10% last 5d']
    # conditions = ['incr top 10% last 5d']
    if not any(stock_df.loc[idx][condition] for condition in conditions):
        return False

    stock_df = stock_df.loc[idx - FROM:idx - TO]
    return stock_df[SR_LEVEL_MAX].any() and stock_df[LOCAL_MAX_PRICE_3RD].any()


def pattern_match(stock_name):
    base_engine = preload(stock_name)
    stock_df, fig = base_engine.stock_df, base_engine.fig

    long_indices = []
    short_indices = []

    # for idx in stock_df.index[-60:-40]:
    for idx in stock_df.index[-10:]:
        if check_long(stock_df, idx):
            long_indices.append(idx)
        if check_short(stock_df, idx):
            short_indices.append(idx)

    if not long_indices and not short_indices:
        return

    fig.add_trace(
        go.Scatter(
            name=f'long',
            x=stock_df.loc[long_indices]['Date'],
            y=stock_df.loc[long_indices]['close'],
            mode='markers', marker=dict(size=10, color='orange'),
        )
    )
    fig.add_trace(
        go.Scatter(
            name=f'short',
            x=stock_df.loc[short_indices]['Date'],
            y=stock_df.loc[short_indices]['close'],
            mode='markers', marker=dict(size=10, color='black'),
        )
    )

    fig.show()


if __name__ == '__main__':
    procs = []

    for _stock_name in ALL:
        proc = Process(target=pattern_match, args=(_stock_name,))
        procs.append(proc)
        proc.start()

    for proc in procs:
        proc.join()
