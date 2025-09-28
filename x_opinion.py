from conf import *

Up = 'up'
Down = 'down'

OPINION = {
    KWEB: [
        ('2025-09-26', Down),
    ],
    AAPL: [
        ('2025-09-26', Up),
    ],
    GOOG: [
        ('2025-09-26', Down),
    ],
    AMZN: [
        ('2025-09-26', Up),
    ],
    META: [
        ('2025-09-26', Up),
    ],
    TSLA: [
        ('2025-09-26', Up),
    ],
    AVGO: [
        ('2025-09-26', Down),
    ],
    LLY: [
        ('2025-09-26', Up),
    ],
    JPM: [
        ('2025-09-26', Down),
    ],
    VISA: [
        ('2025-09-26', Up),
    ],
    ORCL: [
        ('2025-09-26', Down),
    ],
    ASML: [
        ('2025-09-26', Down),
    ],
    XOM: [
        ('2025-09-26', Down),
    ],
    JNJ: [
        ('2025-09-26', Down),
    ],
    PG: [
        ('2025-09-26', Up),
    ],
    KO: [
        ('2025-09-26', Up),
    ],
    BABA: [
        ('2025-09-26', Down),
    ],
    AMD: [
        ('2025-09-26', Up),
    ],
    GS: [
        ('2025-09-26', Down),
    ],
    QCOM: [
        ('2025-09-26', Down),
    ],
    PFE: [
        ('2025-09-26', Up),
    ],
    GILD: [
        ('2025-09-26', Down),
    ],
    SHOP: [
        ('2025-09-26', Down),
    ],
    SPOT: [
        ('2025-09-26', Up),
    ],
    INTC: [
        ('2025-09-26', Down),
    ],
    HOOD: [
        ('2025-09-26', Down),
    ],
    PYPL: [
        ('2025-09-26', Up),
    ],
    COIN: [
        ('2025-09-26', Up),
    ],
    NU: [
        ('2025-09-26', Down),
    ],
    CPNG: [
        ('2025-09-26', Down),
    ],
    TTD: [
        ('2025-09-26', Up),
    ],
    TME: [
        ('2025-09-26', Up),
    ],
    BIDU: [
        ('2025-09-26', Up),
    ],
    HPQ: [
        ('2025-09-26', Up),
    ],
    MRNA: [
        ('2025-09-26', Up),
    ],
    OKTA: [
        ('2025-09-26', Up),
    ],
    AFRM: [
        ('2025-09-26', Up),
    ],
    FUTU: [
        ('2025-09-26', Down),
    ],
    LI: [
        ('2025-09-26', Up),
    ],
    NIO: [
        ('2025-09-26', Down),
    ],
    BILI: [
        ('2025-09-26', Down),
    ],
}


def get_opinion_at(date: str):
    results = []
    for stock_name, opinions in OPINION.items():
        for date_, opinion in opinions:
            if date_ == date:
                results.append(stock_name)
    return results


if __name__ == '__main__':
    print(get_opinion_at('2025-09-26'))
