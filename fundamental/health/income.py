"""
Income Statement 评价标准 (权重 40%)

Revenue Growth (0.05):
    过去三年 年年正增长 + 最新季度 YoY 正增长

Operating Income Growth (0.05):
    过去三年 年年正增长 + 最新季度 YoY 正增长

Net Income Growth (0.05):
    过去三年 年年正增长 + 最新季度 YoY 正增长

EPS Trend (0.20):
    过去三年 EPS 为正且逐年递增
    过去四个季度 EPS 为正，最新季度 YoY 正增长

Margins (0.05):
    毛利率 > 50% 或 净利率 > 15% 为 pass
    毛利率 > 30% 或 净利率 > 10% 为 warn

Interest Coverage (0.04):
    营业利润 / 利息支出 > 5x 为 pass，2-5x 为 warn
    无债务公司直接 pass
"""
from fundamental.health.data import get_val, get_series, growth_rate, make_result, format_value

W_REVENUE_GROWTH = 0.05
W_OI_GROWTH = 0.05
W_NI_GROWTH = 0.05
W_EPS_TREND = 0.20
W_MARGINS = 0.05
W_INTEREST_COVERAGE = 0.04


def _eval_growth(data, field, label, weight):
    annual = data['income_annual']
    quarterly = data['income_quarterly']

    # Annual: all years growing
    series = get_series(annual, field)
    vals = [v for _, v in series if v is not None]
    annual_ok = False
    annual_g = None
    if len(vals) >= 2:
        n = min(len(vals) - 1, 3)
        annual_ok = all(vals[i] > vals[i + 1] for i in range(n))
        annual_g = growth_rate(vals[0], vals[1])

    latest = format_value(vals[0]) if vals else '-'
    pct = ' ({:+.1f}%)'.format(annual_g * 100) if annual_g is not None else ''
    value = '{}{}'.format(latest, pct)

    # Quarterly: YoY (col 0 vs col 4)
    quarterly_ok = False
    if not quarterly.empty and len(quarterly.columns) >= 5:
        new = get_val(quarterly, field, 0)
        old = get_val(quarterly, field, 4)
        g = growth_rate(new, old)
        quarterly_ok = g is not None and g > 0

    parts = []
    if annual_ok:
        parts.append('3yr growing')
    if quarterly_ok:
        parts.append('Q YoY up')
    detail = ', '.join(parts) if parts else 'Not growing'

    if annual_ok and quarterly_ok:
        status = 'pass'
    elif annual_ok or quarterly_ok:
        status = 'warn'
    else:
        status = 'fail'

    return make_result(label, status, value, detail, weight)


def eval_revenue_growth(data):
    return _eval_growth(data, 'Total Revenue', 'Revenue Growth', W_REVENUE_GROWTH)


def eval_op_income_growth(data):
    return _eval_growth(data, 'Operating Income', 'Op Income Growth', W_OI_GROWTH)


def eval_net_income_growth(data):
    return _eval_growth(data, 'Net Income', 'Net Income Growth', W_NI_GROWTH)


def eval_eps_trend(data):
    annual = data['income_annual']
    quarterly = data['income_quarterly']

    # Annual: 3 years EPS positive and trending up
    annual_series = get_series(annual, 'Diluted EPS')
    annual_vals = [v for _, v in annual_series if v is not None]
    annual_ok = False
    if len(annual_vals) >= 3:
        all_positive = True
        trending_up = True
        for v in annual_vals[:3]:
            if v <= 0:
                all_positive = False
        for i in range(min(len(annual_vals) - 1, 3)):
            if annual_vals[i] <= annual_vals[i + 1]:
                trending_up = False
        annual_ok = all_positive and trending_up

    # Quarterly: YoY check (latest vs same quarter last year)
    quarterly_ok = False
    if not quarterly.empty and len(quarterly.columns) >= 5:
        q_vals = [get_val(quarterly, 'Diluted EPS', i) for i in range(5)]
        q_vals_valid = [v for v in q_vals[:4] if v is not None]
        all_positive = len(q_vals_valid) >= 4 and all(v > 0 for v in q_vals_valid)
        new, old = q_vals[0], q_vals[4]
        yoy_up = new is not None and old is not None and new > old
        quarterly_ok = all_positive and yoy_up

    latest_eps = annual_vals[0] if annual_vals else None
    value = '${:.2f}'.format(latest_eps) if latest_eps else '-'

    if annual_ok and quarterly_ok:
        status = 'pass'
        detail = '3yr positive & growing, Q YoY up'
    elif annual_ok:
        status = 'warn'
        detail = '3yr positive & growing, Q mixed'
    elif quarterly_ok:
        status = 'warn'
        detail = '3yr mixed, Q YoY up'
    else:
        status = 'fail'
        detail = 'EPS not consistently growing'

    return make_result('EPS Trend', status, value, detail, W_EPS_TREND)


def eval_margins(data):
    df = data['income_annual']
    revenue = get_val(df, 'Total Revenue')
    gross_profit = get_val(df, 'Gross Profit')
    net_income = get_val(df, 'Net Income')

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

    return make_result('Margins', status, value, '', W_MARGINS)


def eval_interest_coverage(data):
    op_income = get_val(data['income_annual'], 'Operating Income')
    int_exp = get_val(data['income_annual'], 'Interest Expense')

    # Fallback to older periods if latest is missing
    if int_exp is None:
        df = data['income_annual']
        for i in range(1, min(4, len(df.columns) if not df.empty else 0)):
            int_exp = get_val(df, 'Interest Expense', i)
            if int_exp is not None:
                break

    if int_exp is None or int_exp == 0:
        lt_debt = get_val(data['bs_quarterly'], 'Long Term Debt')
        if lt_debt and lt_debt > 0:
            return make_result('Interest Coverage', 'warn', '-', 'No data (has debt)', W_INTEREST_COVERAGE)
        return make_result('Interest Coverage', 'pass', '-', 'No interest expense', W_INTEREST_COVERAGE)

    if op_income is None:
        return make_result('Interest Coverage', 'skip', '-', 'No data', W_INTEREST_COVERAGE)

    ratio = op_income / abs(int_exp)
    value = '{:.1f}x'.format(ratio)
    detail = '{} / {}'.format(format_value(op_income), format_value(abs(int_exp)))

    if ratio > 5:
        status = 'pass'
    elif ratio > 2:
        status = 'warn'
    else:
        status = 'fail'

    return make_result('Interest Coverage', status, value, detail, W_INTEREST_COVERAGE)
