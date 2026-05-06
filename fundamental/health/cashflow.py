"""
Cash Flow 评价标准 (权重 35%)

OCF Trend (0.06):
    过去三年 经营现金流为正，正增长
    过去四个季度 经营现金流为正

Earnings Quality (0.04):
    最近一年 OCF / Net Income > 0.8 为 pass，0.5-0.8 为 warn
    净利润为负直接 fail

Free Cash Flow (0.08):
    过去三年 自由现金流为正
    过去四个季度 自由现金流为正
    注：AI capex 导致 FCF 转负可豁免，需标注

Buyback (0.03):
    过去三年 稳定回购

Dividend (0.02):
    过去三年 稳定分红

Net Buyback (0.04):
    净回购 = |回购| - SBC > 0
    SBC 侵蚀回购超过 50% 为 warn

SBC Ratio (0.04):
    SBC / 营收 < 10% 为 pass，10-15% 为 warn
"""
from fundamental.health.data import get_val, get_series, growth_rate, make_result, format_value

W_OCF_TREND = 0.06
W_EARNINGS_QUALITY = 0.04
W_FCF = 0.08
W_BUYBACK = 0.03
W_DIVIDEND = 0.02
W_NET_BUYBACK = 0.04
W_SBC_RATIO = 0.04


def eval_ocf_trend(data):
    ocf_series = get_series(data['cf_annual'], 'Operating Cash Flow')
    ocf_vals = [v for _, v in ocf_series[:3] if v is not None]

    annual_positive = len(ocf_vals) >= 3 and all(v > 0 for v in ocf_vals)
    annual_growing = len(ocf_vals) >= 2 and all(ocf_vals[i] >= ocf_vals[i + 1] for i in range(len(ocf_vals) - 1))

    ocf_q = get_series(data['cf_quarterly'], 'Operating Cash Flow', count=4)
    ocf_q_vals = [v for _, v in ocf_q if v is not None]
    quarterly_positive = len(ocf_q_vals) >= 4 and all(v > 0 for v in ocf_q_vals)

    latest_ocf = ocf_vals[0] if ocf_vals else None
    value = format_value(latest_ocf) if latest_ocf else '-'

    checks = [annual_positive, annual_growing, quarterly_positive]
    passed = sum(checks)

    if passed >= 2:
        status = 'pass'
    elif passed >= 1:
        status = 'warn'
    else:
        status = 'fail'

    parts = []
    if annual_positive:
        parts.append('3yr positive')
    if annual_growing:
        parts.append('3yr growing')
    if quarterly_positive:
        parts.append('4q positive')
    detail = ', '.join(parts) if parts else 'OCF weak'

    return make_result('OCF Trend', status, value, detail, W_OCF_TREND)


def eval_earnings_quality(data):
    ocf = get_val(data['cf_annual'], 'Operating Cash Flow')
    ni = get_val(data['income_annual'], 'Net Income')

    if ocf is None or ni is None:
        return make_result('Earnings Quality', 'skip', '-', 'No data', W_EARNINGS_QUALITY)
    if ni <= 0:
        return make_result('Earnings Quality', 'fail', '-', 'Negative NI', W_EARNINGS_QUALITY)

    ratio = ocf / ni
    value = 'OCF/NI: {:.2f}'.format(ratio)
    detail = '{} / {}'.format(format_value(ocf), format_value(ni))

    if ratio > 0.8:
        status = 'pass'
    elif ratio > 0.5:
        status = 'warn'
    else:
        status = 'fail'

    return make_result('Earnings Quality', status, value, detail, W_EARNINGS_QUALITY)


def eval_fcf(data):
    annual_series = get_series(data['cf_annual'], 'Free Cash Flow')
    quarterly_series = get_series(data['cf_quarterly'], 'Free Cash Flow', count=4)

    annual_vals = [v for _, v in annual_series[:3] if v is not None]
    quarterly_vals = [v for _, v in quarterly_series if v is not None]

    annual_ok = len(annual_vals) >= 3 and all(v > 0 for v in annual_vals)
    quarterly_ok = len(quarterly_vals) >= 4 and all(v > 0 for v in quarterly_vals)

    latest = annual_vals[0] if annual_vals else None
    value = format_value(latest) if latest else '-'

    # CapEx exemption note
    capex_note = ''
    if not (annual_ok and quarterly_ok):
        ocf = get_val(data['cf_annual'], 'Operating Cash Flow')
        capex = get_val(data['cf_annual'], 'Capital Expenditure')
        if ocf and ocf > 0 and capex and abs(capex) > ocf * 0.3:
            capex_note = ' (high CapEx: {})'.format(format_value(abs(capex)))

    if annual_ok and quarterly_ok:
        status = 'pass'
        detail = '3yr positive, 4q positive'
    elif annual_ok:
        status = 'warn'
        detail = '3yr positive, 4q mixed' + capex_note
    elif quarterly_ok:
        status = 'warn'
        detail = '3yr mixed, 4q positive' + capex_note
    else:
        status = 'fail'
        detail = 'FCF concerns' + capex_note

    return make_result('Free Cash Flow', status, value, detail, W_FCF)


def eval_buyback(data):
    series = get_series(data['cf_annual'], 'Repurchase Of Capital Stock')
    vals = [v for _, v in series[:3] if v is not None]
    consistent = len(vals) >= 3 and all(v < 0 for v in vals)

    if consistent:
        avg = abs(sum(vals) / len(vals))
        status = 'pass'
        value = '{}/yr'.format(format_value(avg))
        detail = '3yr consistent'
    elif vals and any(v < 0 for v in vals):
        status = 'warn'
        value = '-'
        detail = 'Not consistent'
    else:
        status = 'warn'
        value = '-'
        detail = 'No buyback'

    return make_result('Buyback', status, value, detail, W_BUYBACK)


def eval_dividend(data):
    series = get_series(data['cf_annual'], 'Common Stock Dividend Paid')
    vals = [v for _, v in series[:3] if v is not None]
    consistent = len(vals) >= 3 and all(v < 0 for v in vals)

    if consistent:
        avg = abs(sum(vals) / len(vals))
        status = 'pass'
        value = '{}/yr'.format(format_value(avg))
        detail = '3yr consistent'
    elif vals and any(v < 0 for v in vals):
        status = 'warn'
        value = '-'
        detail = 'Not consistent'
    else:
        status = 'warn'
        value = '-'
        detail = 'No dividend'

    return make_result('Dividend', status, value, detail, W_DIVIDEND)


def eval_net_buyback(data):
    buyback = get_val(data['cf_annual'], 'Repurchase Of Capital Stock')
    sbc = get_val(data['cf_annual'], 'Stock Based Compensation')

    if buyback is None or buyback >= 0:
        return make_result('Net Buyback', 'warn', '-', 'No buyback', W_NET_BUYBACK)

    abs_buyback = abs(buyback)
    sbc = sbc if sbc and sbc > 0 else 0
    net = abs_buyback - sbc

    value = 'Net: {}'.format(format_value(net))
    detail = 'Buyback {} - SBC {}'.format(format_value(abs_buyback), format_value(sbc))

    if net > 0:
        status = 'pass'
    elif net > -abs_buyback * 0.5:
        status = 'warn'
    else:
        status = 'fail'

    return make_result('Net Buyback', status, value, detail, W_NET_BUYBACK)


def eval_sbc_ratio(data):
    sbc = get_val(data['cf_annual'], 'Stock Based Compensation')
    revenue = get_val(data['income_annual'], 'Total Revenue')

    if sbc is None or revenue is None or revenue == 0:
        return make_result('SBC Ratio', 'skip', '-', 'No data', W_SBC_RATIO)

    ratio = sbc / revenue
    value = '{:.1f}%'.format(ratio * 100)
    detail = 'SBC {} / Rev {}'.format(format_value(sbc), format_value(revenue))

    if ratio < 0.10:
        status = 'pass'
    elif ratio < 0.15:
        status = 'warn'
    else:
        status = 'fail'

    return make_result('SBC Ratio', status, value, detail, W_SBC_RATIO)
