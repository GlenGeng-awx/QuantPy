import plotly.graph_objects as go
from multiprocessing import Pool
from base_engine import BaseEngine
from conf import *
from preload_conf import *
from guru_wizard import VALID_DATES, PREDICT_MODE
from guru.train import interpolate_context
from technical.prediction import dump_prediction
import guru


def build_tasks():
    tasks = []

    for stock_name in ALL:
        for to_date in VALID_DATES[-1:]:
            # 1y
            from_date, to_date, interval = period_predict(to_date)
            task = (stock_name, from_date, to_date, interval, model_args, PREDICT_MODE)
            tasks.append(task)

            # 4y
            from_date, to_date, interval = period_train(to_date, 48)
            task = (stock_name, from_date, to_date, interval, model_args, PREDICT_MODE)
            # tasks.append(task)

    return tasks


# task: (stock_name, from_date, to_date, interval, args_fn, list of predict_mode)
def predict(task: list):
    stock_name, from_date, to_date, interval, args_fn, predict_modes = task
    args = args_fn()

    base_engine = BaseEngine(stock_name, from_date, to_date, interval)
    base_engine.build_graph(**args)

    stock_df, fig, context = base_engine.stock_df, base_engine.fig, base_engine.context
    context = interpolate_context(stock_df, context)

    figs = []

    for predict_mode in predict_modes:
        print(f'Predicting {stock_name} {to_date} with {predict_mode}')
        fig_ = go.Figure(fig)
        fig_.update_layout(title=f"{fig.layout.title.text}<br>{' ' * 18}{predict_mode}")

        if guru.predict.predict(stock_df, fig_, stock_name, context, predict_mode):
            figs.append(fig_)
            dump_prediction(stock_name, to_date, predict_mode)

    for fig in figs:
        fig.show()

    if figs:
        from_date, to_date, interval = period_ny(years=1)
        args = display_args(with_high=True, with_mid=True, with_low=True, with_guru=True)

        base_engine = BaseEngine(stock_name, from_date, to_date, interval)
        base_engine.build_graph(**args)
        base_engine.fig.show()


if __name__ == '__main__':
    _tasks = build_tasks()

    with Pool(processes=1) as pool:
        pool.map(predict, _tasks)
