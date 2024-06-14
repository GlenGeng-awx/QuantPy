from analysis_engine import AnalysisEngine
from display_engine import DisplayEngine

from util import load_data
from conf import *

STOCK_NAMES_INDEX = [
    IXIC,
    # SS_000300,
    # SS_000001,
    # GC_F,
]

STOCK_NAMES_TIER_0 = [
    # IXIC,
    # MRNA,
    # PDD,
    TSLA,
    # BABA,
    # HK_0700,
    # JD,
    # BEKE,
    # XPEV,
    # IQ,
    # META,
    # COIN,
    # RIVN,
    # PLTR,
    # SNOW,
]

STOCK_NAMES_TIER_1 = [
    PDD,

    BABA,
    JD,
    ZM,
    BEKE,
    MNSO,
    HK_0700,
]

STOCK_NAMES_TIER_2 = [
    SNAP,
    BILI,
    NVDA,
    EDU,
    AMD,
    LI,
    BNTX,
    BA,
    CPNG,
    TSM,
    EBAY,
]

for stock_name in STOCK_NAMES_TIER_0:
    stock_data = load_data(stock_name)

    for (start_date, end_date) in get_period(stock_name):
        ae = AnalysisEngine(stock_name, start_date, end_date)
        ae.analyze()

        de = DisplayEngine(ae, {})
        de.build_graph()
        de.display()
