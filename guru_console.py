import plotly.graph_objects as go
from multiprocessing import Process
from conf import *
from d1_preload import preload
from guru.train import train
from guru.predict import predict


def probe(stock_name):
    base_engine = preload(stock_name)
    stock_df, fig = base_engine.stock_df, base_engine.fig

    # (-440, None)
    # (-440, -15)
    for i in range(-3, 0):
        _stock_df = stock_df.iloc[i - 400:i]
        train(_stock_df, stock_name)
        predict(_stock_df, go.Figure(fig), stock_name)

    stock_df = stock_df.iloc[-400:]
    train(stock_df, stock_name)
    predict(stock_df, go.Figure(fig), stock_name)


if __name__ == '__main__':
    procs = []

    for _stock_name in ALL:
        proc = Process(target=probe, args=(_stock_name,))
        procs.append(proc)
        proc.start()

    for proc in procs:
        proc.join()
