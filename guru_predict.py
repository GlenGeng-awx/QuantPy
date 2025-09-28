import os
import plotly.graph_objects as go
from multiprocessing import Pool
from base_engine import BaseEngine
from conf import *
from preload_conf import *
from util import touch_file
from guru_wizard import PREDICT_MODE, PREDICT_MODE_SELECTED, VALID_DATES
from x_opinion import get_opinion_at
import guru

# ALL = get_opinion_at('2025-09-26')
# PREDICT_MODE = PREDICT_MODE_SELECTED


# (stock_name, from_date, to_date, interval, args_fn) -> list of predict_mode
def build_tasks(stock_name):
    tasks = {}
    for to_date in VALID_DATES[-1:]:
        from_date, to_date, interval = period_1y_to(to_date)
        tasks[(stock_name, from_date, to_date, interval, args_1y_guru)] = PREDICT_MODE[:]

        # from_date, to_date, interval = period_4y_to(to_date)
        # tasks[(stock_name, from_date, to_date, interval, args_4y_guru)] = PREDICT_MODE[:]
    return tasks


def predict(stock_name: str):
    tasks = build_tasks(stock_name)

    figs = []
    hits = set()

    for (stock_name, from_date, to_date, interval, args_fn), predict_modes in tasks.items():
        base_engine = BaseEngine(stock_name, from_date, to_date, interval)
        args = args_fn()
        base_engine.build_graph(**args)

        stock_df, fig, context = base_engine.stock_df, base_engine.fig, base_engine.context

        for predict_mode in predict_modes:
            print(f'Predicting {stock_name} {to_date} with {predict_mode}...')
            fig_ = go.Figure(fig)
            if guru.predict.predict(stock_df, fig_, stock_name, context, predict_mode):
                figs.append(fig_)
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
