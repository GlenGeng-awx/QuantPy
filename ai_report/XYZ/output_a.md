# XYZ — Task A：价格层（daily）
> 更新: 2026-08-09  现价 $79.00（CSV 2026-08-07 close）

## A.1 价格粗筛 + price-dependent 指标（7 项，满足任意 1 条入池）

| # | 条件 | 阈值 | 实际值 | ✓/✗ |
|---|------|------|--------|-----|
| 1 | 1Y 回撤 | >40% | 6.7%（252d 高 $84.64） | ✗ |
| 2 | 2Y 回撤 | >60% | 20.1%（504d 高 $98.92） | ✗ |
| 3 | 距 52W 低 | ≤15% | +61%（$79.00 vs 低 $49.09） | ✗ |
| 4 | P/E TTM | <15x | 141.1x（E=$0.56 GAAP，被 BTC MTM+重组压低，失真） | ✗ |
| 5 | EV/EBITDA | <10x | 30.9x | ✗ |
| 6 | P/B | <1.5x | 2.1x | ✗ |
| 7 | P/S | <2.0x | 1.9x | ✓ |

命中: **1/7**（仅 P/S，且为假便宜——见下方 BTC 毛记账说明）

⚠️ **P/S 假便宜**：XYZ 营收 $25.04B **含 Bitcoin 交易额毛记账**（Cash App BTC 转售，近零毛利），P/S 1.9x 是假象。真实业务规模用毛利润 $11.61B → P/GP = 4.1x。P/S ✓ 不算真入池。

FCF yield = $3.88B（FCF from B） / $47.46B（MCap） = **8.2%**

> 现价 $79.00 从 CSV `stock_data/XYZ_1d.csv` 2026-08-07 close 取。info.json currentPrice $79.00 一致。MCap $47.46B from info.json。

## A.2 估值分位

### 自身 P/E 区间

| 口径 | 当前 | 5yr 高 | 5yr 低 | 5yr 中位 | 分位 | 来源 |
|------|------|--------|--------|---------|------|------|
| GAAP P/E | 141.1x | 3867.5x（2023-12，EPS $0.02） | 0x（2023-09 亏损） | — | **N/A** | [MacroTrends](https://www.macrotrends.net/stocks/charts/XYZ/block/pe-ratio) |
| 正常化 P/E（EPS $0.56） | 141.1x | — | — | — | N/A | 同上 |

> ⚠️ **5yr P/E 分位 N/A — 无参考价值**：XYZ 2022-23 GAAP 长期亏损/微利（EPS −$0.93→$0.02），P/E 历史在 0x（亏损）到 3867x（near-zero EPS）间剧烈摆动，分母塌陷。**不能用 P/E 分位判贵贱**。改用 P/GP + 前瞻 adj P/E + FCF yield 交叉验。

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

## A.3 安全边际（join D 的锚）

| 口径 | 值 | 来源 |
|------|-----|------|
| 现价 | $79.00 | CSV 2026-08-07 |
| 合理价 | $13.16 | from D（EPS $0.56 × 23.5x） |
| 满仓目标 | $8.82 | from D（$13.16 × 0.67） |
| 安全边际 | **−500%** | 1 − 79/13.16（EPS 口径极度买贵） |

> ⚠️ 安全边际 −500% 是 **EPS 口径**（GAAP EPS $0.56 被 BTC MTM −$2.22B + 重组 $1.96B 严重压低）。DCF 口径合理价 $140-200（FCF-based），现价 $79 在 DCF 下方。但框架满仓用 EPS 口径（最保守）。详见 output_d.md D.2b/D.5。

## 结论

入池: **✗**（1/7 + P/S 假便宜 + 5yr P/E 分位 N/A + 安全边际 −500% EPS 口径）

非困境反转标的：好公司（GP +25%、FCF $3.88B、真缩股、adj OpM record 27%）但**麻烦已自愈**（股价 YTD +21%、近 52w 高点），EPS 口径极度买贵了。DCF 口径有 upside 但非框架主口径。需回调或基本面持续兑现（GP 重回 20%+、NM 爬升）才重新评估。
