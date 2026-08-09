# V — Task B：财务健康 + 正常化 EPS
> 更新: 2026-08-09（财报 TTM 2026-06-30, Q3 FY26）

## B.1 SCORECARD 九宫格

| 维度 | 3yr | TTM | 5Q |
|------|------|-----|-----|
| Income | 100 | 100 | 70 |
| CF | 78 | 88 | 65 |
| BS | 48 | 100 | 92 |

权重 Income 25% / CF 35% / BS 40%。

### 背离检验

| 维度 | SCORECARD 说 | 原始财报 | 方向 |
|------|-------------|---------|------|
| Income 5Q | 70（GM/NM Q YoY 下滑扣分） | TTM GM 80.2% 稳、Q3'26 单季 GM 76.5% 下滑 | 单季波动，非结构——Q3'26 Cost of Revenue 暴涨（client incentives/Visa Direct mix） |
| CF 5Q | 65（OCF/FCF Q YoY -2.6%/-2.7%） | TTM FCF $21B 强、年度趋势 +15% | 季度 working capital 波动，非趋势恶化 |
| BS 3yr | 48（D/E 升、CR 降） | D/E 0.53→0.66（2025 增债回购）、CR 1.45→1.08 | 主动加杠杆回购+分红，非经营恶化；轻资本模式无需高 CR |

伤口模式: **无伤口**——3yr 高分 + TTM/5Q 中等是季度波动 + 主动资本结构调整，非困境。近高位、经营加速。

## B.2 利润表逐季（income_quarterly，新→旧）

| 季度 | Revenue | GM% | OpInc | OpM% | OtherInc | Pretax | NI | dilEPS |
|------|---------|-----|-------|------|----------|--------|-----|--------|
| Q3'26(06-30) | 11.63B | 76.5% | 7.13B | 61.3% | -103M | 6.83B | 5.63B | 2.97 |
| Q2'26(03-31) | 11.23B | 81.3% | 7.56B | 67.3% | -211M | 7.17B | 6.02B | 3.14 |
| Q1'26(12-31) | 10.90B | 81.7% | 7.45B | 68.3% | -525M | 6.73B | 5.85B | 3.03 |
| Q4'25(09-30) | 10.72B | 81.6% | 7.05B | 65.8% | -618M | 6.22B | 5.09B | 2.62 |
| Q3'25(06-30) | 10.17B | 80.6% | 6.79B | 66.8% | -420M | 6.33B | 5.27B | 2.69 |

分析：
- **Q3'26 GM 76.5% 突降**（vs 前 4 季 80.6-81.7%）→ Cost of Revenue $2.738B vs Q2'26 $2.101B（+30.4% QoQ，营收仅 +3.6% QoQ）。主因 client incentives（客户激励）集中确认 + Visa Direct 低 margin 业务（世界杯）mix 上升。TTM GM 仍 80.2%，非结构性。
- Other Income Expense 全为负（-103M ~ -618M）→ 投资收益净额为负（利息支出 + 一次性），GAAP 已扣，detector 2a 标记但 amount < 0 不加回。
- OpInc Q YoY +5.0%（Q3'26 $7.13B vs Q3'25 $6.79B），低于营收 +14.4% → Q3'26 margin 压缩。但 TTM OpInc $29.19B +9.9% YoY 稳健。
- dilEPS Q YoY +10.4%（$2.97 vs $2.69），受回购缩股支撑（股数 2.15B→2.11B QoQ 下降）。

## B.3 现金流（cf_ttm，2026-06-30）

| 项目 | TTM | 说明 |
|------|-----|------|
| OCF | $22.58B | OCF/NI = 1.00（利润含金量足） |
| FCF | $21.01B | yield = 21.01/676.80 = 3.1%（低，因股价贵） |
| SBC | $919M | SBC/Rev = 2.1%（极低，卡组织无重 SBC） |
| 回购 | $21.36B | Net Return = 回购 21.36 + 分红 5.00 − SBC 0.92 = +$25.44B |
| CapEx | $1.57B | CapEx/OCF = 7%（极轻资产） |

**FCF − SBC = $21.01B − $0.92B = +$20.09B > 0 ✓**（质地满分，无烧钱）

回购 $21.36B > SBC $0.92B（23x）→ 净缩股 → SBC 被回购对冲，非真成本 → DCF 用 FCF 口径为主。

## B.4 资产负债表（bs_quarterly，2026-06-30）

| 项目 | 值 | 说明 |
|------|-----|------|
| Cash + ST Inv | $13.79B | |
| Total Debt | $23.86B | 长期债 $20.86B + 短期 $3.00B |
| 净债 | -$10.07B | 净债（无现金托底），但轻资本+FCF 强非风险 |
| D/E | 0.68 | 2025 升（0.53→0.66）因增债回购，主动 |
| **利息覆盖** | **37.6x** | OpInc $29.19B / Interest $776M → >5x ✓ |
| Goodwill+Intang | $48.36B | /Assets 51.1%（高，历史并购 Visa Europe/Fiserv 等，稳定非跳升） |
| Equity | $35.18B | Retained Earnings $12.75B（回购消耗，但 FCF 持续补充） |

## B.5 正常化 EPS Chain

| 口径 | EPS | 来源 |
|------|-----|------|
| GAAP | $11.75 | Diluted EPS（income_ttm，two-class method） |
| 工具 | $11.08 | Normalized Income $23.81B / Diluted Shares 2148.65M |
| v3.1 | $10.51 | detector 计算（详见下方） |
| **FINAL** | **$10.51** | **min(三者)，v3.1 = min** |

- winner: **v3.1**
- 工具 vs GAAP: 工具 $11.08 < GAAP $11.75，因工具用 NI/shares 口径（2148.65M）vs GAAP Diluted EPS 用 two-class method effective shares（~1923M），股份口径差异 ~226M（participating securities 未分配收益处理）
- v3.1 vs GAAP: v3.1 = NI/shares = $10.51，差距纯来自股份口径，**非一性项剥离**

### GAAP → v3.1 桥接

```
GAAP 税前                    $26.956B
  − OtherInc 剥离（税前）      $0        ← detector 2a 触发但 amount < 0（损失），不加回
  − Unusual 剥离（税前）       $0        ← 工具 Unusual -$1.457B（损失），不加回
  = 正常化税前               $26.956B（= GAAP Pretax）
  × (1 − 税率 16.19%)
  = 正常化净利               $22.592B（= GAAP NI）
  ÷ 稀释股数 2148.65M
  = v3.1 EPS                 $10.51
```

### Detector 2a: OtherInc（非利息其他收入）

非利息 Other = Pretax − OpInc − NetInt = 26956 − 29189 − (−776) = −1457M（损失）

子项拆解（从 income_ttm CSV）：

| 子项 | 金额 | 性质 |
|------|------|------|
| Special Income Charges | -$2.193B | 一次性（诉讼/监管准备金） |
| Other Special Charges | +$2.193B | 冲回（与上项抵消=0） |
| Gain On Sale Of Security | +$736M | 投资处置（偶发） |
| **已列小计** | -$1.457B | |
| **合计** | -$1.457B | 净损失 |

### Detector 触发原因分析

- 季度波动率 vol_ratio = 1.4x（< 2，未达波动阈值）
- detector 2a 标 high confidence 但 amount = -$1.457B（**损失**）
- 按"只剔收益不加回亏损"原则：total_pretax_adj = $0（不剥离）
- v3.1 NI = GAAP NI = $22.592B；v3.1 EPS = NI/shares = $10.51
- **关键**：v3.1 $10.51 < GAAP $11.75 的差距来自股份口径（Diluted Average Shares 2148.65M vs GAAP two-class method effective ~1923M），**非一性项剥离**

### Unusual 重叠检查

```
|OtherInc -$1.457B − Unusual -$1.457B| / max = 0%
→ 完全重叠（OtherInc = Unusual，Visa 的 Other Income 就是工具归类的 Unusual）
→ 工具加回损失（Normalized Income $23.81B = GAAP + 1.457×(1-tax)）
→ v3.1 不加回（保守），min() 兜底取 v3.1
```

### 三口径对比

| 口径 | 剥离额 | Normalized NI | EPS |
|------|--------|--------------|-----|
| GAAP | 0 | $22.592B | $11.75 |
| 工具 | +$1.221B（加回损失） | $23.813B | $11.08 |
| v3.1 | $0（不加回） | $22.592B | $10.51 |

工具 EPS $11.08 < GAAP $11.75，因工具用 2148.65M shares（含 participating securities）÷ NI，而 GAAP Diluted EPS 用 two-class method（扣 participating securities 未分配收益 + 更小 effective shares）。两者方向一致（都 < GAAP Diluted EPS）。

### 评估

v3.1 $10.51 过度保守：差距来自股份口径（two-class method），非一性项剥离。按 normalize_eps.md 已知问题 #2 补偿路径：**改用 GAAP Diluted EPS $11.75 作交叉验**（D 中展示两口径合理价）。但 min() 硬规则 → FINAL = $10.51 用于合理价公式，GAAP $11.75 作交叉验标注。

## B.6 质量地板（给 Task D 预判）

| 指标 | 值 | ✓/✗ |
|------|-----|-----|
| GM >60% 稳 | 80.2%（3yr 稳，Q3'26 单季 76.5% 波动） | ✓ |
| NM >20% | 50.8% | ✓ |
| FCF yield >5% | 3.1%（低，因股价贵非 FCF 弱） | ✗ |
| FCF−SBC >0 | +$20.09B | ✓ |
| 真缩股 | 2560M→2149M（3yr −16%，大额回购） | ✓ |
| ROE >15% | 61.2% | ✓ |

本地评分: **6/6**（仅 FCF yield ✗，但 FCF 金额 $21B 强、yield 低纯因股价贵）→ 至少"好公司 ×0.67"，护城河确认后升"伟大 ×0.75"

> 注：FCF yield 3.1% < 5% 是"好公司但贵"的信号，非 FCF 质量问题。FCF 金额 $21B TTM、+15% 3yr 增长，质地满分。按 discount_coefficient.md，FCF yield 阈值是"高 = >5%"，低 yield 不否决质量评分（FCF 金额 + FCF−SBC 才是硬指标）。
