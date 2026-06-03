from fundamental.data import get_val, get_series, format_value
from fundamental.health.helpers import growth_rate, make_result, ttm_compare_col


# ===================== 3yr (100 pts) =====================

def _check_3yr_trend(data, field, label, pts):
    series = get_series(data['income_annual'], field)
    vals = [v for _, v in series[:3] if v is not None]

    if len(vals) < 3:
        return make_result(label, 'skip', '-', 'Insufficient data', pts)

    growing = vals[0] > vals[1] > vals[2]
    positive = all(v > 0 for v in vals)

    latest = format_value(vals[0])
    g = growth_rate(vals[0], vals[1])
    pct = ' ({:+.1f}%)'.format(g * 100) if g is not None else ''
    value = '{}{}'.format(latest, pct)

    detail = '{} -> {} -> {}'.format(format_value(vals[2]), format_value(vals[1]), format_value(vals[0]))

    if positive and growing:
        status = 'pass'
    elif positive:
        status = 'warn'
    else:
        status = 'fail'
    return make_result(label, status, value, detail, pts)


def _check_3yr_gm_trend(data, pts):
    series_gp = get_series(data['income_annual'], 'Gross Profit')
    series_rev = get_series(data['income_annual'], 'Total Revenue')
    gp_vals = [v for _, v in series_gp[:3] if v is not None]
    rev_vals = [v for _, v in series_rev[:3] if v is not None and v > 0]

    if len(gp_vals) < 3 or len(rev_vals) < 3:
        return make_result('GM Trend', 'skip', '-', 'Insufficient data', pts)

    gms = [gp / rev for gp, rev in zip(gp_vals, rev_vals)]

    value = '{:.1f}%'.format(gms[0] * 100)
    drop = gms[0] - gms[2]

    detail = '{:.1f}% -> {:.1f}% -> {:.1f}%'.format(gms[2] * 100, gms[1] * 100, gms[0] * 100)

    if gms[0] >= gms[2]:
        status = 'pass'
    elif drop >= -0.05:
        status = 'warn'
    else:
        status = 'fail'
    return make_result('GM Trend', status, value, detail, pts)


def eval_income_3yr(data):
    return [
        _check_3yr_trend(data, 'Total Revenue', 'Revenue Trend', 20),
        _check_3yr_trend(data, 'Operating Income', 'Op Income Trend', 20),
        _check_3yr_trend(data, 'EBITDA', 'EBITDA Trend', 15),
        _check_3yr_trend(data, 'Diluted EPS', 'EPS Trend', 25),
        _check_3yr_gm_trend(data, 20),
    ]


# ===================== TTM (100 pts) =====================

def _check_ttm_growth(data, field, label, pts):
    ttm_df = data['income_ttm']
    ttm_val = get_val(ttm_df, field)

    annual_df = data['income_annual']
    annual_col = ttm_compare_col(ttm_df, annual_df)
    annual_val = get_val(annual_df, field, annual_col)

    if ttm_val is None or annual_val is None:
        return make_result(label, 'skip', '-', 'No data', pts)

    g = growth_rate(ttm_val, annual_val)
    value = '{} ({:+.1f}%)'.format(format_value(ttm_val), g * 100) if g is not None else format_value(ttm_val)
    detail = 'LY: {}'.format(format_value(annual_val))

    if g is None:
        status = 'skip'
    elif g > 0:
        status = 'pass'
    elif g >= -0.03:
        status = 'warn'
    else:
        status = 'fail'
    return make_result(label, status, value, detail, pts)


def _eval_ttm_margins(data, pts):
    ttm = data['income_ttm']
    revenue = get_val(ttm, 'Total Revenue')
    gross_profit = get_val(ttm, 'Gross Profit')
    net_income = get_val(ttm, 'Net Income')

    gm = gross_profit / revenue if revenue and gross_profit else None
    nm = net_income / revenue if revenue and net_income else None

    gm_str = '{:.1f}%'.format(gm * 100) if gm else '-'
    nm_str = '{:.1f}%'.format(nm * 100) if nm else '-'
    value = 'GM: {}, NM: {}'.format(gm_str, nm_str)

    if (gm and gm > 0.5) or (nm and nm > 0.15):
        status = 'pass'
    elif (gm and gm > 0.3) or (nm and nm > 0.10):
        status = 'warn'
    else:
        status = 'fail'
    return make_result('Margins', status, value, '', pts)


def _eval_ttm_interest_coverage(data, pts):
    ttm = data['income_ttm']
    op_income = get_val(ttm, 'Operating Income')
    int_exp = get_val(ttm, 'Interest Expense')

    if op_income is None:
        return make_result('Interest Coverage', 'skip', '-', 'No data', pts)

    if int_exp is None or int_exp == 0:
        lt_debt = get_val(data['bs_quarterly'], 'Long Term Debt')
        if lt_debt and lt_debt > 0:
            return make_result('Interest Coverage', 'warn', '-', 'No data (has debt)', pts)
        return make_result('Interest Coverage', 'pass', '-', 'No interest expense', pts)

    ratio = op_income / abs(int_exp)
    value = '{:.1f}x'.format(ratio)
    detail = '{} / {}'.format(format_value(op_income), format_value(abs(int_exp)))

    if ratio > 5:
        status = 'pass'
    elif ratio > 2:
        status = 'warn'
    else:
        status = 'fail'
    return make_result('Interest Coverage', status, value, detail, pts)


def eval_income_ttm(data):
    return [
        _check_ttm_growth(data, 'Total Revenue', 'Revenue vs LY', 20),
        _check_ttm_growth(data, 'Operating Income', 'Op Income vs LY', 20),
        _check_ttm_growth(data, 'EBITDA', 'EBITDA vs LY', 15),
        _check_ttm_growth(data, 'Diluted EPS', 'EPS vs LY', 25),
        _eval_ttm_margins(data, 10),
        _eval_ttm_interest_coverage(data, 10),
    ]


# ===================== 5Q (100 pts) =====================

def _check_q_yoy(data, field, label, pts):
    quarterly = data['income_quarterly']
    if quarterly.empty or len(quarterly.columns) < 5:
        return make_result(label, 'skip', '-', 'Insufficient data', pts)

    new_val = get_val(quarterly, field, 0)
    old_val = get_val(quarterly, field, 4)
    if new_val is None or old_val is None:
        return make_result(label, 'skip', '-', 'No data', pts)

    g = growth_rate(new_val, old_val)
    value = '{} ({:+.1f}%)'.format(format_value(new_val), g * 100) if g is not None else format_value(new_val)
    detail = 'LY Q: {}'.format(format_value(old_val))

    if g is None:
        status = 'skip'
    elif g > 0:
        status = 'pass'
    elif g >= -0.03:
        status = 'warn'
    else:
        status = 'fail'
    return make_result(label, status, value, detail, pts)


def _check_4q_positive(data, field, label, pts):
    quarterly = data['income_quarterly']
    if quarterly.empty or len(quarterly.columns) < 4:
        return make_result(label, 'skip', '-', 'Insufficient data', pts)

    vals = [get_val(quarterly, field, i) for i in range(4)]
    valid = [v for v in vals if v is not None]
    if len(valid) < 4:
        return make_result(label, 'skip', '-', 'Incomplete data', pts)

    neg_count = sum(1 for v in valid if v <= 0)
    value = '{}'.format(format_value(valid[0]))
    detail = '{}/4 positive'.format(4 - neg_count)

    if neg_count == 0:
        status = 'pass'
    elif neg_count == 1:
        status = 'warn'
    else:
        status = 'fail'
    return make_result(label, status, value, detail, pts)


def _check_4q_margin_trend(data, numerator_field, denominator_field, label, pts):
    quarterly = data['income_quarterly']
    if quarterly.empty or len(quarterly.columns) < 4:
        return make_result(label, 'skip', '-', 'Insufficient data', pts)

    margins = []
    for i in range(4):
        num = get_val(quarterly, numerator_field, i)
        den = get_val(quarterly, denominator_field, i)
        if num is None or den is None or den == 0:
            margins.append(None)
        else:
            margins.append(num / den)

    valid = [m for m in margins if m is not None]
    if len(valid) < 4:
        return make_result(label, 'skip', '-', 'Incomplete data', pts)

    value = '{:.1f}%'.format(margins[0] * 100)
    drop = margins[0] - margins[3]
    detail = '{:.1f}% -> {:.1f}%'.format(margins[3] * 100, margins[0] * 100)

    if margins[0] >= margins[3]:
        status = 'pass'
    elif drop >= -0.03:
        status = 'warn'
    else:
        status = 'fail'
    return make_result(label, status, value, detail, pts)


def eval_income_5q(data):
    return [
        _check_q_yoy(data, 'Total Revenue', 'Revenue Q YoY', 10),
        _check_q_yoy(data, 'Operating Income', 'Op Income Q YoY', 10),
        _check_q_yoy(data, 'EBITDA', 'EBITDA Q YoY', 10),
        _check_q_yoy(data, 'Diluted EPS', 'EPS Q YoY', 15),
        _check_4q_positive(data, 'Total Revenue', 'Revenue 4Q +', 10),
        _check_4q_positive(data, 'Operating Income', 'Op Income 4Q +', 15),
        _check_4q_margin_trend(data, 'Gross Profit', 'Total Revenue', 'GM Trend 4Q', 15),
        _check_4q_margin_trend(data, 'Net Income', 'Total Revenue', 'NM Trend 4Q', 15),
    ]
