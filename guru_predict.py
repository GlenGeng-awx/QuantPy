import os
from multiprocessing import Pool
from base_engine import BaseEngine
from conf import *
from preload_conf import *
from util import touch_file
from guru_train import valid_dates
import guru

spectrum = [
    (period_1y_to(to_date), args_1y_guru())
    for to_date in valid_dates[-1:]
]

spectrum_ = [
    (period_4y_to(valid_dates[-1]), args_4y_guru()),
    (period_1y_to(valid_dates[-1]), args_1y_guru()),
]


def predict(stock_name: str):
    figs = []
    hits = set()

    for (from_date, to_date, interval), args in spectrum:
        base_engine = BaseEngine(stock_name, from_date, to_date, interval)
        base_engine.build_graph(**args)

        stock_df, fig, context = base_engine.stock_df, base_engine.fig, base_engine.context
        if guru.predict.predict(stock_df, fig, stock_name, context):
            figs.append(fig)
            hits.add(to_date)

    # for fig in figs:
    #     fig.show()

    return stock_name, list(hits)


def dump_prediction(results: dict):
    for stock_name in results:
        hits = results[stock_name]
        for date in hits:
            filename = f'_predict/{stock_name}${date}'
            touch_file(filename)


def load_prediction() -> dict:
    results = {}
    for filename in os.listdir('_predict'):
        stock_name, date = filename.split('$')
        results.setdefault(stock_name, []).append(date)
    return results


if __name__ == '__main__':
    with Pool(processes=12) as pool:
        results_ = pool.map(predict, ALL)
        results_ = dict(results_)

    print(f'Candidates: {[k for k, v in results_.items() if v]}')
    dump_prediction(results_)
