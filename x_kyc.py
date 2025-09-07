from conf import *

# (long/short, call/put, date, strike, num, buy_price, sell_price),
# (long/short, call/put, date, strike, num, buy_price, sell_price, txn_date),
# None if no sell_price yet

Call = 'call'
Put = 'put'
LLong = 'long'
Short = 'short'

# profit, 41
P_2025_0801 = {
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
        # should wait, became 15 at midnight, 9.5 finally.
        # success, 230
        (LLong, Put, '2025-08-01', 325, 1, 0.50, 2.80),
    ],
    HOOD: [
        # neutral, -3
        (LLong, Put, '2025-08-01', 91, 1, 0.53, 0.50),
    ],
}

# loss, -520
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
        # success, 251
        # should wait, became 10 at midnight, 15 next day, and 24 finally.
        (LLong, Call, '2025-08-08', 205, 1, 2.50, 5.01),
    ],
}

# profit, 170
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
        # success, 250
        (LLong, Call, '2025-08-15', 240, 1, 2.25, 0.50),
        (LLong, Put, '2025-08-15', 220, 1, 1.75, 6.00),
    ],
    TME: [
        # fail, -65
        # should wait, become 3.9 in next few days.
        (LLong, Call, '2025-08-15', 22, 1, 0.77, 1.15),
        (LLong, Put, '2025-08-15', 22, 1, 1.03, 0.00),
    ],
}

# loss, -406
P_2025_0822 = {
    KWEB: [
        # fail, -107
        # should wait, became 2.95 finally
        (LLong, Call, '2025-08-22', 35.5, 1, 1.05, 0.95),
        (LLong, Put, '2025-08-22', 35.5, 1, 0.97, 0.0),
    ],
    QCOM: [
        # fail, -444
        # should wait, became 9.5 finally
        (LLong, Call, '2025-08-22', 150, 1, 3.70, 2.00),
        (LLong, Put, '2025-08-22', 145, 1, 2.74, 0.0),
    ],
    BAC: [
        # fail, -80
        # should wait, became 4.05 finally
        (LLong, Call, '2025-08-22', 45.5, 1, 1.29, 1.30),
        (LLong, Put, '2025-08-22', 45.5, 1, 0.81, 0.0),
    ],
    PINS: [
        # fail, -116
        (LLong, Call, '2025-08-22', 40.5, 1, 1.70, 0.00),
        (LLong, Put, '2025-08-22', 36.5, 1, 1.56, 2.10),
    ],
    XPEV: [
        # success, 89
        # should wait, became 5.05 finally
        (LLong, Call, '2025-08-22', 19.0, 1, 1.15, 2.55),
        (LLong, Put, '2025-08-22', 19.0, 1, 1.02, 0.51),
    ],
    MS: [
        # success, 252
        (LLong, Call, '2025-08-22', 142, 1, 2.64, 6.50),
        (LLong, Put, '2025-08-22', 137, 1, 1.34, 0.0),
    ],
}

# loss, -834
P_2025_0829 = {
    UBER: [
        # success, 21
        (LLong, Call, '2025-08-29', 92, 1, 2.49, 2.70, '2025-08-12'),
    ],
    XYZ: [
        # success, 45
        (LLong, Call, '2025-08-29', 79, 1, 1.25, 1.70, '2025-08-13'),
    ],
    TSLA: [
        # fail, -245
        (LLong, Call, '2025-08-29', 365, 1, 2.45, 0.0, '2025-08-15'),
    ],
    PDD: [
        # fail, -77
        (LLong, Call, '2025-08-29', 134, 1, 0.77, 0.0, '2025-08-25'),
    ],
    BA: [
        # fail, -238
        (LLong, Put, '2025-08-29', 220, 1, 2.38, 0.0, '2025-08-11'),
    ],
    NVO: [
        # fail, -140
        (LLong, Put, '2025-08-29', 50, 1, 1.40, 0.0, '2025-08-13'),
    ],
    DIS: [
        # fail, -200
        (LLong, Put, '2025-08-29', 116, 1, 2.00, 0.0, '2025-08-14'),
    ],
}

# profit, 265
P_2025_0905 = {
    ORCL: [
        # fail, -220
        (LLong, Call, '2025-09-05', 257.5, 1, 2.20, 0.00, '2025-08-19'),
    ],
    TSM: [
        # fail, -120
        (LLong, Call, '2025-09-05', 240, 1, 2.20, 1.00, '2025-08-20'),
    ],
    PLTR: [
        # fail, -210
        (LLong, Call, '2025-09-05', 165, 1, 2.10, 0.00, '2025-08-20'),
    ],
    EBAY: [
        # success, 900
        (LLong, Put, '2025-09-05', 98, 2, 1.50, 6.00, '2025-08-18'),

        # fail, -85
        (LLong, Put, '2025-09-05', 92, 1, 1.48, 0.25, '2025-08-29'),
        (Short, Put, '2025-09-05', 88, 1, 0.48, 0.10, '2025-09-02'),
    ],
}

P_2025_0912 = {
    OKTA: [
        (LLong, Call, '2025-09-12', 99, 1, 1.25, None, '2025-08-27'),
    ],
    GOOG: [
        (LLong, Put, '2025-09-12', 200, 1, 2.75, None, '2025-08-26'),
        (Short, Put, '2025-09-12', 190, 1, 0.80, None, '2025-09-02'),
    ],
}

P_2025_0919 = {
    JPM: [
        # fail, -85
        (LLong, Call, '2025-09-19', 310, 1, 2.50, 1.65, '2025-08-28'),
    ],
    COIN: [
        (LLong, Call, '2025-09-19', 355, 1, 3.30, None, '2025-08-28'),
        (Short, Call, '2025-09-19', 360, 1, 1.10, None, '2025-09-04'),
    ],
    LI: [
        (LLong, Call, '2025-09-19', 23, 2, 1.28, None, '2025-08-29'),
    ],
    SNAP: [
        (LLong, Call, '2025-09-19', 7.0, 7, 0.3, None, '2025-08-29'),
    ],
    VISA: [
        (LLong, Put, '2025-09-19', 345, 1, 4.15, None, '2025-09-03'),
        (Short, Put, '2025-09-19', 335, 1, 1.75, None, '2025-09-03'),
    ],
}

P_2025_0926 = {
    JPM: [
        (LLong, Put, '2025-09-26', 295, 1, 3.66, None, '2025-09-04'),
        (Short, Put, '2025-09-26', 285, 1, 1.64, None, '2025-09-04'),
    ],
    MSFT: [
        (LLong, Call, '2025-09-26', 515, 1, 2.10, None, '2025-09-05'),
        (LLong, Call, '2025-09-26', 515, 1, 4.00, None, '2025-09-05'),
        (Short, Call, '2025-09-26', 525, 1, 1.80, None, '2025-09-05'),
    ],
}

CLOSED_POSITIONS = [
    P_2025_0829,
    P_2025_0905,
]

ACTIVE_POSITIONS = [
    P_2025_0912, P_2025_0919, P_2025_0926
]


def get_portfolio() -> list:
    portfolio = [QQQ, SS_000300, SS_000001]
    for active_position in ACTIVE_POSITIONS:
        for stock_name in active_position:
            records = active_position[stock_name]
            for record in records:
                if record[6] is None and stock_name not in portfolio:
                    portfolio.append(stock_name)
    return portfolio
