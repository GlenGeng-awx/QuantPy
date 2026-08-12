# GS — Task B：财务健康（银行口径）
> 更新: 2026-08-07（TTM 2026-06，Q2'26 财报 7/14 报告）
> ⚠️ **银行**：用 P/B 不用 EPS×PE；FCF−SBC 不适用（CLAUDE.md: "FCF因贷款流动扭曲, 不适用×0.40"）

## B.1 SCORECARD 九宫格

| 维度 | 3yr | TTM | 5Q |
|------|------|-----|-----|
| Income | — | — | — |
| CF | — | — | — |
| BS | — | — | — |

> 银行 SCORECARD 字段大量空白（无 GM/OpInc/EBITDA/FCF），九宫格不适用。用 **ROE + P/B + CET1** 替代。

### 银行关键指标

| 指标 | TTM | Q2'26 | 说明 |
|------|-----|-------|------|
| **ROE** | **16.9%** | **23.5%**（年化，峰值） | TTM vs Q2 峰值——投行/交易周期性 |
| ROA | 1.07% | — | — |
| P/B | 2.52x | 2.40x | **5yr 100th = 多十年高位** |
| BVPS | $421.15 | — | Q2'06 MacroTrends |
| CET1 | 12.9% | 12.9% | vs 11.4% 要求 = 150bp 缓冲 |
| NI | $20.97B | $6.63B（Q2） | TTM vs 单季 |
| EPS | $64.76 | $20.98（Q2 beat +44%） | — |
| 真缩股 | 358M→310M（−13.4%/3yr） | 291M（Q2'06） | aggressive buyback $4.0B/季 |

## B.2 利润表逐季

```
        Rev      NI      dilEPS   ROE(ann.)  备注
Q2'26  20.34B   6.63B   20.98    23.5%      RECORD: Rev +39.5%、EPS +92%
Q1'26  17.23B   5.63B   17.55    —          —
Q4'25  13.45B   4.62B   14.01    —          —
Q3'25  15.18B   4.10B   12.25    —          —
Q2'25  14.58B   3.72B   10.91    ~13%       —
```

- **Q2'26 RECORD**: Rev $20.34B（+39.5% YoY）、EPS $20.98（+92%）、beat +44%
  - Equities $7.4B（+72%，record）、FICC $4.6B（+32%）、IB fees $3.4B（+55%）
  - Global Banking & Markets $15.52B（+53%）、AWM $4.60B（+20%）
- **TTM EPS $64.76 是峰值**——投行/交易周期性高，不可直接外推
- **营收增长**: $47.37B（2022）→ $58.28B（2025）→ TTM $66.20B（3yr CAGR 11.7%）
- **NI 增长**: $11.26B（2022）→ $17.18B（2025）→ TTM $20.97B（3yr CAGR 23.0%）

## B.3 现金流（不适用）

> ⚠ **银行 FCF 不适用**: StockAnalysis TTM OCF −$39.79B、FCF −$41.92B（正常——交易库存+监管资本导致 working capital 剧烈波动）。**不触发 FCF−SBC ×0.40 规则**。

SBC TTM = $3.46B（参考，不进 FCF−SBC 判断）

## B.4 资产负债表（Q2'06）

| 项目 | 值 | 说明 |
|------|-----|------|
| Total Assets | $2,128B | 巨型 BS |
| Total Equity | $122.7B | BVPS $421.15 |
| Total Debt | $475B | 银行债务=资金来源 |
| CET1 ratio | 12.9% | vs 11.4% 要求 = 150bp 缓冲 |
| Goodwill | $7.34B | Assets 0.3%（极低） |
| Treasury Stock | $129.95B | 累计回购巨量 |
| Ordinary Shares | 291M | 3yr −13.4%（aggressive buyback） |

## B.5 正常化 EPS（银行参考用，不进估值）

| 口径 | EPS | 说明 |
|------|-----|------|
| GAAP TTM | $64.76 | **峰值盈利**（投行/交易周期高位） |
| 中周期估算 | ~$48-52 | 穿越周期中枢（2023 $22.87 → TTM $64.76 = 大幅摆动） |
| **估值口径** | **P/B（非 EPS）** | 银行用 P/B 不用 EPS×PE |

> 银行不适用 normalize_eps.py（Operating Income=$0，Net Interest Income 是核心收入）。EPS 仅供参考。

## B.6 质量地板（银行口径）

| 指标 | 值 | ✓/✗ |
|------|-----|-----|
| GM >60% | N/A（银行） | — |
| NM >20% | 31.7%（$20.97B/$66.20B） | ✓ |
| FCF−SBC >0 | N/A（不适用 ×0.40） | — |
| 真缩股 | 358M→310M（−13.4%） | ✓ |
| ROE >15% | 16.9% TTM（Q2 23.5% 峰值） | ✓ |
| 护城河宽 | #1 全球 M&A + SpaceX IPO + JPM duopoly | ✓ |

有效评分: 3/5 local（NM ✓ + 真缩股 ✓ + ROE ✓；GM ✗(N/A 银行) + FCF−SBC ✗(N/A 银行)）+ 护城河 ✓ = **4/6 = 好公司**

> FCF yield 不在质量评分（在 A.1 粗筛 #5，银行 N/A）。B 只存 FCF 金额。
