from datetime import datetime
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

    def abbr(self):
        raise NotImplementedError("abbr() must be implemented by subclass")


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
               f"{self.buy_price:>5}  {sell_price:>5}  {self.num:>4}  {self.fees}"

    def abbr(self):
        # '-' for open position, 'x' for closed position, ' ' for expired position
        if self.sell_price is None:
            flag = '-'
        else:
            if self.close_date is not None:
                flag = 'x'
            else:
                flag = ' '
        return f"{self.stock_name:<4}  {self.txn_type():<4} {self.strike_price:<5} {flag}"


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
        return f"{self.txn_date:<22}  {self.txn_type():<4}  {stock:<37}  {self.num:>4}  {self.fees}"

    def abbr(self):
        return f"{self.stock_name:<4}  {self.txn_type():<4} {self.stock_price:<5}"


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

TXN_NAME_MAP = {
    CSP: _CSP,
    CC: _CC,
    Put: _PUT,
    Call: _CALL,
    Buy: _BUY,
    Sell: _SELL,
}


class Position:
    def __init__(self, transactions: list):
        self.transactions = transactions

        # 1. total fees
        self.total_fees = sum(txn.total_fees() for txn in transactions)

        # 2. avg_price
        self.buy = [txn for txn in transactions if isinstance(txn, Buy)]
        self.sell = [txn for txn in transactions if isinstance(txn, Sell)]

        self.num = sum(txn.num for txn in self.buy) - sum(txn.num for txn in self.sell)
        self.outflow = sum(txn.stock_price * txn.num for txn in self.buy)
        self.inflow = sum(txn.stock_price * txn.num for txn in self.sell)
        self.avg_price = (self.outflow - self.inflow) / self.num if self.num != 0 else 0.0

        # 3. option pnl and real_price
        self.option = [txn for txn in transactions if isinstance(txn, Option)]

        self.realized_pnl = sum(txn.realized_pnl() for txn in self.option)
        self.unrealized_pnl = sum(txn.unrealized_pnl() for txn in self.option)
        self.real_price = self.avg_price - self.realized_pnl / self.num if self.num != 0 else 0.0

    def log(self, full=False):
        if self.num == 0:
            return
        print(f"\nPosition for {self.transactions[0].stock_name}:")
        print(f"\tNum: {self.num}, Avg Price: {self.avg_price:.2f}, Real Price: {self.real_price:.2f}")
        print(f"\tRealized PnL: {self.realized_pnl:.2f}, Unrealized PnL: {self.unrealized_pnl:.2f}")
        print(f"\tTotal Fees: {self.total_fees:.2f}")

        if not full:
            return
        print(f"\tTransactions:")
        for txn in self.transactions:
            print(f"\t\t{txn}")


def build_transaction(raw_txn) -> Transaction:
    if isinstance(raw_txn, Transaction):
        return raw_txn

    # Option
    if len(raw_txn) == 8:
        txn_type, open_date, close_date, option, buy_price, sell_price, num, fees = raw_txn
        stock_name, expire_date, strike_price = option

        return TXN_TYPE_MAP[txn_type](stock_name, expire_date, strike_price, num, fees,
                                      open_date, close_date, buy_price, sell_price, raw_txn)
    # Stock
    if len(raw_txn) == 5:
        txn_type, txn_date, stock, num, fees = raw_txn
        stock_name, stock_price = stock

        return TXN_TYPE_MAP[txn_type](stock_name, num, fees, txn_date, stock_price, raw_txn)

    raise ValueError(f"Invalid transaction format: {raw_txn}")


def get_pnl_and_fees(transactions: list):
    transactions = [build_transaction(txn) for txn in transactions]
    options = [txn for txn in transactions if isinstance(txn, Option)]

    unrealized_pnl = sum(txn.unrealized_pnl() for txn in options)
    realized_pnl = sum(txn.realized_pnl() for txn in options)
    total_pnl = unrealized_pnl + realized_pnl
    total_fees = sum(txn.total_fees() for txn in transactions)

    print(f"\n\t\tTotal pnl: {total_pnl:.2f}, Total fees: {total_fees:.2f}, "
          f"Realized pnl: {realized_pnl:.2f}, Unrealized pnl: {unrealized_pnl:.2f}")


def get_open_txn(txn_type):
    print(f"\n---------------------\nOpen {TXN_NAME_MAP[txn_type]}\n---------------------")
    date_map = {}
    for raw_txn in TRANSACTION_BOOK:
        txn = build_transaction(raw_txn)
        if isinstance(txn, txn_type) and txn.sell_price is None:
            date_map.setdefault(txn.filtered_date(), []).append(txn)
    for date in sorted(date_map.keys()):
        print(f"\n{date}:")
        for txn in date_map[date]:
            print(f"\t{txn}")
        get_pnl_and_fees(date_map[date])
    return date_map


def list_by_date(full: bool = False):
    print("\nlist by date\n------------")
    # 1. group transactions by date
    date_map = {}
    for raw_txn in TRANSACTION_BOOK:
        txn = build_transaction(raw_txn)
        date_map.setdefault(txn.filtered_date(), []).append(txn)
    # 2. sort by date
    for date in sorted(date_map.keys()):
        transactions = date_map[date]
        transactions.sort(key=lambda x: x.stock_name)
        current_date = datetime.now().strftime('%Y-%m-%d')
        prefix = '-' if date < current_date else '+'
        if not full and prefix == '-':
            continue
        print(f"\n{prefix} {date}:")
        for txn in transactions:
            print(f"\t{txn.abbr()}")
        get_pnl_and_fees(transactions)


def list_by_stock_name():
    print("\nlist by stock name\n------------------")
    stock_name_map = {}
    for raw_txn in TRANSACTION_BOOK:
        txn = build_transaction(raw_txn)
        stock_name_map.setdefault(txn.stock_name, []).append(txn)
    for stock_name in ALL:
        if stock_name in stock_name_map:
            Position(stock_name_map[stock_name]).log(True)


if __name__ == '__main__':
    get_pnl_and_fees(TRANSACTION_BOOK)

    get_open_txn(CSP)
    get_open_txn(Call)
    get_open_txn(CC)
    get_open_txn(Put)

    list_by_date(full=False)
    list_by_stock_name()
