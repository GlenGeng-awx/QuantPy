from multiprocessing import Process
from conf import *
from d1_preload import preload

KEYS = [
    'up thru ma60',                     'down thru ma60',
    'macd golden cross',                'macd death cross',

    'incr top 10% today',               'decr top 10% today',
    'incr top 10% last 3d',             'decr top 10% last 3d',

    'up thru sr level',                 'down thru sr level',
    'yesterday min of last 120d',       'yesterday max of last 120d',

    'long red bar',                     'long green bar',
    'up engulfing',                     'down engulfing',
    'up harami',                        'down harami',

    'extreme high vol',                 'extreme low vol',
    'vol min of last 10d',              'vol max of last 10d',

    'close incr 5d',                    'close decr 5d',
    'vol incr 5d',                      'vol decr 5d',
]

RECALL_DAYS = 2
LEAST_HITS = 5


def collect(stock_name, keys, recall_days):
    base_engine = preload(stock_name)
    stock_df, fig = base_engine.stock_df, base_engine.fig
    # fig.show()

    hits = []
    stock_df = stock_df.iloc[-recall_days:]

    for key in keys:
        if stock_df[key].any():
            hits.append(key)

    if len(hits) < LEAST_HITS:
        return

    origin_title = fig.layout.title.text
    fig.update_layout(title=f'{origin_title}<br>{", ".join(hits)}')
    fig.show()


if __name__ == '__main__':
    procs = []

    for _stock_name in ALL:
        proc = Process(target=collect, args=(_stock_name, KEYS, RECALL_DAYS))
        procs.append(proc)
        proc.start()

    for proc in procs:
        proc.join()
