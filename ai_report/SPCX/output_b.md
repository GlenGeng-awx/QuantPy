# SPCX — Task B：财务健康 + 正常化 EPS
> 更新: 2026-08-09  CSV 戳: TTM 2026-03-31（Q2'26 已 8-05 报但未进 CSV，Q2 数据见 C.4）

## B.1 SCORECARD 九宫格

| 维度 | 3yr | TTM | 5Q |
|------|-----|-----|-----|
| Income | 40 | 25 | —（季度 CSV 仅 2 期，无 5Q 趋势） |
| CF | 53 | 52 | 0（仅 2 期，OCF/NI Q 因 NI 负 ✗） |
| BS | —（年度仅 2 期，无 3yr 趋势） | 50 | 100 |

### 背离检验

| 维度 | SCORECARD 说 | 原始财报 | 方向 |
|------|-------------|---------|------|
| Income 3yr | 40（营收✓/GM✓ 但 OpInc✗/EPS✗） | 营收 $10.4B→$18.7B 增长但 OpInc $507M→−$2.06B 崩塌 | 增收不增利的极端形态 |
| CF | 53/52（OCF 正向） | FCF −$19.8B（CapEx $26.9B 吞噬 OCF） | OCF 正但 FCF 深度负 — 资本支出型烧钱 |
| BS 5Q | 100（Cash/Debt 0.78x, D/E 0.73, CR 1.22 全✓） | 净债 $6.9B，利息覆盖 −1.9x | BS 单期健康但利润无法覆盖利息 |

伤口模式: 3yr 营收增长（+33%/2yr）+ OpInc 从 $507M→−$2.06B 崩塌 = **结构性伤口**（R&D 暴涨 $2.1B→$10.6B 驱动），非情绪伤口。增收不增利，资本开支狂烧。

## B.2 利润表逐季（USD，CSV 仅 2 期可得）

```
            Rev      GM%    OpInc    OpM%     NI       dilEPS   R&D       SGA
Q1'26     4.69B    49.1%   -1.95B  -41.6%  -4.28B    -0.41    3.51B     0.75B   ★ R&D 暴涨，OpInc 转负
Q1'25     4.07B    51.8%    0.06B    1.4%  -0.53B    -0.05    1.56B     0.49B
TTM      19.30B    48.8%   -4.07B  -21.1%  -8.69B    -0.67   10.60B     2.90B
```

### 趋势分析
- **GM 48.8%（TTM）**尚可，但 Q1'26 vs Q1'25 下滑（51.8%→49.1%）；年度 GM 改善（41.2%→49.4%，2023→2025）
- **R&D TTM $10.60B = 54.9% Rev**（hist 3yr 均值 30.4%，spike 24.5pp）→ 触发 detector 2f；R&D 从 $2.1B(2023)→$10.6B(TTM) 5x 暴涨 = Starship/Starlink/Grok 再投资，**结构性非一次性**
- **Q1'26 OpInc −$1.95B vs Q1'25 $55M**：转负，触发 detector 2d
- **OpInc vs NI 背离**：OpInc −$4.07B vs NI −$8.69B，差距来自 Other Inc −$2.33B + Net Interest −$1.57B + Tax +$0.71B
- **税率异常**：TTM Tax $710M on Pretax −$7.975B = −8.9%（pretax 负仍缴税），vs hist Tax Rate For Calcs 7.3%/21%/21%

## B.3 现金流

| 项目 | TTM | 说明 |
|------|-----|------|
| OCF | $7.11B | 正（OCF/NI = −0.82，NI 负致比率失真；OCF 本身来自 D&A $7.7B + SBC $2.35B + WC $3.15B 抵消 NI −$8.69B） |
| **FCF** | **−$19.78B** | **大额负**（CapEx −$26.88B 吞噬全部 OCF + 倒贴） |
| SBC | $2.35B | 高（SBC/Rev = 12.2%，TTM 现算） |
| 回购 | $4.96B | 有回购，但 vs 发股 $26.23B = 净稀释 |
| **FCF−SBC** | **−$22.13B** | **<< 0 → 重麻烦（硬规则 ×0.40，不否决）** |

FCF −$19.78B + SBC $2.35B → **FCF−SBC = −$22.13B << 0**。CapEx $26.88B（太空基建+AI 算力+Starlink 星座）吞噬全部 OCF。Net Return（回购+分红−SBC）= $4.96B + 0 − $2.35B = +$2.61B（回购>SBC），但回购远不足以抵消 $26.2B 发股稀释。

> ⚠ FCF 质量必查：OCF $7.11B 的来源 = D&A $7.7B + SBC $2.35B + ΔWC $3.15B − NI $8.69B。D&A+SBC 合计 $10.05B > OCF $7.11B，说明 OCF 部分靠非现金项撑，NI 负拖累。CapEx $26.88B 全部吞噬 OCF 还倒贴 → 深度负 FCF。

## B.4 资产负债表（Q1'26 snapshot）

| 项目 | 值 | 说明 |
|------|-----|------|
| Cash+STI | $23.68B | — |
| Total Debt | $30.60B（LT $28.73B + Current $1.54B + Cap Lease $0.34B） | 高 |
| **净现金/债** | **−$6.93B（净债）** | Cash < Debt，无托底 |
| D/E | 0.74（$30.60B/$41.58B Equity） | 偏高（含 preferred $7.05B） |
| **利息覆盖** | **−1.88x**（OpInc −$4.073B / Interest $2.162B） | **≤2x ✗**（OpInc 负，无法覆盖利息） |
| Goodwill | $14.39B | Assets 14.1%（$14.39B/$102.09B），无跳升风险 |
| Equity | $41.58B | 含 APIC $74.08B + Retained −$41.31B（累计亏损） |

## B.5 正常化 EPS Chain

| 口径 | EPS | 来源 |
|------|-----|------|
| GAAP | −$0.672 | Diluted EPS (TTM) |
| 工具 | −$0.642 | Normalized Income −$8.393B / Shares 13.076B |
| v3.1 | −$1.738 | detector 计算（**算法失效，见下**） |
| **恢复 EPS** | **−$0.481** | **EPS-4b，结构性亏损（见下）** |
| **FINAL** | **N/A（全负）** | **恢复 EPS 仍负 → PE 公式无意义（详见 D）** |

### Detector 列表（normalize_eps.py 实跑，6 个触发）

| Detector | amount | 信心 | 剥离? | 说明 |
|----------|--------|------|------|------|
| 2a OtherInc | −$2.328B（税前） | high | ❌ 负→不剥离 | vol 1.5x range −$1.865B~−$0.239B |
| 2b Restructuring | $472M（税前） | low | ❌ flag only | 费用非收益，per"不加回亏损"；且 2023-2026 连续 4 年 = 经常性 |
| 2c TaxAnomaly | −$5.58B（税后） | medium | ❌ 负→不剥离 | TTM −8.9% vs hist −78.9%（diff 70pp，亏损年税率失真） |
| 2d OpIncDrop | — | low | ❌ flag only | Q1'26 −$1.954B vs Q1'25 $55M 转负 |
| **2f RDSpike** | **+$4.728B（税前）** | **medium** | **v3.1 剥离（主驱动）** | TTM 54.9% vs hist 30.4%（spike 24.5pp） |
| 2x Unusual | −$486M（税前） | high | ❌ 负→不剥离 | Special Income Charges，diff 79.1% |

v3.1 计算: total_pretax_adj = 2f only = $4.728B（2a/2x 负→0，2b/2d low→skip，2c 税后负→0）。norm_pretax = −$7.975B − $4.728B = −$12.703B。use_tax_rate = hist 均值 −78.9%（2c 触发，亏损年失真）。norm_ni = −$12.703B × (1−(−0.789)) = −$12.703B × 1.789 = −$22.72B。EPS = −$22.72B/13.076B = **−$1.738**。

### ★ v3.1 算法失效（亏损股）

v3.1 = −$1.74 比 GAAP −$0.672 更负，违反"GAAP 兜底"意图。原因:
1. **2f RDSpike 把 R&D 暴涨 +$4.73B 当一次性收益剥离** → pretax 更负（−$7.975B → −$12.703B）。但 R&D 暴涨是 Starship/Starlink/Grok 再投资 = **结构性非一次性**，detector 误判
2. **历史均值税率 −78.9%（亏损年 pretax 负致 tax rate 失真）应用到负 pretax** → ×(1−(−0.789)) = ×1.789 放大亏损

per `normalize_eps.md` 已知问题 #5 + mistakes.md #21: 亏损股 v3.1 若比 GAAP 更负 → 标"算法失效"。v3.1 不进 min 展示。

### 恢复 EPS（EPS-4b，EPS 负值时使用）

```
TTM GAAP Pretax           −$7.975B
  + 一次性费用加回:
    - Impairment            +$0.014B     ← detector 2h（小，真一次性）
    - Restructuring         不加回       ← 2b 连续 4 年 = 经常性非一次性
    - Special Charges       不加回       ← 2023-2026 连续 = 经常性
    - R&D Spike(2f)          不加回       ← 结构性再投资（Starship/Starlink/Grok），非 IPR&D 一次性
  − 一次性收益剥离:          $0          ← 无收益可剥（2f 是费用 spike 非 gain）
  = 恢复 Pretax             −$7.961B
  × (1 − 正常税率 21%)      ← US federal，hist Tax Rate For Calcs 均值（7.3%/21%/21%）
  = 恢复 NI                 −$6.289B
  ÷ 稀释股数 13.076B
  = 恢复 EPS                −$0.481
```

**恢复 EPS = −$0.481（仍负）**。亏损来源 = R&D $10.6B（54.9% Rev）+ Interest $2.16B + SGA $2.9B vs Gross Profit $9.4B = 结构性经营缺口，非一次性麻烦。剥离 ~$14M impairment 远不足以翻转。

> 恢复 EPS 负值 = PE 公式（恢复 EPS × PE）产生负合理价 = 无意义。SPCX 亏损是 hypergrowth 再投资（类早期 AMZN/TSLA），非"暂时困境"。详见 Task D。

### Unusual 重叠检查

```
|OtherInc −$2.328B − Unusual −$0.486B| / max = 79.1% → >20% → 独立
但两者均负（费用/亏损），按"不加回亏损"原则均不剥离 → 无双重剥离风险
```

## B.6 质量地板（给 Task D 预判）

| 指标 | 值 | ✓/✗ |
|------|-----|-----|
| GM >60% 稳 | 48.8%（且 Q1 下滑） | ✗ |
| NM >20% | −45.0% | ✗ |
| FCF−SBC >0 | −$22.13B | ✗ |
| 真缩股 | ✗（IPO 大幅稀释：股数 9.649B(2025)→13.076B(TTM) +35%；发股 $26.2B vs 回购 $5.0B） | ✗ |
| ROIC/ROE >15% | ROIC −5.0% | ✗ |

本地评分: **0/5 local** + 护城河 ✓ = **1/6 = 平庸**。FCF−SBC<0 → 硬规则 ×0.40（重麻烦）。

> SPCX 3yr OpInc 从 $507M → −$2.06B = 盈利能力结构性崩塌。营收增长（$10.4B→$18.7B，2yr CAGR 34%）但增收不增利。R&D 5x 暴涨（$2.1B→$10.6B）+ CapEx 6x 暴涨（$4.4B→$26.9B）= 再投资型烧钱。IPO 2026-06-12，TTM 含 IPO 后大幅发股稀释。
