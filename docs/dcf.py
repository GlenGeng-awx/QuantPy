"""
DCF 交叉验 Checklist v1.0 实装（Gordon 单阶段）

Principle: DCF = 内在价值定义。EPS×PE 模型是简化快捷版。
两者在 FCF≈NI 时一致；高 SBC → DCF>EPS（低估）；高 CapEx → DCF<EPS（高估）。

Formula (trailing, base = TTM FCF):
  DCF/sh = base × (1+g)/(r−g) + net_cash/sh
  P/FCF₀ = min((1+g)/(r−g), 30)      ← g≥r 或接近 r 时封顶 30x
  r = 伟大 9% / 好公司 10% / 平庸 11%  ← 质量调整（与折扣系数共享质量评分）

Usage:
  python3 docs/dcf.py WMT 6 好公司 2.609       # g=6%, quality, EPS for gap
  python3 docs/dcf.py WMT 6 好公司             # 无 EPS → 只输出 DCF，不算 gap
  python3 -c "import sys; sys.path.insert(0,'docs'); from dcf import dcf; import json; print(json.dumps(dcf('WMT',0.06,'好公司',2.609),indent=2,default=str))"

Args: STOCK, G (6 or 0.06), QUALITY (伟大/好公司/平庸), [EPS] optional normalized EPS for gap analysis
"""

import csv
import sys

QUALITY_R = {'伟大': 0.09, '好公司': 0.10, '平庸': 0.11}


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


def dcf(stock, g, quality, eps=None):
    """Compute DCF cross-check. g as decimal (0.06). quality in {伟大,好公司,平庸}.
    eps: normalized EPS for gap analysis (optional). Returns dict."""
    _, _, cf_gv, _ = load_csv('financial_data/%s/cf_ttm.csv' % stock)
    _, _, inc_gv, _ = load_csv('financial_data/%s/income_ttm.csv' % stock)
    _, _, bs_gv, _ = load_csv('financial_data/%s/bs_quarterly.csv' % stock)

    fcf = cf_gv('Free Cash Flow')
    sbc = cf_gv('Stock Based Compensation')
    repurchase = abs(cf_gv('Repurchase Of Capital Stock'))
    shares = inc_gv('Diluted Average Shares')
    gaap_eps = inc_gv('Diluted EPS')

    cash = bs_gv('Cash Cash Equivalents And Short Term Investments')
    total_debt = bs_gv('Total Debt')
    net_cash = cash - total_debt

    if quality not in QUALITY_R:
        raise ValueError('quality must be 伟大/好公司/平庸, got %s' % quality)
    r = QUALITY_R[quality]

    if shares == 0:
        raise ValueError('no shares data for %s' % stock)

    base_fcf = fcf / shares
    base_sbc = (fcf - sbc) / shares
    net_cash_sh = net_cash / shares

    p_fcf = min((1 + g) / (r - g), 30) if r > g else 30

    dcf_fcf = base_fcf * p_fcf + net_cash_sh
    dcf_sbc = base_sbc * p_fcf + net_cash_sh

    result = {
        'stock': stock,
        'g': g,
        'quality': quality,
        'r': r,
        'fcf': fcf,
        'sbc': sbc,
        'repurchase': repurchase,
        'shares': shares,
        'gaap_eps': gaap_eps,
        'base_fcf_sh': base_fcf,
        'base_sbc_sh': base_sbc,
        'net_cash': net_cash,
        'net_cash_sh': net_cash_sh,
        'p_fcf': p_fcf,
        'dcf_fcf': dcf_fcf,
        'dcf_sbc': dcf_sbc,
        'capped': (1 + g) / (r - g) >= 30 if r > g else True,
        'fcf_negative': fcf < 0,
        'sbc_negative': (fcf - sbc) < 0,
    }

    if eps is not None:
        eps_pe = min(8.5 + g * 100, 30)
        eps_fair = eps * eps_pe
        result['eps'] = eps
        result['eps_pe'] = eps_pe
        result['eps_fair'] = eps_fair
        result['gap1_eps_to_sbc'] = dcf_sbc - eps_fair
        result['gap2_sbc_to_fcf'] = dcf_fcf - dcf_sbc
        result['gap3_eps_to_fcf'] = dcf_fcf - eps_fair

    return result


def _fmt_money(v):
    if abs(v) >= 1e9:
        return '$%.2fB' % (v / 1e9)
    if abs(v) >= 1e6:
        return '$%.2fM' % (v / 1e6)
    return '$%.0f' % v


def print_dcf(stock, g, quality, eps=None):
    r = dcf(stock, g, quality, eps)

    print('=' * 70)
    print('DCF 交叉验: %s  (g=%.0f%%, r=%.0f%% %s)' % (stock, g * 100, r['r'] * 100, quality))
    print('=' * 70)
    print()
    print('Inputs (TTM):')
    print('  FCF           = %s   ($%.3f/sh)' % (_fmt_money(r['fcf']), r['base_fcf_sh']))
    sbc_str = _fmt_money(r['sbc']) if r['sbc'] else '$0 (非科技/无 SBC)'
    print('  SBC           = %s   (FCF−SBC $%.3f/sh)' % (sbc_str, r['base_sbc_sh']))
    buyback_cmp = '>' if r['repurchase'] > r['sbc'] else '≤'
    buyback_tag = '缩股→FCF 口径' if r['repurchase'] > r['sbc'] else '稀释→FCF−SBC 口径'
    print('  回购          = %s   %s SBC → 净%s' % (_fmt_money(r['repurchase']), buyback_cmp, buyback_tag))
    print('  shares        = %.3fB' % (r['shares'] / 1e9))
    nc_tag = '净现金' if r['net_cash'] > 0 else '净债无托底'
    print('  net_cash      = %s   ($%.3f/sh, %s)' % (_fmt_money(r['net_cash']), r['net_cash_sh'], nc_tag))
    print()
    raw_mult = (1 + r['g']) / (r['r'] - r['g']) if r['r'] > r['g'] else float('inf')
    raw_str = '{:.1f}'.format(raw_mult) if raw_mult != float('inf') else '∞ (g≥r)'
    print('P/FCF₀ = min((1+g)/(r−g), 30) = min({}, 30) = {:.1f}x  {}'.format(
        raw_str, r['p_fcf'], '← 封顶' if r['capped'] else ''))
    print()

    if r['fcf_negative']:
        print('⚠ FCF < 0 → DCF N/A，用 P/B 或恢复 EPS')
        return
    if r['sbc_negative']:
        print('⚠ FCF−SBC < 0 → 重麻烦 ×0.40（不否决），仅展示 DCF FCF')

    print('| 口径           | base ($/sh) | P/FCF₀ | DCF/sh   |')
    print('|----------------|-------------|--------|----------|')
    if not r['sbc_negative']:
        print('| DCF FCF−SBC   | ${:.3f}      | {:.1f}x   | ${:.2f}  |'.format(r['base_sbc_sh'], r['p_fcf'], r['dcf_sbc']))
    print('| DCF FCF        | ${:.3f}      | {:.1f}x   | ${:.2f}  |'.format(r['base_fcf_sh'], r['p_fcf'], r['dcf_fcf']))
    print()

    if eps is not None:
        print('EPS 模型: EPS ${:.3f} × PE {:.1f} = ${:.2f}'.format(r['eps'], r['eps_pe'], r['eps_fair']))
        print()
        print('gap 分析:')
        g1 = r['gap1_eps_to_sbc']
        g2 = r['gap2_sbc_to_fcf']
        g3 = r['gap3_eps_to_fcf']
        print('  gap 1 (EPS→FCF−SBC): ${:+.2f}  → PE 公式差异 + FCF vs NI 非SBC差异'.format(g1))
        if r['sbc'] > 0:
            print('  gap 2 (FCF−SBC→FCF): ${:+.2f}  → SBC 差异'.format(g2))
        else:
            print('  gap 2 (FCF−SBC→FCF): $0  → SBC=$0，两口径相同')
        print('  gap 3 (EPS→FCF):    ${:+.2f}  → gap1+gap2'.format(g3))
        if r['dcf_fcf'] < r['eps_fair'] - 0.01:
            print('  判断: DCF < EPS 模型（高 CapEx 压低 FCF，GOOG pattern）')
        elif r['dcf_sbc'] > r['eps_fair'] + 0.01:
            print('  判断: DCF > EPS 模型（高 SBC，EPS 被压低，TTD/CRM pattern）')
        else:
            print('  判断: DCF ≈ EPS 模型（FCF≈NI，结论稳健）')
        print()
        print('三口径: ${:.2f} (EPS) {} ${:.2f} (DCF−SBC) {} ${:.2f} (DCF FCF)'.format(
            r['eps_fair'],
            '<' if r['eps_fair'] < r['dcf_sbc'] else '>',
            r['dcf_sbc'],
            '<' if r['dcf_sbc'] < r['dcf_fcf'] else '>',
            r['dcf_fcf']))


def _parse_g(s):
    g = float(s.replace('%', ''))
    return g / 100 if g > 1 else g


if __name__ == '__main__':
    if len(sys.argv) < 4:
        print('Usage: python3 docs/dcf.py STOCK G QUALITY [EPS]')
        print('  G: 6 or 6% or 0.06')
        print('  QUALITY: 伟大 / 好公司 / 平庸')
        print('  EPS: normalized EPS for gap analysis (optional)')
        print()
        print('Examples:')
        print('  python3 docs/dcf.py WMT 6 好公司 2.609')
        print('  python3 docs/dcf.py NVDA 15 伟大 10.03')
        sys.exit(1)
    stock = sys.argv[1]
    g = _parse_g(sys.argv[2])
    quality = sys.argv[3]
    eps = float(sys.argv[4]) if len(sys.argv) > 4 else None
    print_dcf(stock, g, quality, eps)
