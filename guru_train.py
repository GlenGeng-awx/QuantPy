from multiprocessing import Process
from base_engine import BaseEngine
from conf import *
from preload_conf import *
import guru

spectrum = [
    (period_train('2025-08-04'), args_4y_guru()),
]


def train(stock_name: str):
    for (from_date, to_date, interval), args in spectrum:
        base_engine = BaseEngine(stock_name, from_date, to_date, interval)
        base_engine.build_graph(**args)

        stock_df, context = base_engine.stock_df, base_engine.context
        guru.train.train(stock_df, stock_name, context)


if __name__ == '__main__':
    BATCH_SIZE = 10

    for i in range(0, len(ALL), BATCH_SIZE):
        batch = ALL[i:i + BATCH_SIZE]
        processes = []

        for _stock_name in batch:
            p = Process(target=train, args=(_stock_name,))
            processes.append(p)
            p.start()

        for p in processes:
            p.join()
