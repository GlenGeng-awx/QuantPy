import plotly.graph_objects as go
from multiprocessing import Process
from conf import *
from preload import preload
from guru.predict import predict
from guru import PERIOD
import features

FROM = 200  # 3, 2, 1
SZ = 200


def probe(stock_name):
    base_engine = preload(stock_name)
    stock_df, fig = base_engine.stock_df, base_engine.fig
    stock_df = features.calculate_feature(stock_df, stock_name, True)

    for i in range(SZ):
        _stock_df = stock_df.tail(FROM - (i + 1) + PERIOD).head(PERIOD)
        predict(_stock_df, go.Figure(fig), stock_name)


def parallel_probe(stock_names):
    procs = []

    for stock_name in stock_names:
        proc = Process(target=probe, args=(stock_name,))
        procs.append(proc)
        proc.start()

    for proc in procs:
        proc.join()


if __name__ == '__main__':
    parallel_num = 12
    for i in range(0, len(ALL), parallel_num):
        parallel_probe(ALL[i: i + parallel_num])
