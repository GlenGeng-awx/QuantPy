# SNAP — Task A：价格层（daily）
> 更新: 2026-08-08  现价 $5.33（CSV 2026-08-07 close）  ⚠️ FCF−SBC < 0 → 重麻烦 ×0.40（不否决、合理价照算）

## A.1 价格粗筛 + price-dependent 指标（7 项，满足任意 1 条入池）

| # | 条件 | 阈值 | 实际值 | ✓/✗ |
|---|------|------|--------|-----|
| 1 | 1Y 回撤 | >40% | **41.4%**（高 $9.09 → 现 $5.33，peak-to-current） | ✓ |
| 2 | 2Y 回撤 | >60% | 58.6%（高 $12.86 → 现 $5.33，peak-to-current） | ✗（差 1.4pp） |
| 3 | 距 52W 低 | ≤15% | +35.6%（$5.33 vs 52W 低 $3.93） | ✗ |
| 4 | P/E TTM | <15x | N/A（EPS −$0.18 亏损，无意义） | — |
| 5 | EV/EBITDA | <10x | N/A（EBITDA TTM −$99M 亏损，负值无意义；info.json EV/EBITDA −72.3） | — |
| 6 | P/B | <1.5x | 4.3x（MCap $9.01B / Equity $1.93B；info.json priceToBook 4.34） | ✗ |
| 7 | P/S | <2.0x | **1.42x**（MCap $9.01B / TTM Rev $6.35B；info.json priceToSalesTrailing12Months 1.42） | ✓ |

> 回撤口径统一为 peak-to-current `(1Y_high − current)/1Y_high`（per `mistakes.md` 七·line 197，禁用 peak-to-trough 抬高）。cheap 工具报 45%/61% 系 peak-to-trough，本表用 peak-to-current 41.4%/58.6%。

> N/A 项原因: P/E 与 EV/EBITDA 因 TTM 亏损与 EBITDA 负值失效（非"无数据"）。

**命中: 2/7**（1Y 回撤 + P/S）。EV/EBITDA、P/E 双双 N/A 是亏损公司常态 — 估值锚改用 P/S 分位 + DCF FCF（见 A.2 + A.3）。

FCF yield = TTM FCF $705M / MCap $9.01B = **7.8%**（FCF 表面健康，但 FCF−SBC <0 见 B.3 — 此 yield 含 SBC 幻觉，需打折看）

## A.2 估值分位（web search，月度）

### 自身 P/E 区间 — N/A

| 口径 | 当前 | 5yr 高 | 5yr 低 | 5yr 中位 | 分位 | 来源 |
|------|------|--------|--------|---------|------|------|
| P/E TTM | N/A | N/A | N/A | N/A | N/A | [MacroTrends SNAP PE](https://www.macrotrends.net/stocks/charts/SNAP/snap/pe-ratio)（5yr 全期 EPS 负，PE = 0） |

SNAP 5 年（2021-2026）TTM EPS 全程为负（2021 −$0.89 → 2026 −$0.18），P/E 始终 N/A → 改用 P/S 分位作为亏损股估值锚（per `task_a.md` A.2 亏损股特殊处理）。

### 自身 P/S 区间（亏损股替代锚）

| 口径 | 当前 | 5yr 高 | 5yr 低 | 5yr 中位 | 分位 | 来源 |
|------|------|--------|--------|---------|------|------|
| P/S TTM | **1.42x** | 30.17x（2021-09） | 1.27x（2026-03） | ~3.4x | **~1st %**（0.5%） | [MacroTrends SNAP P/S](https://www.macrotrends.net/stocks/charts/SNAP/snap/price-sales-ratio) |

分位 = (1.42 − 1.27) / (30.17 − 1.27) = 0.15 / 28.90 = **0.52%** ≈ 1st percentile

**≤30% 阈值 → ✓ 通过**（SNAP P/S 处 5 年历史最低位附近）

### 同业对比

| 公司 | P/S | P/E | 性质 | vs SNAP |
|------|-----|-----|------|---------|
| SNAP | 1.42x | N/A（亏损） | 年轻用户社交 + AR/相机 + 订阅 | — |
| PINS | 3.67x | N/A（小幅盈利） | 类比广告社交 | PINS **溢价 +158%** |
| META | ~7.7x | 19.92x | 巨头社交广告 | META 溢价 +446%（GM 82% NM 35% 不可比，仅参照方向） |

来源: [MacroTrends SNAP PE](https://www.macrotrends.net/stocks/charts/SNAP/snap/pe-ratio)、[MacroTrends PINS P/S](https://www.macrotrends.net/stocks/charts/PINS/pinterest/price-sales-ratio)

> 剔除性质不可比者: META GM 82% NM 35% — 巨头规模效应、SBC/Rev 2.5%（vs SNAP 16.2%）属不同量级公司，仅作方向参照。PINS 是 SNAP 最可比同业（同为年轻/视觉导向社交广告，规模相近）。

### de-rating 判断

SNAP P/S 从 30.17x（2021-09，COVID hypergrowth 巅峰）→ 1.27-1.48x（2026）= **−95% de-rating**。便宜成因两部分:

1. **范式切换**（约一半）: COVID 期间成长股溢价（P/S 30x）→ 2022 估值范式切换（P/S 4x）→ 持续降级。这部分是泡沫破裂，非错杀
2. **真实恶化**（另一半）: NA DAU −7% YoY（2025）、广告仅 +3%、FCF−SBC <0、累计亏损扩大、SBC 全标的最高。这部分是真实结构性恶化

**当前 P/S 1.4x 处历史最低位**（5yr 分位 1%）— 下行空间有限。但 P/S 低分位对亏损公司不是便宜的同义词（无盈利支撑的 P/S 1.4x 仍可能价值陷阱）。**呼应 Task B/C**: FCF−SBC<0 + GM<60% + 10 年亏损 → P/S 1.4x 的"便宜"在五步框架下需要 ×0.40 折扣 + DCF FCF 验证（见 A.3）。

绿芽（Q2'26 NA DAU 持平、广告 +9%、Snapchat+ +85%）部分对冲"真实恶化"叙事，但未改变 FCF−SBC<0 的硬规则触发。

## A.3 安全边际（join D 的锚）

| 口径 | 值 | 来源 |
|------|-----|------|
| 现价 | **$5.33** | stock_data/SNAP_1d.csv 2026-08-07 close |
| 合理价（DCF FCF 上限） | **$11.61** | from D.2b（base $0.418 × P/FCF 30x + net_cash/sh −$0.93；g=9% capped，r=11%） |
| 满仓目标 | **$4.64** | from D.2（$11.61 × ×0.40 重麻烦折扣） |
| **安全边际** | **+54.1%** | 1 − 5.33/11.61 = +0.541 |

> 安全边际符号: 现价 $5.33 < 合理价 $11.61 → **正**（便宜 vs DCF FCF 上限）。per `mistakes.md` 一·line 33，禁现价低于合理价却写负号。

> 合理价 $11.61 是 DCF FCF 口径（乐观上限）— EPS 模型 N/A（恢复 EPS −$0.18 × 17.5 = −$3.15 负值）、DCF FCF−SBC N/A（base 负）。三口径体系中仅 DCF FCF 可用，详见 `output_d.md` D.2b。这是 SNAP 边界 case — 合理价区间退化为单点。

### 操作建议（通用逻辑）

| 现价位置 | 操作 |
|---------|------|
| ≤ 满仓 $4.64 | 满仓建仓 |
| **满仓 $4.64 < 现价 $5.33 < 合理价 $11.61** | **小仓/观察** |
| ≥ 合理价 $11.61 | 不出手，等回调 |

→ **当前: 小仓/观察**（满仓目标在现价下方 ~13%，需再跌至 $4.64 以下才考虑加仓至满仓位）

## 结论

**入池: ✓**（2/7 粗筛 + P/S 分位 1st % + DCF 安全边际 +54.1%）

但:
- **FCF − SBC = −$325M < 0 → 重麻烦 ×0.40**（硬规则触发，合理价照算）
- EPS 模型 N/A、DCF FCF−SBC N/A，仅 DCF FCF 单口径可估值（边界 case）
- 满仓目标 $4.64 在现价 $5.33 下方 → 不满仓，仅小仓/观察

**归类: 价值陷阱（赌反转，≤小仓）** — P/S 1st percentile 历史最低 + DCF 安全边际 +54% 表面便宜，但 GM<60% + 10 年从未 GAAP 持续盈利 + FCF−SBC<0 + 累计亏损 −$14.8B = 便宜无盈利/资产支撑（"便宜的烂公司"特征）。绿芽真实（Q2'26 NA DAU 止跌、广告 +9%、Snapchat+ +85%、FY27 GAAP EPS 转正共识 +$0.12）= 反转候选，但未坐实 → 价值陷阱当前态 + 赌反转期权。类比 `discount_coefficient.md` INTC 案例（平庸 + 重麻烦 → ×0.40 → ≤小仓不对称投机）。

**重估前提**: 连续 4 季 GAAP 盈利 + SBC/Rev <10% + 北美 DAU 回升 — 若 2-3 季内坐实盈利拐点（FY27 共识 EPS +$0.12 已在前瞻中），可脱离"陷阱"重看；否则维持小仓/观察。

**与 LI 区别**: LI 净现金 88% 市值锁下行（困境反转期权）；SNAP 净负债 −$1.57B、有形净资产 ≈$0 → 下行无底，但 DCF FCF +54% 安全边际 + 持续 FCF 改善 = 不绝对回避，保留小仓席位。
