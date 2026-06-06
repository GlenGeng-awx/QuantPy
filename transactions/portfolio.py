from datetime import datetime

from transactions.book import BOOK
from transactions.position import Position
from fx import to_usd
from conf import ALL


class Portfolio:
    def __init__(self, book):
        self._positions = {}
        for entry in book:
            stock_name = entry[3][0]
            self._positions.setdefault(stock_name, Position(stock_name)).add(entry)

    def display_total_pnl(self):
        sr, su, sf = 0, 0, 0
        or_, ou, of_ = 0, 0, 0
        for stock_name, position in self._positions.items():
            sr += to_usd(position.stock_realized, stock_name)
            su += to_usd(position.stock_unrealized, stock_name)
            sf += to_usd(position.stock_fees, stock_name)
            or_ += to_usd(position.option_realized, stock_name)
            ou += to_usd(position.option_unrealized, stock_name)
            of_ += to_usd(position.option_fees, stock_name)
        print(f"\n{'Stock:':<8} realized={sr:>10.2f}  unrealized={su:>10.2f}  fees={sf:>.2f}")
        print(f"{'Option:':<8} realized={or_:>10.2f}  unrealized={ou:>10.2f}  fees={of_:>.2f}")

    def display_open(self):
        print("\n---------------------\nOpen Positions\n---------------------")
        for stock_name in sorted(self._positions):
            self._positions[stock_name].display_open()

    def display_by_expire(self, full=False):
        print("\n---------------------\nBy Expire\n---------------------")
        current_date = datetime.now().strftime('%Y-%m-%d')

        by_expire = {}
        for position in self._positions.values():
            for option in position.options:
                by_expire.setdefault(option.expire, []).append(option)

        for expire in sorted(by_expire.keys()):
            prefix = '-' if expire < current_date else '+'
            if not full and prefix == '-':
                continue
            contracts = sorted(by_expire[expire], key=lambda option: option.stock_name)
            realized, unrealized, fees = 0, 0, 0
            for option in contracts:
                realized += to_usd(option.pnl[0], option.stock_name)
                unrealized += to_usd(option.pnl[1], option.stock_name)
                fees += to_usd(option.total_fees, option.stock_name)
            print(f"\n{prefix} {expire}:")
            for option in contracts:
                flag = '*' if not option.closed else ' '
                print(f"\t{flag} {option.stock_name:<5} {option}")
            print(f"\t\tSubtotal: realized= {realized:.2f}, unrealized= {unrealized:.2f}, fees= {fees:.2f}")

    def display_by_stock(self):
        print("\n---------------------\nby Stock\n---------------------")
        for stock_name in ALL:
            if stock_name not in self._positions:
                continue
            self._positions[stock_name].display()


if __name__ == '__main__':
    portfolio = Portfolio(BOOK)
    portfolio.display_total_pnl()
    portfolio.display_open()
    portfolio.display_by_expire(full=False)
    portfolio.display_by_stock()
