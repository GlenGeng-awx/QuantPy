"""
输出格式化: print_detail (单股 verbose) + print_ranking (合并表)。
数据来自 price/ta/valuation 三个模块的 registries。
两套契约: check_* 3-tuple (hit,value,detail) / display_* 2-tuple (value,detail)。
"""
from fundamental.cheap.price import PRICE_LABELS, PRICE_SHORT
from fundamental.cheap.ta import TA_LABELS, TA_SHORT
from fundamental.cheap.valuation import VALUATION_LABELS, VALUATION_SHORT


def _1y_dd_num(result):
    val = result['price'][0][1]
    try:
        return float(str(val).rstrip('%'))
    except (ValueError, AttributeError):
        return 0


def _print_check_rows(labels, items):
    # 3-tuple (hit, value, detail); icon ✓ if hit
    for label, (hit, value, detail) in zip(labels, items):
        icon = '✓' if hit else ' '
        detail_str = '  ' + detail if detail else ''
        print('  {} {:<14}{:<14}{}'.format(icon, label, value, detail_str))


def _print_display_rows(labels, items):
    # 2-tuple (value, detail); no hit, icon ' '
    for label, (value, detail) in zip(labels, items):
        detail_str = '  ' + detail if detail else ''
        print('  {} {:<14}{:<14}{}'.format(' ', label, value, detail_str))


def print_detail(result):
    width = 64
    print('\n' + '=' * width)
    print('{:^{}}'.format('CHEAP v2: {} (count={})'.format(result['stock'], result['count']), width))
    print('=' * width)
    _print_check_rows(PRICE_LABELS, result['price'])
    print('  ' + '-' * (width - 4))
    _print_check_rows(TA_LABELS, result['ta'])
    print('  ' + '-' * (width - 4))
    _print_display_rows(VALUATION_LABELS, result['valuation'])
    print('=' * width)


def print_ranking(group, results):
    results.sort(key=lambda r: (-r['count'], -_1y_dd_num(r)))

    price_fmt = ' '.join('{:>5}' for _ in PRICE_SHORT)
    ta_fmt = ' '.join('{:>5}' for _ in TA_SHORT)
    valuation_fmt = ' '.join('{:>8}' for _ in VALUATION_SHORT)
    fmt = '{:<10} ' + price_fmt + '  {:>3}  | ' + ta_fmt + '  | ' + valuation_fmt
    header = fmt.format('Stock', *PRICE_SHORT, 'cnt', *TA_SHORT, *VALUATION_SHORT)
    w = len(header) + 4
    print('\n' + '=' * w)
    print('{:^{}}'.format('{} ({})'.format(group, len(results)), w))
    print('=' * w)
    print('  ' + header)
    print('  ' + '-' * len(header))
    for r in results:
        price_vals = [v if hit else '' for hit, v, _ in r['price']]
        ta_vals = ['✓' if hit else '' for hit, _, _ in r['ta']]
        valuation_vals = [v for v, _ in r['valuation']]
        print('  ' + fmt.format(r['stock'], *price_vals, r['count'], *ta_vals, *valuation_vals))
    print('=' * w + '\n')
