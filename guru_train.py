from multiprocessing import Pool
from base_engine import BaseEngine
from conf import *
from preload_conf import *
import guru

valid_dates = [
    '2025-06-23', '2025-06-24', '2025-06-25', '2025-06-26', '2025-06-27',

    '2025-06-30', '2025-07-01', '2025-07-02', '2025-07-03',
    '2025-07-07', '2025-07-08', '2025-07-09', '2025-07-10', '2025-07-11',
    '2025-07-14', '2025-07-15', '2025-07-16', '2025-07-17', '2025-07-18',
    '2025-07-21', '2025-07-22', '2025-07-23', '2025-07-24', '2025-07-25',
    '2025-07-28', '2025-07-29', '2025-07-30', '2025-07-31', '2025-08-01',

    '2025-08-04', '2025-08-05', '2025-08-06', '2025-08-07', '2025-08-08',
    '2025-08-11', '2025-08-12', '2025-08-13', '2025-08-14', '2025-08-15',
    '2025-08-18', '2025-08-19', '2025-08-20', '2025-08-21', '2025-08-22',
    '2025-08-25', '2025-08-26', '2025-08-27', '2025-08-28', '2025-08-29',

                  '2025-09-02',
]

spectrum = [
    (period_train(to_date), args_4y_guru())
    for to_date in valid_dates[-1:]
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
