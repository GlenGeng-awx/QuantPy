from datetime import datetime
import json
import pandas as pd

from gringotts.giant_model import GiantModel
from gringotts import (MODE, MASK, RECALL_STEP, FORECAST_STEP, MARGIN, HIT_THRESHOLD, SUCCESSFUL_RATE,
                       FROM_DATE, TO_DATE, TRAIN_FROM_DATE, TRAIN_TO_DATE, PREDICT_FROM_DATE, PREDICT_TO_DATE)

from d2_1_periods import get_train_periods, get_predict_periods, get_predict_partial_period
from d2_2_margins import MARGINS


def calculate_margin(stock_name: str, forecast_step: int) -> float:
    margin = MARGINS[stock_name][str(forecast_step)]

    if forecast_step == 10:
        return min(margin['incr'], margin['decr'], 0.18)
    elif forecast_step == 5:
        return min(margin['incr'], margin['decr'], 0.08)
    elif forecast_step == 3:
        return min(margin['incr'], margin['decr'], 0.03)
    else:
        raise ValueError(f'Unknown forecast_step: {forecast_step}')


def get_train_confs(stock_name: str, stock_df: pd.DataFrame, to_date: str) -> list[dict]:
    train_confs = []
    train_periods = get_train_periods(stock_df, to_date)

    # 400/200/100
    # 10/5/3
    # 80/80/90
    for (train_from_date, train_to_date), forecast_step, successful_rate \
            in zip(train_periods, [10, 5, 3], [80, 80, 90]):
        train_conf = {
            MODE: 'train',
            MASK: 4,

            FROM_DATE: train_from_date,
            TO_DATE: train_to_date,

            RECALL_STEP: 4,
            FORECAST_STEP: forecast_step,

            'evaluators': [
                {
                    MARGIN: calculate_margin(stock_name, forecast_step),
                    HIT_THRESHOLD: 4,
                    SUCCESSFUL_RATE: successful_rate,
                }
            ]
        }
        train_confs.append(train_conf)

    return train_confs


def get_predict_confs(stock_name: str, stock_df: pd.DataFrame, to_date: str) -> list[dict]:
    predict_confs = []

    train_periods = get_train_periods(stock_df, to_date)        # 400/200/100
    predict_periods = get_predict_periods(stock_df, to_date)    # 400/200/100

    for (train_from_date, train_to_date), (predict_from_date, predict_to_date), forecast_step, successful_rate \
            in zip(train_periods, predict_periods, [10, 5, 3], [80, 80, 90]):
        predict_conf = {
            MODE: 'predict',
            FROM_DATE: predict_from_date,
            TO_DATE: predict_to_date,

            TRAIN_FROM_DATE: train_from_date,
            TRAIN_TO_DATE: train_to_date,

            RECALL_STEP: 4,
            FORECAST_STEP: forecast_step,

            MARGIN: calculate_margin(stock_name, forecast_step),
            HIT_THRESHOLD: 4,
            SUCCESSFUL_RATE: successful_rate,
        }
        predict_confs.append(predict_conf)

    return predict_confs


def get_predict_partial_confs(stock_name: str, stock_df: pd.DataFrame, to_date: str) -> list[dict]:
    predict_partial_confs = []

    train_periods = get_train_periods(stock_df, to_date)
    predict_partial_from_period, predict_partial_to_period = get_predict_partial_period(stock_df)

    for (train_from_date, train_to_date), forecast_step, successful_rate \
            in zip(train_periods, [10, 5, 3], [80, 80, 90]):
        predict_partial_conf = {
            MODE: 'predict',
            FROM_DATE: predict_partial_from_period,
            TO_DATE: predict_partial_to_period,

            TRAIN_FROM_DATE: train_from_date,
            TRAIN_TO_DATE: train_to_date,

            RECALL_STEP: 4,
            FORECAST_STEP: forecast_step,

            MARGIN: calculate_margin(stock_name, forecast_step),
            HIT_THRESHOLD: 4,
            SUCCESSFUL_RATE: successful_rate,
        }
        predict_partial_confs.append(predict_partial_conf)

    return predict_partial_confs


def get_dev_confs(stock_name: str, stock_df: pd.DataFrame, to_date: str) -> list[dict]:
    dev_confs = []

    train_periods = get_train_periods(stock_df, to_date)
    predict_partial_from_period, predict_partial_to_period = get_predict_partial_period(stock_df)

    for (train_from_date, _), forecast_step, successful_rate \
            in zip(train_periods, [10, 5, 3], [80, 80, 90]):
        dev_conf = {
            MODE: 'dev',
            FROM_DATE: train_from_date,
            TO_DATE: predict_partial_to_period,

            PREDICT_FROM_DATE: predict_partial_from_period,
            PREDICT_TO_DATE: predict_partial_to_period,

            RECALL_STEP: 4,
            FORECAST_STEP: forecast_step,

            MARGIN: calculate_margin(stock_name, forecast_step),
            HIT_THRESHOLD: 4,
            SUCCESSFUL_RATE: successful_rate,
        }
        dev_confs.append(dev_conf)

    return dev_confs


def run_giant_models(stock_name: str, stock_df: pd.DataFrame, confs: list[dict]) -> list[GiantModel]:
    giant_models = []
    start_time = datetime.now()

    for conf in confs:
        print(json.dumps(conf, indent=4))
        giant_model = GiantModel(stock_df, stock_name, conf)
        giant_model.run()

        giant_models.append(giant_model)

    end_time = datetime.now()
    time_cost = (end_time - start_time).total_seconds()
    print(f'{stock_name} finished at {end_time.time()}, cost {time_cost}s')

    return giant_models


if __name__ == '__main__':
    from conf import *
    from d1_1_preload import preload

    for _stock_name in [SNAP]:
        _base_engine = preload(_stock_name)
        _stock_df = _base_engine.stock_df

        _train_confs = get_train_confs(_stock_name, _stock_df, BIG_DATE)
        print(json.dumps(_train_confs, indent=4))

        _predict_confs = get_predict_confs(_stock_name, _stock_df, BIG_DATE)
        print(json.dumps(_predict_confs, indent=4))
