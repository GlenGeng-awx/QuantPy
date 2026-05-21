"""
Cash Flow (100 pts, weight 35%)
  OCF Trend           30    3yr(正+增) + TTM + Q(4q正 + YoY)
  Earnings Quality    15    TTM only (OCF/NI)
  Free Cash Flow      25    3yr(正) + TTM(正) + Q(4q正 + YoY)
  Shareholder Return  15    3yr + TTM
  SBC Ratio           15    TTM only
"""
from fundamental.data.loader import get_val, get_series, format_value
from fundamental.health.helpers import (
    make_result, ttm_compare_col, score_layers, layer_symbols,
)

W_3YR = 0.2
W_TTM = 0.3
W_Q = 0.5

PTS_OCF = 30
PTS_QUALITY = 15
PTS_FCF = 25
PTS_RETURN = 15
PTS_SBC = 15


# --- OCF Trend (3yr + TTM + Q) ---

def eval_ocf_trend(data):
    # 3yr: 年报 OCF 3年正且增长
    series = get_series(data['cf_annual'], 'Operating Cash Flow')
    vals = [v for _, v in series[:3] if v is not None]
    if len(vals) < 3:
        s_3yr = 'skip'
    else:
        positive = vals[0] > 0 and vals[1] > 0 and vals[2] > 0
        growing = vals[0] > vals[1] > vals[2]
        if positive and growing:
            s_3yr = 'pass'
        elif positive or growing:
            s_3yr = 'warn'
        else:
            s_3yr = 'fail'

    # TTM: TTM OCF vs 去年年报正增长
    ttm_ocf = get_val(data['cf_ttm'], 'Operating Cash Flow')
    annual_col = ttm_compare_col(data['cf_ttm'], data['cf_annual'])
    annual_ocf = get_val(data['cf_annual'], 'Operating Cash Flow', annual_col)
    if ttm_ocf is None or annual_ocf is None:
        s_ttm = 'skip'
    else:
        s_ttm = 'pass' if ttm_ocf > annual_ocf else 'fail'

    # Q: 最近4季全部为正 + 最新季 YoY 正增长
    q_series = get_series(data['cf_quarterly'], 'Operating Cash Flow', count=5)
    q_vals = [v for _, v in q_series if v is not None]
    if len(q_vals) < 5:
        s_q = 'skip'
    else:
        q_positive = all(v > 0 for v in q_vals[:4])
        q_yoy = q_vals[0] > q_vals[4]
        if q_positive and q_yoy:
            s_q = 'pass'
        elif q_positive or q_yoy:
            s_q = 'warn'
        else:
            s_q = 'fail'

    layers = [(W_3YR, s_3yr), (W_TTM, s_ttm), (W_Q, s_q)]
    _, status = score_layers(layers, PTS_OCF)

    value = format_value(ttm_ocf) if ttm_ocf else (format_value(vals[0]) if vals else '-')
    detail = layer_symbols([('3yr', s_3yr), ('TTM', s_ttm), ('Q', s_q)])

    return make_result('OCF Trend', status, value, detail, PTS_OCF)


# --- Earnings Quality (TTM only) ---

def eval_earnings_quality(data):
    ocf = get_val(data['cf_ttm'], 'Operating Cash Flow')
    ni = get_val(data['income_ttm'], 'Net Income')

    if ocf is None or ni is None:
        return make_result('Earnings Quality', 'skip', '-', 'No data', PTS_QUALITY)
    if ni <= 0:
        return make_result('Earnings Quality', 'fail', '-', 'Negative NI', PTS_QUALITY)

    ratio = ocf / ni
    value = 'OCF/NI: {:.2f}'.format(ratio)
    detail = '{} / {}'.format(format_value(ocf), format_value(ni))

    if ratio > 0.8:
        status = 'pass'
    elif ratio > 0.5:
        status = 'warn'
    else:
        status = 'fail'

    return make_result('Earnings Quality', status, value, detail, PTS_QUALITY)


# --- Free Cash Flow (3yr + TTM + Q) ---

def eval_fcf(data):
    # 3yr: 年报 FCF 3年为正
    series = get_series(data['cf_annual'], 'Free Cash Flow')
    vals = [v for _, v in series[:3] if v is not None]
    if len(vals) < 3:
        s_3yr = 'skip'
    elif all(v > 0 for v in vals):
        s_3yr = 'pass'
    else:
        s_3yr = 'fail'

    # TTM: TTM FCF > 0
    ttm_fcf = get_val(data['cf_ttm'], 'Free Cash Flow')
    if ttm_fcf is None:
        s_ttm = 'skip'
    elif ttm_fcf > 0:
        s_ttm = 'pass'
    else:
        s_ttm = 'fail'

    # Q: 最近4季全部为正 + 最新季 YoY 正增长
    q_series = get_series(data['cf_quarterly'], 'Free Cash Flow', count=5)
    q_vals = [v for _, v in q_series if v is not None]
    if len(q_vals) < 5:
        s_q = 'skip'
    else:
        q_positive = all(v > 0 for v in q_vals[:4])
        q_yoy = q_vals[0] > q_vals[4]
        if q_positive and q_yoy:
            s_q = 'pass'
        elif q_positive or q_yoy:
            s_q = 'warn'
        else:
            s_q = 'fail'

    layers = [(W_3YR, s_3yr), (W_TTM, s_ttm), (W_Q, s_q)]
    _, status = score_layers(layers, PTS_FCF)

    value = format_value(ttm_fcf) if ttm_fcf else (format_value(vals[0]) if vals else '-')
    detail = layer_symbols([('3yr', s_3yr), ('TTM', s_ttm), ('Q', s_q)])

    return make_result('Free Cash Flow', status, value, detail, PTS_FCF)


# --- Shareholder Return (3yr + TTM) ---

def eval_shareholder_return(data):
    # 3yr: 连续3年每年有 Buyback 或 Dividend
    buyback_series = get_series(data['cf_annual'], 'Repurchase Of Capital Stock')
    dividend_series = get_series(data['cf_annual'], 'Common Stock Dividend Paid')

    years_with_return = 0
    for i in range(3):
        if i < len(buyback_series):
            bb = buyback_series[i][1]
        else:
            bb = None
        if i < len(dividend_series):
            dv = dividend_series[i][1]
        else:
            dv = None
        has_buyback = bb is not None and bb < 0
        has_dividend = dv is not None and dv < 0
        if has_buyback or has_dividend:
            years_with_return += 1

    if years_with_return >= 3:
        s_3yr = 'pass'
    elif years_with_return >= 1:
        s_3yr = 'warn'
    else:
        s_3yr = 'fail'

    # TTM: (|Buyback| + |Dividend| - SBC) > 0
    ttm_bb = get_val(data['cf_ttm'], 'Repurchase Of Capital Stock')
    ttm_div = get_val(data['cf_ttm'], 'Common Stock Dividend Paid')
    ttm_sbc = get_val(data['cf_ttm'], 'Stock Based Compensation')

    abs_bb = abs(ttm_bb) if ttm_bb and ttm_bb < 0 else 0
    abs_div = abs(ttm_div) if ttm_div and ttm_div < 0 else 0
    sbc = ttm_sbc if ttm_sbc and ttm_sbc > 0 else 0
    net = abs_bb + abs_div - sbc

    if net > 0:
        s_ttm = 'pass'
    elif abs_bb + abs_div > 0:
        s_ttm = 'warn'
    else:
        s_ttm = 'fail'

    layers = [(W_3YR, s_3yr), (W_TTM, s_ttm)]
    _, status = score_layers(layers, PTS_RETURN)

    if net != 0:
        value = format_value(net)
    else:
        value = '-'

    detail = layer_symbols([('3yr', s_3yr), ('TTM', s_ttm)])
    parts = []
    if abs_bb > 0:
        parts.append('BB {}'.format(format_value(abs_bb)))
    if abs_div > 0:
        parts.append('Div {}'.format(format_value(abs_div)))
    if sbc > 0:
        parts.append('SBC {}'.format(format_value(sbc)))
    if parts:
        detail += '  ' + ' - '.join(parts)

    return make_result('Shareholder Return', status, value, detail, PTS_RETURN)


# --- SBC Ratio (TTM only) ---

def eval_sbc_ratio(data):
    sbc = get_val(data['cf_ttm'], 'Stock Based Compensation')
    revenue = get_val(data['income_ttm'], 'Total Revenue')

    if sbc is None or revenue is None or revenue == 0:
        return make_result('SBC Ratio', 'skip', '-', 'No data', PTS_SBC)

    ratio = sbc / revenue
    value = '{:.1f}%'.format(ratio * 100)
    detail = 'SBC {} / Rev {}'.format(format_value(sbc), format_value(revenue))

    if ratio < 0.10:
        status = 'pass'
    elif ratio < 0.15:
        status = 'warn'
    else:
        status = 'fail'

    return make_result('SBC Ratio', status, value, detail, PTS_SBC)
