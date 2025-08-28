import json
from multiprocessing import Pool
from base_engine import BaseEngine
from conf import *
from preload_conf import *
from guru_train import valid_dates
import guru

spectrum = [
    (period_1y_to(to_date), args_1y_guru())
    for to_date in valid_dates
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


if __name__ == '__main__':
    with Pool(processes=12) as pool:
        results = pool.map(predict, ALL)
        results = dict(results)

    print(f'Candidates: {[k for k, v in results.items() if v]}')

    with open('_predict', 'w') as fd:
        fd.write(json.dumps(results, indent=2))
