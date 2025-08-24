from multiprocessing import Pool
from base_engine import BaseEngine
from conf import *
from preload_conf import *
import guru

spectrum = [
    (period_train('2025-08-22'), args_4y_guru()),
]


def train(stock_name: str):
    for (from_date, to_date, interval), args in spectrum:
        base_engine = BaseEngine(stock_name, from_date, to_date, interval)
        base_engine.build_graph(**args)

        stock_df, context = base_engine.stock_df, base_engine.context
        guru.train.train(stock_df, stock_name, context)


if __name__ == '__main__':
    with Pool(processes=12) as pool:
        pool.map(train, ALL)
