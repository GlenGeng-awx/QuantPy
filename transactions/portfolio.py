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
        realized, unrealized, fees = 0, 0, 0
        for stock_name, position in self._positions.items():
            realized += to_usd(position.total_realized_pnl, stock_name)
            unrealized += to_usd(position.options.unrealized_pnl, stock_name)
            fees += to_usd(position.total_fees, stock_name)
        print(f"\nTotal: realized={realized:.2f}, unrealized={unrealized:.2f}, fees={fees:.2f}")

    def display_open(self):
        print("\n---------------------\nOpen Positions\n---------------------")
        for stock_name in sorted(self._positions):
            position = self._positions[stock_name]
            if not position.is_open:
                continue

            print(f"\n{stock_name}:")
            if position.stock.num > 0:
                print(f"\t{position.stock}  real={position.stock_real_price:.2f}")

            open_options = sorted(
                [oc for oc in position.options if oc.pnl[1] != 0],
                key=lambda oc: oc.expire,
            )
            for oc in open_options:
                print(f"\t{oc}")

    def display_by_expire(self, full=False):
        print("\n---------------------\nBy Expire\n---------------------")
        current_date = datetime.now().strftime('%Y-%m-%d')

        expire_map = {}
        for position in self._positions.values():
            for oc in position.options:
                expire_map.setdefault(oc.expire, []).append(oc)

        for expire in sorted(expire_map.keys()):
            prefix = '-' if expire < current_date else '+'
            if not full and prefix == '-':
                continue
            contracts = sorted(expire_map[expire], key=lambda oc: oc.stock_name)
            realized, unrealized, fees = 0, 0, 0
            for oc in contracts:
                realized += to_usd(oc.pnl[0], oc.stock_name)
                unrealized += to_usd(oc.pnl[1], oc.stock_name)
                fees += to_usd(oc.total_fees, oc.stock_name)
            print(f"\n{prefix} {expire}:")
            for oc in contracts:
                flag = '*' if oc.pnl[1] != 0 else ' '
                print(f"\t{flag} {oc.stock_name:<5} {oc}")
            print(f"\t\tSubtotal: realized= {realized:.2f}, unrealized= {unrealized:.2f}, fees= {fees:.2f}")

    def display_by_stock(self):
        print("\n---------------------\nby Stock\n---------------------")
        for stock_name in ALL:
            if stock_name not in self._positions:
                continue
            position = self._positions[stock_name]

            print(f"\n{stock_name}:")
            print(f"\tNum: {position.stock.num}, Avg Price: {position.stock.avg_price:.2f}, Real Price: {position.stock_real_price:.2f}")
            print(f"\tRealized: {position.total_realized_pnl:.2f}, Unrealized: {position.options.unrealized_pnl:.2f}")
            print(f"\tFees: {position.total_fees:.2f}")

            for d in position.stock.pnl:
                date, num, avg, sell_price, pnl = d
                print(f"\t\tStock SELL {date}  {num} @ {sell_price:.2f}  cost={avg:.2f}  pnl={pnl:.2f}")

            for oc in sorted(position.options, key=lambda oc: oc.expire):
                flag = '*' if oc.pnl[1] != 0 else ' '
                print(f"\t\t{flag} {oc}")


if __name__ == '__main__':
    portfolio = Portfolio(BOOK)
    portfolio.display_total_pnl()
    portfolio.display_open()
    portfolio.display_by_expire(full=False)
    portfolio.display_by_stock()
