import sys
from conf import ALL
from fundamental.data import INDEX
from fundamental.statements.__main__ import print_statements
from fundamental.cheap.__main__ import evaluate_stock as eval_cheap
from fundamental.cheap.display import print_detail as print_cheap_detail
from fundamental.cheap.price import PRICE_SHORT
from fundamental.cheap.ta import TA_SHORT
from fundamental.cheap.valuation import VALUATION_SHORT
from fundamental.health.scoring import evaluate_stock as eval_health, print_detail as print_health_detail, PERIODS, fmt_score


def print_ranking(results):
    results.sort(key=lambda r: r['cheap']['count'], reverse=True)

    price_header = ' '.join('{:>5}'.format(s) for s in PRICE_SHORT)
    ta_header = ' '.join('{:>5}'.format(s) for s in TA_SHORT)
    val_header = ' '.join('{:>8}'.format(s) for s in VALUATION_SHORT)
    grid_header = '  '.join('{:>4} {:>4} {:>4}'.format('3yr', 'TTM', '5Q') for _ in range(3))
    header = '{:<10} {}  | {}  | {}  | {}'.format('Stock', price_header, ta_header, val_header, grid_header)
    width = len(header) + 4
    print('\n' + '=' * width)
    print('{:^{}}'.format('COMBINE RANKING', width))
    print('=' * width)
    cat_label = '{:<10} {:>{pw}}  | {:>{tw}}  | {:>{vw}}  | {:^14}  {:^14}  {:^14}'.format(
        '', '', '', '', '--- Inc ---', '---- CF ----', '---- BS ----',
        pw=len(price_header), tw=len(ta_header), vw=len(val_header))
    print('  ' + cat_label)
    print('  ' + header)
    print('  ' + '-' * len(header))

    for r in results:
        price_vals = [v if hit else '' for hit, v, _ in r['cheap']['price']]
        ta_vals = ['✓' if hit else '' for hit, _, _ in r['cheap']['ta']]
        val_vals = [v for v, _ in r['cheap']['valuation']]

        g = r['health']['grid']
        grid_scores = []
        for key in ['income', 'cf', 'bs']:
            for p in PERIODS:
                grid_scores.append(g['{}_{}'.format(key, p)]['score'])

        price_cols = ' '.join('{:>5}'.format(s) for s in price_vals)
        ta_cols = ' '.join('{:>5}'.format(s) for s in ta_vals)
        val_cols = ' '.join('{:>8}'.format(s) for s in val_vals)
        grid_cols = '  '.join('{} {} {}'.format(
            fmt_score(grid_scores[i]), fmt_score(grid_scores[i + 1]), fmt_score(grid_scores[i + 2]))
            for i in range(0, 9, 3))

        print('  {:<10} {}  | {}  | {}  | {}'.format(r['stock'], price_cols, ta_cols, val_cols, grid_cols))
    print('=' * width + '\n')


def main():
    if len(sys.argv) > 1:
        targets = [s.upper() for s in sys.argv[1:]]
    else:
        targets = [s for s in ALL if s not in INDEX]

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
