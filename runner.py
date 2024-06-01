from period_analysis import *

STOCK_NAMES_TIER_1 = [
    "META",
    "RIVN",
    "TSLA",
    "BABA",
    "JD",
    "ZM",
    "XPEV",
    "BEKE",
    "MNSO",
    "0700.HK"
    "000300.SS",
]

STOCK_NAMES_TIER_2 = [
    "^IXIC",
    "000001.SS",
    "PDD",
    "COIN",
    "SNAP",
    "BILI",
    "NVDA",
    "EDU",
    "AMD",
    "MRNA",
    "LI",
    "BNTX",
    "BA",
    "CPNG",
    "IQ",
    "TSM",
]

PERIOD = [
    ('2023-05-31', '2024-07-31'),
    ('2023-01-01', '2024-07-31'),
    # ('2022-01-01', '2024-07-31'),
    # ('2021-01-01', '2024-07-31'),
]

for stock_name in STOCK_NAMES_TIER_1:
    stock_data = load_data(stock_name)

    for (start_date, end_date) in PERIOD:
        stock_df = stock_data[(stock_data['Date'] > start_date) & (stock_data['Date'] < end_date)]

        pa = PeriodAnalysis(stock_name, stock_df)
        pa.analyze()
        pa.build_graph()
        pa.fig.show()
