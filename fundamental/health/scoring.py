from fundamental.data import load_statement, load_info, load_price, format_value, get_info_val
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


def load_data(stock_name):
    return {
        'stock_name': stock_name,
        'income_annual': load_statement(stock_name, 'income_annual'),
        'income_quarterly': load_statement(stock_name, 'income_quarterly'),
        'income_ttm': load_statement(stock_name, 'income_ttm'),
        'bs_quarterly': load_statement(stock_name, 'bs_quarterly'),
        'cf_annual': load_statement(stock_name, 'cf_annual'),
        'cf_quarterly': load_statement(stock_name, 'cf_quarterly'),
        'cf_ttm': load_statement(stock_name, 'cf_ttm'),
        'price': load_price(stock_name),
        'info': load_info(stock_name),
    }


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


def evaluate_stock(stock_name):
    data = load_data(stock_name)

    categories = []
    total_weight = 0
    overall_score = 0
    for name, weight, funcs in CATEGORIES:
        cat = evaluate_category(name, weight, funcs, data)
        categories.append(cat)
        total_weight += weight
        overall_score += weight * cat['score']

    overall_score /= total_weight
    return {'stock_name': stock_name, 'overall_score': overall_score,
            'categories': categories, 'data': data}


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


def print_detail(result):
    stock_name = result['stock_name']
    categories = result['categories']
    overall_score = result['overall_score']
    data = result['data']

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
