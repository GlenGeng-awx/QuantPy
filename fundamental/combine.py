import sys
from conf import ALL
from fundamental.data import SKIP
from fundamental.statements.__main__ import print_statements
from fundamental.cheap.scoring import evaluate_stock as eval_cheap, print_detail as print_cheap_detail
from fundamental.cheap.signals import SHORT as SIG_SHORT
from fundamental.cheap.hints import SHORT as HINT_SHORT
from fundamental.health.scoring import evaluate_stock as eval_health, print_detail as print_health_detail, PERIODS, fmt_score


def print_ranking(results):
    results.sort(key=lambda r: r['cheap']['count'], reverse=True)

    sig_header = ' '.join('{:>5}'.format(s) for s in SIG_SHORT)
    hint_header = ' '.join('{:>4}'.format(s) for s in HINT_SHORT)
    grid_header = '  '.join('{:>4} {:>4} {:>4}'.format('3yr', 'TTM', '5Q') for _ in range(3))
    header = '{:<10} {}  | {}  | {}'.format('Stock', sig_header, hint_header, grid_header)
    width = len(header) + 4
    print('\n' + '=' * width)
    print('{:^{}}'.format('COMBINE RANKING', width))
    print('=' * width)
    cat_label = '{:<10} {:>{sig_w}}  | {:>{hint_w}}  | {:^14}  {:^14}  {:^14}'.format(
        '', '', '', '--- Inc ---', '---- CF ----', '---- BS ----',
        sig_w=len(sig_header), hint_w=len(hint_header))
    print('  ' + cat_label)
    print('  ' + header)
    print('  ' + '-' * len(header))

    for r in results:
        signals = [value if hit else '' for hit, value, _ in r['cheap']['signals']]
        hints = ['✓' if hit else '' for hit, _, _ in r['cheap']['hints']]

        g = r['health']['grid']
        grid_scores = []
        for key in ['income', 'cf', 'bs']:
            for p in PERIODS:
                grid_scores.append(g['{}_{}'.format(key, p)]['score'])

        sig_cols = ' '.join('{:>5}'.format(s) for s in signals)
        hint_cols = ' '.join('{:>4}'.format(s) for s in hints)
        grid_cols = '  '.join('{} {} {}'.format(
            fmt_score(grid_scores[i]), fmt_score(grid_scores[i + 1]), fmt_score(grid_scores[i + 2]))
            for i in range(0, 9, 3))

        print('  {:<10} {}  | {}  | {}'.format(r['stock'], sig_cols, hint_cols, grid_cols))
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
        print_statements(stock_name)
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
