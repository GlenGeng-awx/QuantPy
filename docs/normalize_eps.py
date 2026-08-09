"""
Normal EPS Checklist v3.1

Principle: scan ALL income statement lines for one-time items, strip them.
Tool's Total Unusual Items is cross-check, not primary mechanism.

Step 1: GAAP baseline
Step 2: Scan for one-time items (plug-in detectors)
  2a: Other Income -> quarterly volatility -> investment MTM
  2b: Restructuring -> non-zero
  2c: Tax rate -> vs historical
  2d: OpInc -> quarterly trend -> sudden drop (cross-ref 2e/2f/2g)
  2e: Gross Margin -> vs historical -> COGS anomaly (NEW)
  2f: R&D/Revenue -> vs historical -> IPR&D (NEW)
  2g: SGA/Revenue -> vs historical -> legal/impairment (NEW)
  2h: Discontinued operations -> NI vs NI_continuing (NEW)
Step 3: Cross-check with Total Unusual Items, resolve overlaps
Step 4: Normalized NI = GAAP NI - after-tax one-time items
Step 5: Cross-check with tool's Normalized Income
"""

import csv


def load_csv(path):
    with open(path) as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    cols = list(rows[0].keys())
    periods = cols[1:]

    def gv(field, idx=0):
        for r in rows:
            if r[cols[0]] == field:
                v = r[periods[idx]] if idx < len(periods) else ''
                return float(v) if v and v != '' else 0
        return 0

    def has(field):
        return any(r[cols[0]] == field for r in rows)

    return rows, periods, gv, has


def get_net_int(gv, has_fn, idx=0):
    if has_fn('Net Non Operating Interest Income Expense'):
        v = gv('Net Non Operating Interest Income Expense', idx)
        if v != 0:
            return v
    if has_fn('Net Interest Income'):
        v = gv('Net Interest Income', idx)
        if v != 0:
            return v
    return gv('Interest Income Non Operating', idx) - gv('Interest Expense Non Operating', idx)


def get_non_int_other(gv, has_fn, opinc, pretax, net_int, idx=0):
    if has_fn('Other Income Expense') and gv('Other Income Expense', idx) != 0:
        other = gv('Other Income Expense', idx)
        gap = pretax - opinc - other - net_int
        if abs(gap) < max(abs(pretax), 1) * 0.001:
            return other, 'Other Inc (direct)'
        return pretax - opinc - net_int, 'gap (Other=%s gap=%s)' % ('{:,.0f}'.format(other), '{:,.0f}'.format(gap))
    return pretax - opinc - net_int, 'gap'


# ============================================================
# Step 2 Detectors (plug-in architecture)
# ============================================================

def detect_2a_other_income_mtm(ttm_gv, ttm_has, q_gv, q_has, q_periods, ni):
    """2a: Other Income Expense volatility -> investment MTM (HIGH confidence)"""
    opinc = ttm_gv('Operating Income')
    pretax = ttm_gv('Pretax Income')
    net_int = get_net_int(ttm_gv, ttm_has)
    non_int_ttm, src = get_non_int_other(ttm_gv, ttm_has, opinc, pretax, net_int)

    if abs(non_int_ttm) < abs(ni) * 0.01:
        return None

    q_vals = []
    for i in range(min(5, len(q_periods))):
        q_pretax = q_gv('Pretax Income', i)
        q_opinc = q_gv('Operating Income', i)
        q_net_int = get_net_int(q_gv, q_has, i)
        q_non_int, _ = get_non_int_other(q_gv, q_has, q_opinc, q_pretax, q_net_int, i)
        q_vals.append(q_non_int)

    if len(q_vals) < 2:
        return None

    max_v = max(q_vals)
    min_v = min(q_vals)
    range_v = max_v - min_v
    avg_abs = sum(abs(x) for x in q_vals) / len(q_vals)
    vol_ratio = range_v / avg_abs if avg_abs > 0 else 0
    has_neg = any(x < 0 for x in q_vals)

    if vol_ratio > 2 or (has_neg and abs(non_int_ttm) > abs(ni) * 0.03):
        return {
            'name': '2a:OtherInc(MTM)',
            'amount_pretax': non_int_ttm,
            'confidence': 'high',
            'detail': 'vol=%.1fx range=%s~%s' % (vol_ratio, '{:,.0f}'.format(min_v), '{:,.0f}'.format(max_v)),
        }
    return None


def detect_2b_restructuring(ttm_gv, ttm_has):
    """2b: Restructuring charges (FLAG ONLY - expense not gain, per 'don't add back losses')"""
    if not ttm_has('Restructuring And Mergern Acquisition'):
        return None
    r = ttm_gv('Restructuring And Mergern Acquisition')
    if r != 0:
        return {
            'name': '2b:Restructuring',
            'amount_pretax': r,
            'confidence': 'low',
            'detail': '%s (expense, flag only)' % '{:,.0f}'.format(r),
        }
    return None


def detect_2c_tax_anomaly(ttm_gv, a_gv, a_periods, pretax):
    """2c: Tax rate anomaly (MEDIUM confidence)
    Step 1 (abs): TTM rate < 0% on positive pretax = DTA release -> use 21% statutory
    Step 2 (rel): |TTM - hist avg| > 10pp -> use historical average
    Both: abs fires first (returns early); rel only if abs doesn't fire.
    """
    tax = ttm_gv('Tax Provision')
    ttm_rate = tax / pretax if pretax else 0

    # Step 1: Absolute check (NEW) — negative tax rate on positive pretax = DTA release
    STATUTORY_RATE = 0.21
    if pretax > 0 and ttm_rate < 0:
        one_time_tax = tax - STATUTORY_RATE * pretax
        return {
            'name': '2c:TaxAnomaly(abs)',
            'amount_after_tax': one_time_tax,
            'confidence': 'medium',
            'normal_rate': STATUTORY_RATE,
            'detail': 'TTM %.1f%% < 0%% (DTA release) -> statutory 21%%' % (ttm_rate * 100),
        }

    # Step 2: Relative check — vs historical average
    hist_rates = []
    for i in range(min(4, len(a_periods))):
        t = a_gv('Tax Provision', i)
        p = a_gv('Pretax Income', i)
        if t and p and p != 0:
            hist_rates.append(t / p)

    if not hist_rates:
        return None

    avg_rate = sum(hist_rates) / len(hist_rates)
    diff = abs(ttm_rate - avg_rate)

    if diff > 0.10:
        one_time_tax = tax - avg_rate * pretax
        return {
            'name': '2c:TaxAnomaly(rel)',
            'amount_after_tax': one_time_tax,
            'confidence': 'medium',
            'normal_rate': avg_rate,
            'detail': 'TTM %.1f%% vs hist %.1f%% (diff %.1fpp)' % (ttm_rate * 100, avg_rate * 100, diff * 100),
        }
    return None


def detect_2d_opinc_drop(q_gv, q_periods):
    """2d: OpInc sudden drop (LOW confidence, needs external confirmation)"""
    opinc = [q_gv('Operating Income', i) for i in range(min(5, len(q_periods)))]
    revs = [q_gv('Total Revenue', i) for i in range(min(5, len(q_periods)))]
    if len(opinc) < 2:
        return None

    opm0 = opinc[0] / revs[0] * 100 if revs[0] else 0
    opm1 = opinc[1] / revs[1] * 100 if revs[1] else 0

    if opinc[0] is not None and opinc[1] is not None:
        if opinc[0] < 0 and opinc[1] > 0:
            return {
                'name': '2d:OpIncDrop',
                'amount_pretax': None,
                'confidence': 'low',
                'detail': 'OpInc turned neg: Q0=%s Q1=%s' % ('{:,.0f}'.format(opinc[0]), '{:,.0f}'.format(opinc[1])),
            }
        if opinc[1] != 0:
            chg = (opinc[0] / opinc[1] - 1) * 100
            if chg < -30:
                return {
                    'name': '2d:OpIncDrop',
                    'amount_pretax': None,
                    'confidence': 'low',
                    'detail': 'QoQ %+.0f%%: Q0=%s Q1=%s' % (chg, '{:,.0f}'.format(opinc[0]), '{:,.0f}'.format(opinc[1])),
                }
    return None


def detect_2e_gm_drop(ttm_gv, a_gv, a_periods, revenue):
    """2e: Gross Margin drop vs historical -> COGS anomaly (MEDIUM confidence, NEW)"""
    gp = ttm_gv('Gross Profit')
    if not gp or not revenue:
        return None
    ttm_gm_pct = gp / revenue * 100

    hist_gm = []
    for i in range(min(3, len(a_periods))):
        h_gp = a_gv('Gross Profit', i)
        h_rev = a_gv('Total Revenue', i)
        if h_gp and h_rev and h_rev != 0:
            hist_gm.append(h_gp / h_rev * 100)

    if len(hist_gm) < 2:
        return None
    avg_gm = sum(hist_gm) / len(hist_gm)
    drop = avg_gm - ttm_gm_pct

    if drop > 5:
        amount = drop / 100 * revenue
        return {
            'name': '2e:GMDrop',
            'amount_pretax': amount,
            'confidence': 'medium',
            'detail': 'TTM %.1f%% vs hist %.1f%% (drop %.1fpp)' % (ttm_gm_pct, avg_gm, drop),
        }
    return None


def detect_2f_rd_spike(ttm_gv, ttm_has, a_gv, a_has, a_periods, revenue):
    """2f: R&D/Revenue spike vs historical -> IPR&D (MEDIUM confidence, NEW)"""
    if not ttm_has('Research And Development'):
        return None
    rd = ttm_gv('Research And Development')
    if not rd or not revenue:
        return None
    ttm_rd_pct = rd / revenue * 100

    hist_rd = []
    for i in range(min(3, len(a_periods))):
        h_rd = a_gv('Research And Development', i) if a_has('Research And Development') else 0
        h_rev = a_gv('Total Revenue', i)
        if h_rd and h_rev and h_rev != 0:
            hist_rd.append(h_rd / h_rev * 100)

    if len(hist_rd) < 2:
        return None
    avg_rd = sum(hist_rd) / len(hist_rd)
    spike = ttm_rd_pct - avg_rd

    if spike > 3:
        amount = spike / 100 * revenue
        return {
            'name': '2f:RDSpike',
            'amount_pretax': amount,
            'confidence': 'medium',
            'detail': 'TTM %.1f%% vs hist %.1f%% (spike %.1fpp)' % (ttm_rd_pct, avg_rd, spike),
        }
    return None


def detect_2g_sga_spike(ttm_gv, a_gv, a_periods, revenue):
    """2g: SGA/Revenue spike vs historical -> legal/impairment (LOW confidence, NEW)"""
    sga = ttm_gv('Selling General And Administration')
    if not sga or not revenue:
        return None
    ttm_sga_pct = sga / revenue * 100

    hist_sga = []
    for i in range(min(3, len(a_periods))):
        h_sga = a_gv('Selling General And Administration', i)
        h_rev = a_gv('Total Revenue', i)
        if h_sga and h_rev and h_rev != 0:
            hist_sga.append(h_sga / h_rev * 100)

    if len(hist_sga) < 2:
        return None
    avg_sga = sum(hist_sga) / len(hist_sga)
    spike = ttm_sga_pct - avg_sga

    if spike > 3:
        amount = spike / 100 * revenue
        return {
            'name': '2g:SGASpike',
            'amount_pretax': amount,
            'confidence': 'low',
            'detail': 'TTM %.1f%% vs hist %.1f%% (spike %.1fpp)' % (ttm_sga_pct, avg_sga, spike),
        }
    return None


def detect_2h_discontinued(ttm_gv, ttm_has):
    """2h: Discontinued operations (HIGH confidence, NEW)"""
    if not ttm_has('Net Income From Continuing Operation Net Minority Interest'):
        return None
    ni_total = ttm_gv('Net Income')
    ni_cont = ttm_gv('Net Income From Continuing Operation Net Minority Interest')
    diff = ni_total - ni_cont
    if abs(diff) > max(abs(ni_total), 1) * 0.001:
        return {
            'name': '2h:Discontinued',
            'amount_after_tax': diff,
            'confidence': 'high',
            'detail': 'NI=%s vs Cont=%s (diff=%s)' % (
                '{:,.0f}'.format(ni_total), '{:,.0f}'.format(ni_cont), '{:,.0f}'.format(diff)),
        }
    return None


# ============================================================
# Main
# ============================================================

def normalize_eps(stock):
    _, ttm_p, ttm, has_t = load_csv('financial_data/%s/income_ttm.csv' % stock)
    _, q_p, q, has_q = load_csv('financial_data/%s/income_quarterly.csv' % stock)
    _, a_p, a, has_a = load_csv('financial_data/%s/income_annual.csv' % stock)

    # Step 1
    ni = ttm('Net Income')
    gaap_eps = ttm('Diluted EPS')
    shares = ttm('Diluted Average Shares')
    pretax = ttm('Pretax Income')
    tax = ttm('Tax Provision')
    tax_rate = tax / pretax if pretax else 0
    op_inc = ttm('Operating Income')
    revenue = ttm('Total Revenue')
    gross_profit = ttm('Gross Profit')
    rd = ttm('Research And Development')
    sga = ttm('Selling General And Administration')

    # Step 2: Scan
    findings = []

    r = detect_2a_other_income_mtm(ttm, has_t, q, has_q, q_p, ni)
    if r:
        findings.append(r)

    r = detect_2b_restructuring(ttm, has_t)
    if r:
        findings.append(r)

    r = detect_2c_tax_anomaly(ttm, a, a_p, pretax)
    if r:
        findings.append(r)

    r = detect_2d_opinc_drop(q, q_p)
    if r:
        findings.append(r)

    r = detect_2e_gm_drop(ttm, a, a_p, revenue)
    if r:
        findings.append(r)

    r = detect_2f_rd_spike(ttm, has_t, a, has_a, a_p, revenue)
    if r:
        findings.append(r)

    r = detect_2g_sga_spike(ttm, a, a_p, revenue)
    if r:
        findings.append(r)

    r = detect_2h_discontinued(ttm, has_t)
    if r:
        findings.append(r)

    # Step 3: Cross-check with Unusual
    unusual = ttm('Total Unusual Items')
    tax_effect = ttm('Tax Effect Of Unusual Items')
    norm_tool = ttm('Normalized Income')

    # Resolve overlap: Other Income (2a) vs Unusual
    other_finding = None
    for f in findings:
        if 'OtherInc' in f['name']:
            other_finding = f
            break

    if unusual != 0 and other_finding:
        other_amt = other_finding['amount_pretax']
        diff = abs(other_amt - unusual)
        base = max(abs(other_amt), abs(unusual), 1)
        ratio = diff / base
        if ratio < 0.20:
            # Overlap — use larger
            if abs(unusual) > abs(other_amt):
                other_finding['amount_pretax'] = unusual
                other_finding['name'] += '+Unusual'
            other_finding['detail'] += ' | Unusual=%s (overlap %.1f%%)' % ('{:,.0f}'.format(unusual), ratio * 100)
        else:
            # Independent
            findings.append({
                'name': '2x:Unusual(tool)',
                'amount_pretax': unusual,
                'confidence': 'high',
                'detail': '%s (diff %.1f%%)' % ('{:,.0f}'.format(unusual), ratio * 100),
            })
    elif unusual != 0 and not other_finding:
        findings.append({
            'name': '2x:Unusual(tool)',
            'amount_pretax': unusual,
            'confidence': 'high',
            'detail': '%s' % '{:,.0f}'.format(unusual),
        })

    # Step 4: Calculate
    # Only use high+medium confidence findings for calculation
    # Low confidence (2d, 2g) are flagged but not auto-stripped
    total_pretax_adj = 0
    total_after_tax_adj = 0
    for f in findings:
        conf = f.get('confidence', 'medium')
        if conf == 'low':
            continue  # flag only, don't auto-strip
        if f.get('amount_pretax') is not None:
            total_pretax_adj += max(0, f['amount_pretax'])
        elif f.get('amount_after_tax') is not None:
            total_after_tax_adj += max(0, f['amount_after_tax'])

    # Tax rate: use 2c's normal_rate if triggered (statutory for abs, historical for rel)
    has_tax_anomaly = any('TaxAnomaly' in f['name'] for f in findings)
    if has_tax_anomaly:
        tax_finding = next(f for f in findings if 'TaxAnomaly' in f['name'])
        use_tax_rate = tax_finding.get('normal_rate', tax_rate)
    else:
        use_tax_rate = tax_rate

    norm_pretax = pretax - total_pretax_adj
    norm_ni = norm_pretax * (1 - use_tax_rate) - total_after_tax_adj
    norm_eps = norm_ni / shares if shares else 0
    tool_eps = norm_tool / shares if shares else 0

    # Guard: v3.1 > GAAP occurs when negative tax + no stripping; min() catches but v3.1 is meaningless
    v331_gt_gaap = norm_eps > gaap_eps

    return {
        'stock': stock,
        'gaap_eps': gaap_eps,
        'norm_eps': norm_eps,
        'tool_eps': tool_eps,
        'findings': findings,
        'unusual': unusual,
        'total_pretax_adj': total_pretax_adj,
        'total_after_tax_adj': total_after_tax_adj,
        'norm_ni': norm_ni,
        'norm_tool': norm_tool,
        'use_tax_rate': use_tax_rate,
        'v331_gt_gaap': v331_gt_gaap,
    }


if __name__ == '__main__':
    BANKS = {'JPM', 'BAC', 'GS', 'MS'}
    STOCKS = [
        'NVDA', 'GOOG', 'AAPL', 'MSFT', 'AMZN', 'TSM', 'AVGO', 'META', 'TSLA', 'LLY',
        'WMT', 'V', 'JNJ', 'ASML', 'XOM', 'AMD', 'INTC', '0700.HK', 'ORCL', 'MA', 'NFLX',
        'CVX', 'PG', 'KO', 'PLTR', 'BABA', 'MRK', 'NVO', 'QCOM', 'DELL',
        'MCD', 'DIS', 'SHOP', 'PFE', 'GILD', 'BA', 'UBER', 'PDD', 'CRM', 'SPOT',
        'ADBE', 'HOOD', 'NU', 'SE', 'SNOW', 'COIN', 'PYPL', 'CPNG', 'EBAY', 'XYZ',
        'TCOM', 'JD', 'BIDU', 'ERIC', 'BNTX', 'ZM', 'AFRM', 'HPQ', 'RIVN', 'OKTA',
        'BEKE', 'FUTU', 'TME', 'PINS', 'LI', 'XPEV', 'NIO', 'CRCL', 'TTD', 'SNAP',
        'BILI', 'KLAR',
    ]

    print('%-10s %9s %9s %9s %8s  %s' % ('Stock', 'GAAP', 'v3.1', 'Tool', 'vs Tool', 'Detectors triggered'))
    print('-' * 110)

    matched = 0
    for s in STOCKS:
        if s in BANKS:
            continue
        try:
            r = normalize_eps(s)
            diff = r['norm_eps'] - r['tool_eps']
            high_med = [f['name'].split(':')[1].split('(')[0].split('+')[0] for f in r['findings'] if f.get('confidence') in ('high', 'medium')]
            low = [f['name'].split(':')[1].split('(')[0] for f in r['findings'] if f.get('confidence') == 'low']
            detectors = ', '.join(high_med + ['[%s]' % x for x in low]) if (high_med or low) else '(none)'
            print('%-10s $%8.2f $%8.2f $%8.2f %+7.2f  %s' % (
                s, r['gaap_eps'], r['norm_eps'], r['tool_eps'], diff, detectors))
            if abs(diff) < 0.50:
                matched += 1
        except Exception as e:
            print('%-10s ERROR: %s' % (s, e))

    total = len([s for s in STOCKS if s not in BANKS])
    print('\nMatched tool (diff < $0.50): %d/%d' % (matched, total))
