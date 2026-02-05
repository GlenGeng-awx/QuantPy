from datetime import datetime
from util import sort_stock_names
from conf import *

# Transaction Types
CSP = 'CSP'  # Cash Secured Put
CC = 'CC'  # Covered Call
PP = 'PP'  # Protective Put
BUY = 'BUY'  # Buy Stock
SELL = 'SELL'  # Sell Stock

"""
(CC/CSP,   open_date, close_date, (stock_name, expire_date, strike_price), buy_price, sell_price, num, [fees])
(BUY/SELL, txn_date, (stock_name, stock_price), num, [fees])
"""


class Transaction:
    def __init__(self, txn):
        self.transaction = txn
        self.txn_type = txn[0]

        # CSP/CC
        self.stock_name = None
        self.expired_date = None
        self.strike_price = None

        self.open_date = None
        self.close_date = None

        self.buy_price = None
        self.sell_price = None

        self.num = None
        self.fees = None

        # BUY/SELL
        self.txn_date = None
        self.stock_price = None

        if self.txn_type in {CC, CSP}:
            self.open_date, self.close_date, option, self.buy_price, self.sell_price, self.num, self.fees = txn[1:]
            self.stock_name, self.expired_date, self.strike_price = option

        if self.txn_type in {BUY, SELL}:
            self.txn_date, stock, self.num, self.fees = txn[1:]
            self.stock_name, self.stock_price = stock


TRANSACTION_BOOK = [
    # 2025-12-29 ~ 2026-01-02
    (CSP, '2025-12-30', None, (QQQ, '2026-01-30', 600), 5.25, 0.00, 1, [2.51]),
    (CSP, '2025-12-30', None, (GOLD, '2026-01-30', 380), 3.10, 0.00, 1, [2.51]),
    (CSP, '2025-12-30', None, (COIN, '2026-01-23', 230), 9.50, 0.00, 1, [2.51]),  # COIN

    (CSP, '2025-12-31', None, (VOO, '2026-01-30', 612.5), 3.60, 0.00, 1, [2.51]),

    (CSP, '2026-01-02', None, (SLV, '2026-01-09', 60), 0.52, 0.00, 2, [3.03]),
    (CSP, '2026-01-02', None, (ORCL, '2026-01-09', 182.5), 1.07, 0.00, 1, [2.51]),  # ORCL

    # 2026-01-05 ~ 2026-01-09
    (CSP, '2026-01-05', None, (ADBE, '2026-02-06', 320), 6.50, 0.00, 1, [2.51]),  # ADBE
    (CSP, '2026-01-05', None, (ORCL, '2026-02-06', 185), 6.80, 0.00, 1, [2.51]),

    (CSP, '2026-01-06', None, (NFLX, '2026-01-30', 85), 2.06, 0.00, 3, [3.54]),  # NFLX

    (CSP, '2026-01-07', None, (PYPL, '2026-01-30', 57), 0.96, 0.00, 4, [4.66]),  # PYPL

    # 2026-01-12 ~ 2026-01-16
    (CSP, '2026-01-14', '2026-02-04', (TCOM, '2026-02-20', 55), 1.00, 0.60, 2, [3.03, 3.02]),  # TCOM
    (CSP, '2026-01-14', None, (PDD, '2026-02-13', 100), 1.50, None, 1, [2.51]),  # PDD
    (CSP, '2026-01-14', None, (AVGO, '2026-02-06', 315), 5.25, None, 1, [2.51]),  # AVGO

    # 2026-01-19 ~ 2026-01-23
    (CSP, '2026-01-21', '2026-02-04', (TME, '2026-02-20', 16), 0.65, 0.65, 10, [11.66, 11.62]),  # TME

    (CC, '2026-01-23', None, (COIN, '2026-02-06', 240), 2.25, 0.0, 1, [2.51]),

    (BUY, '2026-01-23', (COIN, 230), 100, [0.00]),

    # 2026-01-26 ~ 2026-01-30
    (CSP, '2026-01-26', None, (TTD, '2026-02-20', 33.5), 1.34, None, 6, [7]),  # TTD

    (CSP, '2026-01-28', None, (PDD, '2026-02-13', 100), 1.45, None, 1, [2.51]),

    (CSP, '2026-01-29', None, (QQQ, '2026-02-20', 610), 5.55, None, 1, [2.51]),
    (CSP, '2026-01-29', '2026-02-04', (MSFT, '2026-02-27', 385), 2.50, 2.70, 1, [2.51, 2.50]),  # MSFT

    (CSP, '2026-01-30', '2026-02-04', (GOLD, '2026-02-27', 407), 3.50, 3.50, 1, [2.51, 2.50]),
    (CC, '2026-01-30', None, (PYPL, '2026-02-20', 60), 0.59, None, 4, [4.66]),
    (CC, '2026-01-30', None, (NFLX, '2026-02-20', 90), 0.45, None, 3, [3.54]),

    (BUY, '2026-01-30', (NFLX, 85), 300, [0.00]),
    (BUY, '2026-01-30', (PYPL, 57), 400, [0.00]),

    # 2026-02-02 ~ 2026-02-06
    (CC, '2026-02-03', None, (COIN, '2026-02-20', 230), 1.60, None, 1, [2.51]),
    (CC, '2026-02-03', None, (ADBE, '2026-02-27', 320), 1.50, None, 1, [2.51]),
    (CC, '2026-02-03', None, (ORCL, '2026-02-27', 185), 1.55, None, 1, [2.51]),
    (CSP, '2026-02-03', None, (PYPL, '2026-02-20', 42.5), 1.50, None, 1, [2.51]),

    (CC, '2026-02-04', None, (TTD, '2026-02-27', 35), 0.50, None, 6, [7]),

    (BUY, '2026-02-06', (ADBE, 320), 100, [0.00]),
    (BUY, '2026-02-06', (ORCL, 185), 100, [0.00]),
]


def get_alpha_stock() -> list:
    stock_names = set()
    for transaction in TRANSACTION_BOOK:
        t = Transaction(transaction)
        stock_names.add(t.stock_name)

    stock_names_sorted = sort_stock_names(stock_names)
    print(f"\nalpha stocks: {stock_names_sorted}")
    return stock_names_sorted


def _get_transactions_expired_at(date: str) -> list:
    transactions = []
    current_date = datetime.now().strftime('%Y-%m-%d')

    for transaction in TRANSACTION_BOOK:
        t = Transaction(transaction)

        if t.txn_type in {CC, CSP} and t.expired_date == date:
            transactions.append(f'{t.stock_name} {t.txn_type}')

        if t.txn_type in {BUY, SELL} and t.txn_date == date:
            transactions.append(f'{t.stock_name} {t.txn_type}')

    if not transactions:
        return []

    prefix = '-' if date < current_date else '+'
    print(f"{prefix} expired at {date}: {transactions}")
    return transactions


def list_by_expired_date():
    print("\nlist by expired date:")
    for expired_date in ['2026-01-09', '2026-01-16', '2026-01-23', '2026-01-30',
                         '2026-02-06', '2026-02-13', '2026-02-20', '2026-02-27',
                         '2026-03-06', '2026-03-13', '2026-03-20', '2026-03-27']:
        _get_transactions_expired_at(expired_date)


def list_by_stock_name() -> dict:
    per_stock_view = {}
    for transaction in TRANSACTION_BOOK:
        t = Transaction(transaction)
        per_stock_view.setdefault(t.stock_name, []).append(transaction)

    for stock_name in ALL:
        if stock_name not in per_stock_view:
            continue
        print(f"\n{stock_name}:")
        for transaction in per_stock_view[stock_name]:
            print(f"\t{transaction}")

    return per_stock_view


def get_pnl_and_fees():
    total_pnl = 0.0
    realized_pnl = 0.0
    unrealized_pnl = 0.0
    total_fees = 0.0

    for transaction in TRANSACTION_BOOK:
        t = Transaction(transaction)
        if t.txn_type not in {CC, CSP}:
            continue

        if t.sell_price is None:
            pnl = (t.buy_price - 0.0) * t.num * 100
            total_pnl += pnl
            unrealized_pnl += pnl
        else:
            pnl = (t.buy_price - t.sell_price) * t.num * 100
            total_pnl += pnl
            realized_pnl += pnl

        total_fees += sum(t.fees)

    print(f"\nTotal pnl: {total_pnl}, Total fees: {total_fees}, "
          f"Realized pnl: {realized_pnl}, Unrealized pnl: {unrealized_pnl}")
    return total_pnl, total_fees


def get_potential_position():
    position = {}
    for transaction in TRANSACTION_BOOK:
        t = Transaction(transaction)

        if t.txn_type == CSP and t.sell_price is None:
            position.setdefault(t.expired_date, []).append(transaction)

        if t.txn_type == BUY:
            position.setdefault(t.txn_date, []).append(transaction)

    position = dict(sorted(position.items()))

    print(f"\nPotential Position:")
    for expired_date in position:
        print(f"{expired_date}:")
        for transaction in position[expired_date]:
            print(f"\t{transaction}")
    return position


if __name__ == '__main__':
    get_alpha_stock()

    get_pnl_and_fees()
    get_potential_position()

    list_by_expired_date()
    list_by_stock_name()
