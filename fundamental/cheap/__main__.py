# 用法见 fundamental/cheap/__init__.py
import sys
from conf import ALL
from base_engine import BaseEngine
from preload_conf import period
from fundamental.data import load_info, load_statement, get_val, INDEX
from fundamental.cheap.price import PRICE
from fundamental.cheap.ta import TA
from fundamental.cheap.valuation import VALUATION
from fundamental.cheap.display import print_detail, print_ranking
import guru


def load_data(stock_name):
    from_date, to_date, interval = period(8)
    engine = BaseEngine(stock_name, from_date, to_date, interval)
    context = guru.calculate(engine.stock_df)
    cf_df = load_statement(stock_name, 'cf_ttm')
    fcf = get_val(cf_df, 'Free Cash Flow')
    return {
        'stock_name': stock_name,
        'stock_df': engine.stock_df,
        'info': load_info(stock_name),
        'primary_lines': engine.primary_line.primary_lines,
        'secondary_lines': engine.secondary_line.secondary_lines,
        'neck_lines': engine.neck_line.neck_lines,
        'elliott_dates': engine.elliott.x,
        'guru_context': context,
        'fcf': fcf,
    }


def evaluate_stock(stock_name):
    data = load_data(stock_name)
    price = [fn(data) for fn in PRICE]
    ta = [fn(data) for fn in TA]
    valuation = [fn(data) for fn in VALUATION]

    return {
        'stock': stock_name,
        'price': price,
        'ta': ta,
        'valuation': valuation,
        'count': sum(1 for hit, _, _ in price if hit),
    }


def _parse_args(argv):
    mode = 'stock'
    stocks = []
    for arg in argv:
        if arg.startswith('--mode='):
            mode = arg.split('=', 1)[1]
        else:
            stocks.append(arg)
    return stocks, mode


def _groups(stocks, mode):
    if stocks:
        return [('RANKING', stocks)]
    if mode == 'index':
        return [('INDEX', [s for s in ALL if s in INDEX])]
    return [('STOCK', [s for s in ALL if s not in INDEX])]


def main():
    args, mode = _parse_args(sys.argv[1:])
    for label, targets in _groups(args, mode):
        results = []
        for stock_name in targets:
            result = evaluate_stock(stock_name)
            print_detail(result)
            results.append(result)
        if len(results) > 1:
            print_ranking(label, results)


if __name__ == '__main__':
    main()
