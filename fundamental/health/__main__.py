import sys
from conf import ALL
from fundamental.health.helpers import load_all_data
from fundamental.data import format_value, get_info_val, SKIP
from fundamental.health.income import (
    eval_revenue_growth, eval_op_income_growth, eval_ebitda_growth, eval_eps_trend,
    eval_margins, eval_interest_coverage,
)
from fundamental.health.cashflow import (
    eval_ocf_trend, eval_earnings_quality, eval_fcf,
    eval_shareholder_return, eval_sbc_ratio,
)
from fundamental.health.balance_sheet import (
    eval_cash_adequacy, eval_debt_over_equity, eval_current_ratio,
    eval_ar_growth, eval_ap_stability, eval_risk_flags,
)

CATEGORIES = [
    ('INCOME STATEMENT', 0.25, [
        eval_revenue_growth, eval_op_income_growth, eval_ebitda_growth,
        eval_eps_trend, eval_margins, eval_interest_coverage,
    ]),
    ('CASH FLOW', 0.35, [
        eval_ocf_trend, eval_earnings_quality, eval_fcf,
        eval_shareholder_return, eval_sbc_ratio,
    ]),
    ('BALANCE SHEET', 0.40, [
        eval_cash_adequacy, eval_debt_over_equity, eval_current_ratio,
        eval_ar_growth, eval_ap_stability, eval_risk_flags,
    ]),
]

STATUS_ICON = {'pass': '✓', 'fail': '✗', 'warn': '⚠', 'skip': '-'}


def evaluate_category(name, weight, eval_funcs, data):
    metrics = [f(data) for f in eval_funcs]

    total_pts = sum(m['weight'] for m in metrics if m['status'] != 'skip')
    earned = 0
    for m in metrics:
        if m['status'] == 'skip':
            continue
        if m['status'] == 'pass':
            earned += m['weight']
        elif m['status'] == 'warn':
            earned += m['weight'] * 0.5

    score = earned / total_pts * 100 if total_pts > 0 else 0

    return {'name': name, 'weight': weight, 'score': score, 'metrics': metrics}


def compute_overall_score(categories):
    total_weight = sum(c['weight'] for c in categories)
    return sum(c['weight'] * c['score'] for c in categories) / total_weight


def print_summary(data):
    info = data.get('info', {})
    parts = []
    price = info.get('currentPrice')
    if price:
        parts.append('Price: ${:.2f}'.format(price))
    mcap = info.get('marketCap')
    if mcap:
        parts.append('MCap: {}'.format(format_value(mcap)))
    for key, label in [('trailingPE', 'P/E(TTM)'), ('priceToSalesTrailing12Months', 'P/S(TTM)'),
                       ('pegRatio', 'PEG'), ('enterpriseToEbitda', 'EV/EBITDA')]:
        val = get_info_val(info, key)
        if val:
            parts.append('{}: {:.1f}'.format(label, val))
    if parts:
        print('  ' + '  '.join(parts))


def print_scorecard(stock_name, categories, overall_score, data):
    width = 80
    print('\n' + '=' * width)
    print('{:^{}}'.format('HEALTH SCORECARD: {}'.format(stock_name), width))
    print('=' * width)

    print_summary(data)

    for cat in categories:
        print('\n--- {} ({:.0f}/100, Weight: {:.0f}%) ---'.format(
            cat['name'], cat['score'], cat['weight'] * 100))
        for m in cat['metrics']:
            icon = STATUS_ICON[m['status']]
            detail = '  ' + m['detail'] if m['detail'] else ''
            print('  {} {:<24}{:<24}{}'.format(icon, m['name'], m['value'], detail))

    print('\n' + '=' * width)
    print('  OVERALL SCORE: {:.0f} / 100'.format(overall_score))
    print('=' * width + '\n')


def score_stock(stock_name):
    data = load_all_data(stock_name)

    categories = []
    for name, weight, funcs in CATEGORIES:
        cat = evaluate_category(name, weight, funcs, data)
        categories.append(cat)

    overall_score = compute_overall_score(categories)
    print_scorecard(stock_name, categories, overall_score, data)

    return {'stock_name': stock_name, 'overall_score': overall_score, 'categories': categories}


def print_ranking(results):
    results.sort(key=lambda r: r['overall_score'], reverse=True)
    header = '{:<10} {:>8} {:>8} {:>8} {:>8}'.format(
        'Stock', 'Income', 'CF', 'BS', 'Total')
    width = len(header) + 4
    print('\n' + '=' * width)
    print('{:^{}}'.format('HEALTH RANKING', width))
    print('=' * width)
    print('  ' + header)
    print('  ' + '-' * len(header))
    for r in results:
        cats = {c['name']: c['score'] for c in r['categories']}
        print('  {:<10} {:>7.0f} {:>7.0f} {:>7.0f} {:>7.0f}'.format(
            r['stock_name'],
            cats.get('INCOME STATEMENT', 0),
            cats.get('CASH FLOW', 0),
            cats.get('BALANCE SHEET', 0),
            r['overall_score']))
    print('=' * width + '\n')


def main():
    results = []
    targets = sys.argv[1:] if len(sys.argv) > 1 else ALL
    for stock_name in targets:
        if stock_name in SKIP:
            continue
        results.append(score_stock(stock_name))
    if len(results) > 1:
        print_ranking(results)


if __name__ == '__main__':
    main()
