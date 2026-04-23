from transactions.types import StockContract, OptionContract


class Position:
    """Per-stock position: one StockContract + multiple OptionContracts."""

    def __init__(self, stock_name):
        self.stock_name = stock_name
        self.stock = StockContract(stock_name)
        self._options = {}

    def add(self, entry):
        date, side, status, contract, price, num, fee = entry
        if len(contract) == 1:
            self.stock.add(date, side, price, num, fee)
        else:
            oc = self._options.setdefault(contract, OptionContract(*contract))
            oc.add(date, side, status, price, num, fee)

    @property
    def options(self):
        return list(self._options.values())

    @property
    def num(self):
        return self.stock.num

    @property
    def avg_price(self):
        return self.stock.avg_price

    @property
    def real_price(self):
        if self.num == 0:
            return 0.0
        return self.avg_price - self.realized_pnl / self.num

    @property
    def realized_pnl(self):
        stock = sum(d[4] for d in self.stock.pnl)
        option = sum(c.pnl[0] for c in self._options.values())
        return stock + option

    @property
    def unrealized_pnl(self):
        return sum(c.pnl[1] for c in self._options.values())

    @property
    def total_fees(self):
        return self.stock.total_fees + sum(c.total_fees for c in self._options.values())
