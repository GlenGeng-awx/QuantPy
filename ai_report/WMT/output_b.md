# WMT — Task B：财务健康 + 正常化 EPS
> 更新: 2026-08-09（财报 FY27 Q1，季度截至 2026-04-30）　货币: USD

## B.1 SCORECARD 九宫格

| 维度 | 3yr | TTM | 5Q |
|------|------|-----|-----|
| Income | 100 | 90 | 100 |
| CF | 88 | 85 | 52 |
| BS | 82 | 88 | 60 |

> 权重: Income 25% / CF 35% / BS 40%。工具: `python3 -m fundamental.health WMT`

### 背离检验

| 维度 | SCORECARD 说 | 原始财报 | 方向 |
|------|-------------|---------|------|
| Income | 3yr 100 + TTM 90 + 5Q 100（高） | GM 25% 稳、NM 3.1% 薄、Revenue/OpInc 温和增、利息覆盖 10.5x | 同向（机械高分 + 基本面稳，非困境） |
| CF | 3yr 88 + TTM 85 + 5Q 52（5Q 掉分） | OCF $40.89B 强、FCF $12.55B 正、5Q 掉分因 Q1 FY27 单季 FCF 转负 -$1.95B（CapEx 季节性爬坡） | 伤口模式：5Q 低 = CapEx 季节性，非结构性（情绪伤口轻微） |
| BS | 3yr 82 + TTM 88 + 5Q 60 | 净债 $63.45B 无托底、D/E 0.79、Working Capital -$26B（零售负营运资本浮存） | 同向（杠杆偏高但稳定，零售模型） |

伤口模式: **5Q CF 低分**（52）= Q1 FY27 单季 FCF 转负 -$1.95B，因 CapEx 季节性集中（Q1 CapEx $6.68B vs OCF $4.74B）。属**情绪伤口轻微**（季节性非结构性），TTM FCF 仍 $12.55B 正。

## B.2 利润表逐季（近 5 季，新→旧）

| 季度 | Revenue | GM% | OpInc | OpM% | NI | dilEPS |
|------|---------|-----|-------|------|-----|--------|
| Q1'27 (Apr26) | 177.75B | 25.1% | 7.49B | 4.21% | 5.33B | 0.67 |
| Q4'26 (Jan26) | 190.66B | 24.7% | 8.71B | 4.57% | 4.24B | 0.53 |
| Q3'26 (Oct25) | 179.50B | 25.0% | 6.70B | 3.73% | 6.14B | 0.77 |
| Q2'26 (Jul25) | 177.40B | 25.1% | 7.29B | 4.11% | 7.03B | 0.88 |
| Q1'26 (Apr25) | 165.61B | 25.0% | 7.13B | 4.30% | 4.49B | 0.56 |

分析:
- **GM 稳定** 24.7-25.1%（零售结构性低，无下滑风险）
- **OpM 3.7-4.6%** 波动（季节性，Q3 偏低含 reinvestment）
- **Q1'27 vs Q1'26 YoY**: Revenue +7.3%、OpInc +5.0%、EPS +19.6%（含回购）
- Other Income 波动大: Q4'26 -$2.12B, Q3'26 +$2.08B, Q2'26 +$2.71B → 投资 MTM，detector 2a 触发（见 B.5）
- 税率: TTM 24.5%（Tax Rate For Calcs 0.244979），历史均值 24-34%，当前正常区间

## B.3 现金流（TTM 2026-04）

| 项目 | TTM | 说明 |
|------|-----|------|
| OCF | $40.89B | OCF/NI = 1.80（含金量高，零售浮存+折旧） |
| FCF | $12.55B | yield = 12.55/890.11 = 1.41%（低，CapEx 重） |
| CapEx | -$28.34B | CapEx/OCF = 69%（自动化/配送重投入，吞 FCF） |
| SBC | $0 | **WMT 现金薪酬，无 SBC**（非科技公司） |
| 回购 | -$5.61B | 真缩股（8.20B→8.02B，3yr -2.2%） |
| 分红 | -$7.60B | 48 年股息贵族（payoutRatio 33.5%） |
| Net Return | $13.21B | 回购+分红-SBC = 5.61+7.60-0 = $13.21B（yield ~1.5%） |

**FCF − SBC = $12.55B − $0 = $12.55B 正** ✓

> ⚠ FCF 质量必查: WMT 的负营运资本（-$26B）来自应付账款浮存（AP $62.88B > Inventory $62.57B + AR $10.66B）。零售浮存随销量同向回流，作锚需谨慎（非永久）。但 48 年稳定经营 + 规模护城河 → 浮存可持续。CapEx $28.34B 含增长投资（自动化/电商），维护 CapEx 较低，owner earnings 介于 FCF 和 FCF+部分增长 CapEx 之间。

## B.4 资产负债表（2026-04 季度 snapshot）

| 项目 | 值 | 说明 |
|------|-----|------|
| Cash + ST Inv | $10.73B | |
| Total Debt | $74.18B | 含长期债 $36.89B + 短期债 $14.57B + 租赁 $22.72B |
| **净债** | **-$63.45B** | **净现金为负，无托底**（同 MCD，买贵无资产缓冲） |
| D/E | 0.787 | 杠杆偏高但稳定（零售模型，浮存支撑） |
| **利息覆盖** | **10.5x** | OpInc $30.18B / IntExp $2.86B → **>5x ✓** |
| Goodwill | $28.15B | 稳定（无大额收购跳升，VIZIO 已并表） |
| Stockholders Equity | $94.33B | |
| Working Capital | -$26.19B | 负（零售负营运资本，AP 浮存） |
| Cash/Debt | 0.145x | <1x（低现金覆盖，但 OCF 强可偿债） |

## B.5 正常化 EPS Chain

| 口径 | EPS | 来源 |
|------|-----|------|
| GAAP | $2.84 | Diluted EPS (income_ttm.csv) |
| 工具 | $2.839 | Normalized Income $22.736B / Diluted Shares 8.009B |
| v3.1 | $2.609 | detector 2a OtherInc MTM 剥离 $2.947B（税前） |
| **FINAL** | **$2.609** | **min(三者) → v3.1** |

- **winner: v3.1**
- adj: -8.1% vs GAAP（剥离投资 MTM 收益）
- detectors 触发: **2a OtherInc (MTM)** — confidence high, amount_pretax $2.947B, vol=3.1x（季度范围 -$2.117B ~ +$2.708B）

### GAAP → v3.1 桥接

```
GAAP 税前                    $30.623B
  − OtherInc 剥离（税前）      $2.947B    ← detector 2a (高信心, vol=3.1x)
  − Unusual 剥离              $0         ← 工具无标记（Normalized Income = GAAP NI）
  = 正常化税前               $27.676B
  × (1 − 税率 24.50%)         × 0.7550
  = 正常化净利               $20.896B
  ÷ 稀释股数 8.009B
  = v3.1 EPS                 $2.609
```

### Detector 2a: OtherInc（非利息其他收入）

**定义**: 非利息 Other = Pretax − Operating Income − Net Interest = 30.623 − 30.183 − (−2.507) = $2.947B

子项拆解（从 TTM CSV）:

| 子项 | 金额 | 性质 |
|------|------|------|
| Other Non Operating Income Expenses | $2.947B | TTM 合计（投资 MTM + pension） |
| Net Non Operating Interest Income Expense | -$2.507B | 利息净支出（非 OtherInc 部分） |
| **合计 OtherInc** | **$2.947B** | |

> WMT 非投资控股型公司（与 TSM/0700.HK 不同），OtherInc 主要是投资公允价值变动 + 养老金收入。季度波动大（-2.1B ~ +2.7B）→ detector 2a 高信心触发，剥离 TTM 正值 $2.947B 合理（保守口径）。

### Detector 触发原因分析

- 季度波动率 vol_ratio = 3.1x（**>2 触发**）
- 范围: -$2.117B（Q4'26）~ +$2.708B（Q2'26）
- **半年报复查**: WMT 为美国季报公司，季度 CSV 全有值（无零值），**非假阳性**
- 评估: **真波动触发**（投资 MTM + pension 跨季摆动，方向不定）

### Unusual 重叠检查

```
|OtherInc $2.947B − Unusual $0| / max = 100%
→ 工具无 Unusual 标记，v3.1 独立剥离 OtherInc
```

> 无重叠风险。工具 Normalized Income = GAAP NI（未剔任何一次性），v3.1 比 GAAP 保守 8.1%。

### 三口径对比

| 口径 | 剥离额 | Normalized NI | EPS |
|------|--------|--------------|-----|
| GAAP | $0 | $22.736B | $2.84 |
| 工具 | $0 | $22.736B | $2.839 |
| v3.1 | $2.947B（税前） | $20.896B | $2.609 |

> 工具剥离额 $0 vs v3.1 剥离额 $2.947B：工具未识别 OtherInc 为一次性，v3.1 detector 2a 因波动率高信心剥离。取 min = v3.1 $2.609（保守下限）。

### 评估

v3.1 适度保守（非过度）。WMT 非 TSM/0700.HK 类投资控股型（OtherInc 不含大量经常性分红），剥离投资 MTM 合理。即使保留 GAAP $2.84，合理价 $2.84×14.5=$41.18 vs v3.1 $37.83，差异 ~9%，均远低于现价 $111.85，结论不变（买贵了）。

## B.6 质量地板（给 Task D 预判）

| 指标 | 值 | ✓/✗ |
|------|-----|-----|
| GM >60% 稳 | 25.0% | ✗（零售结构性低，非质量差） |
| NM >20% | 3.1% | ✗（零售薄利本质） |
| FCF yield >5% | 1.41% | ✗（CapEx 重吞 FCF） |
| FCF−SBC >0 | $12.55B（SBC=$0） | ✓ |
| 真缩股 | 8.20B→8.02B（3yr -2.2%） | ✓ |
| ROIC>15% 或 ROE>15% | ROIC 14.4%✗ / ROE 24.1%✓ | ✓（ROE 通过） |

本地评分: **3/6**（FCF−SBC✓ + 真缩股✓ + ROE✓；GM/NM/FCF yield 三项 ✗）→ 至少"**好公司**"（3-5 分区间）。B 地板假设一般麻烦 ×0.67（保守预判，trouble 待 C 定）；C 确认无麻烦 + 护城河宽 → D 升至 **×0.75**（4/7，好公司×无麻烦，见 D.1）

> 注: GM/NM/FCF yield 三项 ✗ 是零售模型本质（薄利、高周转、CapEx 重），非质量缺陷。ROE 24.1% + 真缩股 + FCF−SBC 正 + 利息覆盖 10.5x 体现资本效率。48 年股息贵族印证持久性。
