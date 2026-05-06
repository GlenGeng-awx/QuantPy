"""
Balance Sheet 评价标准 (权重 25%)

Current Ratio (0.04):
    最新季度 流动比率 > 1.0 为 pass，0.8-1.0 为 warn
    剔除递延收入后 > 1.0 亦视为 pass（SaaS 公司常见）

Cash Adequacy (0.04):
    最新季度 (现金 + 短期投资) / 总债务 > 0.5 为 pass，> 0.3 为 warn

Debt/Equity (0.03):
    最新季度 总债务 / 股东权益 < 1.0 为 pass，1.0-2.0 为 warn，> 2.0 为 fail
    无债务直接 pass

AR Growth (0.03):
    季度 YoY 应收增速 ≤ 营收增速 × 1.5 为 pass

AP Stability (0.02):
    最近四个季度 QoQ 环比波动 < 50% 为 pass
"""
from fundamental.health.data import get_val, get_series, growth_rate, make_result, format_value

W_CURRENT_RATIO = 0.04
W_CASH_ADEQUACY = 0.04
W_DEBT_EQUITY = 0.03
W_AR_GROWTH = 0.03
W_AP_STABILITY = 0.02


def eval_current_ratio(data):
    df = data['bs_quarterly']
    ca = get_val(df, 'Current Assets')
    cl = get_val(df, 'Current Liabilities')
    dr = get_val(df, 'Current Deferred Revenue')

    if not ca or not cl:
        return make_result('Current Ratio', 'skip', '-', 'No data', W_CURRENT_RATIO)

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

    return make_result('Current Ratio', status, value, detail, W_CURRENT_RATIO)


def eval_cash_adequacy(data):
    df = data['bs_quarterly']
    liquidity = get_val(df, 'Cash Cash Equivalents And Short Term Investments')
    if liquidity is None:
        liquidity = (get_val(df, 'Cash And Cash Equivalents') or 0) + (get_val(df, 'Other Short Term Investments') or 0)
    lt_debt = get_val(df, 'Long Term Debt')
    ct_debt = get_val(df, 'Current Debt')
    total_debt = (lt_debt or 0) + (ct_debt or 0)

    if total_debt <= 0:
        return make_result('Cash Adequacy', 'pass', format_value(liquidity), 'No debt', W_CASH_ADEQUACY)

    ratio = liquidity / total_debt
    value = '{:.2f}x'.format(ratio)
    detail = '{} / Debt {}'.format(format_value(liquidity), format_value(total_debt))

    if ratio > 0.5:
        status = 'pass'
    elif ratio > 0.3:
        status = 'warn'
    else:
        status = 'fail'

    return make_result('Cash Adequacy', status, value, detail, W_CASH_ADEQUACY)


def eval_debt_over_equity(data):
    df = data['bs_quarterly']
    lt_debt = get_val(df, 'Long Term Debt')
    ct_debt = get_val(df, 'Current Debt')
    equity = get_val(df, 'Stockholders Equity')

    total_debt = (lt_debt or 0) + (ct_debt or 0)

    if total_debt <= 0:
        return make_result('Debt/Equity', 'pass', '-', 'No debt', W_DEBT_EQUITY)

    if not equity or equity <= 0:
        return make_result('Debt/Equity', 'fail', '-', 'Negative equity', W_DEBT_EQUITY)

    ratio = total_debt / equity
    value = '{:.2f}'.format(ratio)
    detail = 'Debt {} / Equity {}'.format(format_value(total_debt), format_value(equity))

    if ratio < 1.0:
        status = 'pass'
    elif ratio < 2.0:
        status = 'warn'
    else:
        status = 'fail'

    return make_result('Debt/Equity', status, value, detail, W_DEBT_EQUITY)


def eval_ar_growth(data):
    bs = data['bs_quarterly']
    income = data['income_quarterly']

    if bs.empty or income.empty or len(bs.columns) < 5 or len(income.columns) < 5:
        return make_result('AR Growth', 'skip', '-', 'Insufficient data', W_AR_GROWTH)

    ar_new = get_val(bs, 'Accounts Receivable', 0)
    ar_old = get_val(bs, 'Accounts Receivable', 4)
    rev_new = get_val(income, 'Total Revenue', 0)
    rev_old = get_val(income, 'Total Revenue', 4)

    ar_g = growth_rate(ar_new, ar_old)
    rev_g = growth_rate(rev_new, rev_old)

    if ar_g is None or rev_g is None:
        return make_result('AR Growth', 'skip', '-', 'No data', W_AR_GROWTH)

    value = 'AR: {:+.0f}%, Rev: {:+.0f}%'.format(ar_g * 100, rev_g * 100)

    if rev_g <= 0:
        status = 'pass' if ar_g <= 0 else 'warn'
    elif ar_g <= rev_g * 1.5:
        status = 'pass'
    elif ar_g <= rev_g * 2.0:
        status = 'warn'
    else:
        status = 'fail'

    return make_result('AR Growth', status, value, '', W_AR_GROWTH)


def eval_ap_stability(data):
    series = get_series(data['bs_quarterly'], 'Accounts Payable', count=4)
    vals = [v for _, v in series if v is not None]

    if len(vals) < 2:
        return make_result('AP Stability', 'skip', '-', 'No data', W_AP_STABILITY)

    max_qoq = 0
    for i in range(len(vals) - 1):
        g = growth_rate(vals[i], vals[i + 1])
        if g is not None:
            max_qoq = max(max_qoq, abs(g))

    value = format_value(vals[0])

    if max_qoq < 0.5:
        status = 'pass'
        detail = 'Stable'
    elif max_qoq < 1.0:
        status = 'warn'
        detail = 'QoQ jump {:.0f}%'.format(max_qoq * 100)
    else:
        status = 'fail'
        detail = 'QoQ jump {:.0f}%'.format(max_qoq * 100)

    return make_result('AP Stability', status, value, detail, W_AP_STABILITY)


