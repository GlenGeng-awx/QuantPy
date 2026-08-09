"""价值投资汇总报告生成器（决策聚焦的多视角机会筛选器）

每日读 ai_report/{STOCK}/output_a.md（现价/安全边际/入池信号/操作）
       + ai_report/{STOCK}/output_d.md（合理价/满仓/系数/DCF 三口径/质量×麻烦）
→ 产 ai_report/comparison.{date}.md（7 章节，含三 Top 10 + 隐藏机会屏 + DCF 信号层）

纯 join + 格式化，不重算 price-derived 量（现价/安全边际/P/E 是 Task A 的活）。
唯一派生：DCF 信号标签、DCF FCF 安全边际、隐藏机会筛选。

Usage:
  python3 docs/gen_comparison.py                       # 用系统当日
  python3 docs/gen_comparison.py --date 2026-08-09
  python3 docs/gen_comparison.py --date 2026-08-09 --out path.md
"""

import unicodedata
import re
import os
import json


def w(s):
    """显示宽度：CJK/全宽=2，其余=1"""
    s = str(s)
    n = 0
    for ch in s:
        n += 2 if unicodedata.east_asian_width(ch) in ('W', 'F') else 1
    return n


def pad(s, width):
    """按显示宽度右 pad 空格"""
    s = str(s)
    return s + ' ' * (width - w(s))


def table(rows, headers):
    """CJK 对齐的 markdown 表格"""
    cols = len(headers)
    cw = [max(w(headers[c]), max((w(r[c]) for r in rows), default=0)) for c in range(cols)]
    out = ['| ' + ' | '.join(pad(headers[c], cw[c]) for c in range(cols)) + ' |']
    out.append('|' + '|'.join('-' * (cw[c] + 2) for c in range(cols)) + '|')
    for r in rows:
        out.append('| ' + ' | '.join(pad(r[c], cw[c]) for c in range(cols)) + ' |')
    return '\n'.join(out)


def _to_float(s):
    """'$10.64' / '62.9%' / '+10.4%' / '−39.7%' → float。失败返回 None"""
    if s is None:
        return None
    s = str(s).replace(',', '').replace('+', '').replace('−', '-').replace('~', '')
    m = re.search(r'-?\d+\.?\d*', s)
    return float(m.group()) if m else None


def _extract_signal_val(val_cell):
    """从 A.1 实际值列提取主数值+单位（括号前，如 18% / 39.4x / -56.2%）；N/A 或 —（轻资产）返回 N/A"""
    if not val_cell:
        return ''
    s = val_cell.strip()
    if 'N/A' in s[:10].upper():
        return 'N/A'
    main = re.split(r'[（(]', s)[0].strip()
    if not main or main in ('—', '-', '—'):
        return 'N/A'
    m = re.search(r'([−–-]?[\d.]+)\s*(%|x)', main)
    if m:
        num = m.group(1).replace('−', '-').replace('–', '-')
        return f'{num}{m.group(2)}'
    return ''


def parse_output_a(path):
    """解析 output_a.md → dict。解析失败字段为 None, 不抛异常。"""
    stock = os.path.basename(os.path.dirname(path))
    try:
        text = open(path, encoding='utf-8').read()
    except FileNotFoundError:
        return {'stock': stock, 'parse_error': 'file not found'}

    r = {'stock': stock, 'date': None, 'price': None,
         'eps_safety_margin': None, 'signal_count': None,
         'drawdown_1y': None, 'operation': None, 'signals': {}, 'signal_values': {}}

    # date + price: > 更新: YYYY-MM-DD  现价 $XX.XX  (多币种 HK$/¥)
    m = re.search(r'更新:\s*(\d{4}-\d{2}-\d{2}).*?现价\s*(?:HK\$|¥|\$)?([\d,]+\.?\d*)', text)
    if m:
        r['date'] = m.group(1)
        r['price'] = _to_float(m.group(2))

    # signal_count: 命中: **N/7** 或 命中: N/7
    m = re.search(r'命中:\s*\**(\d+)/7', text)
    if m:
        r['signal_count'] = int(m.group(1))

    # signals: 7 项粗筛逐项 ✓/✗/— + 实际值（A.1 表 # 1-7 行，末列为状态，cells[3]为实际值）
    signals = {}
    signal_values = {}
    for sm in re.finditer(r'^\|.*$', text, re.MULTILINE):
        cells = [c.strip() for c in sm.group(0).split('|')[1:-1]]
        if not cells or cells[0] not in ('1','2','3','4','5','6','7'):
            continue
        n = int(cells[0])
        if len(cells) >= 5:
            state = cells[-1]
            val_cell = cells[3] if len(cells) > 3 else ''
            if '✓' in state:
                signals[n] = '✓'
            elif '✗' in state:
                signals[n] = '✗'
            else:
                signals[n] = '—'
            signal_values[n] = _extract_signal_val(val_cell)
    r['signals'] = signals
    r['signal_values'] = signal_values
    if r['signal_count'] is None and signals:
        r['signal_count'] = sum(1 for v in signals.values() if v == '✓')

    # drawdown_1y: | 1 | 1Y 回撤 | >40% | NN%(...) |
    m = re.search(r'\|\s*1\s*\|\s*1Y\s*回撤.*?\|\s*[<>]\s*\d+%?\s*\|\s*([\d.]+)%', text)
    if m:
        r['drawdown_1y'] = _to_float(m.group(1))

    # eps_safety_margin: 优先表格 | 安全边际 | ±N% |
    m = re.search(r'\|\s*\**安全边际[^|]*\|\s*\**([-−+\d.]+)%', text)
    if m:
        r['eps_safety_margin'] = _to_float(m.group(1))
    else:
        # fallback: 正文 "安全边际 ... ±N%"
        m = re.search(r'安全边际[^=]*=?\s*\**([-−+\d.]+)%', text)
        if m:
            r['eps_safety_margin'] = _to_float(m.group(1))

    # operation: 归类: 或 操作: 后首个关键词（到 * — ， 。 | 空格 （ ( 止）
    for kw in ['归类:', '操作:']:
        m = re.search(kw + r'\s*\**([^*—，。|\n （(]+)', text)
        if m:
            op = m.group(1).strip().rstrip('*').strip()
            r['operation'] = op
            break
    # 无 归类/操作 行时从 入池/不入池 推断
    if r['operation'] is None:
        if '不入池' in text:
            r['operation'] = '买贵了'
        elif '入池' in text:
            r['operation'] = '小仓/观察'

    return r


def _last_dollar_value(line):
    """取一行中最后一个 $XX.XX 数值。'合理价 = $a × b = $10.64' → 10.64"""
    vals = re.findall(r'(?:HK\$|¥|\$)([\d,]+\.?\d*)', line)
    if vals:
        return _to_float(vals[-1])
    return None


def _parse_dcf_cell(val_cell):
    """解析 DCF 表格第 4 列（DCF/sh）。N/A/nan/空/−/$nan → None"""
    if val_cell is None:
        return None
    if 'N/A' in val_cell or 'nan' in val_cell.lower() or val_cell in ('', '—'):
        return None
    vm = re.search(r'-?~?\$?([\d,]+\.?\d*)', val_cell.replace('−', '-'))
    return _to_float(vm.group()) if vm else None


def parse_output_d(path):
    """解析 output_d.md → dict。解析失败字段为 None, 不抛异常。"""
    stock = os.path.basename(os.path.dirname(path))
    try:
        text = open(path, encoding='utf-8').read()
    except FileNotFoundError:
        return {'stock': stock, 'parse_error': 'file not found'}

    r = {'stock': stock, 'fair_price': None, 'full_position': None,
         'eps_fair_price': None, 'dcf_fcf_sbc': None, 'dcf_fcf': None,
         'quality_trouble': None, 'g': None, 'coefficient': None,
         'eps': None, 'pe': None, 'is_midcycle': False,
         'gaap_eps': None, 'r_rate': None, 'p_fcf0': None,
         'base_fcf': None, 'base_sbc': None}

    # fair_price: 优先无括号 "合理价 = $X"（中值/主口径），fallback 首个有括号 "合理价（口径）= $X"
    last_v_line = None
    for m in re.finditer(r'^(.*?合理价\s*=\s*.+)$', text, re.MULTILINE):
        line = m.group(1)
        if line.strip().startswith('>') or 'EPS 模型合理价' in line:
            continue
        if '无意义' in line or 'N/A' in line.upper() or '负值' in line:
            break
        if re.search(r'[\d.]+\s*-\s*\$?[\d.]+', line.split('=')[-1]):
            break
        v = _last_dollar_value(line)
        if v is not None:
            last_v_line = line
            r['fair_price'] = v
            r['eps_fair_price'] = v
            break
    if last_v_line is None:
        for m in re.finditer(r'^(.*?合理价\s*[（(][^)）]*[)）]\s*=\s*.+)$', text, re.MULTILINE):
            line = m.group(1)
            if line.strip().startswith('>') or 'EPS 模型合理价' in line:
                continue
            if '无意义' in line or 'N/A' in line.upper() or '负值' in line:
                break
            if re.search(r'[\d.]+\s*-\s*\$?[\d.]+', line.split('=')[-1]):
                break
            v = _last_dollar_value(line)
            if v is not None:
                last_v_line = line
                r['fair_price'] = v
                r['eps_fair_price'] = v
                break
    if last_v_line is not None:
        epm = re.search(r'\$([\d.]+)\s*[×x]\s*([\d.]+)\s*=', last_v_line)
        if epm:
            r['eps'] = _to_float(epm.group(1))
            r['pe'] = _to_float(epm.group(2))

    # full_position: "满仓目标 = ... = $YY"
    m = re.search(r'^.*?满仓目标\s*=\s*.+$', text, re.MULTILINE)
    if m:
        line = m.group(0)
        if '不适用' in line or '无意义' in line or '无折扣' in line:
            r['full_position'] = None
        else:
            r['full_position'] = _last_dollar_value(line)
        # coefficient: × 0.67 / ×1.0
        cm = re.search(r'×\s*([\d.]+)', line)
        if cm:
            r['coefficient'] = _to_float(cm.group(1))

    # dcf_fcf_sbc + dcf_fcf: D.2b 表格行
    # DCF FCF−SBC 行（− 或 - 变体）
    for row in re.finditer(r'^\|\s*DCF\s*FCF\s*[-−]\s*SBC\b.*$', text, re.MULTILINE):
        cells = [c.strip() for c in row.group(0).split('|')[1:-1]]
        if len(cells) >= 4:
            r['dcf_fcf_sbc'] = _parse_dcf_cell(cells[3])
            r['base_sbc'] = _parse_dcf_cell(cells[1])
            if r['p_fcf0'] is None:
                pm = re.search(r'([\d.]+)x', cells[2])
                if pm:
                    r['p_fcf0'] = _to_float(pm.group(1))
            break
    # DCF FCF 行（纯 FCF，不含 SBC；用 negative lookahead 排除 SBC 行）
    for row in re.finditer(r'^\|\s*DCF\s*FCF(?!\s*[-−]\s*SBC)\b.*$', text, re.MULTILINE):
        cells = [c.strip() for c in row.group(0).split('|')[1:-1]]
        if len(cells) >= 4:
            r['dcf_fcf'] = _parse_dcf_cell(cells[3])
            r['base_fcf'] = _parse_dcf_cell(cells[1])
            if r['p_fcf0'] is None:
                pm = re.search(r'([\d.]+)x', cells[2])
                if pm:
                    r['p_fcf0'] = _to_float(pm.group(1))
            break

    # g: "g = N%" (from Task C)
    m = re.search(r'\bg\s*=\s*>*(\d+\.?\d*)%', text)
    if m:
        r['g'] = _to_float(m.group(1))

    # r: DCF 折现率 "r = X% (质量)"
    m = re.search(r'\br\s*=\s*(\d+\.?\d*)%', text)
    if m:
        r['r_rate'] = _to_float(m.group(1))

    # gaap_eps: D.1 表 GAAP 行首个 $ 值（多币种取 USD）
    m = re.search(r'^\|\s*GAAP\b.*?([−−-]?\$[\d,]+\.?\d*)', text, re.MULTILINE)
    if m:
        r['gaap_eps'] = _to_float(m.group(1).replace('$', ''))

    # quality_trouble: 分别抓 质量 + 麻烦, 组合
    qm = re.search(r'质量判定[：:]\s*(伟大|好公司|平庸)', text)
    tm = re.search(r'×\s*麻烦\s*(无麻烦|明确一次性|一般|存疑|重)', text)
    if qm and tm:
        r['quality_trouble'] = qm.group(1) + '×' + tm.group(1)
    elif qm:
        r['quality_trouble'] = qm.group(1)

    r['is_midcycle'] = bool(re.search(r'中周期\s*PE|mid-?cycle|不套\s*min\(8\.5\+g|周期股口径', text))

    return r


LOW_THRESHOLD = 1.5   # DCF/EPS > 1.5 → 低估加强
HIGH_THRESHOLD = 0.7  # DCF/EPS < 0.7 → 高估警告


def dcf_signal(dcf_fcf_sbc, fair_price):
    """DCF FCF−SBC / EPS合理价 比值 → 信号标签"""
    if dcf_fcf_sbc is None and fair_price is None:
        return '—（未计）'
    if dcf_fcf_sbc is None or fair_price is None or fair_price == 0:
        return 'DCF N/A'
    ratio = dcf_fcf_sbc / fair_price
    if ratio > LOW_THRESHOLD:
        return '低估加强'
    if ratio < HIGH_THRESHOLD:
        return '高估警告'
    return '结论稳健'


def dcf_fcf_safety_margin(price, dcf_fcf):
    """1 − 现价/DCF FCF（百分比）。缺失返回 None"""
    if price is None or dcf_fcf is None or dcf_fcf == 0:
        return None
    return round((1 - price / dcf_fcf) * 100, 1)


def is_hidden_opportunity(price, fair_price, dcf_fcf_sbc):
    """现价 > EPS合理价 但 < DCF FCF−SBC → EPS 看贵 DCF 看便宜"""
    if None in (price, fair_price, dcf_fcf_sbc):
        return False
    return price > fair_price and price < dcf_fcf_sbc


import glob


def reconcile_operation(parsed_op, price, fair, full):
    """安全边际派生基础操作（task_a.md A.3 操作表）。
    ≤满仓→满仓建仓 / 满仓<现价<合理价→小仓/观察 / ≥合理价→买贵了。
    Task A 特殊归类（不对称投机/价值陷阱/严重买贵/最佳买点/不出手）保留不覆盖。"""
    SPECIAL = ['不对称', '投机', '价值陷阱', '严重买贵', '最佳', '接近最佳', '不出手']
    if parsed_op and any(k in parsed_op for k in SPECIAL):
        return parsed_op
    if None in (price, fair):
        return parsed_op
    if full is not None and price <= full:
        return '满仓建仓'
    if price < fair:
        return '小仓/观察'
    return '买贵了'


def load_52w(stock):
    """从 financial_data/{stock}/info.json 读 52W 高/低（股价币种，price 端可信）"""
    try:
        p = os.path.join('financial_data', stock, 'info.json')
        with open(p, encoding='utf-8') as f:
            info = json.load(f)
        return info.get('fiftyTwoWeekHigh'), info.get('fiftyTwoWeekLow')
    except Exception:
        return None, None


def load_all(ai_report_dir):
    """遍历 ai_report/*/ 加载 a+d 合并 + 派生。返回 list[dict]。"""
    records = []
    for d in sorted(glob.glob(os.path.join(ai_report_dir, '*/'))):
        a_path = os.path.join(d, 'output_a.md')
        d_path = os.path.join(d, 'output_d.md')
        a = parse_output_a(a_path)
        dd = parse_output_d(d_path)
        rec = {**a, **dd}
        stock = os.path.basename(os.path.normpath(d))
        rec['52w_high'], rec['52w_low'] = load_52w(stock)
        rec['dcf_signal'] = dcf_signal(dd.get('dcf_fcf_sbc'), dd.get('fair_price'))
        rec['dcf_fcf_safety_margin'] = dcf_fcf_safety_margin(a.get('price'), dd.get('dcf_fcf'))
        rec['hidden'] = is_hidden_opportunity(a.get('price'), dd.get('fair_price'), dd.get('dcf_fcf_sbc'))
        rec['operation'] = reconcile_operation(a.get('operation'), a.get('price'), dd.get('fair_price'), dd.get('full_position'))
        records.append(rec)
    return records


def _margin_key(r, key='eps_safety_margin'):
    v = r.get(key)
    return v if v is not None else -99999


def eps_margin(r):
    """EPS 安全边际（仅当有 EPS 合理价 fair_price 时有效；亏损股 fair_price=None 用 DCF 口径，不算 EPS 安全边际）"""
    if r.get('fair_price') is None:
        return None
    return r.get('eps_safety_margin')


def _eps_margin_num(r):
    m = eps_margin(r)
    return m if m is not None else -99999


def sort_main_table(records):
    """按 EPS 安全边际降序（最便宜在前）；无 EPS 合理价的标的（亏损股 DCF 口径）排末尾"""
    return sorted(records, key=lambda r: _eps_margin_num(r), reverse=True)


def top10_eps(records):
    valid = [r for r in records if eps_margin(r) is not None]
    return sorted(valid, key=lambda r: _eps_margin_num(r), reverse=True)[:10]


def top10_dcf_fcf(records):
    valid = [r for r in records if r.get('dcf_fcf_safety_margin') is not None]
    return sorted(valid, key=lambda r: r['dcf_fcf_safety_margin'], reverse=True)[:10]


def top10_drawdown(records):
    valid = [r for r in records if r.get('signal_count') is not None]
    return sorted(valid, key=lambda r: (r['signal_count'], r.get('drawdown_1y') or 0), reverse=True)[:10]


def filter_hidden(records):
    return [r for r in records if r.get('hidden')]


def verify(records):
    """跑 5 项 a+d 校验。返回 list[Violation dict]。Flag 不阻断。"""
    violations = []
    for r in records:
        violations += _check1_sign(r)
        violations += _check2_full_position(r)
        violations += _check3_pe_formula(r)
        violations += _check5_great_no_trouble(r)
    return violations


def _check1_sign(r):
    """Check 1: 安全边际符号 = 1 − 现价/合理价（HIGH）"""
    price = r.get('price')
    fair = r.get('fair_price')
    parsed = r.get('eps_safety_margin')
    if None in (price, fair, parsed) or fair == 0:
        return []
    expected = round((1 - price / fair) * 100, 1)
    exp_sign = '+' if expected >= 0 else '−'
    par_sign = '+' if parsed >= 0 else '−'
    if exp_sign != par_sign or abs(expected - parsed) > 1.0:
        return [{'stock': r['stock'], 'check_id': 1,
                 'check_name': '安全边际符号',
                 'severity': 'HIGH',
                 'expected': f'{exp_sign}{abs(expected)}%',
                 'actual': f'{par_sign}{abs(parsed)}%',
                 'message': f"1−{price}/{fair}={expected}% 但标 {parsed}%"}]
    return []


def _check2_full_position(r):
    """Check 2: 满仓 = 合理价 × 系数（MEDIUM）"""
    full = r.get('full_position')
    fair = r.get('fair_price')
    coef = r.get('coefficient')
    if None in (full, fair, coef) or full == 0:
        return []
    expected = round(fair * coef, 2)
    if abs(expected - full) / full > 0.01:
        return [{'stock': r['stock'], 'check_id': 2,
                 'check_name': '满仓=合理价×系数',
                 'severity': 'MEDIUM',
                 'expected': f'${expected}',
                 'actual': f'${full}',
                 'message': f"{fair}×{coef}={expected} 但标 {full}"}]
    return []


def _check3_pe_formula(r):
    """Check 3: 合理 PE = min(8.5+g, 30)（HIGH，含 Check 4 g≥22 封顶）"""
    pe = r.get('pe')
    g = r.get('g')
    if None in (pe, g):
        return []
    if r.get('is_midcycle'):
        return []
    expected_pe = min(8.5 + g, 30)
    if abs(pe - expected_pe) > 0.1:
        cap_note = ' [g≥22 应封顶 30x]' if g >= 22 else ''
        return [{'stock': r['stock'], 'check_id': 3,
                 'check_name': f'合理 PE=min(8.5+g,30){cap_note}',
                 'severity': 'HIGH',
                 'expected': f'{expected_pe}x',
                 'actual': f'{pe}x',
                 'message': f"g={g}%→期望 {expected_pe}x 实际 {pe}x"}]
    return []


def _check5_great_no_trouble(r):
    """Check 5: 伟大+无trouble → ×1.0（HIGH，mistakes.md #3）"""
    qt = r.get('quality_trouble') or ''
    if '伟大' not in qt or '无麻烦' not in qt:
        return []
    coef = r.get('coefficient')
    if coef is None:
        return []
    if abs(coef - 1.0) > 0.001:
        return [{'stock': r['stock'], 'check_id': 5,
                 'check_name': '伟大+无trouble→×1.0',
                 'severity': 'HIGH',
                 'expected': '×1.0',
                 'actual': f'×{coef}',
                 'message': f"伟大×无麻烦应 ×1.0，实际 ×{coef}（mistakes.md #3）"}]
    return []


def write_violations(violations, date_str, ai_report_dir):
    """产 verify.{date}.md 日志内容，返回字符串。"""
    n = len(violations)
    stocks = sorted({v['stock'] for v in violations})
    n_high = sum(1 for v in violations if v['severity'] == 'HIGH')
    n_med = sum(1 for v in violations if v['severity'] == 'MEDIUM')

    L = []
    L.append(f'# 数据校验日志 — {date_str}')
    L.append('')
    L.append('> Phase 1（a+d 检查 1-5）。Flag 不阻断。')
    L.append('')
    L.append('## 摘要')
    L.append('')
    L.append(f'- 总计 {n} 项违规，{len(stocks)} 个标的有问题（HIGH: {n_high} / MEDIUM: {n_med}）')
    if not violations:
        L.append('- 数据自洽 ✓')
    L.append('')

    if violations:
        sev_order = {'HIGH': 0, 'MEDIUM': 1}
        ordered = sorted(violations, key=lambda v: (sev_order.get(v['severity'], 9), v['stock']))
        L.append('## 违规明细（按严重度→标的）')
        L.append('')
        cur_stock = None
        for v in ordered:
            if v['stock'] != cur_stock:
                L.append(f'### ⚠ {v["stock"]}')
                cur_stock = v['stock']
            L.append(f'- [Check {v["check_id"]} {v["severity"]}] {v["check_name"]}: 期望 {v["expected"]} 实际 {v["actual"]}')
            L.append(f'  - {v["message"]}')
        L.append('')

    return '\n'.join(L)


def _save(path, content):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)


def fmt_pct(v):
    if v is None:
        return 'N/A'
    sign = '+' if v >= 0 else '−'
    return f'{sign}{abs(v)}%'


def fmt_price(v, cur='$'):
    if v is None:
        return 'N/A'
    if isinstance(v, str):
        return v
    return f'{cur}{v:g}'


def fmt_unit(v, unit):
    """Ng / N% 格式，缺失返回 N/A"""
    if v is None:
        return 'N/A'
    return f'{v:g}{unit}'


def fmt_full(v, coef):
    """满仓目标 + 系数，如 $28.37 ×0.75"""
    if v is None:
        return 'N/A'
    s = fmt_price(v)
    if coef is not None:
        s += f' ×{coef:g}'
    return s


def fmt_coef(v):
    """折扣系数，如 ×0.75"""
    if v is None:
        return 'N/A'
    return f'×{v:g}'


def _op_tier(op):
    """操作 → 档位排序键（数字越小越前）"""
    if not op:
        return 9
    if '最佳' in op or '满仓' in op:
        return 0
    if '小仓' in op or '观察' in op or '公允' in op:
        return 1
    if '不对称' in op or '投机' in op:
        return 2
    return 3


def gen_report(records, date_str, violations=None):
    """装配完整 7+1 章节报告（含 ⑧ 数据质量）"""
    if violations is None:
        violations = []
    viol_stocks = {v['stock'] for v in violations}
    main = sort_main_table(records)
    t_eps = top10_eps(records)
    t_dcf = top10_dcf_fcf(records)
    t_dd = top10_drawdown(records)
    hidden = filter_hidden(records)

    n_满 = sum(1 for r in records if _op_tier(r.get('operation')) == 0)
    n_小 = sum(1 for r in records if _op_tier(r.get('operation')) == 1)
    n_投机 = sum(1 for r in records if _op_tier(r.get('operation')) == 2)
    n_贵 = sum(1 for r in records if _op_tier(r.get('operation')) == 3)
    n_便宜 = sum(1 for r in records if _eps_margin_num(r) > 0)
    stale = [r for r in records if r.get('date') and r['date'] < date_str]

    L = []
    L.append(f'# 跨标的汇总 — {date_str}（含 DCF 三口径）')
    L.append('')
    L.append('> 决策聚焦的多视角机会筛选器。join Task A(现价/安全边际) + Task D(估值锚/DCF)。')
    L.append('> 三口径：EPS 模型(下限) ≤ DCF FCF−SBC(中性) ≤ DCF FCF(上限)。安全边际 = 1 − 现价/合理价。')
    L.append('')
    L.append('## ① 决策摘要')
    L.append('')
    L.append(f'- 满仓建仓 {n_满} / 小仓 {n_小} / 不对称投机 {n_投机} / 买贵了 {n_贵}')
    L.append(f'- 现价 ≤ EPS合理价（便宜）: {n_便宜}/{len(records)}')
    L.append(f'- 隐藏机会（EPS 看贵 DCF 看便宜）: {len(hidden)} 个')
    L.append(f'- 现金建议: {"保留 60%+" if n_便宜 < 5 else "可加仓至 40%"} 等回调')
    if stale:
        names = ", ".join(r['stock'] for r in stale[:5])
        more = '...' if len(stale) > 5 else ''
        L.append(f'- ⚠ {len(stale)} 个标的 output_a 日期早于 {date_str}，Task A 待刷新: {names}{more}')
    L.append('')

    # ② 买点详情
    L.append('## ② 买点标的详情（满仓/小仓/不对称）')
    L.append('')
    buyable = [r for r in records if _op_tier(r.get('operation')) <= 2]
    buyable.sort(key=lambda r: (_op_tier(r.get('operation')), -_eps_margin_num(r)))
    for r in buyable:
        L.append(f'### {r["stock"]} — {r.get("operation","")}')
        line = f'- 现价 {fmt_price(r.get("price"))} vs [满仓 {fmt_price(r.get("full_position"))}, EPS合理价 {fmt_price(r.get("fair_price"))}, DCF FCF−SBC {fmt_price(r.get("dcf_fcf_sbc"))}, DCF FCF {fmt_price(r.get("dcf_fcf"))}]'
        L.append(line)
        L.append(f'- DCF 信号: {r.get("dcf_signal","")} | EPS安全边际 {fmt_pct(r.get("eps_safety_margin"))} | {r.get("quality_trouble") or "—"}')
        L.append('')
    L.append('')

    # ③ Top 10
    L.append('## ③ Top 10 三视角')
    L.append('')
    L.append('### a. EPS 便宜 Top 10（按 EPS 安全边际降序）')
    h = ['标的', '现价', 'EPS合理价', 'EPS安全边际', '操作']
    rows = [(r['stock'], fmt_price(r.get('price')), fmt_price(r.get('fair_price')),
             fmt_pct(eps_margin(r)), r.get('operation', '')) for r in t_eps]
    L.append(table(rows, h))
    L.append('')
    L.append('### b. DCF FCF 便宜 Top 10（按 DCF FCF 安全边际降序）')
    h = ['标的', '现价', 'DCF FCF', 'DCF FCF安全边际', 'vs EPS安全边际']
    rows = [(r['stock'], fmt_price(r.get('price')), fmt_price(r.get('dcf_fcf')),
             fmt_pct(r.get('dcf_fcf_safety_margin')), fmt_pct(eps_margin(r))) for r in t_dcf]
    L.append(table(rows, h))
    L.append('')
    L.append('### c. 回撤信号全表（全部标的，按 # 命中数降序，7 项粗筛逐项明细）')
    L.append('')
    L.append('信号: 1Y=1Y回撤>40% / 2Y=2Y回撤>60% / 52W低=距52周低≤15% / P/E<15x / EV/E<10x / P/B<1.5x / P/S<2.0x')
    L.append('')
    h = ['标的', '1Y', '2Y', '52W低', 'P/E', 'EV/E', 'P/B', 'P/S', '#', '安全边际', '判读', '现价', '52W高', '52W低']
    rows = []
    dd = sorted(records, key=lambda r: (r.get('signal_count') or -1, r.get('drawdown_1y') or 0), reverse=True)
    for r in dd:
        sigs = r.get('signals') or {}
        svals = r.get('signal_values') or {}
        cells = []
        for i in range(1, 8):
            st = sigs.get(i, '—')
            v = svals.get(i, '')
            cells.append(f'{st} {v}' if v else st)
        eps_m = eps_margin(r)
        if eps_m is not None and eps_m > 0:
            verdict = '错杀'
        elif eps_m is None:
            verdict = '待证'
        else:
            verdict = '真跌'
        sc = r.get('signal_count')
        rows.append((r['stock'], *cells, f'{sc}/7' if sc is not None else '?/7',
                     fmt_pct(eps_m), verdict, fmt_price(r.get('price')),
                     fmt_price(r.get('52w_high')), fmt_price(r.get('52w_low'))))
    L.append(table(rows, h))
    L.append('')

    # ④ 隐藏机会
    L.append('## ④ EPS 看贵 DCF 看便宜的隐藏机会')
    L.append('')
    L.append('> 现价 > EPS合理价 但 < DCF FCF−SBC → 高 SBC+回购>SBC 类，EPS 模型低估，DCF FCF 更准')
    L.append('')
    if hidden:
        h = ['标的', '现价', 'EPS合理价', 'DCF FCF−SBC', 'EPS安全边际', 'DCF−SBC安全边际']
        hidden_sorted = sorted(hidden, key=lambda r: dcf_fcf_safety_margin(r.get('price'), r.get('dcf_fcf_sbc')) or -99999, reverse=True)
        rows = [(r['stock'], fmt_price(r.get('price')), fmt_price(r.get('fair_price')),
                 fmt_price(r.get('dcf_fcf_sbc')), fmt_pct(eps_margin(r)),
                 fmt_pct(dcf_fcf_safety_margin(r.get('price'), r.get('dcf_fcf_sbc')))) for r in hidden_sorted]
        L.append(table(rows, h))
    else:
        L.append('（无）')
    L.append('')

    # ⑤ 全量主表（一行全分析数据，按 EPS 安全边际降序）
    L.append('## ⑤ 全量主表（按 EPS 安全边际降序，一行含全部分析数据）')
    L.append('')
    L.append('> EPS 模型: 合理价=正常EPS×min(8.5+g,30) / 满仓=合理价×系数 / 安全边际=1−现价/合理价')
    L.append('> DCF 交叉验: base×P/FCF₀+net_cash/sh，r=伟大9%/好公司10%/平庸11%，P/FCF₀=min((1+g)/(r−g),30)')
    L.append('')
    h = ['标的', '现价', '合理价', '安全边际', '满仓', '系数', 'g', '合理PE', '正常EPS', 'GAAP EPS', 'FCF/sh', 'FCF-SBC/sh', 'r', 'P/FCF₀', 'DCF FCF-SBC', 'DCF FCF', '质量×麻烦', '操作']
    rows = []
    for r in main:
        prefix = '⚠ ' if r['stock'] in viol_stocks else ''
        rows.append((
            prefix + r['stock'],
            fmt_price(r.get('price')),
            fmt_price(r.get('fair_price')),
            fmt_pct(eps_margin(r)),
            fmt_price(r.get('full_position')),
            fmt_coef(r.get('coefficient')),
            fmt_unit(r.get('g'), '%'),
            fmt_unit(r.get('pe'), 'x'),
            fmt_price(r.get('eps')),
            fmt_price(r.get('gaap_eps')),
            fmt_price(r.get('base_fcf')),
            fmt_price(r.get('base_sbc')),
            fmt_unit(r.get('r_rate'), '%'),
            fmt_unit(r.get('p_fcf0'), 'x'),
            fmt_price(r.get('dcf_fcf_sbc')),
            fmt_price(r.get('dcf_fcf')),
            r.get('quality_trouble', '') or 'N/A',
            r.get('operation', '') or 'N/A',
        ))
    L.append(table(rows, h))
    L.append('')

    # ⑥ 特殊档
    L.append('## ⑥ 特殊档（公式不适用者）')
    L.append('')
    qt = lambda r: r.get('quality_trouble') or ''
    banks = [r for r in records if r.get('dcf_signal') == 'DCF N/A' and '银行' in qt(r)]
    fcf_neg = [r for r in records if r.get('dcf_signal') == 'DCF N/A' and r not in banks]
    great_nt = [r for r in records if r.get('full_position') is None and '伟大' in qt(r) and '无麻烦' in qt(r)]
    L.append(f'**银行**（P/B，DCF N/A）: {", ".join(r["stock"] for r in banks) or "无"}')
    L.append(f'**FCF<0/亏损**（DCF N/A）: {", ".join(r["stock"] for r in fcf_neg) or "无"}')
    L.append(f'**伟大+无trouble**（满仓=合理价）: {", ".join(r["stock"] for r in great_nt) or "无"}')
    L.append('')

    # ⑦ DCF 信号分组
    L.append('## ⑦ DCF 信号分组')
    L.append('')
    for sig in ['低估加强', '结论稳健', '高估警告', 'DCF N/A', '—（未计）']:
        grp = [r['stock'] for r in records if r.get('dcf_signal') == sig]
        L.append(f'- **{sig}**（{len(grp)}）: {", ".join(grp) or "无"}')
    L.append('')

    # ⑧ 数据质量
    L.append('## ⑧ 数据质量（verify）')
    L.append('')
    L.append(f'> Flag 不阻断。违规标的仍在主表（标 ⚠），详见 verify.{date_str}.md。')
    L.append('')
    if not violations:
        L.append('（无违规，数据自洽 ✓）')
    else:
        n_high = sum(1 for v in violations if v['severity'] == 'HIGH')
        n_med = sum(1 for v in violations if v['severity'] == 'MEDIUM')
        L.append(f'- 总计 {len(violations)} 项违规，{len(viol_stocks)} 个标的（HIGH: {n_high} / MEDIUM: {n_med}）')
        L.append('')
        h = ['标的', '检查', '严重度', '期望', '实际', '说明']
        sev_order = {'HIGH': 0, 'MEDIUM': 1}
        ordered = sorted(violations, key=lambda v: (sev_order.get(v['severity'], 9), v['stock']))
        rows = [(v['stock'], v['check_name'], v['severity'], v['expected'], v['actual'], v['message']) for v in ordered]
        L.append(table(rows, h))
    L.append('')
    L.append(f'> 基于 {date_str} output_a/output_d 静态快照。价格漂移 >3-5% 需先刷 Task A。')

    return '\n'.join(L)


import argparse
from datetime import date


def main():
    ap = argparse.ArgumentParser(description='价值投资汇总报告生成器')
    ap.add_argument('--date', default=None, help='日期 YYYY-MM-DD（默认当日）')
    ap.add_argument('--out', default=None, help='comparison 输出路径')
    ap.add_argument('--verify-out', default=None, help='verify 日志输出路径')
    ap.add_argument('--ai-report', default='ai_report', help='ai_report 目录')
    args = ap.parse_args()

    date_str = args.date or date.today().isoformat()
    out_path = args.out or os.path.join(args.ai_report, f'comparison.{date_str}.md')
    ver_path = args.verify_out or os.path.join(args.ai_report, f'verify.{date_str}.md')

    records = load_all(args.ai_report)
    violations = verify(records)
    report = gen_report(records, date_str, violations)
    vlog = write_violations(violations, date_str, args.ai_report)

    _save(out_path, report)
    _save(ver_path, vlog)
    n_viol = len(violations)
    n_viol_stocks = len({v['stock'] for v in violations})
    print(f'written {len(report)} bytes → {out_path}')
    print(f'written {len(vlog)} bytes → {ver_path}')
    print(f'  {len(records)} stocks | 满仓 {sum(1 for r in records if _op_tier(r.get("operation"))==0)} | '
          f'隐藏机会 {len(filter_hidden(records))} | 违规 {n_viol}（{n_viol_stocks} 标的）')


if __name__ == '__main__':
    main()
