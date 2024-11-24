from multiprocessing import Process
from conf import *
from d1_preload import preload
from trading.position import POSITION
from guru.train import train
from guru.predict import predict


def probe(stock_name):
    base_engine = preload(stock_name)
    stock_df, fig = base_engine.stock_df, base_engine.fig

    train(stock_df, stock_name, 50, -2)
    # predict(stock_df, fig, stock_name, 50, -2)


if __name__ == '__main__':
    procs = []

    # for _stock_name in INDEX + list(POSITION.keys()):
    for _stock_name in ALL:
        proc = Process(target=probe, args=(_stock_name,))
        procs.append(proc)
        proc.start()

    for proc in procs:
        proc.join()
