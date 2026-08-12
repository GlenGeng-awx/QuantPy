# JNJ — Task A：价格层（daily）
> 更新: 2026-08-08  现价 $259.24（2026-08-07 close）　货币: USD

## A.1 价格粗筛 + price-dependent 指标（8 项, 满足任意 1 条入池）

| # | 条件 | 阈值 | 实际值 | ✓/✗ |
|---|------|------|--------|-----|
| 1 | 1Y 回撤 | >40% | 3.0% (high $267.24 → $259.24) | ✗ |
| 2 | 2Y 回撤 | >60% | 3.0% | ✗ |
| 3 | 距 52W 低 | ≤15% | +54.9% ($259.24 vs low $167.35) | ✗ |
| 4 | P/E TTM | <15x | 29.9x ($259.24/$8.68 GAAP) | ✗ |
| 5 | FCF yield | >5% | 3.6% (FCF $22.23B / MCap $624.74B) | ✗ |
| 6 | EV/EBITDA | <10x | 18.7x | ✗ |
| 7 | P/B | <1.5x | 7.3x | ✗ |
| 8 | P/S | <2.0x | 6.4x | ✗ |

命中: **0/8**。股价新高附近，全维度贵。

> JNJ 现价 $259.24 接近历史新高（1Y high $267.24, 回撤仅 3%）, 距 52 周低 +55%。全维度贵: P/E 30x / EV/EBITDA 18.7x / P/B 7.3x / P/S 6.4x。非"下跌的好公司"猎场。

FCF yield = FCF $22.23B / MCap $624.74B = **3.6%**（<5%, "贵"的直接证据）

## A.2 估值分位

### 双分位

| 口径 | 当前 | 5yr 高 | 5yr 低 | 分位 | 来源 |
|------|------|--------|--------|------|------|
| GAAP P/E | 29.9x | 30.8x (2023-06) | 9.2x (2024-06) | 97th ✗ | MacroTrends |
| 正常化 P/E | 39.2x（$259.24/$6.61） | 30.8x | 9.2x | >100th ✗ | MacroTrends + B v3.1 |

> 双分位未通过（GAAP 97th ✗ + 正常化 >100th ✗）。P/E 波动大因 GAAP EPS 受 Kenvue 分拆/talc 计提/一次性收益扭曲。正常化 P/E 39x 更贵（min EPS $6.61）。

### 同业对比

| 公司 | P/E | 性质 | vs JNJ |
|------|-----|------|--------|
| **JNJ** | **30.1x** | 药+medtech, AAA, dividend king | 基准 |
| LLY | 37.9x | GLP-1 超高成长（性质不可比） | JNJ 便宜 −21% |
| MRK | 40.0x | Keytruda 专利悬崖, 深度折价反升 | JNJ 便宜 −25% |
| ABBV | 22.4x | Humira 悬崖后恢复 | JNJ 贵 +34% |
| NVS | 17.8x | 瑞士大药企 | JNJ 贵 +69% |
| NVO | 11.4x | GLP-1 估值回落 | JNJ 贵 +164% |
| PFE | 8.6x | 新冠退潮, 深度折价 | JNJ 贵 +250% |
| SNY | 8.8x | 法国大药企 | JNJ 贵 +242% |

> 来源: MacroTrends 同业对比表 https://www.macrotrends.net/stocks/charts/JNJ/johnson-johnson/pe-ratio
> JNJ 在大药企里**偏高端**（仅次于 LLY/MRK 的成长/折价故事）。同业多在 8-18x, JNJ 30x 溢价 = 为 AAA + dividend king + 多元化 durability 付费。

### de-rating 判断

**非 de-rating, 是 re-rating**: 市场把 JNJ 从"低增长价值股（15-18x, 2025 中）"重估到"新药周期成长 + AAA 避险资产（28-30x, 2026）"。溢价含: ① AAA 信用"比国债更安全"避险资金涌入 ② FY26 破 $100B 新药周期 ③ dividend king durability ④ Q2'26 beat+raise。
**框架不付此溢价**: 质量只进折扣系数（×0.67）, 不抬 PE。故结论必然是"买贵了"。
