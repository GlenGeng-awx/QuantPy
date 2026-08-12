# CRCL — Task A：价格层（daily）
> 更新: 2026-08-07  现价 $66.67  ⚠️ 新近 IPO（2025-06-05，<1yr 公开数据）

## A.1 价格粗筛 + price-dependent 指标（8 项，满足任意 1 条入池）

| # | 条件 | 阈值 | 实际值 | ✓/✗ |
|---|------|------|--------|-----|
| 1 | 1Y 回撤 | >40% | **63%**（高 $163.21 → 现 $66.67，peak-to-current） | ✓ |
| 2 | 2Y 回撤 | >60% | N/A（IPO 2025-06，<2yr 数据） | — |
| 3 | 距 52W 低 | ≤15% | 33%（$66.67 vs 低 $50.23，CSV 252d low） | ✗ |
| 4 | P/E TTM | <15x | N/A（CSV Diluted EPS −$0.23 负值；info.json trailingEps $5.26 pro forma 不可信） | ✗ |
| 5 | FCF yield | >5% | 2.5%（FCF $446M / MCap $18.17B） | ✗ |
| 6 | EV/EBITDA | <10x | N/A（EBITDA −$45.6M 负值） | ✗ |
| 7 | P/B | <1.5x | 4.8x（BV $13.88） | ✗ |
| 8 | P/S | <2.0x | 6.3x（MCap $18.17B / Rev $2.86B） | ✗ |

命中: **1/8**（仅 1Y 回撤 63%）。弱入池信号。距 52W 低 +33%（非底部）。P/S 6.3x 极贵（对利率敏感型金融业务）。

> ⚠ **info.json trailingEps $5.26 ≠ CSV Diluted EPS −$0.23**：IPO 公司 info.json 用 pro forma/调整后 EPS（含 IPO 前追溯调整），与 CSV GAAP TTM Diluted EPS 矛盾。**框架用 CSV GAAP EPS = −$0.23 → P/E N/A**。cheap 工具用 info.json → P/E 12.7x ✓ 是错的。
>
> **EV/EBITDA N/A**：EBITDA −$45.6M（负，TTM 含 Q2'25 IPO 巨亏）。info.json EV/EBITDA 66.5x 用绝对值，但 EBITDA 负 → 无意义 → N/A。

FCF yield = $446M / $18.17B = **2.5%**

## A.2 估值分位

### 双分位（暂停 — EPS 负值 + IPO <1yr）

| 口径 | 当前 | 5yr 高 | 5yr 低 | 分位 | 来源 |
|------|------|--------|--------|------|------|
| GAAP P/E TTM | N/A | — | — | — | EPS 负，P/E 不适用 |
| 正常化 P/E | N/A | — | — | — | 恢复 EPS $1.20 → P/E 56x，IPO <1yr 无 5yr 序列 |

> **双分位暂停**：TTM GAAP EPS −$0.23（负）→ P/E N/A。CRCL IPO 2025-06，<1yr 公开历史 → 无 5yr P/E 区间。per 框架硬规则"查不到则暂停，严禁估算"。

### 自身 P/S 区间（IPO 至今，<1yr）

| 口径 | 当前 | IPO 高 | IPO 低 | 说明 |
|------|------|--------|--------|------|
| P/S | 6.3x | ~12x（IPO 首日 $263） | ~3x（低点 ~$50） | 距 IPO 高点回落 48%，但仍 6.3x（贵） |

### 正常化 P/E（用恢复 EPS）

| 口径 | 当前 | 说明 |
|------|------|------|
| GAAP P/E | N/A | TTM EPS −$0.23（负值） |
| 恢复 P/E | 55.6x（$66.67 / $1.20 恢复 EPS） | 极高 |

### 同业对比（稳定币 / 加密金融）

| 公司 | P/S | P/B | 性质 | vs CRCL |
|------|-----|-----|------|---------|
| **CRCL** | **6.3x** | **4.8x** | 稳定币发行人（利率敏感） | — |
| COIN | ~6.7x | ~3.1x | 加密交易所（周期） | CRCL P/S 略低 |
| PYPL | ~4.0x | ~3.0x | 多元支付（成熟） | CRCL 更贵 |
| 传统金融 | 1-2x | ~1x | 银行/券商 | CRCL 3-6x 更贵 |

CRCL P/S 6.3x 与 COIN 类似定位在"加密周期金融股"，但远高于传统金融。市场给了"稳定币 AUM 增长 + 监管护城河"溢价。

### de-rating 判断

1Y 回撤 63% = IPO 定价在利率顶部 → Fed 降息现实 → 营收压缩预期。P/S 从 IPO ~12x 降至 6.3x = de-rating 已发生。但 6.3x 仍是成长溢价（对利率敏感型业务非纯错杀，de-rating 部分合理 + 部分未到位）。
