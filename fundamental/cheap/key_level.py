"""
Key Levels (0.30) — requires core_banking configuration:
    Elliott Hit (0.10): close within ±3% of an Elliott wave point
    Neck Line Hit (0.10): close within ±3% of a neck line
    Trend Line Hit (0.10): close within ±3% of a primary/secondary line
"""
from fundamental.health.data import make_result
from util import shrink_date_str, get_idx_by_date

W_ELLIOTT = 0.10
W_NECK = 0.10
W_TREND = 0.10

TOLERANCE = 0.03


def _recent_dates(stock_df, n=5):
    return set(stock_df['Date'].iloc[-n:].apply(shrink_date_str).values)


def _recent_closes(stock_df, n=5):
    return [float(v) for v in stock_df['close'].iloc[-n:].values]


def _hit_price(closes, target):
    for close in closes:
        if abs(close - target) / target <= TOLERANCE:
            return close
    return None


def eval_elliott_hit(data):
    stock_df = data['stock_df']
    elliott_dates = data['elliott_dates']

    if not elliott_dates:
        return make_result('Elliott Hit', 'fail', '-', 'No config', W_ELLIOTT)

    prices = []
    for date in elliott_dates:
        try:
            idx = get_idx_by_date(stock_df, date)
            prices.append(float(stock_df.loc[idx]['close']))
        except (IndexError, KeyError):
            continue

    if not prices:
        return make_result('Elliott Hit', 'fail', '-', 'No config', W_ELLIOTT)

    closes = _recent_closes(stock_df)
    for target in prices:
        hit = _hit_price(closes, target)
        if hit:
            value = '{:.1f}'.format(target)
            detail = 'Close {:.1f} near {:.1f}'.format(hit, target)
            return make_result('Elliott Hit', 'pass', value, detail, W_ELLIOTT)

    return make_result('Elliott Hit', 'fail', '-', '', W_ELLIOTT)


def eval_neck_line_hit(data):
    neck_lines = data['neck_lines']

    if not neck_lines:
        return make_result('Neck Line Hit', 'fail', '-', 'No config', W_NECK)

    stock_df = data['stock_df']
    closes = _recent_closes(stock_df)

    for dates, prices in neck_lines:
        target = prices[0]
        hit = _hit_price(closes, target)
        if hit:
            value = '{:.1f}'.format(target)
            detail = 'Close {:.1f} near {:.1f}'.format(hit, target)
            return make_result('Neck Line Hit', 'pass', value, detail, W_NECK)

    return make_result('Neck Line Hit', 'fail', '-', '', W_NECK)


def eval_trend_line_hit(data):
    primary = data['primary_lines']
    secondary = data['secondary_lines']
    all_lines = primary + secondary

    if not all_lines:
        return make_result('Trend Line Hit', 'fail', '-', 'No config', W_TREND)

    stock_df = data['stock_df']
    recent = _recent_dates(stock_df)
    closes = _recent_closes(stock_df)

    for line in all_lines:
        for date, target in zip(line[0], line[1]):
            if shrink_date_str(date) in recent:
                hit = _hit_price(closes, target)
                if hit:
                    label = 'primary' if line in primary else 'secondary'
                    value = '{:.1f}'.format(target)
                    detail = 'Close {:.1f} near {} {:.1f}'.format(hit, label, target)
                    return make_result('Trend Line Hit', 'pass', value, detail, W_TREND)

    return make_result('Trend Line Hit', 'fail', '-', '', W_TREND)
