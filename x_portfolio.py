from conf import *

# (long/short, call/put, date, strike, num, buy_price, sell_price),
# None if no sell_price yet

Call = 'call'
Put = 'put'
LLong = 'long'
Short = 'short'

P_2025_0801 = {  # profit, 41
    NVO: [
        # fail, -178
        (LLong, Call, '2025-08-01', 71, 2, 1.71, 0.00),

        (Short, Call, '2025-08-01', 74, 2, 0.24, 0.00),
        (Short, Call, '2025-07-18', 71, 2, 0.58, 0.00),
    ],
    KO: [
        # neutral, -8
        (LLong, Put, '2025-08-01', 68, 4, 0.70, 0.24),

        (Short, Put, '2025-07-25', 68, 4, 0.27, 0.00),
        (Short, Put, '2025-07-18', 68, 4, 0.18, 0.01),
    ],
    AAPL: [
        # neutral, 0
        (LLong, Call, '2025-08-01', 215, 1, 3.15, 0.00),
        (LLong, Put, '2025-08-01', 210, 1, 3.10, 6.25),
    ],
    COIN: [
        #
        # My mistake, became 15 at midnight.
        #
        # success, 230
        (LLong, Put, '2025-08-01', 325, 1, 0.50, 2.80),
    ],
    HOOD: [
        # neutral, -3
        (LLong, Put, '2025-08-01', 91, 1, 0.53, 0.50),
    ],
}

P_2025_0808 = {
    PYPL: [
        # fail, -199
        (LLong, Call, '2025-08-08', 76, 1, 2.65, 0.00),

        (Short, Call, '2025-08-01', 80, 1, 2.42, 0.00),
        (Short, Call, '2025-07-25', 76, 1, 0.66, 2.42),
    ],
    TSLA: [
        # fail, -271
        (LLong, Call, '2025-08-08', 350, 1, 10.6, 2.01),

        (Short, Call, '2025-08-01', 355, 1, 0.89, 0.21),
        (Short, Call, '2025-07-25', 350, 1, 5.20, 0.00),
    ],
    BIDU: [
        # fail, -50
        (LLong, Call, '2025-08-08', 93, 2, 1.68, 0.75),

        (Short, Call, '2025-07-25', 93, 2, 0.68, 0.00),
    ],
    DELL: [
        # fail, -137
        (LLong, Put, '2025-08-08', 127, 1, 3.25, 0.75),

        (Short, Put, '2025-07-25', 127, 1, 1.13, 0.00),
    ],
    FUTU: [
        # fail, -90
        (LLong, Put, '2025-08-08', 150, 1, 3.15, 1.75),

        (Short, Put, '2025-07-25', 150, 1, 0.50, 0.00),
    ],
    DIS: [
        # success, 0
        (LLong, Call, '2025-08-08', 125, 1, 1.75, 0.00),
        (LLong, Put, '2025-08-08', 115, 1, 1.60, 3.35),
    ],
    NVO: [
        # success, -24
        (LLong, Call, '2025-08-08', 53, 1, 1.24, 0.00),
        (LLong, Put, '2025-08-08', 48, 1, 0.64, 1.64),
    ],
    AAPL: [
        #
        # My mistake, became 10 at midnight, become 15 next day.
        #
        # success, 251
        (LLong, Call, '2025-08-08', 205, 1, 2.50, 5.01),
    ],
}

P_2025_0815 = {
    HOOD: [
        # success, 70
        (LLong, Call, '2025-08-15', 110, 1, 4.08, 5.40),

        (Short, Call, '2025-08-01', 115, 1, 1.38, 2.00),
    ],
    QQQ: [
        # success, 101
        (LLong, Call, '2025-08-15', 576, 1, 3.29, 4.63),

        (Short, Call, '2025-08-01', 576, 1, 1.05, 1.38),
    ],
    AAPL: [
        # fail, -36
        (LLong, Call, '2025-08-15', 225, 2, 2.25, 1.56),

        (Short, Call, '2025-08-01', 225, 2, 1.07, 0.56),
    ],
    TSM: [
        # fail, -45
        (LLong, Put, '2025-08-15', 227.5, 1, 2.73, 1.44),

        (Short, Put, '2025-08-01', 227.5, 1, 0.98, 0.14),
    ],
    UBER: [
        # fail, -105
        (LLong, Call, '2025-08-15', 92, 1, 3.45, 1.89),

        (Short, Call, '2025-08-08', 100, 1, 0.85, 0.34),
    ],
    BA: [
        # success, ??
        (LLong, Call, '2025-08-15', 240, 1, 2.25, None),
        (LLong, Put, '2025-08-15', 220, 1, 1.75, 6.00),
    ],
    TME: [
        (LLong, Call, '2025-08-15', 22, 1, 0.77, None),
        (LLong, Put, '2025-08-15', 22, 1, 1.03, None),
    ],
}

P_2025_0822 = {
    KWEB: [
        (LLong, Call, '2025-08-22', 35.5, 1, 1.05, None),
        (LLong, Put, '2025-08-22', 35.5, 1, 0.97, None),
    ],
    QCOM: [
        (LLong, Call, '2025-08-22', 150, 1, 3.70, None),
        (LLong, Put, '2025-08-22', 145, 1, 2.74, None),
    ],
    BAC: [
        (LLong, Call, '2025-08-22', 45.5, 1, 1.29, None),
        (LLong, Put, '2025-08-22', 45.5, 1, 0.81, None),
    ],
    PINS: [
        (LLong, Call, '2025-08-22', 40.5, 1, 1.70, None),
        (LLong, Put, '2025-08-22', 36.5, 1, 1.56, None),
    ],
    XPEV: [
        (LLong, Call, '2025-08-22', 19.0, 1, 1.15, None),
        (LLong, Put, '2025-08-22', 19.0, 1, 1.02, None),
    ],
    MS: [
        (LLong, Call, '2025-08-22', 142, 1, 2.64, None),
        (LLong, Put, '2025-08-22', 137, 1, 1.34, None),
    ],
}

ACTIVE_POSITIONS = [
    P_2025_0801, P_2025_0808, P_2025_0815, P_2025_0822,
]


def get_portfolio() -> list:
    portfolio = []
    for active_position in ACTIVE_POSITIONS:
        for stock_name in active_position:
            records = active_position[stock_name]
            for record in records:
                if record[6] is None and stock_name not in portfolio:
                    portfolio.append(stock_name)
    return portfolio
