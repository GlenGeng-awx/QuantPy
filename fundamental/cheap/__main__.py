import sys
from base_engine import BaseEngine
from preload_conf import period
import guru

from fundamental.cheap.price_signal import (
    eval_1y_drawdown, eval_2y_drawdown, eval_near_52w_low,
    eval_crash_20d, eval_minmax_hit,
)
from fundamental.cheap.key_level import (
    eval_elliott_hit, eval_neck_line_hit, eval_trend_line_hit,
)

CATEGORIES = [
    ('PRICE SIGNAL', 0.70, [
        eval_1y_drawdown, eval_2y_drawdown, eval_near_52w_low, eval_crash_20d, eval_minmax_hit,
    ]),
    ('KEY LEVELS', 0.30, [
        eval_elliott_hit, eval_neck_line_hit, eval_trend_line_hit,
    ]),
]

STATUS_ICON = {'pass': '✓', 'fail': '✗', 'warn': '⚠', 'skip': '-'}
STATUS_SCORE = {'pass': 1.0, 'warn': 0.5, 'fail': 0.0}


def load_data(stock_name):
    from_date, to_date, interval = period(8)
    engine = BaseEngine(stock_name, from_date, to_date, interval)
    context = guru.calculate(engine.stock_df)
    return {
        'stock_name': stock_name,
        'stock_df': engine.stock_df,
        'primary_lines': engine.primary_line.primary_lines,
        'secondary_lines': engine.secondary_line.secondary_lines,
        'neck_lines': engine.neck_line.neck_lines,
        'elliott_dates': engine.elliott.x,
        'guru_context': context,
    }


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
    print('{:^{}}'.format('CHEAP SCORECARD: {}'.format(stock_name), width))
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
    data = load_data(stock_name)

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
