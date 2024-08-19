from datetime import datetime

from base_engine import BaseEngine
from trading.position_analysis import PositionAnalysis

from conf import *

STOCK_NAMES_INDEX = [
    # IXIC,
    # SS_000300,
    # SS_000001,
    GC_F,
]

STOCK_NAMES_TIER_0 = [
    # IXIC,
    # SS_000001,
    # SS_000300,
    # TSLA,
    # META,
    # HK_0700,
    MRNA,
    # BILI,
    # XPEV,
    # CPNG,
    # SNOW,
    # IQ,
    # JD,
    # BEKE,
    # RIVN,
    # MNSO,
    # ZM,
    # BABA,
    # BA,
    # PDD,
    # FUTU,
    # COIN,
]

STOCK_NAMES_TIER_1 = [
    PDD,
    JD,
    BEKE,
    HK_0700,
    NVDA,
    AMD,
    BNTX,
    CPNG,
    TSM,
    EBAY,
    IXIC,
    SS_000001,
    TSLA,
    COIN,
    XPEV,
    MRNA,
    SNOW,
    IQ,
    PLTR,
    RIVN,
    META,
    MNSO,
    ZM,
    BABA,
    EDU,
    BA,
    BILI,
    LI,
    SNAP,
]


def default_period():
    current_date = datetime.now()

    date_0y_ago = datetime(current_date.year, 1, 1).strftime('%Y-%m-%d')
    date_1y_ago = datetime(current_date.year - 1, 1, 1).strftime('%Y-%m-%d')
    date_5y_ago = datetime(current_date.year - 5, 1, 1).strftime('%Y-%m-%d')

    current_date = current_date.strftime('%Y-%m-%d')

    return [
        (date_0y_ago, current_date, '1h'),
        (date_1y_ago, current_date, '1d'),
        (date_5y_ago, current_date, '1wk'),
    ]


def get_period(_stock_name):
    return default_period()


for stock_name in STOCK_NAMES_TIER_0:
    # position
    PositionAnalysis(stock_name, '2024-01-01', datetime.now().strftime('%Y-%m-%d')).analyze()

    for (start_date, end_date, interval) in get_period(stock_name):
        be = BaseEngine(stock_name, start_date, end_date, interval)

        if interval == '1d':
            # candle stick + volume raw
            be.build_graph(enable_candlestick=True, enable_volume_raw=(True, 2))
            be.display()

            # close + volume reg
            be.build_graph(enable_close_price=True, enable_volume_reg=(True, 2))
            be.display()

            # close + volume reg + sr + min/max + ratio
            be.build_graph(enable_close_price=True,
                           enable_sr=True, enable_min_max=True, enable_ratio=True,
                           enable_volume_reg=(True, 2))
            be.display()

            # close + volume reg + wave 3rd + ratio
            be.build_graph(enable_close_price=True, enable_wave=True, enable_ratio=True,
                           enable_volume_reg=(True, 2))
            be.display()

            # close + volume reg + box 3rd
            be.build_graph(enable_close_price=True, enable_box=True,
                           enable_volume_reg=(True, 2))
            be.display()

            # close + rsi + ema 10/20
            be.build_graph(enable_close_price=True, enable_ema=True,
                           enable_rsi=(True, 2))
            be.display()

            # close + rsi + bb
            be.build_graph(enable_close_price=True, enable_bband=True,
                           enable_bband_pst=(True, 2))
            be.display()

            # close + macd
            be.build_graph(enable_close_price=True, enable_macd=(True, 2))
            be.display()

            # misc 1
            be.build_graph(enable_close_price=True,
                           enable_volume_reg=(True, 2),
                           enable_bband_pst=(True, 3),
                           rows=3
                           )
            be.display()

            # misc 2
            be.build_graph(enable_close_price=True,
                           enable_volume_reg=(True, 2),
                           enable_bband_pst=(True, 3),
                           enable_rsi=(True, 4),
                           rows=4,
                           )
            be.display()

        elif interval == '1h':
            be.build_graph(enable_close_price=True, enable_sr=True, enable_min_max=True,
                           enable_rsi=(True, 2))
            be.display()

        elif interval == '1wk':
            # close + volume reg + wave 3rd + ratio
            be.build_graph(enable_close_price=True, enable_wave=True, enable_ratio=True,
                           enable_volume_reg=(True, 2))
            be.display()
