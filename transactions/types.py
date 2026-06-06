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

    def __init__(self, stock_name, last_close):
        self.stock_name = stock_name
        self.last_close = last_close
        self.entries = []

    def add(self, date, side, price, num, fee):
        self.entries.append(StockEntry(date, side, price, num, fee))

    @property
    def num(self):
        buy = sum(entry.num for entry in self.entries if entry.side == BUY)
        sell = sum(entry.num for entry in self.entries if entry.side == SELL)
        return buy - sell

    @property
    def cost(self):
        if self.num == 0:
            return 0.0
        outflow = sum(entry.price * entry.num for entry in self.entries if entry.side == BUY)
        inflow = sum(entry.price * entry.num for entry in self.entries if entry.side == SELL)
        return (outflow - inflow) / self.num

    @property
    def pnl(self):
        """(realized, unrealized, details) FIFO"""
        lots = []
        for entry in self.entries:
            if entry.side == BUY:
                lots.append({'date': entry.date, 'price': entry.price, 'num': entry.num})

        total_realized = 0
        details = []
        for entry in self.entries:
            if entry.side != SELL:
                continue
            to_sell = entry.num
            while to_sell > 0 and lots:
                lot = lots[0]
                matched = min(lot['num'], to_sell)
                realized = (entry.price - lot['price']) * matched
                total_realized += realized
                details.append((entry.date, lot['date'], matched, lot['price'], entry.price, realized))
                lot['num'] -= matched
                to_sell -= matched
                if lot['num'] == 0:
                    lots.pop(0)

        unrealized = 0
        for lot in lots:
            unrealized += (self.last_close - lot['price']) * lot['num']

        return total_realized, unrealized, details

    @property
    def ledger(self):
        entries = []
        for entry in self.entries:
            if entry.side == BUY:
                entries.append(('BUY', entry.date, entry.num, entry.price))
        for sell_date, buy_date, num, cost, sell_price, pnl in self.pnl[2]:
            entries.append(('SELL', sell_date, num, sell_price, cost, pnl))
        entries.sort(key=lambda entry: entry[1])
        return entries

    @property
    def total_fees(self):
        return sum(entry.fee for entry in self.entries)

    def __repr__(self):
        r, u, _ = self.pnl
        lines = [
            f"{self.num} shares  close={self.last_close:.2f}",
            f"cost={self.cost:.2f}  realized={r:.2f}  unrealized={u:.2f}",
        ]
        return '\n'.join(lines)


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
        opened = sum(entry.num for entry in self.entries if entry.side == open_side)
        closed = sum(entry.num for entry in self.entries if entry.side != open_side)
        return opened - closed

    @property
    def pnl(self):
        """(realized, unrealized, details) FIFO"""
        open_side = self.entries[0].side
        sign = 1 if open_side == SELL else -1

        lots = []
        for entry in self.entries:
            if entry.side == open_side:
                lots.append({'date': entry.date, 'price': entry.price, 'num': entry.num})

        realized = 0.0
        details = []
        for entry in self.entries:
            if entry.side == open_side:
                continue
            to_close = entry.num
            while to_close > 0 and lots:
                lot = lots[0]
                matched = min(lot['num'], to_close)
                pnl = sign * (lot['price'] - entry.price) * matched * 100
                details.append((entry.date, lot['date'], matched, lot['price'], entry.price, pnl))
                realized += pnl
                lot['num'] -= matched
                to_close -= matched
                if lot['num'] == 0:
                    lots.pop(0)

        unrealized = sign * sum(lot['price'] * lot['num'] for lot in lots) * 100
        return realized, unrealized, details

    @property
    def total_fees(self):
        return sum(entry.fee for entry in self.entries)

    def __repr__(self):
        r, u, _ = self.pnl
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
        total = 0
        for option in self:
            total += option.pnl[0]
        return total

    @property
    def unrealized_pnl(self):
        total = 0
        for option in self:
            total += option.pnl[1]
        return total

    @property
    def total_fees(self):
        total = 0
        for option in self:
            total += option.total_fees
        return total

    def __iter__(self):
        for contracts in self._contracts.values():
            yield from contracts


def strategy_name(cp, side):
    return {
        (PUT, SELL): 'CSP',
        (PUT, BUY): 'Protect Put',
        (CALL, SELL): 'CC',
        (CALL, BUY): 'Long Call',
    }[(cp, side)]
