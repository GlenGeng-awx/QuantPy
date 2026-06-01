from fundamental.data import get_val, get_series, format_value
from fundamental.health.helpers import growth_rate, make_result, ttm_compare_col


# ===================== 3yr (100 pts) =====================

def _check_3yr_cf_trend(data, field, label, pts):
    series = get_series(data['cf_annual'], field)
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


def _eval_3yr_ocf_ni(data, pts):
    ocf_series = get_series(data['cf_annual'], 'Operating Cash Flow')
    ni_series = get_series(data['income_annual'], 'Net Income')

    ratios = []
    for i in range(min(3, len(ocf_series), len(ni_series))):
        ocf = ocf_series[i][1]
        ni = ni_series[i][1]
        if ocf is not None and ni is not None and ni > 0:
            ratios.append(ocf / ni)

    if len(ratios) < 2:
        return make_result('OCF/NI 3yr', 'skip', '-', 'Insufficient data', pts)

    avg = sum(ratios) / len(ratios)
    value = 'Avg: {:.2f}'.format(avg)
    detail = '{}/3 years: '.format(len(ratios)) + ', '.join('{:.2f}'.format(r) for r in ratios)

    if avg > 0.8:
        status = 'pass'
    elif avg > 0.5:
        status = 'warn'
    else:
        status = 'fail'
    return make_result('OCF/NI 3yr', status, value, detail, pts)


def _eval_3yr_shareholder_return(data, pts):
    bb_series = get_series(data['cf_annual'], 'Repurchase Of Capital Stock')
    div_series = get_series(data['cf_annual'], 'Common Stock Dividend Paid')

    years_with_return = 0
    for i in range(3):
        bb = bb_series[i][1] if i < len(bb_series) else None
        dv = div_series[i][1] if i < len(div_series) else None
        has_bb = bb is not None and bb < 0
        has_dv = dv is not None and dv < 0
        if has_bb or has_dv:
            years_with_return += 1

    value = '{}/3 years'.format(years_with_return)
    if years_with_return >= 3:
        status = 'pass'
    elif years_with_return >= 1:
        status = 'warn'
    else:
        status = 'fail'
    return make_result('Buyback/Div 3yr', status, value, '', pts)


def _eval_3yr_sbc_trend(data, pts):
    sbc_series = get_series(data['cf_annual'], 'Stock Based Compensation')
    rev_series = get_series(data['income_annual'], 'Total Revenue')

    ratios = []
    for i in range(min(3, len(sbc_series), len(rev_series))):
        sbc = sbc_series[i][1]
        rev = rev_series[i][1]
        if sbc is not None and rev is not None and rev > 0:
            ratios.append(sbc / rev)

    if len(ratios) < 2:
        return make_result('SBC/Rev Trend', 'skip', '-', 'Insufficient data', pts)

    value = '{:.1f}%'.format(ratios[0] * 100)
    detail = ' -> '.join('{:.1f}%'.format(r * 100) for r in reversed(ratios))

    if ratios[0] <= ratios[-1]:
        status = 'pass'
    elif ratios[0] - ratios[-1] <= 0.03:
        status = 'warn'
    else:
        status = 'fail'
    return make_result('SBC/Rev Trend', status, value, detail, pts)


def eval_cf_3yr(data):
    return [
        _check_3yr_cf_trend(data, 'Operating Cash Flow', 'OCF Trend', 25),
        _check_3yr_cf_trend(data, 'Free Cash Flow', 'FCF Trend', 20),
        _eval_3yr_ocf_ni(data, 15),
        _eval_3yr_shareholder_return(data, 20),
        _eval_3yr_sbc_trend(data, 20),
    ]


# ===================== TTM (100 pts) =====================

def _eval_ttm_ocf_growth(data, pts):
    ttm_ocf = get_val(data['cf_ttm'], 'Operating Cash Flow')
    annual_col = ttm_compare_col(data['cf_ttm'], data['cf_annual'])
    annual_ocf = get_val(data['cf_annual'], 'Operating Cash Flow', annual_col)

    if ttm_ocf is None or annual_ocf is None:
        return make_result('OCF vs LY', 'skip', '-', 'No data', pts)

    g = growth_rate(ttm_ocf, annual_ocf)
    value = '{} ({:+.1f}%)'.format(format_value(ttm_ocf), g * 100) if g is not None else format_value(ttm_ocf)
    detail = 'LY: {}'.format(format_value(annual_ocf))

    if g is None:
        status = 'skip'
    elif g > 0:
        status = 'pass'
    elif g >= -0.05:
        status = 'warn'
    else:
        status = 'fail'
    return make_result('OCF vs LY', status, value, detail, pts)


def _eval_ttm_fcf(data, pts):
    fcf = get_val(data['cf_ttm'], 'Free Cash Flow')
    if fcf is None:
        return make_result('FCF > 0', 'skip', '-', 'No data', pts)

    value = format_value(fcf)
    status = 'pass' if fcf > 0 else 'fail'
    return make_result('FCF > 0', status, value, '', pts)


def _eval_ttm_ocf_ni(data, pts):
    ocf = get_val(data['cf_ttm'], 'Operating Cash Flow')
    ni = get_val(data['income_ttm'], 'Net Income')

    if ocf is None or ni is None:
        return make_result('OCF/NI', 'skip', '-', 'No data', pts)
    if ni <= 0:
        return make_result('OCF/NI', 'fail', '-', 'Negative NI', pts)

    ratio = ocf / ni
    value = '{:.2f}'.format(ratio)
    detail = 'OCF {} / NI {}'.format(format_value(ocf), format_value(ni))

    if ratio > 0.8:
        status = 'pass'
    elif ratio > 0.5:
        status = 'warn'
    else:
        status = 'fail'
    return make_result('OCF/NI', status, value, detail, pts)


def _eval_ttm_net_return(data, pts):
    if data['cf_ttm'].empty:
        return make_result('Net Return', 'skip', '-', 'No data', pts)

    ttm_bb = get_val(data['cf_ttm'], 'Repurchase Of Capital Stock')
    ttm_div = get_val(data['cf_ttm'], 'Common Stock Dividend Paid')
    ttm_sbc = get_val(data['cf_ttm'], 'Stock Based Compensation')

    abs_bb = abs(ttm_bb) if ttm_bb and ttm_bb < 0 else 0
    abs_div = abs(ttm_div) if ttm_div and ttm_div < 0 else 0
    sbc = ttm_sbc if ttm_sbc and ttm_sbc > 0 else 0
    net = abs_bb + abs_div - sbc

    value = format_value(net) if net != 0 else '-'
    detail = 'BB {} + Div {} - SBC {}'.format(format_value(abs_bb), format_value(abs_div), format_value(sbc))

    if net > 0:
        status = 'pass'
    elif abs_bb + abs_div > 0:
        status = 'warn'
    else:
        status = 'fail'
    return make_result('Net Return', status, value, detail, pts)


def _eval_ttm_sbc_ratio(data, pts):
    sbc = get_val(data['cf_ttm'], 'Stock Based Compensation')
    revenue = get_val(data['income_ttm'], 'Total Revenue')

    if sbc is None or revenue is None or revenue == 0:
        return make_result('SBC/Revenue', 'skip', '-', 'No data', pts)

    ratio = sbc / revenue
    value = '{:.1f}%'.format(ratio * 100)
    detail = 'SBC {} / Rev {}'.format(format_value(sbc), format_value(revenue))

    if ratio < 0.10:
        status = 'pass'
    elif ratio < 0.15:
        status = 'warn'
    else:
        status = 'fail'
    return make_result('SBC/Revenue', status, value, detail, pts)


def eval_cf_ttm(data):
    return [
        _eval_ttm_ocf_growth(data, 25),
        _eval_ttm_fcf(data, 25),
        _eval_ttm_ocf_ni(data, 15),
        _eval_ttm_net_return(data, 20),
        _eval_ttm_sbc_ratio(data, 15),
    ]


# ===================== 5Q (100 pts) =====================

def _check_4q_cf_positive(data, field, label, pts):
    quarterly = data['cf_quarterly']
    if quarterly.empty or len(quarterly.columns) < 4:
        return make_result(label, 'skip', '-', 'Insufficient data', pts)

    vals = [get_val(quarterly, field, i) for i in range(4)]
    valid = [v for v in vals if v is not None]
    if len(valid) < 4:
        return make_result(label, 'skip', '-', 'Incomplete data', pts)

    neg_count = sum(1 for v in valid if v <= 0)
    value = format_value(valid[0])
    detail = '{}/4 positive'.format(4 - neg_count)

    if neg_count == 0:
        status = 'pass'
    elif neg_count == 1:
        status = 'warn'
    else:
        status = 'fail'
    return make_result(label, status, value, detail, pts)


def _check_q_yoy_cf(data, field, label, pts):
    quarterly = data['cf_quarterly']
    if quarterly.empty or len(quarterly.columns) < 5:
        return make_result(label, 'skip', '-', 'Insufficient data', pts)

    new_val = get_val(quarterly, field, 0)
    old_val = get_val(quarterly, field, 4)
    if new_val is None or old_val is None:
        return make_result(label, 'skip', '-', 'No data', pts)

    g = growth_rate(new_val, old_val)
    value = '{} ({:+.1f}%)'.format(format_value(new_val), g * 100) if g is not None else format_value(new_val)
    detail = 'LY Q: {}'.format(format_value(old_val))
    status = 'pass' if g is not None and g > 0 else 'fail'
    return make_result(label, status, value, detail, pts)


def _eval_4q_buyback(data, pts):
    quarterly = data['cf_quarterly']
    if quarterly.empty or len(quarterly.columns) < 4:
        return make_result('4Q Buyback', 'skip', '-', 'Insufficient data', pts)

    count = 0
    for i in range(4):
        bb = get_val(quarterly, 'Repurchase Of Capital Stock', i)
        if bb is not None and bb < 0:
            count += 1

    value = '{}/4 quarters'.format(count)
    status = 'pass' if count > 0 else 'warn'
    return make_result('4Q Buyback', status, value, '', pts)


def _eval_q_ocf_ni(data, pts):
    ocf = get_val(data['cf_quarterly'], 'Operating Cash Flow', 0)
    ni = get_val(data['income_quarterly'], 'Net Income', 0)
    if ocf is None or ni is None:
        return make_result('Q OCF/NI', 'skip', '-', 'No data', pts)
    if ni <= 0:
        return make_result('Q OCF/NI', 'fail', '-', 'Negative NI', pts)

    ratio = ocf / ni
    value = '{:.2f}'.format(ratio)

    if ratio > 0.8:
        status = 'pass'
    elif ratio > 0.5:
        status = 'warn'
    else:
        status = 'fail'
    return make_result('Q OCF/NI', status, value, '', pts)


def eval_cf_5q(data):
    return [
        _check_4q_cf_positive(data, 'Operating Cash Flow', '4Q OCF +', 25),
        _check_q_yoy_cf(data, 'Operating Cash Flow', 'Q YoY OCF', 20),
        _check_4q_cf_positive(data, 'Free Cash Flow', '4Q FCF +', 25),
        _check_q_yoy_cf(data, 'Free Cash Flow', 'Q YoY FCF', 15),
        _eval_4q_buyback(data, 10),
        _eval_q_ocf_ni(data, 5),
    ]
