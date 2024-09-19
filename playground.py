from datetime import datetime
from multiprocessing import Process

from conf import *
from base_engine import BaseEngine

from gringotts import train_confs, predict_confs, MODE
from gringotts.giant_model import GiantModel
import features

INDEX_NAMES = [
    IXIC,
    SS_000300,
    SS_000001,
    # GC_F,
]

STOCK_NAMES_TIER_0 = [
    NIO,
    IQ,
    # PINS,
    # MRNA,
    # RIVN,
    # META,
    # EBAY,
    # CPNG,
    # PLTR,
    # LI,
    # PDD,
    # BILI,
    # FUTU,
    TSLA,
]

STOCK_NAMES_TIER_1 = [
    PFE,
    BABA,
    HK_0700,
    AMD,
    NVDA,
    XPEV,
    EDU,
    COIN,
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
        # fig.show()
        return

    giant_model = GiantModel(stock_df, stock_name, conf)
    giant_model.run()
    giant_model.build_graph(fig, enable=True)

    if conf[MODE] == 'train':
        fig.show()

    if conf[MODE] == 'predict' and giant_model.need_attention():
        fig.show()

    # fig.show()


def handle_stock(stock_name: str, case: int):
    start_time = datetime.now()
    start_date, end_date, interval = default_period()

    if case == 0:
        handle_task(stock_name, {MODE: 'probe'}, start_date, end_date, interval)

    if case == 1:
        procs = []

        for conf in train_confs:
            p = Process(target=handle_task,
                        args=(stock_name, conf, start_date, end_date, interval))
            p.start()
            procs.append(p)

        for p in procs:
            p.join()

    if case == 2:
        procs = []

        for confs in predict_confs:
            for conf in confs:
                p = Process(target=handle_task,
                            args=(stock_name, conf, start_date, end_date, interval))
                p.start()
                procs.append(p)

        for p in procs:
            p.join()

    end_time = datetime.now()
    time_cost = (end_time - start_time).total_seconds()
    print(f'{stock_name} finished at {end_time.time()}, cost {time_cost}s')


if __name__ == '__main__':

    # 0: probe
    # 1: train
    # 2: predict
    for stock_name in STOCK_NAMES_TIER_0:
        handle_stock(stock_name, 2)
