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
        if self.stock.num != 0:
            return True
        for option in self.options:
            if not option.closed:
                return True
        return False

    @property
    def break_even_with_options(self):
        if self.stock.num == 0:
            return 0.0
        return self.stock.break_even - self.option_realized / self.stock.num

    @property
    def stock_realized(self):
        total = 0
        for sell in self.stock.pnl:
            total += sell[5]
        return total

    @property
    def stock_fees(self):
        return self.stock.total_fees

    @property
    def option_realized(self):
        return self.options.realized_pnl

    @property
    def option_unrealized(self):
        return self.options.unrealized_pnl

    @property
    def option_fees(self):
        return self.options.total_fees

    @property
    def total_fees(self):
        return self.stock_fees + self.option_fees

    def display_open(self):
        if not self.is_open:
            return
        print(f"\n{self.stock_name}:")
        if self.stock.num > 0:
            print(f"\t{self.stock}  even(w/ options)={self.break_even_with_options:.2f}")
        open_options = [o for o in self.options if not o.closed]
        open_options.sort(key=lambda o: o.expire)
        for option in open_options:
            print(f"\t{option}")

    def display(self):
        print(f"\n{self.stock_name}:")
        if self.stock.num > 0:
            print(f"\t{self.stock}  even(w/ options)={self.break_even_with_options:.2f}")
        total = self.stock_realized + self.option_realized
        if total != 0:
            print(f"\tTotal Realized: {total:.2f}")
        print(f"\tFees: {self.total_fees:.2f}")

        ledger = self.stock.ledger
        if ledger:
            by_year = {}
            for entry in ledger:
                year = entry[1][:4]
                by_year.setdefault(year, []).append(entry)
            for year in sorted(by_year):
                year_realized = sum(e[5] for e in by_year[year] if e[0] == 'SELL')
                print(f"\t\t--- Stock {year} ---")
                for entry in by_year[year]:
                    if entry[0] == 'BUY':
                        _, date, num, price = entry
                        print(f"\t\t  {date[5:]}  BUY  {num} shares @ {price:.2f}")
                    else:
                        _, date, num, sell_price, cost, pnl = entry
                        print(f"\t\t  {date[5:]}  SELL {num} shares @ {sell_price:.2f}  cost={cost:.2f}  pnl={pnl:.2f}")
                if year_realized != 0:
                    print(f"\t\t  Realized: {year_realized:.2f}")

        events = []
        for option in self.options:
            _, _, details = option.pnl
            for close_date, open_date, num, open_price, close_price, pnl in details:
                events.append((close_date, open_date, option, num, pnl))
        events.sort(key=lambda x: x[0])

        if events:
            by_year = {}
            for close_date, open_date, option, num, pnl in events:
                year = close_date[:4]
                by_year.setdefault(year, []).append((close_date, open_date, option, num, pnl))
            for year in sorted(by_year):
                year_realized = sum(e[4] for e in by_year[year])
                print(f"\t\t--- Option {year} ---")
                for close_date, open_date, option, num, pnl in by_year[year]:
                    line = f"{close_date[5:]}  {option.strategy:<12} {option.expire} {option.strike:>7}  x{num:<2}"
                    line += f"  pnl={pnl:>8.2f}  (opened {open_date[5:]})"
                    print(f"\t\t  {line}")
                print(f"\t\t  Realized: {year_realized:.2f}")

        open_opts = [o for o in self.options if not o.closed]
        open_opts.sort(key=lambda o: o.expire)
        if open_opts:
            print(f"\t\t--- Option Open ---")
            for option in open_opts:
                r, u, _ = option.pnl
                line = f"{option.strategy:<12} {option.expire} {option.strike:>7}  x{option.num}"
                line += f"  unrealized={u:>8.2f}"
                print(f"\t\t  * {line}")
