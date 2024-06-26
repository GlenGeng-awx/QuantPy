from analysis_engine import AnalysisEngine
from display_engine import DisplayEngine

from conf import *

STOCK_NAMES_INDEX = [
    IXIC,
    # SS_000300,
    SS_000001,
    # GC_F,
]

STOCK_NAMES_TIER_0 = [
    IXIC,
    SS_000001,
    TSLA,
    COIN,
    XPEV,
    MRNA,
    SNOW,
    IQ,
    JD,
    PLTR,
    BEKE,
    RIVN,
    META,
    MNSO,
    ZM,
    BABA,
    EDU,
    BA,
    BILI,
    LI,
    PDD,
    SNAP,
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
]

for stock_name in STOCK_NAMES_TIER_0:
    for (start_date, end_date, interval) in get_period(stock_name):
        ae = AnalysisEngine(stock_name, start_date, end_date, interval)
        ae.analyze()

        de = DisplayEngine(ae)
        de.build_graph()

        de.display()
