from datetime import datetime

import pandas as pd
import plotly.graph_objects as go

from gringotts import (predict_confs, dev_confs, FROM_DATE, TO_DATE,
                       TRAIN_FROM_DATE, TRAIN_TO_DATE, PREDICT_FROM_DATE, PREDICT_TO_DATE)
from gringotts.giant_model import GiantModel

from d0_preload import preload
from d2_periods import get_train_periods, get_predict_partial_period


def predict_partial(stock_name: str, stock_df: pd.DataFrame, to_date: str):
    giant_models = []

    start_time = datetime.now()
    train_periods = get_train_periods(stock_df, to_date)
    predict_partial_from_period, predict_partial_to_period = get_predict_partial_period(stock_df)

    for confs, (train_from_date, train_to_date) in zip(predict_confs, train_periods):
        for conf in confs:
            period = {
                FROM_DATE: predict_partial_from_period,
                TO_DATE: predict_partial_to_period,

                TRAIN_FROM_DATE: train_from_date,
                TRAIN_TO_DATE: train_to_date,
            }

            conf = conf.copy()
            conf.update(period)

            giant_model = GiantModel(stock_df, stock_name, conf)
            giant_model.run()

            giant_models.append(giant_model)

    end_time = datetime.now()
    time_cost = (end_time - start_time).total_seconds()
    print(f'{stock_name} finished at {end_time.time()}, cost {time_cost}s')

    return giant_models


def dev(stock_name: str, stock_df: pd.DataFrame, to_date: str):
    giant_models = []

    start_time = datetime.now()
    train_periods = get_train_periods(stock_df, to_date)
    predict_partial_from_period, predict_partial_to_period = get_predict_partial_period(stock_df)

    for confs, (train_from_date, train_to_date) in zip(dev_confs, train_periods):
        for conf in confs:
            period = {
                FROM_DATE: train_from_date,
                TO_DATE: predict_partial_to_period,

                PREDICT_FROM_DATE: predict_partial_from_period,
                PREDICT_TO_DATE: predict_partial_to_period,
            }

            conf = conf.copy()
            conf.update(period)

            giant_model = GiantModel(stock_df, stock_name, conf)
            giant_model.run()

            giant_models.append(giant_model)

    end_time = datetime.now()
    time_cost = (end_time - start_time).total_seconds()
    print(f'{stock_name} finished at {end_time.time()}, cost {time_cost}s')

    return giant_models


if __name__ == '__main__':
    from conf import *

    for _stock_name in [PDD]:
        _base_engine = preload(_stock_name)
        _stock_df, _fig = _base_engine.stock_df, _base_engine.fig

        giant_models_p = predict_partial(_stock_name, _stock_df, BIG_DATE)
        giant_models_d = dev(_stock_name, _stock_df, BIG_DATE)

        for giant_model_p, giant_model_d in zip(giant_models_p, giant_models_d):
            if giant_model_p.need_attention():
                fig = go.Figure(_fig)
                giant_model_p.build_graph(fig, enable=True)
                fig.show()

                fig = go.Figure(_fig)
                giant_model_d.build_graph(fig, enable=True)
                fig.show()
