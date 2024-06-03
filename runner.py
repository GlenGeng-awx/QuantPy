from period_analysis import *

STOCK_NAMES_INDEX = [
    # "^IXIC",
    # "000300.SS",
    # "000001.SS",
    # "GC=F",
]

STOCK_NAMES_TIER_1 = [
    "MRNA",
    "PDD",
    "COIN",
    # "META",
    # "RIVN",
    # "TSLA",
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

DEFAULT_PERIOD = [
    # ('2023-05-31', '2024-07-31'),
    ('2023-01-01', '2024-07-31'),
    # ('2022-01-01', '2024-07-31'),
    # ('2021-01-01', '2024-07-31'),
    # ('2020-01-01', '2024-07-31'),
    ('2019-01-01', '2024-07-31'),
]

CUSTOMIZED_PERIOD = {
    # "XPEV": [
    #     ('2021-01-01', '2024-07-31'),
    #     ('2020-01-01', '2024-07-31'),
    #     ('2019-01-01', '2024-07-31'),
    # ],
    # "META": [
    #     ('2023-01-01', '2024-07-31'),
    #     ('2021-01-01', '2024-07-31'),
    #     ('2020-01-01', '2024-07-31'),
    #     ('2019-01-01', '2024-07-31'),
    # ],
}

for stock_name in STOCK_NAMES_TIER_1:
    stock_data = load_data(stock_name)

    for (start_date, end_date) in CUSTOMIZED_PERIOD.get(stock_name, DEFAULT_PERIOD):
        stock_df = stock_data[(stock_data['Date'] > start_date) & (stock_data['Date'] < end_date)]

        pa = PeriodAnalysis(stock_name, stock_df)
        pa.analyze()
        pa.build_graph()
        pa.fig.show()
