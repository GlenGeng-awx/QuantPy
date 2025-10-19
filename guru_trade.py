import plotly.graph_objects as go
from multiprocessing import Pool
from base_engine import BaseEngine
from conf import *
from preload_conf import *
from guru_wizard import VALID_DATES
from guru_kym import filter_predict_modes
import guru


def build_tasks():
    tasks = []

    for stock_name in ALL:
        predict_modes = filter_predict_modes(stock_name)
        if not predict_modes:
            continue

        for to_date in VALID_DATES[-1:]:
            # 1y
            from_date, to_date, interval = period_predict(to_date)
            tasks.append((stock_name, from_date, to_date, interval, args_1y_guru, predict_modes[:]))

            # 4y
            from_date, to_date, interval = period_train(to_date, 48)
            tasks.append((stock_name, from_date, to_date, interval, args_4y_guru, predict_modes[:]))

    return tasks


# task: (stock_name, from_date, to_date, interval, args_fn, list of (predict_mode, model_rate, count_hit))
def predict(task: list):
    stock_name, from_date, to_date, interval, args_fn, predict_modes = task
    args = args_fn()

    base_engine = BaseEngine(stock_name, from_date, to_date, interval)
    base_engine.build_graph(**args)

    stock_df, fig, context = base_engine.stock_df, base_engine.fig, base_engine.context

    figs = []

    for predict_mode, model_rate, count_hit, nature_rate, count_all in predict_modes:
        print(f'Predicting {stock_name} {to_date} with {predict_mode} {model_rate} {count_hit}')
        fig_ = go.Figure(fig)

        sub_title = f'{predict_mode} {model_rate * 100:.1f}% {count_hit} hit <-- nature {nature_rate * 100:.1f}% {count_all} total'
        fig_.update_layout(title=f"{fig.layout.title.text}<br>{' ' * 18}{sub_title}")

        if guru.predict.predict(stock_df, fig_, stock_name, context, predict_mode):
            figs.append(fig_)

    for fig in figs:
        fig.show()

    if figs:
        (from_date, to_date, interval), args = period_1y(), args_1y_guru()
        base_engine = BaseEngine(stock_name, from_date, to_date, interval)
        base_engine.build_graph(**args)
        base_engine.fig.show()


if __name__ == '__main__':
    _tasks = build_tasks()

    with Pool(processes=1) as pool:
        pool.map(predict, _tasks)
