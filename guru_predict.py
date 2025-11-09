import os
from multiprocessing import Pool
from base_engine import BaseEngine
from conf import *
from preload_conf import *
from util import touch_file
from guru_wizard import PREDICT_MODE, VALID_DATES
from guru.train import interpolate_context
import guru


def build_tasks():
    tasks = []
    for stock_name in ALL:
        for to_date in VALID_DATES[-1:]:
            for model_name in guru.models:  # box or trend
                from_date, to_date, interval = period_predict(to_date)
                task = (stock_name, from_date, to_date, interval, model_args, PREDICT_MODE[:], model_name)
                tasks.append(task)
    return tasks


# task: (stock_name, from_date, to_date, interval, args_fn, list of predict_mode, model_name)
def predict(task: list):
    stock_name, from_date, to_date, interval, args_fn, predict_modes, model_name = task
    args = args_fn()

    base_engine = BaseEngine(stock_name, from_date, to_date, interval)
    base_engine.build_graph(**args)

    stock_df, context = base_engine.stock_df, base_engine.context
    context = interpolate_context(stock_df, context)

    for predict_mode in predict_modes:
        print(f'Predicting {stock_name} {to_date} with {predict_mode} {model_name}...')
        if guru.predict.predict(stock_df, None, stock_name, context, predict_mode, model_name):
            dump_prediction(stock_name, to_date, predict_mode, model_name)


# box/_predict_36m_t4_h4/WMT$2025-10-21
def dump_prediction(stock_name: str, to_date: str, predict_mode: str, model_name: str):
    filename = f'{model_name}/{predict_mode}/{stock_name}${to_date}'
    touch_file(filename)


def load_prediction(predict_mode: str, model_name: str) -> dict:
    results = {}
    for filename in os.listdir(f'{model_name}/{predict_mode}'):
        stock_name, date = filename.split('$')
        results.setdefault(stock_name, []).append(date)
    return results


if __name__ == '__main__':
    _tasks = build_tasks()

    with Pool(processes=12) as pool:
        pool.map(predict, _tasks)
