from datetime import datetime, timedelta
from period_util import load_data
from period_analysis import PeriodAnalysis
from period_display import PeriodDisplay
from period_forecast import PeriodForecast
from period_conf import *

STOCK_NAMES_INDEX = [
    # IXIC,
    # SS_000300,
    SS_000001,
    # GC_F,
]

STOCK_NAMES_TIER_0 = [
    IXIC,
    MRNA,
    PDD,
    TSLA,
    BABA,
    HK_0700,
    JD,
    BEKE,
]

STOCK_NAMES_TIER_1 = [
    # MRNA,
    PDD,
    # COIN,
    # META,
    # RIVN,
    # TSLA,
    # BABA,
    # JD,
    # ZM,
    # XPEV,
    # BEKE,
    # MNSO,
    # HK_0700,
    # IQ,
    # PLTR,
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


for stock_name in STOCK_NAMES_TIER_1:
    stock_data = load_data(stock_name)

    for (start_date, end_date) in get_period(stock_name):
        condition = (stock_data['Date'] > start_date) & (stock_data['Date'] < end_date)
        stock_df = stock_data[condition]

        # step 1: analyze
        pa = PeriodAnalysis(stock_name, stock_df)
        pa.analyze()

        # step 2: display
        pd = PeriodDisplay(pa)
        pd.build_graph()

        # step 3: forecast
        PeriodForecast(pd).forecast()

        pd.fig.show()

