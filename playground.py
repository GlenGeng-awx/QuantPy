from datetime import datetime
from multiprocessing import Process

from conf import *
from base_engine import BaseEngine

from gringotts.trend import Trend
from gringotts.giant_model import calculate_giant_model, display_giant_model
from baseline import calculate_baseline, display_baseline


STOCK_NAMES_INDEX = [
    IXIC,
    # SS_000300,
    # SS_000001,
    # GC_F,
]

STOCK_NAMES_TIER_0 = [
    TSLA,
    BILI,
    HK_0700,
    IXIC,
    BABA,
    PDD,
    COIN,
    BA,
    FUTU,
    CPNG,
    PLTR,
    BNTX,
    AMD,
    SNOW,
    SS_000300,
    JD,
    BEKE,
    NVDA,
    IQ,
    SS_000001,
]

STOCK_NAMES_TIER_1 = [
    TSM,
    EBAY,
    IXIC,
    XPEV,
    MRNA,
    RIVN,
    META,
    MNSO,
    ZM,
    EDU,
    LI,
    SNAP,
]


def default_period():
    current_date = datetime.now()

    date_1y_ago = datetime(current_date.year - 1, 1, 1).strftime('%Y-%m-%d')
    current_date = current_date.strftime('%Y-%m-%d')

    return date_1y_ago, current_date, '1d'


def train_task(stock_name, start_date, end_date, interval):
    be = BaseEngine(stock_name, start_date, end_date, interval)

    stock_df = be.stock_df
    Trend(stock_df)

    print(f'start handle {stock_name} at time {datetime.now()}')

    with open(f'report/{stock_name}', 'w') as fd:
        calculate_baseline(stock_df, fd)
        calculate_giant_model(stock_df, stock_name, fd)

    print(f'finish handle {stock_name} at time {datetime.now()}')


def display_task(stock_name, start_date, end_date, interval):
    be = BaseEngine(stock_name, start_date, end_date, interval)

    be.build_graph(
        enable_close_price=False,
        # enable_ma=True,
        enable_min_max=True,
        enable_wave=True,
        enable_sr=True,
        enable_line=True,
        # enable_macd=True,
        # enable_bband=True,
        enable_bband_pst=(True, 3),
        enable_rsi=(True, 4),
        enable_volume_reg=(True, 2),
        # enable_ema=True,
        # enable_rsi=True,
        rows=4,
    )

    stock_df, fig = be.stock_df, be.fig
    # Trend(stock_df).build_graph(fig)
    Trend(stock_df)

    with open(f'report/{stock_name}', 'r') as fd:
        display_baseline(stock_df, fig)
        # display_giant_model(stock_df, fd, fig)


if __name__ == '__main__':
    start_date, end_date, interval = default_period()

    # procs = []
    #
    # for stock_name in STOCK_NAMES_TIER_0:
    #     p = Process(target=train_task, args=(stock_name, start_date, end_date, interval))
    #     p.start()
    #     procs.append(p)
    #
    # for p in procs:
    #     p.join()

    for stock_name in STOCK_NAMES_TIER_0:
        display_task(stock_name, start_date, end_date, interval)
