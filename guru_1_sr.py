from multiprocessing import Process
from conf import *
from d1_preload import preload
from guru import train


def probe(stock_name):
    base_engine = preload(stock_name)
    stock_df, fig = base_engine.stock_df, base_engine.fig

    # hit = search(stock_df, fig, -60, -40)
    # hit = search(stock_df, fig, -5, -2)
    hit = train(stock_df, fig, 50, -2)

    # if hit:
    #     fig.show()


if __name__ == '__main__':
    procs = []

    for _stock_name in [LI]:
        proc = Process(target=probe, args=(_stock_name,))
        procs.append(proc)
        proc.start()

    for proc in procs:
        proc.join()
