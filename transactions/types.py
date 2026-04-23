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
        sells = [e.price for e in self.entries if e.side == SELL for _ in range(e.num)]
        buys = [e.price for e in self.entries if e.side == BUY for _ in range(e.num)]

        realized = sum((s - b) * 100 for s, b in zip(sells, buys))
        matched = min(len(sells), len(buys))
        unrealized = sum(p * 100 for p in sells[matched:]) - sum(p * 100 for p in buys[matched:])
        return realized, unrealized

    @property
    def total_fees(self):
        return sum(e.fee for e in self.entries)


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
