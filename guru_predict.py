from multiprocessing import Process, Queue
from base_engine import BaseEngine
from conf import *
from preload_conf import *
import guru

spectrum = [
    (period_4y(), args_4y_guru()),
    (period_1y(), args_1y_guru()),
]


def predict(stock_name: str, q: Queue):
    figs = []

    for (from_date, to_date, interval), args in spectrum:
        base_engine = BaseEngine(stock_name, from_date, to_date, interval)
        base_engine.build_graph(**args)

        stock_df, fig, context = base_engine.stock_df, base_engine.fig, base_engine.context
        if guru.predict.predict(stock_df, fig, stock_name, context):
            figs.append(fig)

    for fig in figs:
        fig.show()

    if figs:
        q.put(stock_name)


if __name__ == '__main__':
    BATCH_SIZE = 10
    candidates = []

    for i in range(0, len(ALL), BATCH_SIZE):
        batch = ALL[i:i + BATCH_SIZE]
        processes = []
        queue = Queue()

        for _stock_name in batch:
            p = Process(target=predict, args=(_stock_name, queue))
            processes.append(p)
            p.start()

        for p in processes:
            p.join()

        while not queue.empty():
            candidates.append(queue.get())

    print(f'Candidates: {candidates}')
