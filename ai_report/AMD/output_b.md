# AMD — Task B：财务健康 + 正常化 EPS
> 更新: 2026-08-06（财报 FY26 Q1，2026-05-05 发；下次 Q2 ~2026-08）  ⚠️ 周期股

## B.1 SCORECARD 九宫格

| 维度 | 3yr | TTM | 5Q |
|------|-----|-----|-----|
| Income | 100 | 100 | 92 |
| CF | 100 | 90 | 100 |
| BS | 82 | 100 | 100 |

权重: Income 25% / CF 35% / BS 40%

### 背离检验

| 维度×窗口 | SCORECARD 说 | 原始财报 | 背离方向 |
|------|------|------|------|
| Income 5Q=92 | GM Q YoY 微降 68.6%→67.2% | **轻度误伤**：GM 稳 50-54%（GAAP），波动系 MI308 减值一次性 | **噪声** |
| 全部高分 | 营收/OpInc/FCF 全面加速 | **证实但需正常化**：GAAP NI 被 Xilinx 无形摊销 ~$1B/季压低 → GAAP EPS 偏低 | **低估贵反向**（GAAP 偏低 → 正常化后更贵） |

伤口模式: **无伤口**。高分健康 + 高分股价 = 买贵了典型。AI 数据中心狂热中 YTD +152%。

## B.2 利润表逐季（GAAP）

```
          Rev     GM%    OpInc   OpM%    NI      EPS     dilShares
Q1'25  7.44B   50.3%   806M    10.8%   709M    0.44    1.63B
Q2'25  7.68B   39.8%  -134M    -1.7%   872M    0.54    1.63B   ← MI308 减值 ~$800M
Q3'25  9.25B   51.7%  1.27B    13.7%  1.24B    0.75    1.64B
Q4'25 10.27B   54.3%  1.75B    17.0%  1.51B    0.92    1.65B
Q1'26 10.25B   52.8%  1.48B    14.4%  1.38B    0.84    1.65B   ← 最新
```

- **营收 Q1'26 +37.8% YoY**——数据中心引擎猛
- **GAAP GM ~50-54%**（非 GAAP ~56%）——半导体中等，远低于 NVDA 75%
- **GAAP OpM 仅 10-17%**——Xilinx 无形摊销 ~$1B/季吃掉利润，非 GAAP OpM ~35%
- Q2'25 MI308 对华禁运 ~$800M 减值（一次性坑）
- 税率异常：Q2'25 税收 −$834M（递延税收益）扭曲当季 NI
- dilShares 1.63B→1.65B（微增，回购仅对冲 SBC）

## B.3 现金流

| 项目 | TTM | 说明 |
|------|-----|------|
| OCF | $9.72B（3yr +153%） | 真实改善；OCF/NI 1.94（GAAP NI 被摊销压低所致） |
| FCF | $8.57B | CapEx $1.15B（12% OCF）；yield 见 A（1.1%） |
| SBC | $1.76B（SBC/Rev 4.7%，下降中） | 中等 |
| 回购 | $1.50B | 仅对冲 SBC，未真缩股 |
| 分红 | $0 | 零分红；Net Return = **−$262M**（回购 − SBC = 净稀释） |
| 净现金 | $8.48B | 现金 $12.35B − 总债 $3.87B |

FCF − SBC = 8.57 − 1.76 = **$6.81B > 0**（合格）

⚠ 回购仅对冲 SBC，Net Return −$262M = 净稀释。FCF yield 1.1% = 好价格证据完全缺失。

## B.4 资产负债表（bs_quarterly 2026-03-31）

| 项目 | 值 | 说明 |
|------|-----|------|
| 现金+短投 | $12.35B | Cash $5.58B + 短投 $6.76B |
| 总债 | $3.87B | 长期 $2.35B + 短期 $874M + 租赁 $647M |
| 净现金 | $8.48B | 温和（Cash/Debt 3.19x） |
| D/E | 0.06 | $3.87B / $64.46B（极低杠杆） |
| Goodwill | $41.50B | Assets 52.1%（Xilinx 收购累积，高但稳定） |
| Retained Earnings | $8.08B | 从 FY22 −$131M 回填 |
| Stockholders Equity | $64.46B | BV/share ~$39.5 |
| **利息覆盖** | **29.5x** | $4.36B OpInc / $148M Interest；>5x ✓ |

> BS 强：净现金 $8.48B、D/E 0.06、利息覆盖 29.5x。Goodwill 52% 是 Xilinx 收购遗留（$25.3B GW + $16.2B 无形），但占比在下降（54%→52%）。

## B.5 正常化 EPS Chain

| 口径 | EPS | 来源 |
|------|-----|------|
| GAAP | $3.05 | Diluted EPS (income_ttm, 2026-03-31) |
| 工具 | $2.78 | Normalized Income $4.57B / 1.64B shares |
| v3.1 | $2.68 | detector 2c TaxAnomaly + 2h Discontinued + 2x Unusual |
| **FINAL** | **$2.68** | **min(三者)** |

- winner: v3.1
- adj: −12%（$3.05 → $2.68）
- detectors: 2c TaxAnomaly（$799M after-tax，TTM 税率 0.2% vs 历史 −16%）+ 2h Discontinued（$77M）+ 2x Unusual（$366M pretax）

> ⚠ 旧分析用 $5.13（非 GAAP，加回 Xilinx 摊销 ~$3.4B 税后）。框架 min 规则不回加摊销 → FINAL = $2.68。差异 48%。周期股用中周期 EPS（见 output_d），非 TTM min。

### GAAP vs 非 GAAP 背离

- Xilinx 收购无形摊销 ~$1B/季 ≈ $4B/年（税前）跑进 GAAP
- Q1'26: GAAP EPS $0.84 vs 非 GAAP $1.37（[AMD IR](https://ir.amd.com/news-events/press-releases/detail/1284/amd-reports-first-quarter-2026-financial-results)）
- 框架立场：摊销是 GAAP 成本（虽非现金），min 规则不回加 → 用 $2.68

## B.6 质量地板（给 Task D 预判）

| 指标 | 值 | ✓/✗ |
|------|-----|-----|
| GM >60% 稳 | 50.3%（GAAP TTM；3yr 46%→49%→50% 改善但 <60%） | ✗ |
| NM >20% | 13.4% | ✗ |
| FCF yield >5% | 1.1% | ✗ |
| FCF−SBC >0 | $6.81B | ✓ |
| 真缩股 | 1.57B→1.64B（3yr +4.5% 稀释） | ✗ |
| ROIC >15% 或 ROE >15% | ROIC 7.8% / ROE 8.1% | ✗ |

本地评分: 1/6（仅 FCF−SBC ✓，其余 5 项全 ✗）+ 护城河中等（不加）= 1/7 = **平庸**

> ⚠ 旧 output_b 误标 ROIC ✓*（实际 7.8% <15%），已修正 → 评分从 2/6 降至 1/6。GAAP 指标被 Xilinx 摊销压低（非 GAAP GM 56%/NM 25% 更高），但框架用 GAAP → 1/7 平庸。BS 强（净现金 $8.48B、利息覆盖 29.5x）但盈利质量指标（GM/NM/ROIC）均不达标。
