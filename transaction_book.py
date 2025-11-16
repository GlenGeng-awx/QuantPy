import datetime

from conf import *

# Each transaction: (transaction_date, expiration_date, stock_name, list of strike_prices)
TRANSACTION_BOOK = [
    ('2025-10-20', '2025-11-07', MS, [155, 160, 165, 170]),
    ('2025-10-20', '2025-11-07', KWEB, [36, 38.5, 41, 43.5]),

    ('2025-11-04', '2025-11-21', AMZN, [240, 245, 257.5, 262.5]),

    ('2025-11-06', '2025-11-28', AAPL, [255, 260, 275, 280]),
    ('2025-11-10', '2025-11-28', GOOG, [265, 270, 290, 295]),
    ('2025-11-11', '2025-11-28', COIN, [292.5, 297.5, 337.5, 342.5]),
    ('2025-11-12', '2025-11-28', SEA, [135, 140, 150, 155]),
    ('2025-11-13', '2025-11-28', SPOT, [615, 620, 670, 675]),
]


def get_unexpired_stock_names():
    stock_names = []

    today = datetime.date.today()
    for _, expire_date, stock_name, _ in TRANSACTION_BOOK:
        expire_date = datetime.datetime.strptime(expire_date, '%Y-%m-%d').date()
        if today <= expire_date:
            stock_names.append(stock_name)

    return stock_names


if __name__ == '__main__':
    stock_names_ = get_unexpired_stock_names()
    print("unexpired transactions:", stock_names_)
