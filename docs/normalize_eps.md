# 正常化 EPS Checklist v3.1

> 被引用自 `docs/task_b.md`。正常化 EPS 的计算方法独立封装于此。

## 原理

GAAP NI 是确定锚。反过来想——**找所有 abnormal 的一次性收入/费用，从 GAAP NI 里减掉**。工具的 `Total Unusual Items` 是交叉验，不是主角。

**核心原则：正常化 EPS = min(GAAP EPS, 工具 EPS, v3.1 EPS)**

三个口径各有盲区，取最低 = 最保守。哪怕错过机会，不要做错。

| 口径 | 来源 | 能抓什么 | 盲区 |
|------|------|---------|------|
| GAAP EPS | `Diluted EPS` | 无（原始）| 不剔任何一次性 |
| 工具 EPS | `Normalized Income / Shares` | 正式归类 Unusual | 漏剔走 Other Income 的 MTM |
| v3.1 EPS | detector 计算 | Other Income MTM + 更多 | 可能过度剔/误剔 |

- 一次性**收益** → 工具或 v3.1 剔掉 → 取最低 → 防止买到"假便宜"（NI 注水）
- 一次性**损失** → 工具或 v3.1 可能加回 → 但 min(GAAP) 兜底 → 不加回 → 保守

```
正常化 EPS = min(GAAP EPS, 工具 EPS, v3.1 EPS)
```

## 数据源

| 文件 | 用途 |
|------|------|
| `income_ttm.csv` | TTM 值（主计算） |
| `income_quarterly.csv` | 季度波动测试 + OpInc 趋势 |
| `income_annual.csv` | 3 年历史均值（ratio 基准） |

CSV 列结构：列0=字段名，列1=最新期（新→旧）。

## 关键字段

| key | 含义 | 可用性 |
|-----|------|--------|
| `Net Income` | GAAP NI（起点） | 全部 |
| `Diluted EPS` | GAAP EPS | 全部 |
| `Diluted Average Shares` | 稀释股数（常量） | 全部 |
| `Pretax Income` | 税前利润 | 全部 |
| `Tax Provision` | 所得税 | 全部 |
| `Operating Income` | 营业利润 | 71（缺银行） |
| `Total Revenue` | 营收 | 全部 |
| `Gross Profit` | 毛利 | 71 |
| `Research And Development` | R&D | 56 |
| `Selling General And Administration` | SGA | 74 |
| `Tax Rate For Calcs` | 工具税率 | 全部 |
| `Other Income Expense` | 非利息 Other（已不含利息） | 66 |
| `Net Non Operating Interest Income Expense` | 利息净收入 | 66 |
| `Total Unusual Items` | 工具归类一次性项（税前） | 61 |
| `Tax Effect Of Unusual Items` | Unusual 税效应 | 全部 |
| `Normalized Income` | 工具预算 NI（交叉验） | 全部 |
| `Restructuring And Mergern Acquisition` | 重组 | 19 |
| `Net Income From Continuing Operation Net Minority Interest` | 持续经营 NI | 全部 |

**数据结构**（已验证 76 只中 64 只成立）：
```
Pretax = Operating Income + Other Income Expense + Net Interest Income
```
→ `Other Income Expense` 已不含利息，直接用。

## EPS-1: GAAP 基准

```
文件: income_ttm.csv
GAAP NI    = ['Net Income'][0]
GAAP EPS   = ['Diluted EPS'][0]
稀释股数    = ['Diluted Average Shares'][0]
Pretax     = ['Pretax Income'][0]
Tax        = ['Tax Provision'][0]
有效税率    = Tax / Pretax  或 ['Tax Rate For Calcs'][0]
Revenue    = ['Total Revenue'][0]
GrossProfit = ['Gross Profit'][0]
R&D        = ['Research And Development'][0]        ← 可能缺失
SGA        = ['Selling General And Administration'][0]
```

## EPS-2: 扫描一次性费用（插件架构）

每个 detector 独立运行，互不影响。加新 detector 只需写一个函数。

### 2a: Other Income → 投资 MTM（高信心）

```
文件: income_ttm.csv + income_quarterly.csv
key:  Other Income Expense, Net Non Operating Interest Income Expense

非利息Other = ['Other Income Expense'][0]  ← 直接用（已不含利息）
  若缺失 → gap = Pretax - OpInc - NetInt
  NetInt 来源: ['Net Non Operating Interest Income Expense'] > ['Net Interest Income'] > IntInc-IntExp

若 < 1% of NI → 跳过（Type A 干净）

季度波动测试 (近 5 季):
  波动率 = range / avg_abs
  ├ > 2x 或 正负摆动 → 投资 MTM → 标记一次性，amount = 非利息Other（pre-tax）
  └ 稳定 → 经常性 → 保留
```

> ⚠ **半年报复查**：半年报公司（中概/港股如 0700.HK/BABA/PDD/JD）季度 CSV 多数为零 → vol_ratio 虚高 > 2 → **假阳性**。分析时若季度 CSV {N}/{M} 期为零，标"假阳性"，不计为真波动。详见已知问题 #6。

### 2b: Restructuring → 重组费用（只标记不自动剔）

```
若 ['Restructuring And Mergern Acquisition'][0] ≠ $0 → 标记
amount = 该值（pre-tax，仅供分析参考，不进 total_strip）
```

> ⚠ 重组是**费用**不是收益。CSV 存正数（=费用金额），旧版误当收益剥离 = `Pretax − 重组` 双重扣减（GAAP 已扣一次）。Per "**只剔收益不加回亏损**"：费用不剥离，留在 GAAP NI。另：重组常连续多年 = 经常性，非一次性。若确认真一次性，Task D 手动加回。

### 2c: Tax → 税率异常（中信心）

```
TTM 税率 vs income_annual 近 3-4 年均值
若 |TTM - 均值| > 10pp → 标记一次性税收
  one_time_tax = TTM Tax - 均值税率 × TTM Pretax
  amount = one_time_tax（after-tax）
若触发 → 正常税率用历史均值，否则用 TTM 税率
```

### 2d: OpInc → 季度趋势（低信心，只标记不自动剔）

```
近 5 季 Operating Income + OpM%
若 OpInc 暴跌 >30% QoQ 或转负 → 标记可疑
交叉定位:
  GM% 暴跌 → COGS 侧（2e 定位）
  R&D% 暴涨 → IPR&D？（2f 定位）
  SGA% 暴涨 → 诉讼/减值？（2g 定位）
  以上都没触发 → 需外部确认
amount = 需外部确认（CSV 无法自动量化）
```

### 2e: Gross Margin → COGS 一次性（中信心，NEW）

```
TTM GM% = GrossProfit / Revenue
3yr 均值 GM% = mean(income_annual['Gross Profit'][i] / ['Total Revenue'][i], i=0..2)
若 3yr均值 - TTM > 5pp → GM 暴跌 → 可能存货减值/COGS 一次性
amount = (3yr均值GM% - TTM GM%) × TTM Revenue（pre-tax）
```

### 2f: R&D / Revenue → IPR&D 冲减（中信心，NEW）

```
TTM R&D% = R&D / Revenue（若 R&D 字段缺失 → 跳过）
3yr 均值 R&D% = mean(income_annual['R&D'][i] / ['Revenue'][i], i=0..2)
若 TTM - 3yr均值 > 3pp → R&D 暴涨 → 可能 IPR&D
amount = (TTM R&D% - 3yr均值R&D%) × TTM Revenue（pre-tax）
交叉验: 若同时触发 2d(OpIncDrop) → 信心提高
```

### 2g: SGA / Revenue → 诉讼/减值（低信心，只标记，NEW）

```
TTM SGA% = SGA / Revenue
3yr 均值 SGA% = mean(income_annual['SGA'][i] / ['Revenue'][i], i=0..2)
若 TTM - 3yr均值 > 3pp → SGA 暴涨 → 可能一次性
amount = (TTM SGA% - 3yr均值SGA%) × TTM Revenue（pre-tax）
低信心：SGA 增长原因多，可能是业务扩张
```

### 2h: Discontinued Operations（高信心，NEW）

```
NI_total = ['Net Income'][0]
NI_continuing = ['Net Income From Continuing Operation Net Minority Interest'][0]
若 NI_total ≠ NI_continuing → 有终止经营
amount = NI_total - NI_continuing（after-tax）
```

## EPS-3: 交叉验 Total Unusual Items

```
工具的 Unusual vs 我们检测到的一次性项:

1. 工具抓了我没抓的？→ 补上
2. 我抓了工具没抓的？→ 预期行为（工具漏剔非 Unusual MTM）
3. 两者重叠？
   若 |某项 - Unusual| / max < 20% → 同一项目，取大值，不重复剔
   若差异大 → 独立项目，都剔
```

## EPS-4: 计算

```
GAAP EPS   = ['Diluted EPS'][0]
工具 EPS   = ['Normalized Income'][0] / ['Diluted Average Shares'][0]
v3.1 EPS   = (Pretax - sum(max(0, 各 detector 剔除额))) × (1-税率) / 稀释股数

正常化 EPS = min(GAAP EPS, 工具 EPS, v3.1 EPS)
```

保证: 正常化 EPS ≤ GAAP EPS（永远不高于 GAAP）

三个口径的关系:
- GAAP ≥ 工具（工具只剔 Unusual，可能剔 gain 也可能加回 loss）
- GAAP ≥ v3.1（v3.1 只剔 gain 不加回 loss，保证 ≤ GAAP）
- 工具 vs v3.1: 工具抓正式 Unusual，v3.1 抓非 Unusual MTM，各有盲区
- 取 min = 三者中最保守的 = 防止任何单一口径过于乐观

v3.1 内部计算:
```
只剔 high + medium 信心的 detector 结果

对于每个 detector 的 amount:
  amount > 0（收益）→ 剔掉（降低 NI）
  amount < 0（损失）→ 不加回（保持 GAAP，更保守）

total_strip_pretax = sum(max(0, amount) for pre-tax detectors)
total_strip_after_tax = sum(max(0, amount) for after-tax detectors)

v3.1 税前 = Pretax - total_strip_pretax
v3.1 NI = v3.1 税前 × (1 - 正常税率) - total_strip_after_tax
v3.1 EPS = v3.1 NI / 稀释股数
```

## 信心等级

| Detector | 信心 | 自动剔？ | 理由 |
|----------|------|---------|------|
| 2a OtherInc (MTM) | 高 | ✅ | 波动 = MTM 几乎确定 |
| 2b Restructuring | 中 | ❌ 只标记 | 费用非收益，per"不加回亏损"不剥离；常连续多年=经常性 |
| 2h Discontinued | 高 | ✅ | 明确归类 |
| 2c TaxAnomaly | 中 | ✅ | 可能是税率结构变化 |
| 2e GMDrop | 中 | ✅ | 可能结构性 GM 下滑 |
| 2f RDSpike | 中 | ✅ | 可能结构性研发增加 |
| 2d OpIncDrop | 低 | ❌ 只标记 | 需外部确认原因和金额 |
| 2g SGASpike | 低 | ❌ 只标记 | SGA 增长原因多 |

## 扩展性

加新 detector 只需写一个函数 + 加到 detectors 列表。例如：

```python
def detect_2i_fx_anomaly(ttm_gv, q_gv, q_periods):
    """2i: FX 收益/损失（若大且波动 → 标记一次性）"""
    ...
```

现有 detector 不受影响——每个独立扫描、独立返回，最后汇总。

## 实装

代码: `docs/normalize_eps.py`

```bash
python3 -c "import sys; sys.path.insert(0,'docs'); from normalize_eps import normalize_eps; print(normalize_eps('NVDA'))"  # 单只
```

## 已知问题

1. **银行不适用**：JPM/BAC/GS/MS/**NU** 结构不同（Operating Income=$0，Net Interest Income 是核心经营收入），用 P/B 不用 EPS
2. **OtherInc 过度剔——投资控股型公司**：detector 2a 把 Pretax − OpInc − NetInt 的全部"非利息其他收入"当投资 MTM 剥离，但其中含**经常性**投资分红/利息。典型：TSM $74B 含权益法收入、0700.HK ¥25B 含上市公司分红（Meituan/PDD 等）。→ v3.1 EPS 过度保守。**补偿**：被剥离的经常性收入对应 BS 股权投资组合 → Task D SOTP 加回；或改用工具 EPS（含投资收入）交叉验，两路殊途同归则结论稳健
3. **TaxAnomaly 过度触发**：中国公司（BEKE/BIDU）税率结构不同 → 考虑提高阈值或排除
4. **OpIncDrop 无法量化**：需外部 10-K 确认 IPR&D/减值金额
5. **min() 原则**：正常化 EPS 永远 ≤ GAAP EPS → 只防"买贵"，不追"低估修复"的 alpha
6. **半年报假阳性**（NEW）：detector 2a 用季度波动率判断 OtherInc 是否波动。半年报公司（0700.HK、BABA、PDD、JD 等中概/港股）季度 CSV 多数为零 → vol_ratio = (max−0)/(avg含零) 虚高 > 2 → **误触发**。实质是"数据缺失被当成高波动"，非投资收益真波动。→ 分析时**必须半年报复查**：若季度 CSV {N}/{M} 期为零，标"假阳性"，v3.1 在此情况下过度保守
7. **OtherInc 与 Unusual 重叠但判独立**（NEW）：EPS-3 交叉验用 `|OtherInc − Unusual| / max < 10%` 判重叠。但投资控股型公司两者可能含交叉投资收益却差异率 >10% → 判独立 → 双重剥离同一笔收益 → 过度保守。→ 分析时检查 OtherInc 子项与 Unusual 是否有交叉，若有则标注"可能重叠但判独立"。**v3.1 已修：阈值 10%→20%，当两者均为正（收益）且 diff < 20% → 取 max 不重复剔**
8. **Restructuring 双重扣减**（NEW，已修）：detector 2b 旧版将重组费用（CSV 正数=费用）当收益剥离 → `Pretax − 重组` = GAAP 已扣一次 + v3.1 再扣一次 = 双重扣减。且重组常连续多年（CRM 5 年、ORCL 等）= 经常性非一次性。**已修：2b 改为只标记不自动剔（confidence=low）**，per"只剔收益不加回亏损"原则，费用留在 GAAP NI
