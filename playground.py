from datetime import datetime
from multiprocessing import Process
import pandas as pd

from conf import *
from base_engine import BaseEngine
from util import shrink_date_str

from gringotts import (train_confs, predict_confs, dev_confs, MODE, FROM_DATE, TO_DATE,
                       TRAIN_FROM_DATE, TRAIN_TO_DATE, PREDICT_FROM_DATE, PREDICT_TO_DATE)
from gringotts.giant_model import GiantModel
import features

INDEX_NAMES = [
    IXIC,
    # SS_000300,
    # SS_000001,
    # GC_F,
]

STOCK_NAMES_TIER_0 = [
    PLTR,
    COIN,
    NIO,
    RIVN,
]

STOCK_NAMES_TIER_1 = [
    IQ,
    PINS,
    MRNA,
    META,
    EBAY,
    CPNG,
    LI,
    PDD,
    BILI,
    FUTU,
    TSLA,
    PFE,
    BABA,
    HK_0700,
    AMD,
    NVDA,
    XPEV,
    EDU,
    SNOW,
    MNSO,
    BA,
    BNTX,
    JD,
    BEKE,
    TSM,
    ZM,
    SNAP,
    TTD,
    YY,
    MCD,
    GILD,
    TCOM,
    MRK,
    ADBE,
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
    SQ,
]


def default_period():
    current_date = datetime.now()

    date_1y_ago = datetime(current_date.year - 1, 1, 1).strftime('%Y-%m-%d')
    current_date = current_date.strftime('%Y-%m-%d')

    return date_1y_ago, current_date, '1d'


def handle_task(stock_name: str, conf: dict, start_date, end_date, interval):
    base_engine = BaseEngine(stock_name, start_date, end_date, interval)

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

    if conf[MODE] == 'probe':
        fig.show()
        return

    print('ATTENTION!!!', conf)

    giant_model = GiantModel(stock_df, stock_name, conf)
    giant_model.run()
    giant_model.build_graph(fig, enable=True)

    # if conf[MODE] == 'train':
    #     fig.show()

    # if conf[MODE] == 'predict' and giant_model.need_attention():
    if conf[MODE] == 'predict':
        fig.show()

    if conf[MODE] == 'dev':
        fig.show()


def dispatch(stock_name: str, case: int, period: dict = None):
    start_time = datetime.now()

    if case == 0:
        handle_task(stock_name, {MODE: 'probe'}, *default_period())

    if case == 1:
        for conf in train_confs:
            conf = conf.copy()
            conf.update(period)
            handle_task(stock_name, conf, *default_period())

    if case == 2:
        for confs in predict_confs:
            for conf in confs:
                conf = conf.copy()
                conf.update(period)
                handle_task(stock_name, conf, *default_period())

    if case == 3:
        for confs in dev_confs:
            for conf in confs:
                conf = conf.copy()
                conf.update(period)
                handle_task(stock_name, conf, *default_period())

    end_time = datetime.now()
    time_cost = (end_time - start_time).total_seconds()
    print(f'{stock_name} finished at {end_time.time()}, cost {time_cost}s')


# return last n period: [train_from_date, train_to_date, predict_from_date, predict_to_date]
def get_periods(stock_df: pd.DataFrame, n) -> list[list[str]]:
    fridays = []

    for idx in reversed(stock_df.index[:-6]):
        date_str = stock_df.loc[idx]['Date']
        date = datetime.strptime(shrink_date_str(date_str), '%Y-%m-%d')

        if date.weekday() == 4:
            fridays.append(idx)

        if len(fridays) == n:
            break

    periods = []

    for idx in fridays:
        train_from_idx = idx - 200
        train_to_idx = idx

        predict_from_idx = idx + 6
        predict_to_idx = min(idx + 10, stock_df.index[-1])

        period = [shrink_date_str(stock_df.loc[i]['Date'])
                  for i in (train_from_idx, train_to_idx, predict_from_idx, predict_to_idx)]

        periods.append(period)

    return list(reversed(periods))


if __name__ == '__main__':
    # 0: probe
    # 1: train
    # 2: predict
    # 3: dev
    for stock_name in STOCK_NAMES_TIER_1:
        # dispatch(stock_name, 0)
        # continue

        base_engine = BaseEngine(stock_name, *default_period())
        stock_df = base_engine.stock_df

        for train_from_date, train_to_date, predict_from_date, predict_to_date in get_periods(stock_df, 1):
            # train
            period = {
                FROM_DATE: train_from_date,
                TO_DATE: train_to_date,
            }
            dispatch(stock_name, 1, period)

            # predict
            period = {
                FROM_DATE: train_from_date,
                TO_DATE: train_to_date,

                TRAIN_FROM_DATE: train_from_date,
                TRAIN_TO_DATE: train_to_date,
            }
            dispatch(stock_name, 2, period)

            # predict
            period = {
                FROM_DATE: predict_from_date,
                TO_DATE: predict_to_date,

                TRAIN_FROM_DATE: train_from_date,
                TRAIN_TO_DATE: train_to_date,
            }
            dispatch(stock_name, 2, period)

            # dev
            period = {
                FROM_DATE: train_from_date,
                TO_DATE: predict_to_date,

                PREDICT_FROM_DATE: predict_from_date,
                PREDICT_TO_DATE: predict_to_date,
            }
            dispatch(stock_name, 3, period)
