# SNAP — Task A：价格层（daily）
> 更新: 2026-08-08  现价 $5.33（CSV 2026-08-07 close）  ⚠️ FCF−SBC < 0 → 重麻烦 ×0.40（不否决、合理价照算）

## A.1 价格粗筛 + price-dependent 指标（8 项，满足任意 1 条入池）

| # | 条件 | 阈值 | 实际值 | ✓/✗ |
|---|------|------|--------|-----|
| 1 | 1Y 回撤 | >40% | **41.4%**（高 $9.09 → 现 $5.33，peak-to-current） | **✓** |
| 2 | 2Y 回撤 | >60% | 58.6%（高 $12.86 → 现 $5.33，peak-to-current） | ✗ |
| 3 | 距 52W 低 | ≤15% | +35.6%（$5.33 vs 52W 低 $3.93） | ✗ |
| 4 | P/E TTM | <15x | N/A（EPS −$0.18 亏损） | ✗ |
| 5 | FCF yield | >5% | **7.8%**（$705M FCF / $9.01B MCap；⚠ FCF−SBC<0 → yield 含 SBC 幻觉） | **✓** |
| 6 | EV/EBITDA | <10x | N/A（EBITDA 负） | ✗ |
| 7 | P/B | <1.5x | 4.3x | ✗ |
| 8 | P/S | <2.0x | **1.42x** | **✓** |

命中: **3/8**（1Y 回撤 + FCF yield + P/S）

> 回撤口径 peak-to-current。cheap 工具报 45%/61% 系 peak-to-trough。

## A.2 估值分位（web search，月度）

| 口径 | 当前 | 5yr 高 | 5yr 低 | 5yr 中位 | 分位 | 来源 |
|------|------|--------|--------|---------|------|------|
| GAAP P/E | N/A（负） | — | — | — | **暂停** ✗ | EPS 贯穿负（5yr 全期） |
| 正常化 P/E | N/A（负） | — | — | — | **暂停** ✗ | 恢复 EPS 负 |

> **双分位暂停**（EPS 贯穿负 → P/E 无意义，严禁估算）。P/S 1.42x 处 5yr ~1st 分位（仅作补充参考）。

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
