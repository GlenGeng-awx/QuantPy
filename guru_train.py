import re
import random
from multiprocessing import Pool
from base_engine import BaseEngine
from conf import *
from preload_conf import *
from guru_wizard import TRAIN_MODE, valid_dates
import guru


def build_tasks() -> list:
    tasks = []
    for stock_name in ALL:
        for to_date in valid_dates[-1:]:
            for train_mode in TRAIN_MODE:
                # _train_48m/42m/36m
                months = re.search(r'\d+', train_mode).group()
                from_date, to_date, interval = period_train(to_date, int(months))
                tasks.append((stock_name, from_date, to_date, interval, args_4y_guru(), train_mode))
    return tasks


# task: (stock_name, from_date, to_date, interval, args, train_mode)
def train(task: list):
    stock_name, from_date, to_date, interval, args, train_mode = task

    base_engine = BaseEngine(stock_name, from_date, to_date, interval)
    base_engine.build_graph(**args)

    stock_df, context = base_engine.stock_df, base_engine.context
    guru.train.train(stock_df, stock_name, context, train_mode)


if __name__ == '__main__':
    _tasks = build_tasks()
    random.shuffle(_tasks)

    with Pool(processes=12) as pool:
        pool.map(train, _tasks)
