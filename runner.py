from period_analysis import *

STOCK_NAMES = [
    "^IXIC",
    "META",
    "MNSO",
    "TSLA",
    "RIVN",
    "ZM",
    "XPEV",
    "PDD",
    "COIN",
    "SNAP",
    "BILI",
    "NVDA",
    "EDU",
    "AMD",
    "BEKE",
    "MRNA",
    "BABA",
    "LI",
    "BNTX",
    "JD",
    "BA",
    "CPNG"
]

PERIOD = [
    ('2023-05-31', '2024-05-31'),
    ('2023-01-01', '2024-05-31'),
    ('2022-01-01', '2024-05-31'),
    ('2021-01-01', '2024-05-31'),
]

for stock_name in STOCK_NAMES:
    stock_data = load_data(stock_name)

    for (start_date, end_date) in PERIOD:
        stock_df = stock_data[(stock_data['Date'] > start_date) & (stock_data['Date'] < end_date)]

        pa = PeriodAnalysis(stock_name, stock_df)
        pa.analyze()
        pa.build_graph()
        pa.fig.show()
