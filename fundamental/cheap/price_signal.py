"""
Price Signal (0.70):
    1Y Drawdown (0.14): week low vs 1-year high, >40% pass, 20-40% warn, <20% fail
    2Y Drawdown (0.14): week low vs 2-year high, >60% pass, 30-60% warn, <30% fail
    Near 52W Low (0.14): current price vs 52-week low, <=10% pass, <=20% warn, >20% fail
    Crash 20d (0.14): crash 20d signal in past week
    MinMax 4th Hit (0.14): close within ±3% of a 4th-level local min/max
"""
from fundamental.health.data import make_result
from technical.min_max import LOCAL_MAX_PRICE_4TH, LOCAL_MIN_PRICE_4TH
from util import shrink_date_str

W_1Y = 0.14
W_2Y = 0.14
W_52W_LOW = 0.14
W_CRASH = 0.14
W_MINMAX = 0.14

TOLERANCE = 0.03


# --- drawdown ---

def _eval_drawdown(data, days, pass_thresh, warn_thresh, label, weight):
    stock_df = data['stock_df']
    if stock_df.shape[0] < days:
        return make_result(label, 'skip', '-', 'Insufficient data', weight)

    week_low = float(stock_df['close'].iloc[-5:].min())
    period_high = float(stock_df['close'].iloc[-days:].max())
    drawdown = (period_high - week_low) / period_high * 100

    value = '{:.0f}%'.format(drawdown)
    detail = 'Low {:.1f} vs High {:.1f}'.format(week_low, period_high)

    if drawdown >= pass_thresh:
        status = 'pass'
    elif drawdown >= warn_thresh:
        status = 'warn'
    else:
        status = 'fail'

    return make_result(label, status, value, detail, weight)


def eval_1y_drawdown(data):
    return _eval_drawdown(data, 252, 40, 20, '1Y Drawdown', W_1Y)


def eval_2y_drawdown(data):
    return _eval_drawdown(data, 504, 60, 30, '2Y Drawdown', W_2Y)


def eval_near_52w_low(data):
    stock_df = data['stock_df']
    if stock_df.shape[0] < 252:
        return make_result('Near 52W Low', 'skip', '-', 'Insufficient data', W_52W_LOW)

    current = float(stock_df['close'].iloc[-1])
    low_52w = float(stock_df['close'].iloc[-252:].min())
    above = (current - low_52w) / low_52w * 100

    value = '+{:.0f}%'.format(above)
    detail = 'Cur {:.1f} vs Low {:.1f}'.format(current, low_52w)

    if above <= 10:
        status = 'pass'
    elif above <= 20:
        status = 'warn'
    else:
        status = 'fail'

    return make_result('Near 52W Low', status, value, detail, W_52W_LOW)


# --- signals ---

def eval_crash_20d(data):
    stock_df = data['stock_df']
    recent_dates = set(stock_df['Date'].iloc[-5:].apply(shrink_date_str).values)

    hit_dates = data['guru_context'].get('crash 20d', [])
    hits = [d for d in hit_dates if shrink_date_str(d) in recent_dates]

    if hits:
        return make_result('Crash 20d', 'pass', 'Hit', '{} signal(s)'.format(len(hits)), W_CRASH)
    return make_result('Crash 20d', 'fail', '-', '', W_CRASH)


def _hit_price(closes, target):
    for close in closes:
        if abs(close - target) / target <= TOLERANCE:
            return close
    return None


def eval_minmax_hit(data):
    stock_df = data['stock_df']

    minmax_df = stock_df[stock_df[LOCAL_MAX_PRICE_4TH] | stock_df[LOCAL_MIN_PRICE_4TH]]
    if minmax_df.empty:
        return make_result('MinMax 4th Hit', 'fail', '-', 'No data', W_MINMAX)

    targets = [float(v) for v in minmax_df['close'].values]
    closes = [float(v) for v in stock_df['close'].iloc[-5:].values]

    for target in targets:
        hit = _hit_price(closes, target)
        if hit:
            value = '{:.1f}'.format(target)
            detail = 'Close {:.1f} near {:.1f}'.format(hit, target)
            return make_result('MinMax 4th Hit', 'pass', value, detail, W_MINMAX)

    return make_result('MinMax 4th Hit', 'fail', '-', '', W_MINMAX)
