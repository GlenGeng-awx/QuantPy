# XYZ — Task A：价格层（daily）
> 更新: 2026-08-09  现价 $79.00（CSV 2026-08-07 close）

## A.1 价格粗筛 + price-dependent 指标（8 项，满足任意 1 条入池）

| # | 条件 | 阈值 | 实际值 | ✓/✗ |
|---|------|------|--------|-----|
| 1 | 1Y 回撤 | >40% | 6.7% | ✗ |
| 2 | 2Y 回撤 | >60% | 20.1% | ✗ |
| 3 | 距 52W 低 | ≤15% | +61% | ✗ |
| 4 | P/E TTM | <15x | 141.1x（GAAP $0.56 被 BTC MTM+重组压低，失真） | ✗ |
| 5 | FCF yield | >5% | **8.2%**（$3.88B FCF / $47.46B MCap） | **✓** |
| 6 | EV/EBITDA | <10x | 30.9x | ✗ |
| 7 | P/B | <1.5x | 2.1x | ✗ |
| 8 | P/S | <2.0x | 1.9x | **✓** |

命中: **2/8**（FCF yield + P/S；⚠ P/S 假便宜——BTC 毛记账，真实 P/GP 4.1x）

## A.2 估值分位

### 自身 P/E 区间

| 口径 | 当前 | 5yr 高 | 5yr 低 | 5yr 中位 | 分位 | 来源 |
|------|------|--------|--------|---------|------|------|
| GAAP P/E | 141.1x | 3867.5x（EPS $0.02） | 0x（亏损） | — | **暂停** ✗ | EPS near-zero 剧烈摆动，分母塌陷 |
| 正常化 P/E | 141.1x（$79/$0.56） | 3867.5x | 0x | — | **暂停** ✗ | 同 GAAP（v3.1 ≈ GAAP） |

> **双分位暂停**（EPS near-zero → P/E 无意义，严禁估算）。改用 P/GP 4.1x + 前瞻 adj P/E 19.7x + FCF yield 8.2% 交叉验。

### 替代估值口径

| 口径 | 当前值 | 说明 |
|------|--------|------|
| P/GP | 4.1x（$47.46B / $11.61B） | 价/毛利润（剔除 BTC 毛记账失真） |
| 前瞻 adj P/E | 19.7x（$79 / FY26 adj EPS $4.02 guide） | 管理层指引口径 |
| 前瞻 NTM P/E | ~17x | [TIKR](https://www.tikr.com/blog/block-stock-fell-6-after-its-most-profitable-quarter-ever-heres-where-xyz-could-go-in-2026) |
| FCF yield | 8.2% | $3.88B / $47.46B |

### 同业对比

| 公司 | 前瞻 P/E | 性质 | vs XYZ |
|------|---------|------|--------|
| **XYZ** | adj ~19.7x | 转型中、NM 1.4% 薄、FCF yield 8.2% | — |
| PYPL | ~12x | 更便宜、GM 下滑、FCF yield ~16% | XYZ 溢价 64% |
| Diversified Financials 行业中位 | ~15x | [SimplyWallSt](https://simplywall.st/stocks/us/diversified-financials/nyse-xyz/block/news/block-sq-stock-valuation-after-q1-beat-raised-2026-outlook-a) | XYZ 溢价 ~32%（adj 口径） |

XYZ adj P/E 19.7x 相对 GP +21% 增速不算离谱（PEG ~0.94），但**相对 PYPL（12x）有溢价**，且 XYZ 无 PYPL 的规模护城河、NM 更薄。

### de-rating 判断

XYZ 从 2021 泡沫高点（$280+）跌去 ~72%，是"高增长小盈利→薄盈利"范式切换 + BTC 叙事退潮，**大部分 de-rating 合理**（当年溢价来自 BTC/成长泡沫）。现价 $79 已从 52w 低 $49 反弹 +61%，YTD +21%，**近 52w 高点**（距高 $84.64 仅 −6.7%）。Q2'26 beat 后 sell-the-news 跌 6%，但**不在低位**。**非困境反转标的**——便宜已被市场消化。
