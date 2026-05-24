"""
Balance Sheet (100 pts, weight 40%)
  Cash Adequacy     30    最新季快照
  Debt/Equity       30    最新季快照
  Current Ratio     20    最新季快照 (含递延收入豁免)
  AR Growth         10    最新季 YoY
  AP Stability      10    最新季 YoY
  Risk Flags       -15    商誉+经营租赁倒扣（额外扣分）
"""
from fundamental.data import get_val, get_series, format_value
from fundamental.health.helpers import growth_rate, make_result

PTS_CASH = 30
PTS_DE = 30
PTS_CR = 20
PTS_AR = 10
PTS_AP = 10


def eval_cash_adequacy(data):
    df = data['bs_quarterly']

    liquidity = get_val(df, 'Cash Cash Equivalents And Short Term Investments')
    if liquidity is None:
        liquidity = (get_val(df, 'Cash And Cash Equivalents') or 0) + (get_val(df, 'Other Short Term Investments') or 0)

    lt_debt = get_val(df, 'Long Term Debt')
    ct_debt = get_val(df, 'Current Debt')
    total_debt = (lt_debt or 0) + (ct_debt or 0)

    if total_debt <= 0:
        return make_result('Cash Adequacy', 'pass', format_value(liquidity), 'No debt', PTS_CASH)

    ratio = liquidity / total_debt
    value = '{:.2f}x'.format(ratio)
    detail = '{} / Debt {}'.format(format_value(liquidity), format_value(total_debt))

    if ratio > 0.5:
        status = 'pass'
    elif ratio > 0.3:
        status = 'warn'
    else:
        status = 'fail'

    return make_result('Cash Adequacy', status, value, detail, PTS_CASH)


def eval_debt_over_equity(data):
    df = data['bs_quarterly']
    lt_debt = get_val(df, 'Long Term Debt')
    ct_debt = get_val(df, 'Current Debt')
    equity = get_val(df, 'Stockholders Equity')

    total_debt = (lt_debt or 0) + (ct_debt or 0)

    if total_debt <= 0:
        return make_result('Debt/Equity', 'pass', '-', 'No debt', PTS_DE)

    if not equity or equity <= 0:
        return make_result('Debt/Equity', 'fail', 'Neg equity', '', PTS_DE)

    ratio = total_debt / equity
    value = '{:.2f}'.format(ratio)
    detail = 'Debt {} / Equity {}'.format(format_value(total_debt), format_value(equity))

    if ratio < 1.0:
        status = 'pass'
    elif ratio < 2.0:
        status = 'warn'
    else:
        status = 'fail'

    return make_result('Debt/Equity', status, value, detail, PTS_DE)


def eval_current_ratio(data):
    df = data['bs_quarterly']
    ca = get_val(df, 'Current Assets')
    cl = get_val(df, 'Current Liabilities')
    dr = get_val(df, 'Current Deferred Revenue')

    if not ca or not cl:
        return make_result('Current Ratio', 'skip', '-', 'No data', PTS_CR)

    raw = ca / cl
    adj = ca / (cl - dr) if dr and (cl - dr) > 0 else None
    effective = max(raw, adj) if adj else raw

    value = '{:.2f}'.format(raw)
    detail = '{} / {}'.format(format_value(ca), format_value(cl))
    if raw < 1.0 and adj and adj > 1.0:
        value += ' (adj: {:.2f})'.format(adj)
        detail += ', excl deferred revenue'

    if effective > 1.0:
        status = 'pass'
    elif effective > 0.8:
        status = 'warn'
    else:
        status = 'fail'

    return make_result('Current Ratio', status, value, detail, PTS_CR)


def eval_ar_growth(data):
    bs = data['bs_quarterly']
    income = data['income_quarterly']

    if bs.empty or income.empty or len(bs.columns) < 5 or len(income.columns) < 5:
        return make_result('AR Growth', 'skip', '-', 'Insufficient data', PTS_AR)

    ar_new = get_val(bs, 'Accounts Receivable', 0)
    ar_old = get_val(bs, 'Accounts Receivable', 4)
    rev_new = get_val(income, 'Total Revenue', 0)
    rev_old = get_val(income, 'Total Revenue', 4)

    ar_g = growth_rate(ar_new, ar_old)
    rev_g = growth_rate(rev_new, rev_old)

    if ar_g is None or rev_g is None:
        return make_result('AR Growth', 'skip', '-', 'No data', PTS_AR)

    value = 'AR: {:+.0f}%, Rev: {:+.0f}%'.format(ar_g * 100, rev_g * 100)

    if ar_g <= rev_g * 1.5:
        status = 'pass'
    elif ar_g <= rev_g * 2.0:
        status = 'warn'
    else:
        status = 'fail'

    return make_result('AR Growth', status, value, '', PTS_AR)


def eval_ap_stability(data):
    bs = data['bs_quarterly']

    if bs.empty or len(bs.columns) < 5:
        return make_result('AP Stability', 'skip', '-', 'Insufficient data', PTS_AP)

    ap_new = get_val(bs, 'Accounts Payable', 0)
    ap_old = get_val(bs, 'Accounts Payable', 4)

    if ap_new is None or ap_old is None or ap_old == 0:
        return make_result('AP Stability', 'skip', '-', 'No data', PTS_AP)

    change = growth_rate(ap_new, ap_old)
    detail = 'YoY {:+.0f}%'.format(change * 100)

    if abs(change) < 0.5:
        status = 'pass'
    elif abs(change) < 1.0:
        status = 'warn'
    else:
        status = 'fail'

    return make_result('AP Stability', status, format_value(ap_new), detail, PTS_AP)


def eval_risk_flags(data):
    df = data['bs_quarterly']
    penalties = 0
    flags = []

    goodwill = get_val(df, 'Goodwill And Other Intangible Assets') or 0
    total_assets = get_val(df, 'Total Assets')

    if total_assets and total_assets > 0 and goodwill / total_assets > 0.3:
        ni_series = get_series(data['income_annual'], 'Net Income')
        ni_vals = [v for _, v in ni_series[:3] if v is not None]
        if len(ni_vals) >= 2 and ni_vals[0] < ni_vals[1]:
            penalties -= 10
            flags.append('Goodwill {:.0f}% + NI declining'.format(goodwill / total_assets * 100))

    lease = get_val(df, 'Capital Lease Obligations') or 0
    if total_assets and total_assets > 0 and lease / total_assets > 0.2:
        penalties -= 5
        flags.append('Lease {:.0f}%'.format(lease / total_assets * 100))

    if penalties == 0:
        return make_result('Risk Flags', 'pass', '-', 'No flags', 0)

    value = '{:+d}'.format(penalties)
    detail = ', '.join(flags)
    return make_result('Risk Flags', 'fail', value, detail, abs(penalties))
