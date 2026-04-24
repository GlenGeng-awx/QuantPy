from datetime import datetime

from transactions.book import BOOK
from transactions.position import Position
from transactions.types import strategy_name
from conf import ALL


class Portfolio:
    def __init__(self, book):
        self._positions = {}
        for entry in book:
            stock_name = entry[3][0]
            self._positions.setdefault(stock_name, Position(stock_name)).add(entry)

    def total_pnl(self):
        realized = sum(p.total_realized_pnl for p in self._positions.values())
        unrealized = sum(p.options.unrealized_pnl for p in self._positions.values())
        fees = sum(p.total_fees for p in self._positions.values())
        print(f"\nTotal: realized={realized:.2f}, unrealized={unrealized:.2f}, fees={fees:.2f}")

    def list_open(self):
        print("\n---------------------\nOpen Positions\n---------------------")
        for name in sorted(self._positions):
            p = self._positions[name]
            if p.stock.num == 0 and not p.options.unrealized_pnl:
                continue

            print(f"\n{name}:")
            if p.stock.num > 0:
                print(f"\tStock: {p.stock.num} shares @ {p.stock.avg_price:.2f}")

            open_options = sorted(
                [oc for oc in p.options if oc.pnl[1] != 0],
                key=lambda oc: oc.expire,
            )
            for oc in open_options:
                first_entry = oc.entries[0]
                name_str = strategy_name((oc.stock_name, oc.cp, oc.expire, oc.strike), first_entry.side)
                print(f"\t{name_str:<12} {oc.expire} {oc.strike:>7}  unrealized={oc.pnl[1]:>8.2f}")

    def list_by_date(self, full=False):
        print("\n---------------------\nList by Date\n---------------------")
        current_date = datetime.now().strftime('%Y-%m-%d')

        date_map = {}
        for p in self._positions.values():
            for oc in p.options:
                date_map.setdefault(oc.expire, []).append(oc)

        for date in sorted(date_map.keys()):
            prefix = '-' if date < current_date else '+'
            if not full and prefix == '-':
                continue
            contracts = sorted(date_map[date], key=lambda oc: oc.stock_name)
            pnl_total = sum(oc.pnl[0] + oc.pnl[1] for oc in contracts)
            fees_total = sum(oc.total_fees for oc in contracts)
            print(f"\n{prefix} {date}:")
            for oc in contracts:
                first_entry = oc.entries[0]
                name_str = strategy_name((oc.stock_name, oc.cp, oc.expire, oc.strike), first_entry.side)
                r, u = oc.pnl
                flag = '*' if u != 0 else ' '
                print(f"\t{flag} {oc.stock_name:<5} {name_str:<12} {oc.strike:>7}  pnl={r + u:>8.2f}")
            print(f"\t\tSubtotal: pnl={pnl_total:.2f}, fees={fees_total:.2f}")

    def list_by_stock_name(self):
        print("\n---------------------\nList by Stock\n---------------------")
        for stock_name in ALL:
            if stock_name not in self._positions:
                continue
            p = self._positions[stock_name]
            if p.stock.num == 0 and not p.total_realized_pnl and not p.options.unrealized_pnl:
                continue

            print(f"\n{stock_name}:")
            print(f"\tNum: {p.stock.num}, Avg Price: {p.stock.avg_price:.2f}, Real Price: {p.stock_real_price:.2f}")
            print(f"\tRealized: {p.total_realized_pnl:.2f}, Unrealized: {p.options.unrealized_pnl:.2f}")
            print(f"\tFees: {p.total_fees:.2f}")

            for d in p.stock.pnl:
                date, num, avg, sell_price, pnl = d
                print(f"\t\tStock SELL {date}  {num} @ {sell_price:.2f}  cost={avg:.2f}  pnl={pnl:.2f}")

            for oc in sorted(p.options, key=lambda oc: oc.expire):
                first_entry = oc.entries[0]
                name_str = strategy_name((oc.stock_name, oc.cp, oc.expire, oc.strike), first_entry.side)
                r, u = oc.pnl
                flag = '*' if u != 0 else ' '
                print(f"\t\t{flag} {name_str:<12} {oc.expire} {oc.strike:>7}  realized={r:>8.2f}  unrealized={u:>8.2f}")


if __name__ == '__main__':
    portfolio = Portfolio(BOOK)
    portfolio.total_pnl()
    portfolio.list_open()
    portfolio.list_by_date(full=False)
    portfolio.list_by_stock_name()
