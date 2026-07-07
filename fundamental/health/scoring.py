from fundamental.data import load_statement, load_info, load_price, format_value, get_info_val, get_val
from fundamental.health.helpers import score_dimension
from fundamental.health.income import eval_income_3yr, eval_income_ttm, eval_income_5q
from fundamental.health.cashflow import eval_cf_3yr, eval_cf_ttm, eval_cf_5q
from fundamental.health.balance_sheet import eval_bs_3yr, eval_bs_ttm, eval_bs_5q, eval_risk_flags

DIMENSIONS = [
    ('Income', 'income', [eval_income_3yr, eval_income_ttm, eval_income_5q]),
    ('CF', 'cf', [eval_cf_3yr, eval_cf_ttm, eval_cf_5q]),
    ('BS', 'bs', [eval_bs_3yr, eval_bs_ttm, eval_bs_5q]),
]

PERIODS = ['3yr', 'ttm', '5q']

STATUS_ICON = {'pass': '✓', 'fail': '✗', 'warn': '⚠', 'skip': '-'}


def load_data(stock_name):
    return {
        'stock_name': stock_name,
        'income_annual': load_statement(stock_name, 'income_annual'),
        'income_quarterly': load_statement(stock_name, 'income_quarterly'),
        'income_ttm': load_statement(stock_name, 'income_ttm'),
        'bs_annual': load_statement(stock_name, 'bs_annual'),
        'bs_quarterly': load_statement(stock_name, 'bs_quarterly'),
        'cf_annual': load_statement(stock_name, 'cf_annual'),
        'cf_quarterly': load_statement(stock_name, 'cf_quarterly'),
        'cf_ttm': load_statement(stock_name, 'cf_ttm'),
        'price': load_price(stock_name),
        'info': load_info(stock_name),
    }


def evaluate_stock(stock_name):
    data = load_data(stock_name)
    grid = {}

    for label, key, funcs in DIMENSIONS:
        for func, period in zip(funcs, PERIODS):
            metrics = func(data)
            score = score_dimension(metrics)
            dim_key = '{}_{}'.format(key, period)
            grid[dim_key] = {'score': score, 'metrics': metrics}

    risk = eval_risk_flags(data)
    if risk['status'] == 'fail':
        bs_5q = grid['bs_5q']
        if bs_5q['score'] is not None:
            bs_5q['score'] = max(0, bs_5q['score'] - risk['weight'])
        bs_5q['risk'] = risk

    return {'stock_name': stock_name, 'grid': grid, 'data': data}


def fmt_score(score, width=4):
    if score is None:
        return '{:>{}}'.format('-', width)
    return '{:>{}.0f}'.format(score, width)


def _compute_roic(data):
    # NOPAT / 投入资本(债+权益−现金及短投,剔闲置流动资产);金融股/负分母/低谷各有护栏
    info = data.get('info', {})
    if 'Financial' in (info.get('sector') or ''):
        return None, 'financial'  # 银行/保险 ROIC 无意义,看 ROA

    income_ttm = data.get('income_ttm')
    bs_quarterly = data.get('bs_quarterly')

    op_income = get_val(income_ttm, 'Operating Income')
    debt = get_val(bs_quarterly, 'Total Debt')
    equity = get_val(bs_quarterly, 'Stockholders Equity')
    if op_income is None or debt is None or equity is None:
        return None, 'n/a'

    tax_rate = get_val(income_ttm, 'Tax Rate For Calcs')
    if tax_rate is None or tax_rate < 0 or tax_rate > 0.5:
        tax_rate = 0.21

    cash = get_val(bs_quarterly, 'Cash Cash Equivalents And Short Term Investments')
    if cash is None:
        cash = get_val(bs_quarterly, 'Cash And Cash Equivalents') or 0

    invested_capital = debt + equity - cash
    if invested_capital <= 0:
        return None, 'n/m'  # 净现金>投入资本 或 回购致负权益,分母失效

    nopat = op_income * (1 - tax_rate)
    roic = nopat / invested_capital
    return roic, ('trough' if op_income < 0 else '')


def print_summary(data):
    info = data.get('info', {})

    price = info.get('currentPrice')
    mcap = info.get('marketCap')
    pe = get_info_val(info, 'trailingPE')
    ps = get_info_val(info, 'priceToSalesTrailing12Months')
    pb = get_info_val(info, 'priceToBook')
    peg = get_info_val(info, 'pegRatio')
    ev_ebitda = get_info_val(info, 'enterpriseToEbitda')

    # 身份/规模
    ident = [
        'Price: ${:.2f}'.format(price) if price else 'Price: -',
        'MCap: {}'.format(format_value(mcap)) if mcap else 'MCap: -',
    ]
    print('  ' + '  '.join(ident))

    # 好价格:估值倍数
    value = [
        'P/E(TTM): {:.1f}'.format(pe) if pe and pe > 0 else 'P/E(TTM): -',
        'P/S(TTM): {:.1f}'.format(ps) if ps else 'P/S(TTM): -',
        'P/B: {:.1f}'.format(pb) if pb and pb > 0 else 'P/B: -',
        'EV/EBITDA: {:.1f}'.format(ev_ebitda) if ev_ebitda else 'EV/EBITDA: -',
        'PEG: {:.1f}'.format(peg) if peg else 'PEG: -',
    ]
    print('  ' + '  '.join(value))

    # 好公司:资本回报(ROIC 剔杠杆与闲置现金,比 ROE 回购虚高/ROA 商誉虚低干净)
    roic, note = _compute_roic(data)
    roe = info.get('returnOnEquity')
    roa = info.get('returnOnAssets')
    if roic is None:
        roic_str = 'ROIC: ' + {'financial': 'n/m(financial)', 'n/m': 'n/m'}.get(note, '-')
    else:
        roic_str = 'ROIC: {:.1f}%{}'.format(roic * 100, '(trough)' if note == 'trough' else '')
    quality = [
        roic_str,
        'ROE: {:.1f}%'.format(roe * 100) if roe is not None else 'ROE: -',
        'ROA: {:.1f}%'.format(roa * 100) if roa is not None else 'ROA: -',
    ]
    print('  ' + '  '.join(quality))

    mkt_ccy = info.get('currency', '')
    fin_ccy = info.get('financialCurrency', '')
    print('  Stock price in {}; Financial statements in {}'.format(mkt_ccy, fin_ccy))


def print_detail(result):
    stock_name = result['stock_name']
    grid = result['grid']
    data = result['data']

    width = 80
    print('\n' + '=' * width)
    print('{:^{}}'.format('HEALTH SCORECARD: {}'.format(stock_name), width))
    print('=' * width)

    print_summary(data)

    # 9-grid summary
    print('\n{:>18} {:>7} {:>7} {:>7}'.format('', '3yr', 'TTM', '5Q'))
    for label, key, _ in DIMENSIONS:
        scores = [grid['{}_{}'.format(key, p)]['score'] for p in PERIODS]
        print('{:>18} {:>7} {:>7} {:>7}'.format(
            label, *[fmt_score(s, 7) for s in scores]))

    # detail per dimension
    for label, key, _ in DIMENSIONS:
        for period in PERIODS:
            dim_key = '{}_{}'.format(key, period)
            dim = grid[dim_key]
            score_str = '{:.0f}'.format(dim['score']) if dim['score'] is not None else '-'
            print('\n--- {} {} ({}/100) ---'.format(label, period, score_str))
            for m in dim['metrics']:
                icon = STATUS_ICON[m['status']]
                detail = '  ' + m['detail'] if m['detail'] else ''
                print('  {} {:<24}{:<24}{}'.format(icon, m['name'], m['value'], detail))

    # risk flags
    risk = grid['bs_5q'].get('risk')
    if risk:
        print('\n--- RISK FLAGS ---')
        print('  {} {:<24}{:<24}{}'.format(
            STATUS_ICON[risk['status']], risk['name'], risk['value'],
            '  ' + risk['detail'] if risk['detail'] else ''))
    else:
        print('\n--- RISK FLAGS ---')
        print('  ✓ No flags')

    print('=' * width + '\n')


def print_ranking(results):
    header = '{:<10}  {:>4} {:>4} {:>4}  {:>4} {:>4} {:>4}  {:>4} {:>4} {:>4}'.format(
        'Stock', *['3yr', 'TTM', '5Q'] * 3)
    width = len(header) + 4
    print('\n' + '=' * width)
    print('{:^{}}'.format('HEALTH RANKING', width))
    print('=' * width)
    cat_header = '{:<10}  {:^14}  {:^14}  {:^14}'.format('', '--- Income ---', '---- CF ----', '---- BS ----')
    print('  ' + cat_header)
    print('  ' + header)
    print('  ' + '-' * len(header))
    for r in results:
        g = r['grid']
        scores = []
        for key in ['income', 'cf', 'bs']:
            for p in PERIODS:
                scores.append(g['{}_{}'.format(key, p)]['score'])
        fmt_scores = ' '.join(
            '{} {} {}'.format(fmt_score(scores[i]), fmt_score(scores[i + 1]), fmt_score(scores[i + 2]))
            for i in range(0, 9, 3))
        print('  {:<10}  {}'.format(r['stock_name'], fmt_scores))
    print('=' * width + '\n')
