# PFE — Task B：财务健康 + 正常化 EPS
> 更新: 2026-08-08（财报 TTM 截至 2026-06, FY2025 annual）　货币: USD

## B.1 SCORECARD 九宫格

| 维度 | 3yr | TTM | 5Q |
|------|------|-----|-----|
| Income | 70 | 50 | 42 |
| CF | 68 | 100 | 90 |
| BS | 85 | 100 | 65 |

### 背离检验

| # | 维度 | SCORECARD 说 | 原始财报 | 方向 |
|---|------|------|------|------|
| ① | Income TTM=50/5Q=42 | ✗ EPS −44% YoY、✗ NM −1.6% Q1'26 → 机械看恶化 | **证实恶化**: EPS $0.76 TTM 被 OtherInc −$11.8B（Seagen 减值/摊销）压低; Q1'26 NM −1.6%（单季亏损）= Seagen 摊销+重组拖累。**但 OpInc $17.0B 仍正、GM 73.2% 稳** → 核心经营未崩 | **Seagen 会计拖累, 非经营崩溃** |
| ② | BS 5Q=65 | ✗ Cash/Debt 0.19x、Risk Flag Goodwill 60% + NI declining | **证实**: 净债 $51.5B, Goodwill 60%（Seagen $43B）; Cash/Debt 0.19x → 现金薄 | **高杠杆 + 减值风险** |
| ③ | CF TTM=100 | ✓ OCF +14.5%、✓ FCF $10.98B、✓ OCF/NI 3.09 | **证实**: FCF 远超 NI（D&A $6.58B + 损失加回）; 但分红 $9.79B > FCF payout 89% | **FCF 强但分红吃满** |

**伤口模式**: 非暂时困境被错杀, 是 **COVID 退潮 + Seagen 摊销 + 专利悬崖** 三重结构性压力。无情绪伤口可恢复。

## B.2 利润表逐季

```
         Rev     GM%    OpInc   OpM%    NI       OtherInc   dilEPS
Q1'25  13.71B  79.3%   4.42B   32.2%   2.97B   -1.13B     $0.52
Q2'25  14.65B  74.3%   3.77B   25.7%   2.91B   -0.23B     $0.51
Q3'25  16.65B  74.9%   5.53B   33.2%   3.54B   -1.68B     $0.62
Q4'25  17.56B  70.0%   3.69B   21.0%  -1.65B   -4.79B    -$0.29   ← Seagen 减值
Q1'26  15.03B  72.8%   3.54B   23.6%  -0.23B   -0.46B    -$0.04   ← 单季亏损
```

- **GM 稳 70-79%** — 基础药定价权尚可; Q4'25 70% 低系季节性+成本
- **OtherInc 巨额负值主导 GAAP 波动**: Q4'25 −$4.79B 拖累致单季亏损; 全年 OtherInc −$11.8B = Seagen 无形摊销+减值+重组 → **半经营性质**（买增长代价, 非纯一次性）
- **正常化 NI**: tool $11.42B vs GAAP $4.33B → gap $7.1B = Seagen 摊销+减值（重复发生, 不全额加回）
- **营收**: 2025 $62.6B vs 2022 $101.2B = COVID 退潮 −38%; FY26 指引 $59.5-62.5B = 再降

## B.3 现金流

| 项目 | TTM | 说明 |
|------|-----|------|
| OCF | $13.40B | +14.5% YoY; OCF/NI=3.09（NI 低因 Seagen 损失, 非经营恶化） |
| FCF | $10.98B | CapEx $2.42B（18% OCF, 轻） |
| SBC | $947M（实查 cf_ttm） | SBC/Rev=1.5%（低） |
| 回购 | $0（TTM, 零回购） | 分红为主 |
| 分红 | $9.79B | **yield 6.56%!** 但 payout 89%（分红≈FCF） |

FCF − SBC = $10.98B − $0.947B = **$10.04B > 0 ✓**

> ⚠️ **分红 $9.79B ≈ FCF $10.98B → payout 89%**: 分红几乎吃满 FCF → 无余力回购或再投资。若 FCF 下降（专利悬崖）→ 分红可能削减。
> FCF yield = $10.98B / $152.52B = **7.2%**（>5% ✓, 但因股价跌而非 FCF 强）

## B.4 资产负债表

| 项目 | 值 | 说明 |
|------|-----|-----|
| 现金 | $11.70B | Q1'26, 极薄 |
| 总债 | $63.19B | Seagen $43B 收购举债 |
| **净债** | **$51.50B** | 无净现金托底（vs MRK $43B, JNJ $46B） |
| D/E | 0.74 | 温和 |
| **利息覆盖** | **6.3x** | OpInc $17.02B / IntExp $2.70B → **>5x ✓** |
| Goodwill | 60% Assets | **Risk Flag!** Seagen $43B 堆积, 减值风险 |
| ROE | 5.0% | 极低（NI 被 Seagen 压） |
| ROIC | 7.5% | <15% |

## B.5 正常化 EPS Chain

| 口径 | EPS | 来源 |
|------|-----|------|
| GAAP | $0.76 | Diluted EPS TTM（被 OtherInc −$11.8B 压低） |
| 工具 | $1.99 | Normalized Income $11.42B / 5.726B shares（加回 unusual 损失） |
| v3.1 | $0.76 | OtherInc/Unusual 均为损失 → 不剥离 → ≈ GAAP |
| **FINAL** | **$0.76** | **min = GAAP = v3.1** |

> ⚠️ **GAAP $0.76 被 Seagen 减值/摊销严重压低**。Tool $1.99 加回了 $7.1B unusual 损失 → 但 per "不加回亏损" → 损失不剥离 → min = $0.76。
> 旧 base 正常化 EPS $2.60（adj 指引, 加回 Seagen 摊销）→ **违反 min 规则**（加回亏损 = 取上界）。修正: min = $0.76。
> **但**: $0.76 含重复发生的 Seagen 摊销（买增长的真实经济代价）→ 保守但合理。

### Detector 触发列表（实跑 normalize_eps.py）

| Detector | 信心 | amount | 说明 |
|----------|------|--------|------|
| 2a OtherInc+Unusual | high | −$11.8B (pretax) | vol=2.1x; **损失 → 不剥离** |
| 2b Restructuring | low | $1.96B | 费用, 只标记 |
| 2c TaxAnomaly | medium | +$885M (after-tax) | TTM −3.9% vs 均值 −24.9% (diff 21pp) |
| 2h Discontinued | high | −$5M | 微小 |

> OtherInc −$11.8B + Unusual −$11.8B overlap 9.8% → 判独立但均为损失 → 均不剥离 → v3.1 = GAAP = $0.76

## B.6 质量地板

| 指标 | 值 | ✓/✗ |
|------|-----|-----|
| GM >60% 稳 | 73.2%（3yr 58→72→74%, COVID 恢复后稳） | ✓ |
| NM >20% | 6.8% TTM（被 Seagen 压; FY25 12.4%） | ✗ |
| FCF−SBC >0 | $10.04B | ✓ |
| 真缩股 | 零回购 + 股数 5.93B→5.73B（3yr 微降, 靠退休金扣除非主动回购） | ✗ |
| ROIC >15% 或 ROE >15% | ROIC 7.5%, ROE 5.0% | ✗ |
| 护城河宽 | ✗（专利到期=护城河收窄; Eliquis 2028, Ibrance 已到期; Seagen ADC 关键试验失败） | ✗ |

本地评分: 2/5 local + 护城河 ✗ = 2/6 = **平庸**
> GM ✓ + FCF−SBC ✓ = 2 通过；NM ✗ + 真缩股 ✗ + ROIC ✗ + 护城河 ✗ = 4 失败

→ **3/6 = 好公司**（NM 低 + 无缩股 + ROIC 低 + 护城河收窄 → 限制不进伟大）
