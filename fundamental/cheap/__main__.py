import sys
from base_engine import BaseEngine
from preload_conf import period
from conf import ALL, CN_INDEX, US_INDEX
from fundamental.health.data import load_info
from fundamental.cheap.signals import CHECKS as SIG_CHECKS, LABELS as SIG_LABELS, SHORT as SIG_SHORT
from fundamental.cheap.hints import CHECKS as HINT_CHECKS, LABELS as HINT_LABELS, SHORT as HINT_SHORT
import guru


def load_data(stock_name):
    from_date, to_date, interval = period(8)
    engine = BaseEngine(stock_name, from_date, to_date, interval)
    context = guru.calculate(engine.stock_df)
    return {
        'stock_name': stock_name,
        'stock_df': engine.stock_df,
        'info': load_info(stock_name),
        'primary_lines': engine.primary_line.primary_lines,
        'secondary_lines': engine.secondary_line.secondary_lines,
        'neck_lines': engine.neck_line.neck_lines,
        'elliott_dates': engine.elliott.x,
        'guru_context': context,
    }


def eval_stock(stock_name):
    data = load_data(stock_name)
    signals = [fn(data) for fn in SIG_CHECKS]
    hints = [fn(data) for fn in HINT_CHECKS]

    return {
        'stock': stock_name,
        'signals': signals,
        'hints': hints,
        'count': sum(1 for hit, _, _ in signals if hit),
    }


def print_detail(result):
    width = 60
    print('\n' + '=' * width)
    print('{:^{}}'.format('CHEAP: {}'.format(result['stock']), width))
    print('=' * width)

    for label, (hit, value, detail) in zip(SIG_LABELS, result['signals']):
        icon = '✓' if hit else ' '
        detail_str = '  ' + detail if detail else ''
        print('  {} {:<16}{:<14}{}'.format(icon, label, value, detail_str))
    print('  ' + '-' * (width - 4))
    for label, (hit, value, detail) in zip(HINT_LABELS, result['hints']):
        icon = '✓' if hit else ' '
        detail_str = '  ' + detail if detail else ''
        print('  {} {:<16}{:<14}{}'.format(icon, label, value, detail_str))
    print('=' * width)


def print_ranking(results):
    results.sort(key=lambda r: r['count'], reverse=True)
    header = '{:<10} {:>4} {:>4} {:>4} {:>6} {:>6} {:>5}  | {:>4} {:>4} {:>4} {:>4}'.format(
        'Stock', *SIG_SHORT, *HINT_SHORT)
    width = len(header) + 4
    print('\n' + '=' * width)
    print('{:^{}}'.format('CHEAP RANKING', width))
    print('=' * width)
    print('  ' + header)
    print('  ' + '-' * len(header))
    for r in results:
        signals = [value if hit else '' for hit, value, _ in r['signals']]
        hints = ['✓' if hit else '' for hit, _, _ in r['hints']]
        print('  {:<10} {:>4} {:>4} {:>4} {:>6} {:>6} {:>5}  | {:>4} {:>4} {:>4} {:>4}'.format(
            r['stock'], *signals, *hints))
    print('=' * width + '\n')


def main():
    if len(sys.argv) > 1:
        targets = [s.upper() for s in sys.argv[1:]]
    else:
        skip = set(CN_INDEX + US_INDEX)
        targets = [s for s in ALL if s not in skip]

    results = []
    for stock_name in targets:
        result = eval_stock(stock_name)
        print_detail(result)
        results.append(result)
    if len(results) > 1:
        print_ranking(results)


if __name__ == '__main__':
    main()
