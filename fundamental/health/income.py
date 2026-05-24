"""
Income Statement (100 pts, weight 25%)
  Revenue Growth     15    3yr(正+增) + TTM + Q(4q正 + YoY)
  Op Income Growth   15    3yr(正+增) + TTM + Q(4q正 + YoY)
  EBITDA Growth      15    3yr(正+增) + TTM + Q(4q正 + YoY)
  EPS Trend          30    3yr(正+增) + TTM + Q(4q正 + YoY)
  Margins            15    TTM only
  Interest Coverage  10    TTM only
"""
from fundamental.data import get_val, get_series, format_value
from fundamental.health.helpers import growth_rate, make_result, ttm_compare_col, score_layers, layer_symbols

W_3YR = 0.2
W_TTM = 0.3
W_Q = 0.5

PTS_REVENUE = 15
PTS_OI = 15
PTS_EBITDA = 15
PTS_EPS = 30
PTS_MARGINS = 15
PTS_INTEREST = 10


def _check_3yr(data, field):
    series = get_series(data['income_annual'], field)
    vals = [v for _, v in series[:3] if v is not None]
    if len(vals) < 3:
        return 'skip', None
    growing = vals[0] > vals[1] > vals[2]
    positive = vals[0] > 0 and vals[1] > 0 and vals[2] > 0
    g = growth_rate(vals[0], vals[1])
    if positive and growing:
        return 'pass', g
    elif positive or growing:
        return 'warn', g
    return 'fail', g


def _check_ttm_vs_annual(data, field):
    ttm_df = data['income_ttm']
    annual_df = data['income_annual']
    ttm_val = get_val(ttm_df, field)
    annual_col = ttm_compare_col(ttm_df, annual_df)
    annual_val = get_val(annual_df, field, annual_col)
    if ttm_val is None or annual_val is None:
        return 'skip'
    return 'pass' if ttm_val > annual_val else 'fail'


def _check_q_yoy(data, field):
    quarterly = data['income_quarterly']
    if quarterly.empty or len(quarterly.columns) < 5:
        return 'skip'

    q_vals = [get_val(quarterly, field, i) for i in range(5)]
    valid = [v for v in q_vals if v is not None]
    if len(valid) < 5:
        return 'skip'
    if not all(v > 0 for v in valid[:4]):
        return 'fail'

    return 'pass' if q_vals[0] > q_vals[4] else 'fail'


# --- growth metrics ---

def _eval_growth(data, field, label, pts):
    s_3yr, annual_g = _check_3yr(data, field)
    s_ttm = _check_ttm_vs_annual(data, field)
    s_q = _check_q_yoy(data, field)

    layers = [(W_3YR, s_3yr), (W_TTM, s_ttm), (W_Q, s_q)]
    score, status = score_layers(layers, pts)

    series = get_series(data['income_annual'], field)
    vals = [v for _, v in series if v is not None]
    latest = format_value(vals[0]) if vals else '-'
    pct = ' ({:+.1f}%)'.format(annual_g * 100) if annual_g is not None else ''
    value = '{}{}'.format(latest, pct)

    detail = layer_symbols([('3yr', s_3yr), ('TTM', s_ttm), ('Q', s_q)])

    return make_result(label, status, value, detail, pts)


def eval_revenue_growth(data):
    return _eval_growth(data, 'Total Revenue', 'Revenue Growth', PTS_REVENUE)


def eval_op_income_growth(data):
    return _eval_growth(data, 'Operating Income', 'Op Income Growth', PTS_OI)


def eval_ebitda_growth(data):
    return _eval_growth(data, 'EBITDA', 'EBITDA Growth', PTS_EBITDA)


def eval_eps_trend(data):
    return _eval_growth(data, 'Diluted EPS', 'EPS Trend', PTS_EPS)


# --- ratio metrics (TTM only) ---

def eval_margins(data):
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

    return make_result('Margins', status, value, '', PTS_MARGINS)


def eval_interest_coverage(data):
    ttm = data['income_ttm']
    op_income = get_val(ttm, 'Operating Income')
    int_exp = get_val(ttm, 'Interest Expense')

    if op_income is None:
        return make_result('Interest Coverage', 'skip', '-', 'No data', PTS_INTEREST)

    if int_exp is None or int_exp == 0:
        lt_debt = get_val(data['bs_quarterly'], 'Long Term Debt')
        if lt_debt and lt_debt > 0:
            return make_result('Interest Coverage', 'warn', '-', 'No data (has debt)', PTS_INTEREST)
        return make_result('Interest Coverage', 'pass', '-', 'No interest expense', PTS_INTEREST)

    ratio = op_income / abs(int_exp)
    value = '{:.1f}x'.format(ratio)
    detail = '{} / {}'.format(format_value(op_income), format_value(abs(int_exp)))

    if ratio > 5:
        status = 'pass'
    elif ratio > 2:
        status = 'warn'
    else:
        status = 'fail'

    return make_result('Interest Coverage', status, value, detail, PTS_INTEREST)
