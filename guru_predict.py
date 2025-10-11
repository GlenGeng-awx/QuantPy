import os
import plotly.graph_objects as go
from multiprocessing import Pool
from base_engine import BaseEngine
from conf import *
from preload_conf import *
from util import touch_file
from guru_wizard import PREDICT_MODE, VALID_DATES
import guru


def build_tasks():
    tasks = []
    for stock_name in ALL:
        for to_date in VALID_DATES[-1:]:
            from_date, to_date, interval = period_predict(to_date)
            tasks.append((stock_name, from_date, to_date, interval, args_1y_guru, PREDICT_MODE[:]))
    return tasks


# task: (stock_name, from_date, to_date, interval, args_fn, list of predict_mode)
def predict(task: list):
    stock_name, from_date, to_date, interval, args_fn, predict_modes = task
    args = args_fn()

    base_engine = BaseEngine(stock_name, from_date, to_date, interval)
    base_engine.build_graph(**args)

    stock_df, fig, context = base_engine.stock_df, base_engine.fig, base_engine.context

    for predict_mode in predict_modes:
        print(f'Predicting {stock_name} {to_date} with {predict_mode}...')
        if guru.predict.predict(stock_df, go.Figure(fig), stock_name, context, predict_mode):
            dump_prediction(stock_name, to_date, predict_mode)


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
    _tasks = build_tasks()

    with Pool(processes=12) as pool:
        pool.map(predict, _tasks)
