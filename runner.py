from datetime import datetime

from analysis_engine import AnalysisEngine
from display_engine import DisplayEngine
from trading.position_analysis import PositionAnalysis

from conf import *

STOCK_NAMES_INDEX = [
    IXIC,
    SS_000300,
    SS_000001,
    GC_F,
]

STOCK_NAMES_TIER_0 = [
    # XPEV,
    # IXIC,
    # SS_000001,
    # SS_000300,
    # TSLA,
    # MRNA,
    CPNG,
    # SNOW,
    # IQ,
    # JD,
    # BEKE,
    # RIVN,
    # META,
    # MNSO,
    # ZM,
    # BABA,
    # BA,
    # BILI,
    # PDD,
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
        # (date_5y_ago, current_date, '1wk'),
    ]


def get_period(_stock_name):
    return default_period()


for stock_name in STOCK_NAMES_TIER_0:
    # position
    PositionAnalysis(stock_name, '2024-01-01', datetime.now().strftime('%Y-%m-%d')).analyze()

    for (start_date, end_date, interval) in get_period(stock_name):
        ae = AnalysisEngine(stock_name, start_date, end_date, interval)
        ae.analyze()

        de = DisplayEngine(ae)

        if interval == '1d':
            # candle stick + volume raw
            de.build_graph(enable_candlestick=True, enable_volume_raw=True)
            de.display()

            # close + volume reg
            de.build_graph(enable_close_price=True, enable_volume_reg=True)
            de.display()

            # close + volume reg + sr + min/max
            de.build_graph(enable_close_price=True, enable_volume_reg=True, enable_sr=True, enable_min_max=True)
            de.display()

            # close + rsi + wave 3rd
            de.build_graph(enable_close_price=True, enable_rsi=True, enable_wave=True)
            de.display()

            # close + volume reg + box 3rd
            de.build_graph(enable_close_price=True, enable_volume_reg=True, enable_box=True)
            de.display()

            # close + rsi + ema 10/20
            de.build_graph(enable_close_price=True, enable_rsi=True, enable_ema=True)
            de.display()

            # close + rsi + bb
            de.build_graph(enable_close_price=True, enable_rsi=True, enable_bband=True)
            de.display()

            # close + macd
            de.build_graph(enable_close_price=True, enable_macd=True)
            de.display()

        elif interval == '1h':
            de.build_graph(enable_close_price=True, enable_macd=True, enable_sr=True, enable_min_max=True)
            de.display()
