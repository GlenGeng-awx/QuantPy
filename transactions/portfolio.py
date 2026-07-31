from datetime import datetime, timedelta

from transactions.book import BOOK_HK, BOOK_US
from transactions.position import Position
from conf import ALL, CN_INDEX


class Portfolio:

    def __init__(self, book, currency='USD'):
        self._currency = currency
        self._positions = {}
        for entry in book:
            stock_name = entry[3][0]
            self._positions.setdefault(stock_name, Position(stock_name)).add(entry)

    def open_positions(self):
        return [name for name, position in self._positions.items() if position.is_open]

    def display_total_pnl(self):
        print(f"\n===== {self._currency} =====")
        sr, su, sf = 0, 0, 0
        or_, ou, of_ = 0, 0, 0
        for position in self._positions.values():
            sr += position.stock_realized
            su += position.stock_unrealized
            sf += position.stock_fees
            or_ += position.option_realized
            ou += position.option_unrealized
            of_ += position.option_fees
        print(f"\n{'Stock:':<8} realized={sr:>10.2f}  unrealized={su:>10.2f}  fees={sf:>.2f}")
        print(f"{'Option:':<8} realized={or_:>10.2f}  unrealized={ou:>10.2f}  fees={of_:>.2f}")

    def display_open(self):
        print(f"\n---------------------\nOpen Positions ({self._currency})\n---------------------")
        for stock_name in sorted(self._positions):
            self._positions[stock_name].display_open()

    def display_by_expire(self, full=False):
        print(f"\n---------------------\nBy Expire ({self._currency})\n---------------------")
        current_date = datetime.now().strftime('%Y-%m-%d')
        cutoff = (datetime.now() - timedelta(weeks=2)).strftime('%Y-%m-%d')

        by_expire = {}
        for position in self._positions.values():
            for option in position.options:
                by_expire.setdefault(option.expire, []).append(option)

        for expire in sorted(by_expire.keys()):
            prefix = '-' if expire < current_date else '+'
            if not full and expire < cutoff:
                continue
            contracts = sorted(by_expire[expire], key=lambda option: option.stock_name)
            realized, unrealized, fees = 0, 0, 0
            for option in contracts:
                realized += option.pnl[0]
                unrealized += option.pnl[1]
                fees += option.total_fees
            print(f"\n{prefix} {expire}:")
            for option in contracts:
                flag = '*' if not option.closed else ' '
                print(f"\t{flag} {option.stock_name:<5} {option}")
            print(f"\t\tSubtotal: realized= {realized:.2f}, unrealized= {unrealized:.2f}, fees= {fees:.2f}")

    def display_by_stock(self):
        print(f"\n---------------------\nBy Stock ({self._currency})\n---------------------")
        for stock_name in ALL:
            if stock_name not in self._positions:
                continue
            self._positions[stock_name].display()


class PortfolioGroup:

    def __init__(self):
        self._portfolios = [
            Portfolio(BOOK_HK, 'HKD'),
            Portfolio(BOOK_US, 'USD'),
        ]

    def open_positions(self):
        names = []
        for pf in self._portfolios:
            names.extend(pf.open_positions())
        return names

    def display_total_pnl(self):
        for pf in self._portfolios:
            pf.display_total_pnl()

    def display_open(self):
        for pf in self._portfolios:
            pf.display_open()

    def display_by_expire(self, full=False):
        for pf in self._portfolios:
            pf.display_by_expire(full)

    def display_by_stock(self):
        for pf in self._portfolios:
            pf.display_by_stock()


def get_current_positions():
    pg = PortfolioGroup()
    return pg.open_positions() + CN_INDEX


if __name__ == '__main__':
    pg = PortfolioGroup()
    pg.display_total_pnl()
    pg.display_open()
    pg.display_by_expire(full=False)
    pg.display_by_stock()
    print(f"\nOpen positions: {get_current_positions()}")
