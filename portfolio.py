from conf import *

# (long/short, call/put, date, strike, num, buy_price, sell_price),
# None if no sell_price yet

Call = 'call'
Put = 'put'
LLong = 'long'
Short = 'short'

P_2025_0801 = {
    NVO: [
        (LLong, Call, '2025-08-01', 71, 2, 1.71, None),

        (Short, Call, '2025-08-01', 74, 2, 0.24, None),
        (Short, Call, '2025-07-18', 71, 2, 0.58, 0.00),
    ],
    KO: [
        (LLong, Put, '2025-08-01', 68, 4, 0.70, 0.24),  # -0.02 x 4 = -0.08

        (Short, Put, '2025-07-25', 68, 4, 0.27, 0.00),
        (Short, Put, '2025-07-18', 68, 4, 0.18, 0.01),
    ],
}

P_2025_0808 = {
    PYPL: [
        (LLong, Call, '2025-08-08', 76, 1, 2.65, None),

        (Short, Call, '2025-08-01', 80, 1, 2.42, None),
        (Short, Call, '2025-07-25', 76, 1, 0.66, 2.42),
    ],
    TSLA: [
        (LLong, Call, '2025-08-08', 350, 1, 10.6, None),  # 2.7

        (Short, Call, '2025-08-01', 355, 1, 0.89, None),
        (Short, Call, '2025-07-25', 350, 1, 5.20, 0.00),
    ],
    BIDU: [
        (LLong, Call, '2025-08-08', 93, 2, 1.68, None),

        (Short, Call, '2025-07-25', 93, 2, 0.68, 0.00),
    ],
    DELL: [
        (LLong, Put, '2025-08-08', 127, 1, 3.25, None),  # 1.06

        (Short, Put, '2025-07-25', 127, 1, 1.13, 0.00),
    ],
    FUTU: [
        (LLong, Put, '2025-08-08', 150, 1, 3.15, None),  # 1.325

        (Short, Put, '2025-07-25', 150, 1, 0.50, 0.00),
    ],
}

P_2025_0815 = {
    HOOD: [
        (LLong, Call, '2025-08-15', 110, 1, 4.08, None),

        (Short, Call, '2025-08-01', 115, 1, 1.38, None),
    ],
    QQQ: [
        (LLong, Call, '2025-08-15', 576, 1, 3.29, None),

        (Short, Call, '2025-08-01', 576, 1, 1.05, None),
    ],
    AAPL: [
        (LLong, Call, '2025-08-15', 225, 2, 2.25, None),

        (Short, Call, '2025-08-01', 225, 2, 1.07, None),
    ],
    TSM: [
        (LLong, Put, '2025-08-15', 227.5, 1, 2.73, None),

        (Short, Put, '2025-08-01', 227.5, 1, 0.98, None),
    ],
    UBER: [
        (LLong, Call, '2025-08-15', 92, 1, 3.45, None),

        (Short, Call, '2025-08-08', 100, 1, 0.85, None),
    ],
}

ACTIVE_PORTFOLIO = [
    P_2025_0801, P_2025_0808, P_2025_0815
]

position = [k for portfolio in ACTIVE_PORTFOLIO for k in portfolio]
