from datetime import datetime
from util import sort_stock_names
from transaction_book import _BUY, _SELL, _CALL, _PUT, _CSP, _CC, TRANSACTION_BOOK, ALL, get_current_position


class Transaction:
    def __init__(self, stock_name, num, fees, raw_txn):
        self.stock_name = stock_name
        self.num = num
        self.fees = fees
        self.raw_txn = raw_txn

    def txn_type(self):
        return self.__class__.__name__

    def total_fees(self):
        return sum(self.fees)

    def filtered_date(self):
        raise NotImplementedError("filtered_date() must be implemented by subclass")


class Option(Transaction):
    def __init__(self, stock_name, expire_date, strike_price, num, fees,
                 open_date, close_date, buy_price, sell_price, raw_txn):
        Transaction.__init__(self, stock_name, num, fees, raw_txn)

        self.expire_date = expire_date
        self.strike_price = strike_price

        self.open_date = open_date
        self.close_date = close_date

        self.buy_price = buy_price
        self.sell_price = sell_price

    def filtered_date(self):
        return self.expire_date

    def unrealized_pnl(self):
        raise NotImplementedError("unrealized_pnl() must be implemented by subclass")

    def realized_pnl(self):
        raise NotImplementedError("realized_pnl() must be implemented by subclass")

    def __str__(self):
        close_date = str(self.close_date)
        sell_price = str(self.sell_price)
        option = f"({self.stock_name:<4} {self.expire_date} {self.strike_price})"

        return f"{self.open_date}  {close_date:<10}  {self.txn_type():<4}  {option:<25}" \
               f"{self.buy_price:>4}  {sell_price:>4}  {self.num:>4}  {self.fees}"


class Long(Option):
    def unrealized_pnl(self):
        if self.sell_price is None:
            return (0.0 - self.buy_price) * self.num * 100
        return 0.0

    def realized_pnl(self):
        if self.sell_price is not None:
            return (self.sell_price - self.buy_price) * self.num * 100
        return 0.0


class Put(Long):
    pass


class Call(Long):
    pass


class Short(Option):
    def unrealized_pnl(self):
        if self.sell_price is None:
            return (self.buy_price - 0.0) * self.num * 100
        return 0.0

    def realized_pnl(self):
        if self.sell_price is not None:
            return (self.buy_price - self.sell_price) * self.num * 100
        return 0.0


class CSP(Short):
    pass


class CC(Short):
    pass


class Stock(Transaction):
    def __init__(self, stock_name, num, fees, txn_date, stock_price, raw_txn):
        Transaction.__init__(self, stock_name, num, fees, raw_txn)

        self.txn_date = txn_date
        self.stock_price = stock_price

    def filtered_date(self):
        return self.txn_date

    def __str__(self):
        stock = f"({self.stock_name:<4} {self.stock_price})"
        return f"{self.txn_date:<22}  {self.txn_type():<4}  {stock:<35}  {self.num:>4}  {self.fees}"


class Buy(Stock):
    pass


class Sell(Stock):
    pass


TXN_TYPE_MAP = {
    _CSP: CSP,
    _CC: CC,
    _PUT: Put,
    _CALL: Call,
    _BUY: Buy,
    _SELL: Sell,
}


def build_transaction(raw_txn) -> Transaction:
    if len(raw_txn) == 8:
        txn_type, open_date, close_date, option, buy_price, sell_price, num, fees = raw_txn
        stock_name, expire_date, strike_price = option

        return TXN_TYPE_MAP[txn_type](stock_name, expire_date, strike_price, num, fees,
                                      open_date, close_date, buy_price, sell_price, raw_txn)

    if len(raw_txn) == 5:
        txn_type, txn_date, stock, num, fees = raw_txn
        stock_name, stock_price = stock

        return TXN_TYPE_MAP[txn_type](stock_name, num, fees, txn_date, stock_price, raw_txn)

    raise ValueError(f"Invalid transaction format: {raw_txn}")


def get_alpha_stock() -> list:
    stock_names = set()
    for raw_txn in TRANSACTION_BOOK:
        txn = build_transaction(raw_txn)
        stock_names.add(txn.stock_name)

    stock_names_sorted = sort_stock_names(stock_names)
    print(f"alpha stocks:\n\t{stock_names_sorted}\n")
    return stock_names_sorted


def get_pnl_and_fees():
    total_pnl = 0.0
    total_fees = 0.0

    realized_pnl = 0.0
    unrealized_pnl = 0.0

    for raw_txn in TRANSACTION_BOOK:
        txn = build_transaction(raw_txn)
        total_fees += txn.total_fees()

        if not isinstance(txn, Option):
            continue

        total_pnl += txn.unrealized_pnl() + txn.realized_pnl()
        unrealized_pnl += txn.unrealized_pnl()
        realized_pnl += txn.realized_pnl()

    print(f"Total pnl: {total_pnl}, Total fees: {total_fees:.2f}, "
          f"Realized pnl: {realized_pnl}, Unrealized pnl: {unrealized_pnl}\n")
    return total_pnl, total_fees


def get_potential_position():
    position = {}

    for raw_txn in TRANSACTION_BOOK:
        txn = build_transaction(raw_txn)

        if (isinstance(txn, CSP) and txn.sell_price is None) \
                or isinstance(txn, Buy):
            position.setdefault(txn.filtered_date(), []).append(raw_txn)

    position = dict(sorted(position.items()))

    print(f"Potential Position:")
    for filtered_date in position:
        print(f"{filtered_date}:")
        for raw_txn in position[filtered_date]:
            print(f"\t{raw_txn}")
    return position


def _filter_transactions_by_date(date: str) -> list:
    transactions = []

    for raw_txn in TRANSACTION_BOOK:
        txn = build_transaction(raw_txn)

        if txn.filtered_date() != date:
            continue

        if isinstance(txn, Option):
            if txn.sell_price is None:
                transactions.append(f'{txn.stock_name} {txn.txn_type()} (_)')
            else:
                transactions.append(f'{txn.stock_name} {txn.txn_type()}')

        if isinstance(txn, Stock):
            transactions.append(f'{txn.stock_name} {txn.txn_type()}')

    if not transactions:
        return []

    current_date = datetime.now().strftime('%Y-%m-%d')
    prefix = '-' if date < current_date else '+'
    print(f"{prefix} {date}: {transactions}")
    return transactions


def list_by_date():
    print("\nlist by date:")
    for filter_date in ['2026-01-09', '2026-01-16', '2026-01-23', '2026-01-30',
                        '2026-02-06', '2026-02-13', '2026-02-20', '2026-02-27',
                        '2026-03-06', '2026-03-13', '2026-03-20', '2026-03-27']:
        _filter_transactions_by_date(filter_date)


def list_by_stock_name() -> dict:
    stock_name_view = {}

    for raw_txn in TRANSACTION_BOOK:
        txn = build_transaction(raw_txn)
        stock_name_view.setdefault(txn.stock_name, []).append(txn)

    for stock_name in ALL:
        if stock_name not in stock_name_view:
            continue
        if stock_name not in get_current_position():
            continue
        print(f"\n{stock_name}:")
        for txn in stock_name_view[stock_name]:
            print(f"\t{txn}")

    return stock_name_view


if __name__ == '__main__':
    get_alpha_stock()

    get_pnl_and_fees()
    get_potential_position()

    list_by_date()
    list_by_stock_name()
