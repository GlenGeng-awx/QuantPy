import sys
from fundamental.health.data import load_all_data
from fundamental.health.income import (
    eval_revenue_growth, eval_op_income_growth, eval_net_income_growth, eval_eps_trend,
    eval_margins, eval_interest_coverage,
)
from fundamental.health.cashflow import (
    eval_ocf_trend, eval_earnings_quality, eval_fcf, eval_buyback, eval_dividend,
    eval_net_buyback, eval_sbc_ratio
)
from fundamental.health.balance_sheet import (
    eval_current_ratio, eval_cash_adequacy, eval_debt_over_equity,
    eval_ar_growth, eval_ap_stability,
)

CATEGORIES = [
    ('INCOME STATEMENT', 0.40, [
        eval_revenue_growth, eval_op_income_growth, eval_net_income_growth,
        eval_eps_trend, eval_margins, eval_interest_coverage,
    ]),
    ('CASH FLOW', 0.35, [
        eval_ocf_trend, eval_earnings_quality, eval_fcf, eval_buyback, eval_dividend,
        eval_net_buyback, eval_sbc_ratio
    ]),
    ('BALANCE SHEET', 0.25, [
        eval_current_ratio, eval_cash_adequacy, eval_debt_over_equity,
        eval_ar_growth, eval_ap_stability,
    ]),
]

STATUS_ICON = {'pass': '✓', 'fail': '✗', 'warn': '⚠', 'skip': '-'}
STATUS_SCORE = {'pass': 1.0, 'warn': 0.5, 'fail': 0.0}


def evaluate_category(name, weight, eval_funcs, data):
    metrics = [f(data) for f in eval_funcs]

    scored = [(m['weight'], STATUS_SCORE[m['status']]) for m in metrics if m['status'] != 'skip']
    if scored:
        total_weight = sum(w for w, _ in scored)
        score = sum(w * s for w, s in scored) / total_weight * 100
    else:
        score = 0

    return {'name': name, 'weight': weight, 'score': score, 'metrics': metrics}


def compute_overall_score(categories):
    total_weight = sum(c['weight'] for c in categories)
    return sum(c['weight'] * c['score'] for c in categories) / total_weight


def print_scorecard(stock_name, categories, overall_score):
    width = 80
    print('\n' + '=' * width)
    print('{:^{}}'.format('HEALTH SCORECARD: {}'.format(stock_name), width))
    print('=' * width)

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
    print_scorecard(stock_name, categories, overall_score)

    return {'stock_name': stock_name, 'overall_score': overall_score, 'categories': categories}


def main():
    if len(sys.argv) > 1:
        for stock_name in sys.argv[1:]:
            score_stock(stock_name.upper())
    else:
        from conf import ALL, CN_INDEX, US_INDEX
        skip = set(CN_INDEX + US_INDEX)
        for stock_name in ALL:
            if stock_name in skip:
                continue
            score_stock(stock_name)


if __name__ == '__main__':
    main()
