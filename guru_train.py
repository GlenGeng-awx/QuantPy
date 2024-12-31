from multiprocessing import Process
from conf import *
from preload import preload
from guru.train import train
from guru.train_cross import train_cross
from util import shrink_date_str

FROM = 3    # 3    or 30
SZ = FROM   # FROM or 20


def probe(stock_name):
    base_engine = preload(stock_name)
    stock_df = base_engine.stock_df

    for i in range(SZ):
        _stock_df = stock_df.tail(FROM - (i + 1) + 400).head(400)
        train(_stock_df, stock_name)


if __name__ == '__main__':
    procs = []

    for _stock_name in ALL:
        proc = Process(target=probe, args=(_stock_name,))
        procs.append(proc)
        proc.start()

    for proc in procs:
        proc.join()

    for _date in preload(IXIC).stock_df.tail(FROM).head(SZ)['Date']:
        _date = shrink_date_str(_date)
        train_cross(_date)
