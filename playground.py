from datetime import datetime
from multiprocessing import Process

from conf import *
from base_engine import BaseEngine

from gringotts import stock_confs, index_confs
from gringotts.giant_model import GiantModel
import features

INDEX_NAMES = [
    IXIC,
    SS_000300,
    SS_000001,
    # GC_F,
]

STOCK_NAMES_TIER_0 = [
    # BABA,
    # IQ,
    # AMD,
    # PFE,
    # NIO,
    NVDA,
    # RIVN,
    # XPEV,
    # EDU,
]

STOCK_NAMES_TIER_1 = [
    # TSLA,
    # HK_0700,
    # BILI,
    # PDD,
    # COIN,
    # PLTR,
    # SNOW,
    # MRNA,
    # MNSO,
    # BA,
    # FUTU,
    # CPNG,
    # BNTX,
    # JD,
    # BEKE,
    # TSM,
    # EBAY,
    # META,
    # ZM,
    # LI,
    # SNAP,
    # TTD,
    # YY,
    # MCD,
    # GILD,
    # TCOM,
    # MRK,
    # ADBE,
    # DIS,
    # TME,
    # GS,
    # SE,
    # ERIC,
    # UBER,
    # INTC,
    # MS,
    # OKTA,
    # CFLT,
    # QCOM,
    # ETSY,
    # SHOP,
    # GTLB,
    # PINS,
    # SQ,
]


def default_period():
    current_date = datetime.now()

    date_1y_ago = datetime(current_date.year - 1, 1, 1).strftime('%Y-%m-%d')
    current_date = current_date.strftime('%Y-%m-%d')

    return date_1y_ago, current_date, '1d'


def handle_task(stock_name, conf, start_date, end_date, interval):
    be = BaseEngine(stock_name, start_date, end_date, interval)

    be.build_graph(
        enable_close_price=False,
        # enable_ma=True,
        # enable_ema=True,
        # enable_bband=True,
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

    stock_df, fig = be.stock_df, be.fig

    features.calculate_feature(stock_df)
    features.plot_feature(stock_df, fig)

    if conf is not None:
        giant_model = GiantModel(stock_df, stock_name, conf, 'train')
        # giant_model = GiantModel(stock_df, stock_name, conf, 'predict')
        giant_model.run()
        giant_model.build_graph(fig, enable=True)

    fig.show()


if __name__ == '__main__':
    start_date, end_date, interval = default_period()

    for stock_name in STOCK_NAMES_TIER_0:
        handle_task(stock_name, None, start_date, end_date, interval)

        start_time = datetime.now()

        procs = []
        for conf in stock_confs:
            p = Process(target=handle_task, args=(stock_name, conf, start_date, end_date, interval))
            p.start()
            procs.append(p)

        for p in procs:
            p.join()

        end_time = datetime.now()
        time_cost = (end_time - start_time).total_seconds()
        print(f'{stock_name} finished at {end_time.time()}, cost {time_cost}s')

    # for stock_name in INDEX_NAMES:
    #     handle_task(stock_name, None, start_date, end_date, interval)
    #
    #     procs = []
    #     for conf in index_confs:
    #         p = Process(target=handle_task, args=(stock_name, conf, start_date, end_date, interval))
    #         p.start()
    #         procs.append(p)
    #
    #     for p in procs:
    #         p.join()
