from datetime import datetime
from multiprocessing import Process

import pandas as pd
import plotly.graph_objects as go

from conf import *
from base_engine import BaseEngine
from util import shrink_date_str

from gringotts import (train_confs, predict_confs, dev_confs, MODE, FROM_DATE, TO_DATE,
                       TRAIN_FROM_DATE, TRAIN_TO_DATE, PREDICT_FROM_DATE, PREDICT_TO_DATE)
from gringotts.giant_model import GiantModel
import features

INDEX_NAMES = [
    IXIC,
    SS_000300,
    # SS_000001,
    # GC_F,
]

STOCK_NAMES_TIER_0 = [
    AMD,
    ZM,
    TSM,
    BA,
    SQ,
    PINS,
    IQ,
    RIVN,
    CPNG,
    ADBE,
]

STOCK_NAMES_TIER_1 = [
    NIO,
    TSLA,
    PLTR,
    MRNA,
    PFE,
    COIN,
    META,
    EBAY,
    LI,
    PDD,
    BILI,
    FUTU,
    BABA,
    HK_0700,
    NVDA,
    XPEV,
    EDU,
    SNOW,
    MNSO,
    BNTX,
    JD,
    BEKE,
    SNAP,
    TTD,
    YY,
    MCD,
    GILD,
    TCOM,
    MRK,
    DIS,
    TME,
    GS,
    SEA,
    ERIC,
    UBER,
    INTC,
    MS,
    OKTA,
    CFLT,
    QCOM,
    ETSY,
    SHOP,
    GTLB,
]


def default_period() -> tuple:
    current_date = datetime.now()

    date_1y_ago = datetime(current_date.year - 1, 1, 1).strftime('%Y-%m-%d')
    current_date = current_date.strftime('%Y-%m-%d')

    return date_1y_ago, current_date, '1d'


def prepare(stock_name: str) -> BaseEngine:
    base_engine = BaseEngine(stock_name, *default_period())

    base_engine.build_graph(
        enable_close_price=False,
        enable_min_max=True,
        enable_wave=True,
        enable_sr=True,
        enable_line=True,
        enable_volume_reg=(True, 3),
        enable_bband_pst=(True, 4),
        enable_rsi=(True, 5),
        enable_macd=(True, 6),
        rows=6,
    )

    stock_df, fig = base_engine.stock_df, base_engine.fig

    features.calculate_feature(stock_df)
    features.plot_feature(stock_df, fig)

    return base_engine


# return 400/200/100 period
# in the format of[train_from_date, train_to_date, predict_from_date, predict_to_date]
def get_periods(stock_df: pd.DataFrame) -> list[list[str]]:
    idx_of_last_friday = None

    # for idx in reversed(stock_df.index[:-6]):
    for idx in reversed(stock_df.index[:-11]):
        date_str = stock_df.loc[idx]['Date']
        date = datetime.strptime(shrink_date_str(date_str), '%Y-%m-%d')

        if date.weekday() == 4:
            idx_of_last_friday = idx
            break

    periods = []

    for sz in [400, 200, 100]:
        train_from_idx = idx_of_last_friday - sz
        train_to_idx = idx_of_last_friday

        predict_from_idx = idx_of_last_friday + 1
        predict_to_idx = stock_df.index[-1]

        period = [shrink_date_str(stock_df.loc[i]['Date'])
                  for i in (train_from_idx, train_to_idx, predict_from_idx, predict_to_idx)]

        periods.append(period)

    return periods


def handle_task(stock_name: str, stock_df: pd.DataFrame, fig: go.Figure, conf: dict):
    print('ATTENTION!!!', conf)

    fig = go.Figure(fig)
    giant_model = GiantModel(stock_df, stock_name, conf)
    giant_model.run()
    giant_model.build_graph(fig, enable=True)

    if conf[MODE] == 'train':
        fig.show()

    if conf[MODE] == 'predict' and giant_model.need_attention():
        fig.show()

    if conf[MODE] == 'dev' and giant_model.need_attention():
        fig.show()


def dispatch(stock_name: str, stock_df: pd.DataFrame, fig: go.Figure, case: int):
    start_time = datetime.now()
    periods = get_periods(stock_df)

    if case == 1:
        for conf, (train_from_date, train_to_date, _, _) in zip(train_confs, periods):
            period = {
                FROM_DATE: train_from_date,
                TO_DATE: train_to_date,
            }

            conf = conf.copy()
            conf.update(period)
            handle_task(stock_name, stock_df, fig, conf)

    if case == 2 or case == 3:
        for confs, (train_from_date, train_to_date, predict_from_date, predict_to_date) in zip(predict_confs, periods):
            for conf in confs:
                if case == 2:
                    period = {
                        FROM_DATE: train_from_date,
                        TO_DATE: predict_to_date,

                        TRAIN_FROM_DATE: train_from_date,
                        TRAIN_TO_DATE: train_to_date,
                    }
                elif case == 3:
                    period = {
                        FROM_DATE: predict_from_date,
                        TO_DATE: predict_to_date,

                        TRAIN_FROM_DATE: train_from_date,
                        TRAIN_TO_DATE: train_to_date,
                    }
                else:
                    raise ValueError(f'invalid case: {case}')

                conf = conf.copy()
                conf.update(period)
                handle_task(stock_name, stock_df, fig, conf)

    if case == 4:
        for confs, (train_from_date, _, predict_from_date, predict_to_date) in zip(dev_confs, periods):
            for conf in confs:
                period = {
                    FROM_DATE: train_from_date,
                    TO_DATE: predict_to_date,

                    PREDICT_FROM_DATE: predict_from_date,
                    PREDICT_TO_DATE: predict_to_date,
                }

                conf = conf.copy()
                conf.update(period)
                handle_task(stock_name, stock_df, fig, conf)

    end_time = datetime.now()
    time_cost = (end_time - start_time).total_seconds()
    print(f'{stock_name} finished at {end_time.time()}, cost {time_cost}s')


if __name__ == '__main__':
    # 1: train
    # 2: predict full
    # 3: predict partial
    # 4: dev
    for stock_name in INDEX_NAMES:
        base_engine = prepare(stock_name)
        stock_df, fig = base_engine.stock_df, base_engine.fig
        fig.show()

        # train
        dispatch(stock_name, stock_df, fig, 1)

        # predict full
        dispatch(stock_name, stock_df, fig, 2)

        # predict partial
        dispatch(stock_name, stock_df, fig, 3)

        # dev
        dispatch(stock_name, stock_df, fig, 4)
