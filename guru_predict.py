import plotly.graph_objects as go
from multiprocessing import Process
from conf import *
from preload import preload
from guru.predict import predict

FROM = 3  # 3, 2, 1
SZ = 1


def probe(stock_name):
    base_engine = preload(stock_name)
    stock_df, fig = base_engine.stock_df, base_engine.fig

    for i in range(SZ):
        _stock_df = stock_df.tail(FROM - (i + 1) + 400).head(400)
        predict(_stock_df, go.Figure(fig), stock_name)


if __name__ == '__main__':
    procs = []

    for _stock_name in ALL:
        proc = Process(target=probe, args=(_stock_name,))
        procs.append(proc)
        proc.start()

    for proc in procs:
        proc.join()
