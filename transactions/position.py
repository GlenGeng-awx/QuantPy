from transactions.types import StockContract, OptionContracts


class Position:

    def __init__(self, stock_name):
        self.stock_name = stock_name
        self.stock = StockContract(stock_name)
        self.options = OptionContracts()

    def add(self, entry):
        date, side, status, contract, price, num, fee = entry
        if len(contract) == 1:
            self.stock.add(date, side, price, num, fee)
        else:
            self.options.add(contract, date, side, status, price, num, fee)

    @property
    def is_open(self):
        return self.stock.num != 0 or self.options.unrealized_pnl != 0

    @property
    def stock_real_price(self):
        if self.stock.num == 0:
            return 0.0
        return self.stock.avg_price - self.options.realized_pnl / self.stock.num

    @property
    def total_realized_pnl(self):
        stock = sum(d[4] for d in self.stock.pnl)
        return stock + self.options.realized_pnl

    @property
    def total_fees(self):
        return self.stock.total_fees + self.options.total_fees
