from fundamental.data import get_val, get_series, format_value
from fundamental.health.helpers import growth_rate, make_result, ttm_compare_col


# ===================== 3yr (100 pts) =====================

def _compute_de(df, col):
    lt_debt = get_val(df, 'Long Term Debt', col)
    ct_debt = get_val(df, 'Current Debt', col)
    equity = get_val(df, 'Stockholders Equity', col)
    total_debt = (lt_debt or 0) + (ct_debt or 0)
    if equity is None or equity <= 0 or total_debt <= 0:
        return None
    return total_debt / equity


def _compute_cr(df, col):
    ca = get_val(df, 'Current Assets', col)
    cl = get_val(df, 'Current Liabilities', col)
    if not ca or not cl:
        return None
    return ca / cl


def _compute_goodwill_ratio(df, col):
    gw = get_val(df, 'Goodwill And Other Intangible Assets', col)
    ta = get_val(df, 'Total Assets', col)
    if gw is None or ta is None or ta <= 0:
        return None
    return gw / ta


def _eval_3yr_trend(data, compute_fn, label, pts, rising_is_bad=True, warn_threshold=None):
    """3yr 趋势通用函数。rising_is_bad=True 表示上升是坏事（如 D/E），False 表示下降是坏事（如 CR）"""
    df = data['bs_annual']
    if df.empty or len(df.columns) < 3:
        return make_result(label, 'skip', '-', 'Insufficient data', pts)

    vals = [compute_fn(df, i) for i in range(3)]
    valid = [v for v in vals if v is not None]
    if len(valid) < 3:
        return make_result(label, 'skip', '-', 'Incomplete data', pts)

    value = '{:.2f}'.format(vals[0])
    detail = '{:.2f} -> {:.2f} -> {:.2f}'.format(vals[2], vals[1], vals[0])
    delta = vals[0] - vals[2]

    if rising_is_bad:
        if delta <= 0:
            status = 'pass'
        elif warn_threshold and delta <= warn_threshold:
            status = 'warn'
        else:
            status = 'fail'
    else:
        if delta >= 0:
            status = 'pass'
        elif warn_threshold and abs(delta) <= warn_threshold:
            status = 'warn'
        else:
            status = 'fail'

    return make_result(label, status, value, detail, pts)


def eval_bs_3yr(data):
    return [
        _eval_3yr_trend(data, _compute_de, 'D/E Trend', 35,
                        rising_is_bad=True, warn_threshold=0.3),
        _eval_3yr_trend(data, _compute_cr, 'CR Trend', 35,
                        rising_is_bad=False, warn_threshold=0.3),
        _eval_3yr_trend(data, _compute_goodwill_ratio, 'GW/Assets Trend', 30,
                        rising_is_bad=True, warn_threshold=0.05),
    ]


# ===================== TTM (100 pts) =====================
# BS 无 TTM 累加概念，实际为最新季 vs 一年前同季 (Q0 vs Q4) 的 YoY 对比

def _eval_ttm_vs_revenue(data, bs_field, label, pts, fail_on_exceed=True):
    bs = data['bs_quarterly']
    income = data['income_quarterly']

    if bs.empty or income.empty or len(bs.columns) < 5 or len(income.columns) < 5:
        return make_result(label, 'skip', '-', 'Insufficient data', pts)

    new = get_val(bs, bs_field, 0)
    old = get_val(bs, bs_field, 4)
    rev_new = get_val(income, 'Total Revenue', 0)
    rev_old = get_val(income, 'Total Revenue', 4)

    item_g = growth_rate(new, old)
    rev_g = growth_rate(rev_new, rev_old)

    if item_g is None or rev_g is None:
        return make_result(label, 'skip', '-', 'No data', pts)

    value = '{:+.0f}% vs Rev {:+.0f}%'.format(item_g * 100, rev_g * 100)
    detail = '{} -> {}'.format(format_value(old), format_value(new))

    if item_g <= rev_g * 1.5:
        status = 'pass'
    else:
        status = 'fail' if fail_on_exceed else 'warn'
    return make_result(label, status, value, detail, pts)


def _eval_ttm_capex_ocf(data, pts):
    capex = get_val(data['cf_ttm'], 'Capital Expenditure')
    ocf = get_val(data['cf_ttm'], 'Operating Cash Flow')

    if capex is None or ocf is None:
        return make_result('CapEx/OCF', 'skip', '-', 'No data', pts)
    if ocf <= 0:
        return make_result('CapEx/OCF', 'fail', '-', 'Negative OCF', pts)

    ratio = abs(capex) / ocf
    value = '{:.0f}%'.format(ratio * 100)
    detail = 'CapEx {} / OCF {} (from CF TTM)'.format(format_value(abs(capex)), format_value(ocf))

    if ratio < 0.5:
        status = 'pass'
    elif ratio < 0.8:
        status = 'warn'
    else:
        rev_ttm = get_val(data['income_ttm'], 'Total Revenue')
        annual_col = ttm_compare_col(data['income_ttm'], data['income_annual'])
        rev_annual = get_val(data['income_annual'], 'Total Revenue', annual_col)
        rev_growing = rev_ttm and rev_annual and rev_ttm > rev_annual
        if rev_growing:
            status = 'warn'
            detail += ' (high CapEx, revenue growing)'
        else:
            status = 'fail'
    return make_result('CapEx/OCF', status, value, detail, pts)


def eval_bs_ttm(data):
    return [
        _eval_ttm_vs_revenue(data, 'Accounts Receivable', 'AR vs Revenue', 35, fail_on_exceed=True),
        _eval_ttm_vs_revenue(data, 'Accounts Payable', 'AP vs Revenue', 30, fail_on_exceed=False),
        _eval_ttm_vs_revenue(data, 'Inventory', 'Inventory vs Revenue', 10, fail_on_exceed=False),
        _eval_ttm_capex_ocf(data, 25),
    ]


# ===================== 5Q (100 pts) =====================

def _eval_5q_cash_debt(data, pts):
    df = data['bs_quarterly']

    liquidity = get_val(df, 'Cash Cash Equivalents And Short Term Investments')
    if liquidity is None:
        liquidity = (get_val(df, 'Cash And Cash Equivalents') or 0) + (get_val(df, 'Other Short Term Investments') or 0)

    lt_debt = get_val(df, 'Long Term Debt')
    ct_debt = get_val(df, 'Current Debt')
    total_debt = (lt_debt or 0) + (ct_debt or 0)

    if total_debt <= 0:
        return make_result('Cash/Debt', 'pass', format_value(liquidity), 'No debt', pts)

    ratio = liquidity / total_debt
    value = '{:.2f}x'.format(ratio)
    detail = '{} / {}'.format(format_value(liquidity), format_value(total_debt))

    if ratio > 0.5:
        status = 'pass'
    elif ratio > 0.3:
        status = 'warn'
    else:
        status = 'fail'
    return make_result('Cash/Debt', status, value, detail, pts)


def _eval_5q_debt_equity(data, pts):
    df = data['bs_quarterly']

    lt_debt = get_val(df, 'Long Term Debt')
    ct_debt = get_val(df, 'Current Debt')
    total_debt = (lt_debt or 0) + (ct_debt or 0)

    equity = get_val(df, 'Stockholders Equity')

    if total_debt <= 0:
        return make_result('Debt/Equity', 'pass', '-', 'No debt', pts)

    if not equity or equity <= 0:
        liquidity = get_val(df, 'Cash Cash Equivalents And Short Term Investments')
        if liquidity is None:
            liquidity = (get_val(df, 'Cash And Cash Equivalents') or 0)
        if liquidity and total_debt > 0 and liquidity / total_debt > 0.3:
            return make_result('Debt/Equity', 'warn',
                               'Neg equity', 'Cash/Debt {:.2f}'.format(liquidity / total_debt), pts)
        return make_result('Debt/Equity', 'fail', 'Neg equity', '', pts)

    ratio = total_debt / equity
    value = '{:.2f}'.format(ratio)
    detail = '{} / {}'.format(format_value(total_debt), format_value(equity))

    if ratio < 1.0:
        status = 'pass'
    elif ratio < 2.0:
        status = 'warn'
    else:
        status = 'fail'
    return make_result('Debt/Equity', status, value, detail, pts)


def _eval_5q_current_ratio(data, pts):
    df = data['bs_quarterly']

    ca = get_val(df, 'Current Assets')
    cl = get_val(df, 'Current Liabilities')
    dr = get_val(df, 'Current Deferred Revenue')

    if not ca or not cl:
        return make_result('Current Ratio', 'skip', '-', 'No data', pts)

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
    return make_result('Current Ratio', status, value, detail, pts)


def _eval_5q_ar_yoy(data, pts):
    bs = data['bs_quarterly']
    income = data['income_quarterly']
    if bs.empty or income.empty or len(bs.columns) < 5 or len(income.columns) < 5:
        return make_result('AR YoY', 'skip', '-', 'Insufficient data', pts)

    ar_new = get_val(bs, 'Accounts Receivable', 0)
    ar_old = get_val(bs, 'Accounts Receivable', 4)
    rev_new = get_val(income, 'Total Revenue', 0)
    rev_old = get_val(income, 'Total Revenue', 4)

    ar_g = growth_rate(ar_new, ar_old)
    rev_g = growth_rate(rev_new, rev_old)

    if ar_g is None or rev_g is None:
        return make_result('AR YoY', 'skip', '-', 'No data', pts)

    value = 'AR {:+.0f}% vs Rev {:+.0f}%'.format(ar_g * 100, rev_g * 100)
    status = 'pass' if ar_g <= rev_g * 1.5 else 'fail'
    return make_result('AR YoY', status, value, '', pts)


def _eval_5q_ap_yoy(data, pts):
    bs = data['bs_quarterly']
    if bs.empty or len(bs.columns) < 5:
        return make_result('AP YoY', 'skip', '-', 'Insufficient data', pts)

    ap_new = get_val(bs, 'Accounts Payable', 0)
    ap_old = get_val(bs, 'Accounts Payable', 4)
    if ap_new is None or ap_old is None or ap_old == 0:
        return make_result('AP YoY', 'skip', '-', 'No data', pts)

    change = growth_rate(ap_new, ap_old)
    value = '{:+.0f}%'.format(change * 100)
    status = 'pass' if abs(change) < 0.5 else 'fail'
    return make_result('AP YoY', status, value, '', pts)


def eval_bs_5q(data):
    return [
        _eval_5q_cash_debt(data, 25),
        _eval_5q_debt_equity(data, 20),
        _eval_5q_current_ratio(data, 15),
        _eval_5q_ar_yoy(data, 20),
        _eval_5q_ap_yoy(data, 20),
    ]


# ===================== Risk Flags =====================

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
