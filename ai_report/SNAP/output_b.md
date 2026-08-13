# SNAP — Task B：财务健康 + 正常化 EPS
> 更新: 2026-08-08（财报 Q2'26，2026-08-03 发；TTM 截 2026-06）  货币: USD

## B.1 SCORECARD 九宫格

| 维度 | 3yr | TTM | 5Q | 权重 |
|------|------|-----|-----|------|
| Income | 40 | 90 | 85 | 25% |
| CF | 100 | 60 | 95 | 35% |
| BS | 50 | 83 | 70 | 40% |

### 背离检验

| 维度 | SCORECARD 说 | 原始财报 | 方向 |
|------|-------------|---------|------|
| CF | 3yr/5Q 高分（100/95）— FCF 转正且增长 | TTM FCF $705M 但 **SBC $1.03B → FCF−SBC = −$325M < 0**（伪 FCF） | **陷阱 = 危险**（高分是 SBC 加回幻觉） |
| Income | TTM 90 高分（亏损收窄改善率） | TTM OpInc −$323M（仍亏），10 年从未 GAAP 持续盈利 | **陷阱 = 危险**（亏损收窄 ≠ 盈利） |
| BS | 3yr 50 低分 | 净负债 −$1.57B、有形净资产 ≈$0.06B、3yr 杠杆高位 | 同向 |

### 伤口模式

Income 3yr=40 + 十年累计亏损 −$14.8B = **结构性伤口**（区别于 ADBE 情绪伤口）。3yr 收入增长（CAGR 8.8%）但 OpInc 持续负值 → 增长不经济。TTM/5Q 高分是亏损收窄的改善率假象，不是盈利能力——别误读。

工具: `python3 -m fundamental.health SNAP`（health/scoring.py）

## B.2 利润表逐季（income_quarterly.csv）

```
           Rev      GM%     OpInc    OpM%    NI       dilEPS   dilShares
Q2'26     1.60B    58.2%   -170M    -10.6%  -163M    -0.10    1.66B
Q1'26     1.53B    56.4%    -74M     -4.8%   -88M     -0.05    1.69B
Q4'25     1.72B    58.7%    +49M     +2.9%   +45M     +0.03    1.71B
Q3'25     1.51B    55.0%   -128M     -8.5%  -103M     -0.06    1.70B
Q2'25     1.34B    51.4%   -259M    -19.4%  -262M     -0.16    1.67B
```

分析:
- **GAAP 仍亏**：5 季仅 Q4'25（假日旺季）单季转正，其余全负。TTM OpInc −$323M、NI −$311M、EPS −$0.18
- **GM 改善但 <60% 阈值**：51.4%→58.2%（Q2'25→Q2'26），远低于 META 82% / TTD 78% — 广告业务规模不经济。TTM GM 57.3% <60% → 质量评分 ✗
- **营收加速**：Q2'26 +19% YoY（vs Q1'26 +12%、Q4'25 +14%），但拆开看：广告仅 +9%、其他 +85%（Snapchat+/Memory Storage/Lens+ 订阅）。Q3'26 指引 +14% YoY（midpoint $1.72B vs Q3'25 $1.51B）— 因世界杯支出正常化而放缓
- **税率扭曲小**：TTM Tax −$1M / Pretax −$312M ≈ 0%（亏损/NOL）；2025 实际税率 2%（9M/451M）
- **OpInc vs NI 背离小**：TTM OpInc −$323M vs NI −$311M，差 $12M = OtherInc + Net Interest（利息支出 $144M、OtherInc +$41M）

## B.3 现金流（cf_ttm.csv）

| 项目 | TTM | 说明 |
|------|-----|------|
| OCF | $919M（+40.1% YoY） | OCF/NI 负值无意义（NI 负） |
| FCF | $705M（3yr 34→218→437→705 增长） | yield = 705/9014 = **7.8%** |
| SBC | **$1.03B（SBC/Rev 16.2%）** | 全标的最高之一（NVDA 2.5%、GOOG 11%、SNAP 16.2%）；3yr 自 28.7% 降至 16.2%（纪律改善但仍高） |
| 回购 | $851M（TTM） | 净缩股 ✗（股数 1.61B→1.69B 3yr 仍在膨胀） |
| Net Return | $851M − $1.03B = **−$179M** | 回购填不平稀释，股东价值净流出 |
| CapEx | $213M（CapEx/OCF 23%） | 轻资产 |

**FCF − SBC = $705M − $1.03B = −$325M < 0** → 硬规则触发 → 重麻烦 ×0.40（不否决、总是估值）

> ⚠ FCF 质量必查：SNAP 正 FCF 全靠 SBC 加回（16.2% 营收）。SBC 是真成本（稀释股东），正 FCF 是会计幻觉。TTM 连续 8 季 FCF 为正，但 FCF−SBC<0 = 真实现金创造为负。

## B.4 资产负债表（bs_quarterly.csv，最新 2026-06）

| 项目 | 值 | 说明 |
|------|-----|------|
| Cash + ST Inv | $2.66B | — |
| 总债 | $4.23B | 含租赁 $691M |
| **净现金/债** | **−$1.57B（净负债）** | 无净现金缓冲，无清算托底 |
| D/E | 1.83（5Q） | 杠杆偏高；3yr 1.55→1.49→1.55 |
| **利息覆盖** | **−2.2x**（TTM OpInc −$323M / Interest $144M） | ✗ **负经营利润**（亏损公司无意义） |
| Goodwill + 无形 | $1.87B | 3yr 1.85→1.79→1.87，2026 跳升系收购（待查） |
| 股东权益 | $1.93B | 3yr 2.58→2.41→2.28→1.93（持续下行，回购+SBC 稀释 vs 累计亏损） |
| 有形净资产 | 1.93 − 1.87 = **$0.06B** | 几乎为零，无下行保护 |
| 累计亏损 | Retained Earnings −$14.80B | 10 年累计亏损，NOL 巨额（递延税资产未量化） |

工具: `python3 -m fundamental.statements SNAP`

## B.5 正常化 EPS Chain（min 三者 + 恢复 EPS）

| 口径 | EPS | 来源 |
|------|-----|------|
| GAAP | **−$0.18** | Diluted EPS（TTM） |
| 工具 | **−$0.184** | Normalized Income −$311M / 1.69B shares |
| v3.1 | **−$0.208** | detector 计算（剥离 OtherInc +$41M gain → 更负） |
| **FINAL** | **−$0.18**（恢复 EPS） | 三者均负 → 用恢复 EPS（EPS-4b） |

- winner: GAAP（v3.1 最负，工具/GAAP 接近）
- adj: v3.1 比 GAAP −15%（剥离 +$41M OtherInc gain）
- detectors: 2a OtherInc MTM 触发（vol_ratio 3.0x，amount_pretax +$41M，high confidence）

### GAAP → v3.1 桥接

```
GAAP Pretax (TTM)                     −$312M
  − OtherInc 剥离（税前）              +$41M    ← detector 2a（MTM gain）
  − Unusual 剥离                        $0      ← 工具无标记
  = v3.1 税前                          −$353M
  × (1 − 正常税率 15%*)               ×0.85
  = v3.1 NI                            −$300M
  ÷ 稀释股数 1.69B
  = v3.1 EPS                           −$0.177
```

*正常税率：SNAP 累计亏损 −$14.8B → NOL 巨额 → 实际税率 ~2%（2025）。但 NOL 终将耗尽，用 15% 为正常化税率（保守估）。

### Detector 2a: OtherInc（非利息其他收入）

**定义**：非利息 Other = Pretax − Operating Income − Net Interest
= −$312M − (−$323M) − $144M = +$41M（正值 = 净 Other 收益）

子项拆解：income_ttm.csv 未列 Other Income 子项明细，仅汇总行 `Other Income Expense $41M`。从 Q2'26 财报电话会议推断主要为投资组合 MTM（SNAP 持有部分战略投资）。

- 季度波动率 vol_ratio = 3.0x（range −$6.9M ~ +$27.6M）> 2x → 触发，标为一次性
- **半年报复查**：不适用（SNAP 是美股季报公司，季度 CSV 数据齐全，非假阳性）
- 评估：真波动触发（vol_ratio 3x），但金额小（$41M = 13% of Pretax abs），影响有限

### Unusual 重叠检查

```
工具 Total Unusual Items = $0（CSV 标记为零）
|OtherInc $41M − Unusual $0| / max = ∞ → 独立
→ OtherInc 独立剥离（无重叠）
```

### 三口径对比

| 口径 | 剥离额 | Normalized NI | EPS |
|------|--------|--------------|-----|
| GAAP | 0 | −$311M | −$0.18 |
| 工具 | $0 | −$311M | −$0.184 |
| v3.1 | +$41M（gain） | −$300M | −$0.177 |

### 评估

v3.1 与 GAAP 差距小（剥离 OtherInc $41M gain，影响 ~$0.02 EPS）。**三者均负**，无单一口径能给出正 EPS。

### 恢复 EPS（EPS-4b，EPS 负值时使用）

```
TTM GAAP NI                            −$311M
  + 一次性费用加回                      $0     ← 无重组/罚款/减值/代金券
  − 一次性收益剥离                     −$41M   ← detector 2a OtherInc gain
  = 调整后 Pretax                     −$353M
  × (1 − 正常税率 15%)
  = 恢复 NI                           −$300M
  ÷ 稀释股数 1.69B
  = 恢复 EPS                          −$0.18
```

**恢复 EPS = −$0.18**（与 GAAP 一致，因为损失是结构性的，无一次性费用可加回；剥离的小额 gain 反而让损失略加深）。SNAP 的亏损不是一次性因素造成 → "恢复" 概念无法挽救。EPS 模型公式（合理价 = EPS × min(8.5+g, 30)）给出负值 → **EPS 模型 N/A**，估值改用 DCF FCF 交叉验（见 output_d.md D.2b）。

## B.6 质量地板（给 Task D 预判）

| 指标 | 值 | ✓/✗ |
|------|-----|-----|
| GM >60% 稳 | TTM 57.3%（Q2'26 58.2%，3yr 54→55→55→57 改善但未过 60% 阈值） | ✗ |
| NM >20% | TTM −4.9%（亏损） | ✗ |
| FCF − SBC >0 | −$325M（硬规则触发） | ✗ |
| 真缩股 | 1.61B→1.69B 3yr（膨胀 +5%） | ✗ |
| ROIC/ROE >15% | ROIC −9.2%、ROE −15.6%（全负） | ✗ |

本地评分: **0/5 local** + 护城河 ✗（窄，份额流失中）= **0/6 = 平庸**。FCF−SBC<0 → 硬规则 ×0.40（重麻烦）。

> 按 `discount_coefficient.md`：本地 0/6 + 护城河窄（0）= 1/6 = **平庸**；FCF−SBC<0 自动触发重麻烦档 → **平庸 × 重麻烦 = ×0.40**。
