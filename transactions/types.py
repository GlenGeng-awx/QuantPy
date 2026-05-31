from collections import namedtuple

BUY = 'buy'
SELL = 'sell'

CALL = 'call'
PUT = 'put'

OPEN = 'open'
CLOSE = 'close'
EXPIRED = 'expired'
ASSIGNED = 'assigned'
EXERCISED = 'exercised'

StockEntry = namedtuple('StockEntry', ['date', 'side', 'price', 'num', 'fee'])
OptionEntry = namedtuple('OptionEntry', ['date', 'side', 'status', 'price', 'num', 'fee'])


# (stock,)
class StockContract:

    def __init__(self, stock_name):
        self.stock_name = stock_name
        self.entries = []

    def add(self, date, side, price, num, fee):
        self.entries.append(StockEntry(date, side, price, num, fee))

    @property
    def num(self):
        buy = sum(e.num for e in self.entries if e.side == BUY)
        sell = sum(e.num for e in self.entries if e.side == SELL)
        return buy - sell

    @property
    def avg_price(self):
        if self.num == 0:
            return 0.0
        outflow = sum(e.price * e.num for e in self.entries if e.side == BUY)
        inflow = sum(e.price * e.num for e in self.entries if e.side == SELL)
        return (outflow - inflow) / self.num

    @property
    def pnl(self):
        """realized PnL per sell event for tax reporting: [(date, num, avg_price, sell_price, pnl)]"""
        avg_price = 0.0
        num = 0
        details = []

        for e in self.entries:
            if e.side == BUY:
                avg_price = (avg_price * num + e.price * e.num) / (num + e.num)
                num += e.num
            else:
                pnl = (e.price - avg_price) * e.num
                details.append((e.date, e.num, avg_price, e.price, pnl))
                num -= e.num

        return details

    @property
    def total_fees(self):
        return sum(e.fee for e in self.entries)

    def __repr__(self):
        return f"Stock: {self.num} shares @ {self.avg_price:.2f}"


# (stock, CALL/PUT, expire, strike)
class OptionContract:

    def __init__(self, stock_name, cp, expire, strike):
        self.stock_name = stock_name
        self.cp = cp
        self.expire = expire
        self.strike = strike
        self.entries = []

    def add(self, date, side, status, price, num, fee):
        self.entries.append(OptionEntry(date, side, status, price, num, fee))

    @property
    def strategy(self):
        return strategy_name(self.cp, self.entries[0].side)

    @property
    def closed(self):
        return self.entries and self.num == 0

    @property
    def num(self):
        open_side = self.entries[0].side
        opened = sum(e.num for e in self.entries if e.side == open_side)
        closed = sum(e.num for e in self.entries if e.side != open_side)
        return opened - closed

    @property
    def pnl(self):
        """(realized, unrealized) PnL in USD, using moving average cost"""
        open_side = self.entries[0].side
        sign = 1 if open_side == SELL else -1

        avg_price = 0.0
        num = 0
        realized = 0.0

        for e in self.entries:
            if e.side == open_side:
                avg_price = (avg_price * num + e.price * e.num) / (num + e.num)
                num += e.num
            else:
                realized += sign * (avg_price - e.price) * e.num * 100
                num -= e.num

        unrealized = sign * avg_price * num * 100
        return realized, unrealized

    @property
    def total_fees(self):
        return sum(e.fee for e in self.entries)

    def __repr__(self):
        r, u = self.pnl
        return f"{self.strategy:<12} {self.expire} {self.strike:>7} x{self.num}  realized={r:>8.2f}  unrealized={u:>8.2f}"


class OptionContracts:

    def __init__(self):
        self._contracts = {}  # contract_tuple -> [OptionContract, ...]

    def add(self, contract, date, side, status, price, num, fee):
        if contract not in self._contracts:
            self._contracts[contract] = [OptionContract(*contract)]

        current = self._contracts[contract][-1]

        if current.closed:
            self._contracts[contract].append(OptionContract(*contract))
            current = self._contracts[contract][-1]

        current.add(date, side, status, price, num, fee)

    @property
    def realized_pnl(self):
        return sum(c.pnl[0] for cs in self._contracts.values() for c in cs)

    @property
    def unrealized_pnl(self):
        return sum(c.pnl[1] for cs in self._contracts.values() for c in cs)

    @property
    def total_fees(self):
        return sum(c.total_fees for cs in self._contracts.values() for c in cs)

    def __iter__(self):
        for cs in self._contracts.values():
            yield from cs


def strategy_name(cp, side):
    return {
        (PUT, SELL): 'CSP',
        (PUT, BUY): 'Protect Put',
        (CALL, SELL): 'CC',
        (CALL, BUY): 'Long Call',
    }[(cp, side)]
