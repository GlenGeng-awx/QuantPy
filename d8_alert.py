from multiprocessing import Process
from conf import *
from d1_preload import preload

KEYS = [
    'decr top 10% today',
    'decr top 10% last 3d',

    'incr top 10% today',
    'incr top 10% last 3d',

    'close incr 5d',
    'close decr 5d',

    'long green bar',
    'long red bar',

    'extreme high vol',
    'extreme low vol',

    'high vol',
    'low vol',

    'macd death cross',
    'macd golden cross',

    'up engulfing',
    'down engulfing',
]

RECALL_DAYS = 3


def alert(stock_name, keys, recall_days):
    base_engine = preload(stock_name)
    stock_df, fig = base_engine.stock_df, base_engine.fig
    # fig.show()

    title = []
    stock_df = stock_df.iloc[-recall_days:]

    for key in keys:
        if stock_df[key].any():
            title.append(key)

    if len(title) < 3:
        return

    origin_title = fig.layout.title.text
    fig.update_layout(title=f'{origin_title}<br>{", ".join(title)}')
    fig.show()


if __name__ == '__main__':
    procs = []

    for _stock_name in ALL:
        proc = Process(target=alert, args=(_stock_name, KEYS, RECALL_DAYS))
        procs.append(proc)
        proc.start()

    for proc in procs:
        proc.join()
