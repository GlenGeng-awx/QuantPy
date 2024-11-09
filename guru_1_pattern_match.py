import pandas as pd
import plotly.graph_objects as go
from multiprocessing import Process
from conf import *
from d1_preload import preload

CONDITIONS = [
    # [['long green bar'], ['fake green bar'], ['incr top 10% today']],
    # ['long red bar'], ['fake red bar'], ['decr top 10% today'],
    ['long red bar'], ['high vol'], ['up thru ma20', 'up thru ma60'],
]

RECALL_DAYS = 1


def check_idx_cond(stock_df: pd.DataFrame, conditions: list[list], recall_days: int, idx: int) -> bool:
    stock_df = stock_df.loc[idx - recall_days + 1:idx]

    for condition in conditions:
        hit = False

        for key in condition:
            if stock_df[key].any():
                hit = True
                break

        if not hit:
            return False

    return True


# check every day
def retro_cond(stock_name, conditions, recall_days):
    base_engine = preload(stock_name)
    stock_df, fig = base_engine.stock_df, base_engine.fig

    indices = []
    for idx in stock_df.index[recall_days:]:
        if check_idx_cond(stock_df, conditions, recall_days, idx):
            indices.append(idx)

    if not indices:
        return

    dates = stock_df.loc[indices]['Date']
    close = stock_df.loc[indices]['close']

    fig.add_trace(
        go.Scatter(
            name=f'filtered', x=dates, y=close, mode='markers', marker=dict(size=10, color='black'),
        )
    )
    fig.show()


if __name__ == '__main__':
    procs = []

    for _stock_name in ALL:
        # proc = Process(target=collect, args=(_stock_name, KEYS, RECALL_DAYS))
        proc = Process(target=retro_cond, args=(_stock_name, CONDITIONS, RECALL_DAYS))
        procs.append(proc)
        proc.start()

    for proc in procs:
        proc.join()
