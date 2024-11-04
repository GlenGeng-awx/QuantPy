import pandas as pd
import plotly.graph_objects as go
from multiprocessing import Process
from d1_preload import preload


def recall_1day(stock_df: pd.DataFrame, idx: int, stat: dict) -> bool:
    for key in stat:
        if not stock_df.loc[idx][key]:
            return False
    return True


def recall(stock_name, stats):
    base_engine = preload(stock_name)
    stock_df, fig = base_engine.stock_df, base_engine.fig

    stats = [stat for idx, stat in stats.items()]
    indices = []

    for idx in stock_df.index:
        match = True

        for stat, i in zip(stats, range(idx, idx + 1_000)):
            if not recall_1day(stock_df, i, stat):
                match = False
                break

        if match:
            indices.append(idx)

    dates = stock_df.loc[indices]['Date']
    close = stock_df.loc[indices]['close']

    if len(dates) == 0:
        return

    fig.add_trace(
        go.Scatter(
            name=f'filtered', x=dates, y=close, mode='markers', marker=dict(size=8, color='blue'),
        )
    )
    fig.show()


if __name__ == '__main__':
    from conf import *
    from guru_2_repo import GURU_REPO

    procs = []

    for _stock_name in ALL:
        proc = Process(target=recall, args=(_stock_name, GURU_REPO[SS_000300]))
        procs.append(proc)
        proc.start()

    for proc in procs:
        proc.join()
