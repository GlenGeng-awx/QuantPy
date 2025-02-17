import plotly.graph_objects as go
from multiprocessing import Process
from conf import *
from preload import preload, preload_impl
from guru.predict import predict

FROM = 1  # 3, 2, 1
SZ = 1


def predict_proxy(stock_name, load_from_date, load_to_date, predict_from_date, predict_to_date):
    base_engine = preload_impl(stock_name, load_from_date, load_to_date, '1d')
    stock_df, fig = base_engine.stock_df, base_engine.fig

    condition = (stock_df['Date'] >= predict_from_date) & (stock_df['Date'] <= predict_to_date)
    stock_df = stock_df.copy()[condition]
    predict(stock_df, go.Figure(fig), stock_name, show=True)


def probe(stock_name):
    base_engine = preload(stock_name)
    stock_df, fig = base_engine.stock_df, base_engine.fig

    for i in range(SZ):
        _stock_df = stock_df.tail(FROM - (i + 1) + 400).head(400)

        hit = predict(_stock_df, go.Figure(fig), stock_name)
        if not hit:
            continue

        load_from_date = stock_df.iloc[0]['Date']
        # load_to_date = stock_df.iloc[-1]['Date']
        load_to_date = _stock_df.iloc[-1]['Date']

        predict_from_date = _stock_df.iloc[0]['Date']
        predict_to_date = _stock_df.iloc[-1]['Date']

        predict_proxy(stock_name, load_from_date, load_to_date, predict_from_date, predict_to_date)


if __name__ == '__main__':
    procs = []

    for _stock_name in CANDIDATES:
        proc = Process(target=probe, args=(_stock_name,))
        procs.append(proc)
        proc.start()

    for proc in procs:
        proc.join()
