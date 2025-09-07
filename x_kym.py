from conf import *

# 急5 缓7 平15
# 暴涨之前总有震仓，暴跌之前总有拉升

# 顺势而为 or 调整结束 - 逆短顺长
FOLLOW_TREND = "follow_trend"

# 趋势反转 or 调整开始 - 逆长顺短
REVERSE_TREND = "reverse_trend"

KYM_0711 = {
    FOLLOW_TREND: [
        (LI, '2025-07-07'),
        (TSLA, '2025-07-08'),
        (PLTR, '2025-07-10'),
        (HK_0700, '2025-07-11'),
    ],
    REVERSE_TREND: [
        (BABA, '2025-07-09'),
    ],
}

KYM_0718 = {
    FOLLOW_TREND: [
        (HK_0700, '2025-07-14'),
        (PDD, '2025-07-14'),
        (SHOP, '2025-07-15'),
        (XYZ, '2025-07-15'),
    ],
    REVERSE_TREND: [
        (ASML, '2025-07-14'),
        (SEA, '2025-07-17'),
        (COIN, '2025-07-18'),
    ],
}

KYM_0725 = {
    FOLLOW_TREND: [
        (EBAY, '2025-07-21'),
        (CFLT, '2025-07-24'),
        (META, '2025-07-25'),
        (LLY, '2025-07-25'),
        (NVO, '2025-07-25'),
    ],
    REVERSE_TREND: [
        (XPEV, '2025-07-21'),
        (COIN, '2025-07-21'),
        (SNOW, '2025-07-25'),
    ],
}

KYM_0801 = {
    FOLLOW_TREND: [
        (LLY, '2025-07-28'),
        (META, '2025-07-29'),
        (SPOT, '2025-07-29'),
        (EBAY, '2025-07-30'),
        (PFE, '2025-07-30'),
        (KWEB, '2025-08-01'),
        (AAPL, '2025-08-01'),
        (TSLA, '2025-08-01'),
        (TME, '2025-08-01'),
        (HPQ, '2025-08-01'),
        (MNSO, '2025-08-01')
    ],
    REVERSE_TREND: [
        (SNOW, '2025-07-28'),
        (QCOM, '2025-07-29'),
    ],
}

KYM_0808 = {
    FOLLOW_TREND: [
        (SS_000001, '2025-08-08'),
        (MNSO, '2025-08-04'),
        (NIO, '2025-08-04'),
        (TME, '2025-08-04'),
        (BAC, '2025-08-06'),
        (QCOM, '2025-08-06'),
        (PFE, '2025-08-06'),
        (XYZ, '2025-08-08'),
        (TCOM, '2025-08-08'),
    ],
    REVERSE_TREND: [
        (ZM, '2025-08-05'),
        (LLY, '2025-08-08'),
    ],
}

KYM_0815 = {
    FOLLOW_TREND: [
        (SNOW, '2025-08-11'),
        (XYZ, '2025-08-11'),
        (TCOM, '2025-08-12'),
    ],
    REVERSE_TREND: [
        (LLY, '2025-08-11'),
        (GILD, '2025-08-11'),
        (NVO, '2025-08-12'),
        (AMD, '2025-08-14'),
        (DELL, '2025-08-15'),
        (ORCL, '2025-08-15'),
        (EBAY, '2025-08-15'),
        (ZM, '2025-08-15'),
    ],
}

KYM_0822 = {
    FOLLOW_TREND: [
        (HPQ, '2025-08-20'),
        (AVGO, '2025-08-20'),
        (GOOG, '2025-08-21'),
        (BABA, '2025-08-21'),
    ],
    REVERSE_TREND: [
        (ORCL, '2025-08-18'),
        (PLTR, '2025-08-18'),
        (DELL, '2025-08-18'),
        (ZM, '2025-08-19'),
        (XPEV, '2025-08-22'),
    ],
}

KYM_ALL = [
    KYM_0711, KYM_0718, KYM_0725,
    KYM_0801, KYM_0808, KYM_0815, KYM_0822,
]


def get_kym_dates(stock_name) -> list:
    dates = []
    for kym_by_week in KYM_ALL:
        for category in [FOLLOW_TREND, REVERSE_TREND]:
            for _stock_name, date in kym_by_week[category]:
                if _stock_name == stock_name:
                    dates.append(date)
    return dates
