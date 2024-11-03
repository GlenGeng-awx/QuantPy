import json

import pandas as pd
import plotly.graph_objects as go
from multiprocessing import Process

from features import FEATURE_BUF
from conf import *
from d1_preload import preload
from util import get_idx_by_date

coin = [
    'long green bar',
    'short lower shadow',
    'decr top 10% today',
    'decr top 10% last 3d',
    # 'macd death cross',
    # 'baseline decr 1d',
    'vol max of last 10d',

    # 'long upper shadow',
    # 'short lower shadow',
    # 'up harami',
    # 'real red bar',
]

cflt = [
    # 'extreme high vol',
    'vol max of last 10d',
    'incr top 10% today',
    # 'incr top 10% last 3d',
    'long upper shadow',
    'long green bar',
    # 'fake green bar',
    # 'rsi above 70',
    # 'baseline decr 1d',
]

pfe = [
    'extreme high vol',
    'down engulfing',
]


def search(stock_name, keys):
    base_engine = preload(stock_name)
    stock_df, fig = base_engine.stock_df, base_engine.fig
    # fig.show()

    condition = pd.Series([True] * len(stock_df), index=stock_df.index)
    for key in keys:
        condition &= stock_df[key]

    dates = stock_df[condition]['Date']
    close = stock_df[condition]['close']

    if len(dates) == 0:
        return

    fig.add_trace(
        go.Scatter(
            name=f'filtered', x=dates, y=close, mode='markers', marker=dict(size=8, color='blue'),
        )
    )
    fig.show()


if __name__ == '__main__':
    stock_name = ETSY
    date = '2024-11-01'

    base_engine = preload(stock_name)
    stock_df, fig = base_engine.stock_df, base_engine.fig
    fig.show()

    idx = get_idx_by_date(stock_df, date)
    stats = {}

    for feature in FEATURE_BUF:
        key = feature.KEY
        if stock_df.loc[idx][key]:
            stats[key] = len(stock_df[stock_df[key]])

    stats = sorted(stats.items(), key=lambda x: x[1])
    print(json.dumps(stats, indent=4))

    keys = [stats[i][0] for i in range(4)]
    print(keys)

    procs = []

    for _stock_name in ALL:
        proc = Process(target=search, args=(_stock_name, keys))
        procs.append(proc)
        proc.start()

    for proc in procs:
        proc.join()
