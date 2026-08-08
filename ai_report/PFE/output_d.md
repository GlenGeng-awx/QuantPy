# PFE — Task D：估值汇聚
> 更新: 2026-08-08

## D.1 三要素

### 正常化 EPS（from Task B）

| 口径 | EPS | 来源 |
|------|-----|------|
| GAAP | $0.76 | Diluted EPS TTM（被 OtherInc −$11.8B Seagen 摊销/减值压低） |
| 工具 | $1.99 | Normalized Income $11.42B / 5.726B shares（加回 unusual 损失） |
| v3.1 | $0.76 | OtherInc/Unusual 均为损失 → 不剥离 → ≈ GAAP |
| **FINAL** | **$0.76** | **min = GAAP = v3.1** |

> ⚠️ 旧 base 正常化 EPS $2.60（adj 指引, 加回 Seagen 摊销）→ **违反 min 规则**（加回亏损 = 取上界）。修正: min = $0.76。
> GAAP $0.76 被 Seagen 减值/摊销（$11.8B）严重压低; tool $1.99 加回 unusual 损失 → 但 per "不加回亏损" → 损失不剥离 → min = $0.76。
> **但**: Seagen 摊销是重复发生的经济现实（买增长代价）→ $0.76 保守但合理。

### 前瞻 g（from Task C）
g = 0%（G-3: Step 2 剔 3 COVID CAGR + earningsGrowth; Step 3 剔 PEG; Step 4 均值 2.6%; Step 5 调至 0% 因 Eliquis 2028 + COVID 退潮 + FY26 指引再降 = 外部结构性冲击; g<0 → 封底 0%）

### 合理 PE
PE = min(8.5 + 0, 30) = 8.5x

### 折扣系数（from B 质量地板 + C 护城河/麻烦）

质量评分:

| 指标 | ✓/✗ |
|------|-----|
| GM >60% 稳 | ✓（73.2%, COVID 后恢复稳） |
| NM >20% | ✗（6.8% TTM, FY25 12.4%; 被 Seagen 压） |
| FCF yield >5% | ✓（7.2%） |
| FCF−SBC >0 | ✓（$10.04B） |
| 真缩股 | ✗（零回购; 股数微降靠退休金非主动） |
| ROIC >15% 或 ROE >15% | ✗（ROIC 7.5%, ROE 5.0%） |
| 护城河宽 | ✗（Eliquis 2028 悬崖 + Seagen ADC 失败 + COVID 退潮 = 收窄） |

→ **3/7 = 好公司**（GM + FCF yield + FCF−SBC 通过; NM + 缩股 + ROIC + 护城河 失败）

麻烦定性: **存疑** — COVID 退潮 = 永久（非一次性）; Eliquis 2028 = 结构性; Seagen 失败 = 管线存疑。**非明确一次性, 非一般, 趋向结构性恶化**
→ 折扣系数 = **×0.60**（好公司 × 存疑）

## D.2 合理价 + 满仓目标（估值锚, 低频）

```
合理价 = $0.76 × 8.5 = $6.46
满仓目标 = $6.46 × 0.60 = $3.88
锚定: EPS=$0.76(min/GAAP), g=0%, PE=8.5x, 系数=×0.60, 日期: 2026-08-08
```

> 安全边际 join A(现价) + D(合理价) 算, 见 output_a.md A.3。

## D.2b DCF 交叉验

> 与 D.2 EPS 模型并列。详见 `docs/dcf.md`。

```
r = 11% (好公司 3/7)
g = 0% (from Task C)
P/FCF₀ = min((1+0)/(0.11−0), 30) = min(9.09, 30) = 9.09x  ← NOT capped! (g << r)
```

| 口径 | base ($/sh) | P/FCF₀ | DCF/sh | vs EPS 合理价 |
|------|-------------|--------|--------|---------------|
| DCF FCF−SBC | $1.76 | 9.09x | $6.98 | +8% |
| DCF FCF | $1.93 | 9.09x | $8.49 | +31% |

```
FCF (TTM) = $10.98B（实查 cf_ttm）
SBC (TTM) = $947M（实查 cf_ttm）
FCF−SBC = $10.04B
Shares = 5.700B
FCF/sh = $1.93
(FCF-SBC)/sh = $1.76
net_cash = $11.70B − $63.19B = −$51.50B（实查 bs_quarterly）
net_cash/sh = −$9.04
分红 $9.79B payout 89% ≈ FCF → 净现金 trapped in dividends
```

> ✅ **DCF 不封顶 → 交叉验有意义!** g=0% << r=11%, P/FCF=9.09x < 30 → Gordon 正常工作。
> **DCF FCF−SBC $6.98 ≈ EPS 合理价 $6.46** → gap 仅 $0.52（8%）! 两模型基本一致!
> 原因: FCF/sh $1.76 >> EPS $0.76（**2.3x!** 因 D&A $6.58B + 损失加回 → FCF 远超 NI）; 但 P/FCF 9.09x << PE 8.5x... wait, P/FCF > PE? No: P/FCF=9.09, PE=8.5 → P/FCF > PE by 7% → 部分对冲 FCF>NI → gap 小。
> gap 拆解: ① FCF/sh $1.76 vs EPS $0.76（FCF = NI × 2.3x, D&A + 损失加回）② P/FCF 9.09x vs PE 8.5x（Gordon 略高于框架）③ 净债 −$9.04/sh → 三部分: FCF高 + P/FCF高 = 抬高; 净债 = 压低 → 接近对消 → gap 小
> **DCF FCF $8.49 vs DCF FCF−SBC $6.98**: gap $1.51 → SBC 差异（$947M/5.7B × 9.09 = $0.166 × 9.09 = $1.51 ✓）
> 分红 $9.79B ≈ FCF $10.98B → payout 89% → 净现金 trapped in dividends, 无回购空间

gap 分析:
- gap 1 (EPS→DCF FCF−SBC): $6.98 − $6.46 = **$0.52** → 极小 gap! ① FCF/sh $1.76 vs EPS $0.76（FCF = NI × 2.3x）② P/FCF 9.09x vs PE 8.5x ③ 净债 −$9.04 → 三者接近对消
- gap 2 (DCF FCF−SBC→DCF FCF): $8.49 − $6.98 = **$1.51** → SBC 差异（$0.166 × 9.09 = $1.51 ✓）
- **判断: DCF 与 EPS 基本一致** — gap 仅 $0.52（8%）→ 两模型互相验证, 结论稳健。**PFE 确实深度高估**: DCF $7-8, EPS $6.5, 现价 $26.76 → 均远超。

## D.3 敏感性表

| 情景 | EPS | g | 合理 PE | 合理价 | 满仓目标 (×0.60) |
|------|-----|---|---------|--------|------------------|
| 熊（Eliquis 悬崖兑现, Seagen 减值, g=0%） | $0.76 | 0% | 8.5x | $6.46 | $3.88 |
| **基准（g=0%, COVID 退潮+专利悬崖）** | **$0.76** | **0%** | **8.5x** | **$6.46** | **$3.88** |
| 牛（管线兑现, adj EPS $2.80, g=3%） | $2.80 | 3% | 11.5x | $32.20 | $19.32 |
| 强牛（Seagen 爆发, adj EPS $3.00, g=5%） | $3.00 | 5% | 13.5x | $40.50 | $24.30 |

> 基准 $6.46 vs 现价 $26.76 → 安全边际 −314% → 极端买贵了
> 但: 牛口径用 adj EPS $2.80（旧 base 加回摊销）→ $32 接近现价; 强牛 $40.50 > 现价
> **核心分歧**: GAAP $0.76（保守, Seagen 摊销不剥离）vs adj $2.80（旧 base, 加回摊销）
> 框架 min = $0.76 → 合理价 $6.46 → 极端高估; adj $2.80 → $32 → 接近现价
> 取 min（保守）→ 买贵了（极端）

## D.4 护栏检查

- [✓] 回购不进 g: g=0% 用业务增长, 零回购
- [✓] g 质量: FCF−SBC > 0（$10.04B）
- [✓] 高增长封顶: g=0% < 22%, PE=8.5x 不封顶
- [△] EPS 被 Seagen 摊销压低: $0.76 含重复发生摊销 → 保守但合理（不违反 min）
- [✓] 三重保守: EPS min($0.76) + g 封底(0%) + ×0.60
- [✓] DCF 交叉验: g << r → 不封顶 → 有意义! DCF $7 ≈ EPS $6.5 → 一致

## D.5 质量判定

```
质量判定：好公司（3/7: GM 73.2% + FCF yield 7.2% + FCF−SBC $10.04B；
✗ 4项: NM 6.8% + 零回购 + ROIC 7.5% + 护城河收窄[Eliquis 2028+Seagen失败+COVID退潮]）
× 麻烦存疑（COVID永久退潮 + Eliquis 2028悬崖 + Seagen ADC失败 = 结构性恶化趋向;
非明确一次性, 非一般, 介于存疑与重麻烦之间）
→ 折扣系数 ×0.60（好公司 × 存疑）→ 满仓目标 $3.88
```

> 好价格判定、归类、操作建议不在 D 里——汇总时 join A(price) + D(锚) 算。
