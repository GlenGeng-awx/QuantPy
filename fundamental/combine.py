import sys
from conf import ALL
from fundamental.data import SKIP
from fundamental.cheap.scoring import evaluate_stock as eval_cheap, print_detail as print_cheap_detail
from fundamental.cheap.signals import SHORT as SIG_SHORT
from fundamental.cheap.hints import SHORT as HINT_SHORT
from fundamental.health.scoring import evaluate_stock as eval_health, print_detail as print_health_detail


def print_ranking(results):
    results.sort(key=lambda r: r['cheap']['count'], reverse=True)

    sig_header = ' '.join('{:>5}'.format(s) for s in SIG_SHORT)
    hint_header = ' '.join('{:>4}'.format(s) for s in HINT_SHORT)
    header = '{:<10} {}  | {}  |  {:>3} {:>4} {:>4} {:>5}'.format(
        'Stock', sig_header, hint_header, 'Inc', 'CF', 'BS', 'Total')
    width = len(header) + 4
    print('\n' + '=' * width)
    print('{:^{}}'.format('COMBINE RANKING', width))
    print('=' * width)
    print('  ' + header)
    print('  ' + '-' * len(header))

    for r in results:
        signals = [value if hit else '' for hit, value, _ in r['cheap']['signals']]
        hints = ['✓' if hit else '' for hit, _, _ in r['cheap']['hints']]

        cats = {c['name']: c['score'] for c in r['health']['categories']}
        inc = cats.get('INCOME STATEMENT', 0)
        cf = cats.get('CASH FLOW', 0)
        bs = cats.get('BALANCE SHEET', 0)
        total = r['health']['overall_score']

        sig_cols = ' '.join('{:>5}'.format(s) for s in signals)
        hint_cols = ' '.join('{:>4}'.format(s) for s in hints)
        print('  {:<10} {}  | {}  |  {:>3.0f} {:>4.0f} {:>4.0f} {:>5.0f}'.format(
            r['stock'], sig_cols, hint_cols, inc, cf, bs, total))
    print('=' * width + '\n')


def main():
    if len(sys.argv) > 1:
        targets = [s.upper() for s in sys.argv[1:]]
    else:
        targets = [s for s in ALL if s not in SKIP]

    results = []
    for stock_name in targets:
        cheap_result = eval_cheap(stock_name)
        health_result = eval_health(stock_name)
        print_cheap_detail(cheap_result)
        print_health_detail(health_result)
        results.append({
            'stock': stock_name,
            'cheap': cheap_result,
            'health': health_result,
        })

    if len(results) > 1:
        print_ranking(results)


if __name__ == '__main__':
    main()
