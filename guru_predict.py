import os
from multiprocessing import Pool
from base_engine import BaseEngine
from conf import *
from preload_conf import *
from util import touch_file
from guru_wizard import PREDICT_MODE, valid_dates
from x_kym import get_kym_dates
import guru


def build_tasks(stock_name):
    tasks = []
    # for to_date in get_kym_dates(_stock_name):
    for to_date in valid_dates[:65]:
        for predict_mode in PREDICT_MODE:
            from_date, to_date, interval = period_1y_to(to_date)
            args = args_1y_guru()
            tasks.append((stock_name, from_date, to_date, interval, args, predict_mode))

            # from_date, to_date, interval = period_4y_to(to_date)
            # args = args_4y_guru()
            # tasks.append((stock_name, from_date, to_date, interval, args, predict_mode))
    return tasks


def predict(stock_name: str):
    tasks = build_tasks(stock_name)

    figs = []
    hits = set()

    for task in tasks:
        stock_name, from_date, to_date, interval, args, predict_mode = task

        base_engine = BaseEngine(stock_name, from_date, to_date, interval)
        base_engine.build_graph(**args)

        stock_df, fig, context = base_engine.stock_df, base_engine.fig, base_engine.context
        if guru.predict.predict(stock_df, fig, stock_name, context, predict_mode):
            figs.append(fig)
            hits.add(to_date)
            dump_prediction(stock_name, to_date, predict_mode)

    # for fig in figs:
    #     fig.show()

    return stock_name, list(hits)


def dump_prediction(stock_name: str, to_date: str, predict_mode: str):
    filename = f'{predict_mode}/{stock_name}${to_date}'
    touch_file(filename)


def load_prediction(predict_mode: str) -> dict:
    results = {}
    for filename in os.listdir(predict_mode):
        stock_name, date = filename.split('$')
        results.setdefault(stock_name, []).append(date)
    return results


if __name__ == '__main__':
    with Pool(processes=12) as pool:
        results_ = pool.map(predict, ALL)
        results_ = dict(results_)

    print(f'Candidates: {[k for k, v in results_.items() if v]}')
