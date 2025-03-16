from multiprocessing import Process
from conf import *
from preload import preload
from guru.train import train
from guru import PERIOD
import features

FROM = 200   # 3    or 30
SZ = 200     # FROM or 20


def probe(stock_name):
    base_engine = preload(stock_name)
    stock_df = base_engine.stock_df
    stock_df = features.calculate_feature(stock_df, stock_name, True)

    for i in range(SZ):
        _stock_df = stock_df.tail(FROM - (i + 1) + PERIOD).head(PERIOD)
        train(_stock_df, stock_name)


def parallel_probe(stock_names):
    procs = []

    for stock_name in stock_names:
        proc = Process(target=probe, args=(stock_name,))
        procs.append(proc)
        proc.start()

    for proc in procs:
        proc.join()


if __name__ == '__main__':
    parallel_num = 12
    for i in range(0, len(ALL), parallel_num):
        parallel_probe(ALL[i: i + parallel_num])
