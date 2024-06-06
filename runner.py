from datetime import datetime, timedelta
from period_analysis import *
from period_display import *

STOCK_NAMES_INDEX = [
    # "^IXIC",
    # "000300.SS",
    # "000001.SS",
    # "GC=F",
]

STOCK_NAMES_TIER_1 = [
    # "MRNA",
    # "PDD",
    # "COIN",
    # "META",
    # "RIVN",
    "TSLA",
    # "BABA",
    # "JD",
    # "ZM",
    # "XPEV",
    # "BEKE",
    # "MNSO",
    # "0700.HK"
]

STOCK_NAMES_TIER_2 = [
    "SNAP",
    "BILI",
    "NVDA",
    "EDU",
    "AMD",
    "LI",
    "BNTX",
    "BA",
    "CPNG",
    "IQ",
    "TSM",
    "EBAY",
]


def default_period():
    current_date = datetime.now()
    date_300_days_ago = current_date - timedelta(days=365 * 1.5)
    date_600_days_ago = current_date - timedelta(days=365 * 3)
    date_900_days_ago = current_date - timedelta(days=365 * 4.5)

    return [
        (date_300_days_ago.strftime('%Y-%m-%d'), current_date.strftime('%Y-%m-%d')),
        (date_600_days_ago.strftime('%Y-%m-%d'), current_date.strftime('%Y-%m-%d')),
        (date_900_days_ago.strftime('%Y-%m-%d'), current_date.strftime('%Y-%m-%d')),
    ]


for stock_name in STOCK_NAMES_TIER_1:
    stock_data = load_data(stock_name)

    for (start_date, end_date) in default_period():
        condition = (stock_data['Date'] > start_date) & (stock_data['Date'] < end_date)
        stock_df = stock_data[condition]

        pa = PeriodAnalysis(stock_name, stock_df)
        pa.analyze()

        pd = PeriodDisplay(pa)
        pd.build_graph()
        pd.fig.show()

