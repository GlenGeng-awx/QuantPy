import os
import pandas as pd
from fundamental.yahoo.format import load_csv, format_value


def get_val(df, field, col_idx=0):
    if df.empty or field not in df.index or col_idx >= len(df.columns):
        return None
    val = df.iloc[df.index.get_loc(field), col_idx]
    if pd.isna(val):
        return None
    return float(val)


def get_series(df, field, count=None):
    """Returns [(period_str, value), ...] newest first."""
    if df.empty or field not in df.index:
        return []
    cols = list(df.columns)[:count] if count else list(df.columns)
    result = []
    for col in cols:
        val = df.loc[field, col]
        result.append((col[:7], None if pd.isna(val) else float(val)))
    return result


def growth_rate(new, old):
    if new is None or old is None or old == 0:
        return None
    return (new - old) / abs(old)


def make_result(name, status, value, detail, weight):
    return {'name': name, 'status': status, 'value': value, 'detail': detail, 'weight': weight}


# --- price data ---

def load_price_data(stock_name):
    path = os.path.join('stock_data', '{}_1d.csv'.format(stock_name))
    if not os.path.exists(path):
        return pd.DataFrame()
    df = pd.read_csv(path)
    df['date'] = df['Date'].apply(lambda x: x.split()[0])
    return df


def get_price_at_date(price_df, date_str):
    """Find close price on or before date_str (YYYY-MM-DD)."""
    if price_df.empty:
        return None
    mask = price_df['date'] <= date_str
    if not mask.any():
        return None
    idx = mask[mask].index[-1]
    return float(price_df.loc[idx, 'close'])


# --- EDGAR EPS ---

def load_edgar_eps(stock_name):
    """Returns (quarterly_eps, annual_eps).
    quarterly_eps: [(month, eps), ...] chronological, single-quarter values
    annual_eps: {month: eps} full-year values
    Returns (None, None) if no data.
    """
    path = os.path.join('financial_data/edgar', '{}.json'.format(stock_name))
    if not os.path.exists(path):
        return None, None

    from fundamental.edgar.format import (
        load_facts, to_month, ANNUAL_FORMS, QUARTERLY_FORMS,
    )

    us_gaap = load_facts(stock_name)

    eps_field = None
    for name in ['EarningsPerShareDiluted', 'EarningsPerShareBasic']:
        if name in us_gaap:
            eps_field = name
            break
    if not eps_field:
        return None, None

    all_entries = []
    for unit_entries in us_gaap[eps_field].get('units', {}).values():
        all_entries.extend(unit_entries)

    # Annual EPS (10-K/20-F, latest filed wins)
    fy_raw = {}
    for e in all_entries:
        if e.get('form') not in ANNUAL_FORMS:
            continue
        month = to_month(e['end'])
        filed = e.get('filed', '')
        if month not in fy_raw or filed > fy_raw[month][1]:
            fy_raw[month] = (e['val'], filed)
    annual_eps = {m: v for m, (v, _) in fy_raw.items()}

    # Single-quarter EPS from 10-Q (latest start = shortest period)
    q_raw = {}
    for e in all_entries:
        if e.get('form') not in QUARTERLY_FORMS:
            continue
        if not e.get('start'):
            continue
        month = to_month(e['end'])
        start = e['start']
        filed = e.get('filed', '')
        if month not in q_raw or (start, filed) > (q_raw[month][1], q_raw[month][2]):
            q_raw[month] = (e['val'], start, filed)
    single_q = {m: v for m, (v, _, _) in q_raw.items()}

    # Q4: FY - Q3 YTD (earliest start = longest period)
    ytd_raw = {}
    for e in all_entries:
        if e.get('form') not in QUARTERLY_FORMS:
            continue
        if not e.get('start'):
            continue
        month = to_month(e['end'])
        start = e['start']
        if month not in ytd_raw or start < ytd_raw[month][1]:
            ytd_raw[month] = (e['val'], start)

    for fy_month, fy_val in annual_eps.items():
        if fy_month in single_q:
            continue
        candidates = [(m, v) for m, (v, _) in ytd_raw.items() if m < fy_month]
        if candidates:
            candidates.sort(reverse=True)
            _, q3_ytd_val = candidates[0]
            single_q[fy_month] = round(fy_val - q3_ytd_val, 4)

    if not single_q:
        return None, annual_eps or None

    quarterly_eps = sorted(single_q.items())
    return quarterly_eps, annual_eps


# --- aggregate loader ---

def load_all_data(stock_name):
    quarterly_eps, annual_eps = load_edgar_eps(stock_name)
    return {
        'stock_name': stock_name,
        'income_annual': load_csv(stock_name, 'income_annual'),
        'income_quarterly': load_csv(stock_name, 'income_quarterly'),
        'bs_quarterly': load_csv(stock_name, 'bs_quarterly'),
        'cf_annual': load_csv(stock_name, 'cf_annual'),
        'cf_quarterly': load_csv(stock_name, 'cf_quarterly'),
        'price': load_price_data(stock_name),
        'edgar_quarterly_eps': quarterly_eps,
        'edgar_annual_eps': annual_eps,
    }
