import os
import json

DATA_DIR = 'financial_data'

ANCHOR_FIELDS = [
    'NetIncomeLoss',
    'ProfitLoss',
    'Assets',
    'NetCashProvidedByUsedInOperatingActivities',
    'Revenues',
    'RevenueFromContractWithCustomerExcludingAssessedTax',
    'RevenuesNetOfInterestExpense',
]


def load_facts(stock_name):
    path = os.path.join(DATA_DIR, '{}.json'.format(stock_name))
    with open(path) as f:
        data = json.load(f)
    return data['facts'].get('us-gaap', {})


def to_month(date_str):
    return date_str[:7]


def safe_fp(entry):
    return entry.get('fp') or ''


# --- period discovery ---

def find_periods(us_gaap, forms, count):
    months = set()
    for field_name in ANCHOR_FIELDS:
        field_data = us_gaap.get(field_name, {})
        for entries in field_data.get('units', {}).values():
            for e in entries:
                if e.get('form') in forms:
                    months.add(to_month(e['end']))
    return sorted(months, reverse=True)[:count]


def get_annual_periods(us_gaap, count=5):
    return find_periods(us_gaap, ['10-K', '20-F'], count)


def get_quarterly_periods(us_gaap):
    # Q4 has no 10-Q filing, so add annual periods to cover Q4
    q_periods = find_periods(us_gaap, ['10-Q', '6-K'], 20)
    a_periods = get_annual_periods(us_gaap)
    return sorted(set(q_periods + a_periods), reverse=True)


# --- single-period value extraction ---

def get_value(us_gaap, field_name, month, forms):
    field_data = us_gaap.get(field_name, {})

    for entries in field_data.get('units', {}).values():
        candidates = []
        for e in entries:
            if to_month(e['end']) == month and e.get('form') in forms:
                candidates.append(e)
        if candidates:
            candidates.sort(key=lambda e: e.get('filed', ''), reverse=True)
            return candidates[0]['val']
    return None


def get_ytd_value(us_gaap, field_name, month):
    forms = ['10-Q', '6-K']
    field_data = us_gaap.get(field_name, {})

    for entries in field_data.get('units', {}).values():
        candidates = []
        for e in entries:
            if to_month(e['end']) == month and e.get('form') in forms and safe_fp(e).startswith('Q'):
                candidates.append(e)
        if candidates:
            # earliest start = longest period = YTD cumulative (not single quarter)
            candidates.sort(key=lambda e: e.get('start', ''))
            return candidates[0]['val'], safe_fp(candidates[0])
    return None, None


def resolve_field(us_gaap, field_names, month, forms):
    for field_name in field_names:
        val = get_value(us_gaap, field_name, month, forms)
        if val is not None:
            return val, field_name
    return None, None


def resolve_ytd_field(us_gaap, field_names, month):
    for field_name in field_names:
        val, fp = get_ytd_value(us_gaap, field_name, month)
        if val is not None:
            return val, fp, field_name
    return None, None, None


# --- per-period extraction ---

def extract_annual_statement(us_gaap, template, month):
    statement = {}
    for label, field_names in template:
        if field_names:
            val, _ = resolve_field(us_gaap, field_names, month, ['10-K', '20-F'])
            statement[label] = val
        else:
            statement[label] = None
    return statement


def extract_quarterly_statement(us_gaap, template, month, prev_month, fy_month, is_period_data, pit_fields=None):
    """Extract single-quarter values for one period.

    For period data (income/cashflow):
      - Q1 (prev_month is None): take YTD directly
      - Q2/Q3 (prev_month set): current YTD - prev YTD
      - Q4 (fy_month set): FY - Q3 YTD (prev_month is Q3)

    For point-in-time data (balance sheet): take value directly
    pit_fields: fields to treat as point-in-time even in period data (e.g. EPS, shares)
    """
    statement = {}
    for label, field_names in template:
        if not field_names:
            statement[label] = None
            continue

        is_pit = pit_fields and set(field_names) & pit_fields

        if not is_period_data or is_pit:
            if fy_month:
                val, _ = resolve_field(us_gaap, field_names, fy_month, ['10-K', '20-F'])
            else:
                val, _ = resolve_field(us_gaap, field_names, month, ['10-Q', '6-K'])
            statement[label] = val
            continue

        if fy_month:
            # Q4 = FY - Q3 YTD
            fy_val, matched_field = resolve_field(us_gaap, field_names, fy_month, ['10-K', '20-F'])

            if fy_val is not None and prev_month:
                q3_ytd, _ = get_ytd_value(us_gaap, matched_field, prev_month)
                if q3_ytd is not None:
                    statement[label] = fy_val - q3_ytd
                else:
                    statement[label] = None
            else:
                statement[label] = None

        elif prev_month is None:
            # Q1: YTD = single quarter
            val, _, _ = resolve_ytd_field(us_gaap, field_names, month)
            statement[label] = val

        else:
            # Q2 or Q3: current YTD - prev YTD
            curr_val, _, matched_field = resolve_ytd_field(us_gaap, field_names, month)
            if curr_val is not None and matched_field:
                prev_val, _ = get_ytd_value(us_gaap, matched_field, prev_month)
                if prev_val is not None:
                    statement[label] = curr_val - prev_val
                else:
                    statement[label] = curr_val
            else:
                statement[label] = None

    return statement


# --- high-level extraction ---

def extract_annual(us_gaap, template, count=5):
    periods = get_annual_periods(us_gaap, count)

    period_statements = []
    for month in periods:
        statement = extract_annual_statement(us_gaap, template, month)
        period_statements.append((month, statement))

    return {
        'periods': periods,
        'rows': _pivot_rows(template, period_statements),
    }


def extract_quarterly(us_gaap, template, count=8, is_period_data=True, pit_fields=None):
    all_q_periods = get_quarterly_periods(us_gaap)
    annual_months = set(get_annual_periods(us_gaap))

    quarters = []
    for i, month in enumerate(all_q_periods):
        if month in annual_months:
            # Q4
            prev_month = all_q_periods[i + 1] if i + 1 < len(all_q_periods) else None
            quarters.append((month, prev_month, month))
        else:
            _, fp, _ = resolve_ytd_field(us_gaap, ANCHOR_FIELDS, month)
            if fp == 'Q1':
                quarters.append((month, None, None))
            else:
                prev_month = all_q_periods[i + 1] if i + 1 < len(all_q_periods) else None
                quarters.append((month, prev_month, None))

        if len(quarters) >= count:
            break

    period_statements = []
    for month, prev_month, fy_month in quarters:
        statement = extract_quarterly_statement(us_gaap, template, month, prev_month, fy_month, is_period_data, pit_fields)
        period_statements.append((month, statement))

    return {
        'periods': [m for m, _ in period_statements],
        'rows': _pivot_rows(template, period_statements),
    }


def _pivot_rows(template, period_statements):
    # transpose from per-period statements to per-account rows
    rows = []
    for label, _ in template:
        row = {'label': label}
        for period, statement in period_statements:
            row[period] = statement.get(label)
        rows.append(row)
    return rows


# --- display ---

def format_value(v):
    if v is None:
        return '-'
    if isinstance(v, float) and abs(v) < 100:
        return '{:.2f}'.format(v)
    sign = '-' if v < 0 else ''
    v = abs(v)
    if v >= 1e9:
        return '{}{:.2f}B'.format(sign, v / 1e9)
    if v >= 1e6:
        return '{}{}M'.format(sign, int(v / 1e6))
    if v >= 1e3:
        return '{}{}K'.format(sign, int(v / 1e3))
    return '{}{:.0f}'.format(sign, v)


def print_statement(title, statement_data):
    periods = statement_data['periods']
    rows = statement_data['rows']

    print('\n===== {} ====='.format(title))
    if not periods:
        print('  No data')
        return

    col_width = 12
    label_width = 40

    header = '{:<{w}}'.format('', w=label_width)
    for p in periods:
        header += '{:>{w}}'.format(p, w=col_width)
    print(header)
    print('-' * len(header))

    for row in rows:
        label = row['label']
        if not label:
            print()
            continue
        line = '{:<{w}}'.format(label, w=label_width)
        for p in periods:
            line += '{:>{w}}'.format(format_value(row.get(p)), w=col_width)
        print(line)
