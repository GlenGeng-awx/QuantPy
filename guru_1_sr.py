from multiprocessing import Process
from conf import *
from d1_preload import preload
from guru import STRATEGY, plot_strategy


def probe(stock_name):
    base_engine = preload(stock_name)
    stock_df, fig = base_engine.stock_df, base_engine.fig

    hit = False
    for strategy in STRATEGY:
        # hit |= plot_strategy(stock_df, fig, -60, -40, strategy)
        # hit |= plot_strategy(stock_df, fig, -5, -2, strategy)
        hit |= plot_strategy(stock_df, fig, 50, -2, strategy)

    if hit:
        fig.show()


if __name__ == '__main__':
    procs = []

    for _stock_name in ALL:
        proc = Process(target=probe, args=(_stock_name,))
        procs.append(proc)
        proc.start()

    for proc in procs:
        proc.join()
