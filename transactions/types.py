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


class StockContract(namedtuple('_StockContract', ['stock_name'])):

    def __init__(self, stock_name):
        self.entries = []

    def add(self, date, side, price, num, fee):
        self.entries.append(StockEntry(date, side, price, num, fee))

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
    def total_fees(self):
        return sum(e.fee for e in self.entries)


class OptionContract(namedtuple('_OptionContract', ['stock_name', 'cp', 'expire', 'strike'])):

    def __init__(self, stock_name, cp, expire, strike):
        self.entries = []

    def add(self, date, side, status, price, num, fee):
        self.entries.append(OptionEntry(date, side, status, price, num, fee))

    @property
    def pnl(self):
        """(realized, unrealized) PnL using moving average cost, for tax reporting"""
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


class OptionContracts:

    def __init__(self):
        self._contracts = {}

    def add(self, contract, date, side, status, price, num, fee):
        oc = self._contracts.setdefault(contract, OptionContract(*contract))
        oc.add(date, side, status, price, num, fee)

    @property
    def realized_pnl(self):
        return sum(c.pnl[0] for c in self._contracts.values())

    @property
    def unrealized_pnl(self):
        return sum(c.pnl[1] for c in self._contracts.values())

    @property
    def total_fees(self):
        return sum(c.total_fees for c in self._contracts.values())

    def __iter__(self):
        return iter(self._contracts.values())


def strategy_name(contract, side):
    if len(contract) == 1:
        return 'Buy' if side == BUY else 'Sell'
    _, cp, _, _ = contract
    return {
        (PUT, SELL): 'CSP',
        (CALL, SELL): 'CC',
        (CALL, BUY): 'Long Call',
        (PUT, BUY): 'Protect Put',
    }[(cp, side)]
