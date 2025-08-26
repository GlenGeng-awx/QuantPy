import json
from multiprocessing import Pool
from base_engine import BaseEngine
from conf import *
from preload_conf import *
import guru

spectrum = [
    (period_1y_to(to_date), args_1y_guru())
    for to_date in [
        '2025-07-14', '2025-07-15', '2025-07-16', '2025-07-17', '2025-07-18',
        '2025-07-21', '2025-07-22', '2025-07-23', '2025-07-24', '2025-07-25',
        '2025-07-28', '2025-07-29', '2025-07-30', '2025-07-31', '2025-08-01',

        '2025-08-04', '2025-08-05', '2025-08-06', '2025-08-07', '2025-08-08',
        '2025-08-11', '2025-08-12', '2025-08-13', '2025-08-14', '2025-08-15',
        '2025-08-18', '2025-08-19', '2025-08-20', '2025-08-21', '2025-08-22',
        '2025-08-25',
    ]
]

spectrum_ = [
    (period_4y_to('2025-08-22'), args_4y_guru()),
    (period_1y_to('2025-08-22'), args_1y_guru()),
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
