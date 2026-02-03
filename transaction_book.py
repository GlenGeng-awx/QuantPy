from datetime import datetime
from util import sort_stock_names
from conf import *

# Transaction Types
CSP = 'CSP'  # Cash Secured Put
CC = 'CC'  # Covered Call
BUY = 'BUY'  # Buy Stock
SELL = 'SELL'  # Sell Stock

"""
(CC/CSP,   txn_date, expire_date, stock_name, strike_price, buy_price, sell_price, [fees])
  or
(CC/CSP,   txn_date, expire_date, stock_name, strike_price, buy_price, sell_price, num, [fees])
  or
(BUY/SELL, txn_date, None,        stock_name, stock_price,  num,       [fees])
"""
TRANSACTION_BOOK = [
    # 2025-12-29 ~ 2026-01-02
    (CSP, '2025-12-30', '2026-01-30', QQQ, 600, 5.25, 0.00, [2.51]),
    (CSP, '2025-12-30', '2026-01-30', GOLD, 380, 3.10, 0.00, [2.51]),
    (CSP, '2025-12-30', '2026-01-23', COIN, 230, 9.50, 0.00, [2.51]),  # COIN
    (CSP, '2025-12-31', '2026-01-30', VOO, 612.5, 3.60, 0.00, [2.51]),
    (CSP, '2026-01-02', '2026-01-09', SLV, 60, 0.52, 0.00, 2, [3.03]),
    (CSP, '2026-01-02', '2026-01-09', ORCL, 182.5, 1.07, 0.00, [2.51]),  # ORCL

    # 2026-01-05 ~ 2026-01-09
    (CSP, '2026-01-05', '2026-02-06', ADBE, 320, 6.50, None, [2.51]),  # ADBE
    (CSP, '2026-01-05', '2026-02-06', ORCL, 185, 6.80, None, [2.51]),
    (CSP, '2026-01-06', '2026-01-30', NFLX, 85, 2.06, 0.00, 3, [3.54]),  # NFLX
    (CSP, '2026-01-07', '2026-01-30', PYPL, 57, 0.96, 0.00, 4, [4.66]),  # PYPL

    # 2026-01-12 ~ 2026-01-16
    (CSP, '2026-01-14', '2026-02-20', TCOM, 55, 1.00, None, 2, [3.03]),  # TCOM
    (CSP, '2026-01-14', '2026-02-13', PDD, 100, 1.50, None, [2.51]),  # PDD
    (CSP, '2026-01-14', '2026-02-06', AVGO, 315, 5.25, None, [2.51]),  # AVGO

    # 2026-01-19 ~ 2026-01-23
    (CSP, '2026-01-21', '2026-02-20', TME, 16, 0.65, None, 10, [11.66]),  # TME
    (CC, '2026-01-23', '2026-02-06', COIN, 240, 2.25, None, [2.51]),
    (BUY, '2026-01-23', COIN, 230, 100, [0.00]),

    # 2026-01-26 ~ 2026-01-30
    (CSP, '2026-01-26', '2026-02-20', TTD, 33.5, 1.34, None, 6, [7]),  # TTD
    (CSP, '2026-01-28', '2026-02-13', PDD, 100, 1.45, None, [2.51]),
    (CSP, '2026-01-29', '2026-02-20', QQQ, 610, 5.55, None, [2.51]),
    (CSP, '2026-01-29', '2026-02-27', MSFT, 385, 2.50, None, [2.51]),  # MSFT
    (CSP, '2026-01-30', '2026-02-27', GOLD, 407, 3.50, None, [2.51]),
    (CC, '2026-01-30', '2026-02-20', PYPL, 60, 0.59, None, 4, [4.66]),
    (CC, '2026-01-30', '2026-02-20', NFLX, 90, 0.45, None, 3, [3.54]),
    (BUY, '2026-01-30', NFLX, 85, 300, [0.00]),
    (BUY, '2026-01-30', PYPL, 57, 400, [0.00]),

    # 2026-02-02 ~ 2026-02-06
]


def get_alpha_stock() -> list:
    stock_names = set()
    for transaction in TRANSACTION_BOOK:
        txn_type = transaction[0]
        if txn_type not in {CC, CSP}:
            continue

        stock_name = transaction[3]
        stock_names.add(stock_name)

    stock_names_sorted = sort_stock_names(stock_names)
    print(f"\nalpha stocks: {stock_names_sorted}")
    return stock_names_sorted


def get_transactions_expired_at(date: str) -> list:
    transactions = []
    current_date = datetime.now().strftime('%Y-%m-%d')

    for transaction in TRANSACTION_BOOK:
        txn_type = transaction[0]

        if txn_type in {CC, CSP}:
            expire_date, stock_name = transaction[2], transaction[3]
            if expire_date == date:
                transactions.append(f'{stock_name} {txn_type}')

        if txn_type in {BUY, SELL}:
            txn_date, stock_name = transaction[1], transaction[3]
            if txn_date == date:
                transactions.append(f'{stock_name} {txn_type}')

    if not transactions:
        return []

    prefix = '-' if date < current_date else '+'
    print(f"{prefix} expired at {date}: {transactions}")
    return transactions


def get_per_stock_view() -> dict:
    per_stock_view = {}
    for transaction in TRANSACTION_BOOK:
        stock_name = transaction[3]
        per_stock_view.setdefault(stock_name, []).append(transaction)

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
        txn_type = transaction[0]
        if txn_type not in {CC, CSP}:
            continue

        num = 1
        if len(transaction) == 9:  # num is not 1
            num = transaction[7]

        buy_price, sell_price = transaction[5], transaction[6]
        if sell_price is None:
            sell_price = 0.0
            pnl = (buy_price - sell_price) * num * 100
            total_pnl += pnl
            unrealized_pnl += pnl
        else:
            pnl = (buy_price - sell_price) * num * 100
            total_pnl += pnl
            realized_pnl += pnl

        fees = transaction[-1]
        total_fees += sum(fees)

    print(f"\nTotal pnl: {total_pnl}, Total fees: {total_fees}, "
          f"Realized pnl: {realized_pnl}, Unrealized pnl: {unrealized_pnl}")
    return total_pnl, total_fees


if __name__ == '__main__':
    for expired_date in ['2026-01-09', '2026-01-16', '2026-01-23', '2026-01-30',
                         '2026-02-06', '2026-02-13', '2026-02-20', '2026-02-27', ]:
        get_transactions_expired_at(expired_date)

    get_alpha_stock()
    get_per_stock_view()
    get_pnl_and_fees()
