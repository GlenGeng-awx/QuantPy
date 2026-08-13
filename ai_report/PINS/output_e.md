# PINS — Task E：决策
> 更新: 2026-08-08  现价 $23.68

## E.1 粗筛信号（from A）

| # | 条件 | 阈值 | 实际值 | ✓/✗ |
|---|------|------|--------|-----|
| 1 | 1Y 回撤 | >40% | 40.6%（高 $39.2 → 低 $23.3） | ✓（边缘） |
| 2 | 2Y 回撤 | >60% | 41.8%（高 $40.0 → 低 $23.3） | ✗ |
| 3 | 距 52W 低 | ≤15% | +54%（$23.7 vs 低 $15.4） | ✗ |
| 4 | P/E TTM | <15x | 67.7x（P=$23.68, E=$0.35 screen） | ✗ |
| 5 | EV/EBITDA | <10x | 42.1x（EV=$13.33B, EBITDA=$317M） | ✗ |
| 6 | P/B | <1.5x | 4.6x | —（轻资产: GM 79.5% > 60%，P/B 不适用） |
| 7 | P/S | <2.0x | 2.9x（NM 5.5% < 25% → 不放宽至 4.0x） | ✗ |

命中: 1/7（1Y 回撤 40.6%，边缘）

FCF yield = $1.28B / $13.41B = **9.5%**
FCF−SBC yield = $0.26B / $13.41B = **1.9%**（SBC 吃 80% FCF）

> P/E 67.7x 被 SBC $1.02B（22% Rev）压低利润。屏幕 E $0.35（info.json trailingEps）vs CSV Diluted EPS $0.34，差 2.9% < 3%，口径对齐。

## E.2 估值锚（from D）

| 口径 | 值 |
|------|-----|
| 合理价 | $7.99（$0.34 × 23.5x） |
| 满仓目标 | $5.35（×0.67） |
| 系数 | ×0.67（好公司×一般） |
| g | 15.0% |
| 合理 PE | 23.5x |
| 正常化 EPS | $0.34 |
| GAAP EPS | $0.34 |
| FCF/sh | $1.99 |
| FCF−SBC/sh | $0.41 |
| r | 10.0% |
| P/FCF₀ | 30.0x |
| DCF FCF−SBC | $12.27 |
| DCF FCF | $59.93 |
| 质量×麻烦 | 好公司×一般 |

## E.3 安全边际 + 操作（join A price + D anchor）

| 口径 | 合理价 | 安全边际 | 满仓 | 操作 |
|------|--------|---------|------|------|
| EPS 模型 | $7.99 | -196.0% | $5.35 | 小仓/观察 |
| DCF FCF | $59.93 | +60.5% | — | — |
| DCF FCF−SBC | $12.27 | -93.0% | — | — |

## E.4 归类
小仓/观察

## E.5 双分位（from A）

### 自身 P/E 区间

| 口径 | 当前 | 5yr 高 | 5yr 低 | 5yr 中位 | 分位 | 来源 |
|------|------|--------|--------|---------|------|------|
| 正常化 P/E | 69.6x（$23.68/$0.34） | 332.9x（Q3'22, near-zero EPS） | 10.9x（Q4'24, 税收益膨胀 EPS） | — | **⚠ 无意义** | [MacroTrends](https://www.macrotrends.net/stocks/charts/PINS/pinterest/pe-ratio) |
| P/S | 2.94x | 13.57x（Q3'21, IPO 泡沫） | 2.84x（Q1'26） | ~6.3x | **~1st** | [MacroTrends P/S](https://www.macrotrends.net/stocks/charts/PINS/pinterest/price-sales) |

**⚠ P/E 5yr 分位无意义**：
- 2022-2023 全年亏损 → P/E = 0/N/A
- 2024 Q4 P/E 10.9x = $1.57B 递延税备抵转回（一次性）膨胀 EPS $2.67 → 假低 P/E
- 2025 H2 P/E 11-13x = 税收益 TTM 滚动期 → 仍含一次性
- 2026 P/E 38-70x = 税收益 roll-off 后 GAAP EPS 回落至 $0.34-0.61 → SBC 压低 → P/E 飙高
- 分位 18.3% 看似 ≤30%，但高/低均被一次性扭曲 → **严禁用此判便宜**

**P/S 5yr 分位 ~1st ≤30% ✓**：但需打折看——高 13.57x 来自 2021 IPO 泡沫（PINS IPO $19 → 峰值 $89），低 2.84x 来自收入增长 $2.58B→$4.56B（+77%）跑赢市值缩水。部分是范式切换（hypergrowth → mature），非纯错杀。

### 同业对比

| 公司 | P/E (TTM) | P/S (TTM) | GM% | 性质 | vs PINS |
|------|-----------|-----------|-----|------|---------|
| **PINS** | 67.7x | 2.9x | 79.5% | 视觉发现，下漏斗购物 | — |
| META | 22.2x | 6.6x | 81.7% | 社交广告龙头，规模+AI | P/S 折 56% |
| GOOG | 17.9x | 9.7x | 60.9% | 搜索+YouTube，最宽护城河 | P/S 折 70% |
| SNAP | N/A（亏损） | 1.4x | 57.3% | 更小、变现更弱 | P/S 溢 107% |

来源: 本地 info.json（2026-08-07 close）; [MacroTrends PINS P/E](https://www.macrotrends.net/stocks/charts/PINS/pinterest/pe-ratio)

PINS P/S 显著低于 META/GOOG——反映**规模小（MCap $13B vs META $1492B）、被 AI 搜索/TikTok 视觉搜索威胁、广告定价弱、SBC 22% 压低利润**的折价。相对便宜有其理由，非纯错杀。SNAP 更便宜但亏损（GM 57% < 60%，无盈利）。

### de-rating 判断

P/E de-rating 是**结构性**的（SBC 22% 永久压低 GAAP EPS），非一次性范式切换。P/S de-rating 部分是 IPO 泡沫破裂（2021 P/S 13-23x → 2026 P/S 2.9x），部分是真实（收入 CAGR 14.7% 跑赢市值缩水）。**"便宜"在 P/S 端真实，在 P/E 端无意义。FCF yield 9.5% 是最有利的口径（P/FCF ~10.5x 对 15% 增速合理），但 FCF−SBC yield 仅 1.9%（P/FCF−SBC 53x → 贵）。**
