# WMT — Task A：价格层（daily）
> 更新: 2026-08-09  现价 $111.85（2026-08-07 收盘）

## A.1 价格粗筛 + price-dependent 指标（8 项，满足任意 1 条入池）

| # | 条件 | 阈值 | 实际值 | ✓/✗ |
|---|------|------|--------|-----|
| 1 | 1Y 回撤 | >40% | 18% | ✗ |
| 2 | 2Y 回撤 | >60% | 18% | ✗ |
| 3 | 距 52W 低 | ≤15% | +17% | ✗ |
| 4 | P/E TTM | <15x | 39.4x（GAAP）/ 42.9x（正常化 $2.609） | ✗ |
| 5 | FCF yield | >5% | 1.41%（$12.55B FCF / $890.11B MCap） | ✗ |
| 6 | EV/EBITDA | <10x | 21.4x | ✗ |
| 7 | P/B | <1.5x | 9.4x | ✗ |
| 8 | P/S | <2.0x | 1.2x | **✓** |

命中: **1/8**（仅 P/S，零售薄利结构性低非便宜信号）

## A.2 估值分位

### 自身 P/E 区间（5yr，MacroTrends 季度数据）

| 口径 | 当前 | 5yr 高 | 5yr 低 | 5yr 中位 | 分位 | 来源 |
|------|------|--------|--------|---------|------|------|
| GAAP P/E | 39.38x | 48.85x | 24.92x | 35.08x | **60.4th** ✗ | [MacroTrends](https://www.macrotrends.net/stocks/charts/WMT/walmart/pe-ratio) |
| 正常化 P/E | 42.87x（$111.85/$2.609） | 48.85x | 24.92x | 35.08x | **75.0th** ✗ | 同 GAAP 5yr 区间 |

> **双分位均 >30% → 不通过。** WMT 被 re-rate 上修（广告/会员/AI 叙事），当前 60-75th 是新 regime 内高位。

### 同业对比（2026-08-07，MacroTrends P/E）

| 公司 | P/E | 性质 | vs WMT |
|------|-----|------|--------|
| COST | 47.68x | 会员仓储零售，规模+会员护城河（同 WMT Sam's） | WMT 折 17.4%（更便宜） |
| **WMT** | **39.38x** | 全球最大零售商 + 广告/会员高 margin | — |
| TGT | 19.78x | 传统综合零售，未 re-rate 到 WMT 程度（Jan26 12.72x → Aug 19.78x，部分 re-rate） | WMT 溢 99.1% |
| KR | 11.46x | 纯杂货零售，无广告/会员引擎 | WMT 溢 243.6% |

> WMT 在传统零售里**最贵**（仅低于 COST）。COST/WMT 的 re-rate 溢价来自"零售 + 广告/会员高 margin + AI"叙事；TGT/KR 无此溢价。来源: macrotrends.net（COST/TGT/KR 各自 pe-ratio 页）

### de-rating 判断

**WMT 不是被 de-rate，是被 re-rate 上修**:
- 2024-04 P/E 24.92x（5yr 低，"旧 regime"——纯零售估值）
- 2025-01 P/E 40.18x（re-rate 起步——Walmart Connect 广告 + 会员 + margin mix 叙事）
- 2026-04 P/E 46.37x（re-rate 顶峰——AI + 自动化叙事加持）
- 2026-08 P/E 39.38x（回调 15%——Oppenheimer 降级 + UBS Q2 放缓预警）

**当前 60th 分位 ≠ 便宜**: 
- 5yr 低 24.92x 是 re-rate **前**的"旧 regime"估值（纯零售 25-30x）
- 当前 39.38x 是 re-rate **后**回调，仍在新 regime 区间（35-46x），非回归旧 regime
- 近期回调（46.37 → 39.38）是**新 regime 内的正常波动**，非 de-rating 回归历史
- 市场为"防御 + 广告/AI re-rate"付满价，**非错杀**

呼应 Task B/C: GM 稳 25%、NM 3.1% 薄（零售本质未变）、广告 +44% + 会员 +17.4% 支撑 re-rate 叙事但增速若回落则溢价逆转风险大。
