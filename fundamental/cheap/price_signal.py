"""
Price Signal (0.70), 8 items each 0.0875:
    1Y Drawdown: week low vs 1-year high, >40% pass, 20-40% warn, <20% fail
    2Y Drawdown: week low vs 2-year high, >60% pass, 30-60% warn, <30% fail
    Near 52W Low: current price vs 52-week low, <=10% pass, <=20% warn, >20% fail
    Crash 5d: crash 5d signal in past week
    Crash 10d: crash 10d signal in past week
    Crash 20d: crash 20d signal in past week
    High Vol: high volume signal in past week
    MinMax 4th Hit: close within ±3% of a 4th-level local min/max
"""
from fundamental.health.data import make_result
from technical.min_max import LOCAL_MAX_PRICE_4TH, LOCAL_MIN_PRICE_4TH
from util import shrink_date_str

W = 0.0875

TOLERANCE = 0.03


# --- drawdown ---

def _eval_drawdown(data, days, pass_thresh, warn_thresh, label):
    stock_df = data['stock_df']
    if stock_df.shape[0] < days:
        return make_result(label, 'skip', '-', 'Insufficient data', W)

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

    return make_result(label, status, value, detail, W)


def eval_1y_drawdown(data):
    return _eval_drawdown(data, 252, 40, 20, '1Y Drawdown')


def eval_2y_drawdown(data):
    return _eval_drawdown(data, 504, 60, 30, '2Y Drawdown')


def eval_near_52w_low(data):
    stock_df = data['stock_df']
    if stock_df.shape[0] < 252:
        return make_result('Near 52W Low', 'skip', '-', 'Insufficient data', W)

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

    return make_result('Near 52W Low', status, value, detail, W)


# --- guru signals ---

def _eval_guru_signal(data, key, label):
    stock_df = data['stock_df']
    recent_dates = set(stock_df['Date'].iloc[-5:].apply(shrink_date_str).values)

    hit_dates = data['guru_context'].get(key, [])
    hits = [d for d in hit_dates if shrink_date_str(d) in recent_dates]

    if hits:
        return make_result(label, 'pass', 'Hit', '{} signal(s)'.format(len(hits)), W)
    return make_result(label, 'fail', '-', '', W)


def eval_crash_5d(data):
    return _eval_guru_signal(data, 'crash 5d', 'Crash 5d')


def eval_crash_10d(data):
    return _eval_guru_signal(data, 'crash 10d', 'Crash 10d')


def eval_crash_20d(data):
    return _eval_guru_signal(data, 'crash 20d', 'Crash 20d')


def eval_high_vol(data):
    return _eval_guru_signal(data, 'high vol', 'High Vol')


# --- price hit ---

def _hit_price(closes, target):
    for close in closes:
        if abs(close - target) / target <= TOLERANCE:
            return close
    return None


def eval_minmax_hit(data):
    stock_df = data['stock_df']

    minmax_df = stock_df[stock_df[LOCAL_MAX_PRICE_4TH] | stock_df[LOCAL_MIN_PRICE_4TH]]
    if minmax_df.empty:
        return make_result('MinMax 4th Hit', 'fail', '-', 'No data', W)

    targets = [float(v) for v in minmax_df['close'].values]
    closes = [float(v) for v in stock_df['close'].iloc[-5:].values]

    for target in targets:
        hit = _hit_price(closes, target)
        if hit:
            value = '{:.1f}'.format(target)
            detail = 'Close {:.1f} near {:.1f}'.format(hit, target)
            return make_result('MinMax 4th Hit', 'pass', value, detail, W)

    return make_result('MinMax 4th Hit', 'fail', '-', '', W)
