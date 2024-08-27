from datetime import datetime

from conf import *
from base_engine import BaseEngine

from gringotts.trend import Trend
from gringotts.giant_model import calculate_giant_model
from baseline import calculate_baseline, display_baseline


STOCK_NAMES_INDEX = [
    IXIC,
    # SS_000300,
    # SS_000001,
    # GC_F,
]

STOCK_NAMES_TIER_0 = [
    BA,
    FUTU,
    PLTR,
    COIN,
    # TSLA,
    # BNTX,
    # AMD,
    # SNOW,
    # HK_0700,
    # SS_000300,
]

STOCK_NAMES_TIER_1 = [
    PDD,
    # JD,
    # BEKE,
    # HK_0700,
    # NVDA,
    # AMD,
    # BNTX,
    # CPNG,
    # TSM,
    # EBAY,
    # IXIC,
    # SS_000001,
    # TSLA,
    # COIN,
    # XPEV,
    # MRNA,
    # SNOW,
    # IQ,
    # PLTR,
    # RIVN,
    # META,
    # MNSO,
    # ZM,
    # BABA,
    # EDU,
    # BA,
    # BILI,
    # LI,
    # SNAP,
    # FUTU,
]


def default_period():
    current_date = datetime.now()

    date_0y_ago = datetime(current_date.year, 1, 1).strftime('%Y-%m-%d')
    date_1y_ago = datetime(current_date.year - 1, 1, 1).strftime('%Y-%m-%d')
    date_5y_ago = datetime(current_date.year - 5, 1, 1).strftime('%Y-%m-%d')

    current_date = current_date.strftime('%Y-%m-%d')

    return [
        # (date_0y_ago, current_date, '1h'),
        (date_1y_ago, current_date, '1d'),
        # (date_5y_ago, current_date, '1wk'),
    ]


def get_period(_stock_name):
    return default_period()


for stock_name in STOCK_NAMES_TIER_1:
    for (start_date, end_date, interval) in get_period(stock_name):
        de = BaseEngine(stock_name, start_date, end_date, interval)
        de.build_graph(
                       enable_close_price=True,
                       enable_ma=True,
                       enable_min_max=True,
                       # enable_macd=True,
                       # enable_bband=True,
                       enable_bband_pst=(True, 2),
                       enable_rsi=(True, 3),
                       enable_volume_reg=(True, 4),
                       # enable_ema=True,
                       # enable_sr=True,
                       # enable_min_max=True
                       # enable_rsi=True,
                       rows=4,
                       )

        stock_df, fig = de.stock_df, de.fig
        Trend(stock_df).build_graph(fig)

        with open(f'report/{stock_name}', 'w') as fd:
            print(f'handle {stock_name} at time {datetime.now()}')
            # display_baseline(stock_df, fig)

            calculate_baseline(stock_df, fd)
            calculate_giant_model(stock_df, fd)
