# XYZ — Task E：决策
> 更新: 2026-08-09  现价 $79.00

## E.1 粗筛信号（from A）

| # | 条件 | 阈值 | 实际值 | ✓/✗ |
|---|------|------|--------|-----|
| 1 | 1Y 回撤 | >40% | 6.7% | ✗ |
| 2 | 2Y 回撤 | >60% | 20.1% | ✗ |
| 3 | 距 52W 低 | ≤15% | +61% | ✗ |
| 4 | P/E TTM | <15x | 141.1x（GAAP 失真） | ✗ |
| 5 | FCF yield | >5% | **8.2%**（$3.88B / $47.46B MCap） | **✓** |
| 6 | EV/EBITDA | <10x | 30.9x | ✗ |
| 7 | P/B | <1.5x | 2.1x | ✗ |
| 8 | P/S | <2.0x | 1.9x | **✓** |

命中: **2/8**（FCF yield + P/S；⚠ P/S 假便宜 BTC 毛记账）

> P/E 141x 失真（GAAP $0.56 被 BTC MTM +重组压低）。P/S 1.9x 含 BTC 毛记账（真实 P/GP 4.1x）。

## E.2 估值锚（from D）

| 口径 | 值 |
|------|-----|
| 合理价 | $13.16（$0.56 × 23.5x） |
| 满仓目标 | $7.90（×0.60） |
| 系数 | ×0.60（平庸×一般） |
| g | 15.0% |
| 合理 PE | 23.5x |
| 正常化 EPS | $0.56 |
| GAAP EPS | $0.56 |
| FCF/sh | $6.38 |
| FCF−SBC/sh | $4.41 |
| r | 11.0% |
| P/FCF₀ | 30.0x |
| DCF FCF−SBC | $140.61 |
| DCF FCF | $199.88 |
| 质量×麻烦 | 平庸×一般 |

## E.3 安全边际 + 操作（join A price + D anchor）

| 口径 | 合理价 | 安全边际 | 满仓 | 操作 |
|------|--------|---------|------|------|
| EPS 模型 | $13.16 | -500.0% | $7.90 | 小仓/观察 |
| DCF FCF | $199.88 | +60.5% | — | — |
| DCF FCF−SBC | $140.61 | +43.8% | — | — |

## E.4 归类

**小仓/观察 — 平庸+一般，EPS 模型过度保守（BTC MTM），DCF 口径有 upside**

- **好价格（部分满足）**: 粗筛 2/8 入池（FCF yield 8.2%✓ + P/S 1.9x✓ 假便宜 BTC 毛记账）。双分位暂停（EPS near-zero → P/E 无意义）。距 52W 低 +61%（近高位，YTD +21%）。
- **好公司（不满足）**: 质量 2/6 = 平庸（FCF−SBC $2.68B✓ + 真缩股✓；GM 46.4%✗ + NM 1.4%✗ + ROIC 11.1%✗ + 护城河中✗）。GAAP NI 被 BTC MTM −$2.22B + 重组 $1.96B 严重压低 → "低 GAAP 盈利 + 强 FCF"类（同 COIN）。
- **麻烦（一般）**: adj 盈利 record + GP +24.8% 加速 = 非结构性恶化。DOJ ongoing + 重组 recurring + NM 薄。
- **质量×麻烦×系数**: 平庸 × 一般 = ×0.60 → 满仓 $7.90
- **DCF 交叉验**: DCF 封顶（g=15% > r=11% → 30x）→ DCF FCF−SBC $140.61 >> EPS $13.16。gap 10x+ 因 GAAP NI 被非现金项压低 → EPS 模型过度保守，DCF 更准确。DCF 口径下现价 $79 有 upside。
- **关键风险**: (1) GAAP EPS $0.56 被 BTC MTM 压低（EPS 模型 $13.16 过度保守）；(2) DOJ 法律风险 ongoing；(3) 重组 recurring（$1.96B/yr 连续 5 年增长）；(4) NM 1.4% 极薄；(5) P/E 141x 表面极贵但失真。
- **操作**: 现价 $79 → EPS 口径 −500%（过度保守），DCF FCF−SBC $141 有 upside → 小仓/观察。满仓 $7.90（EPS 口径，过度保守）。等 DCF FCF−SBC $141 以下或 adj 盈利持续坐实。

## E.5 双分位（from A）

| 口径 | 当前 | 5yr 高 | 5yr 低 | 5yr 中位 | 分位 | 来源 |
|------|------|--------|--------|---------|------|------|
| GAAP P/E | 141.1x | 3867.5x（EPS $0.02） | 0x（亏损） | — | **暂停** ✗ | EPS near-zero 剧烈摆动 |
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
