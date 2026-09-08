# 参考表 + Edge Cases

> **纯查表文件, 不含规则。** 规则在 owner 节 (§-ID), 本文件只列固定参数 + FX + edge case 指针。
> 改规则 = 改 owner 节; 本文件只随参数/FX 更新。

## 固定参数表

| 参数 | 值 | 来源 / owner |
|------|-----|------|
| DCF N (高增长年数) | 5 年 | 固定 |
| DCF g_terminal | 3% | 固定 (≈GDP) |
| DCF r | 9% / 10% / 11% (伟大/好公司/平庸) | §3.2 |
| Graham PE | 8.5 + g | 保守档/入场基准, 公式 owner §5.1 |
| Fisher PE | 8.5 + 2g | 乐观档/出场基准, 公式 owner §5.1 |
| 分位反推 Nth | 30th | §4.2 |
| derating 阈值 | g < 5yr avg × 0.70 | §4.3 |
| CSP sigma N | 2.5 | §6.4 (行权 ~0.6%) |
| CSP T | 15 交易日 (3 周) | §6.4 |
| 折扣系数表 | ×1.0/0.85/0.70/0.67/0.50/0.40 | §3.2 (2D 表) |
| 硬规则 | FCF-SBC<0 → ×0.40 | §3.2 |

## FX 汇率

> 多币种股 (ADR) 做 EPS 转换时用当前汇率。
> **更新日期**: 2026-08-19 | 每 3-5 天更新

| 币种对 | 近似值 | 涉及标的 |
|--------|--------|---------|
| CNY/USD | ~6.8 | BABA PDD JD TCOM BIDU BEKE BILI FUTU TME NIO LI XPEV |
| CNY/HKD | ~1.1 | 0700.HK |
| TWD/USD | ~32 | TSM |
| EUR/USD | ~1.15 | ASML BNTX SPOT |
| DKK/USD | ~6.48 | NVO |
| SEK/USD | ~10.5 | ERIC |
| SGD/USD | ~1.35 | SE |

> FX 来源优先级: ① Google Finance spot (playwright) > ② 上表近似值 > ③ 反推值 (CSV EPS / info.json trailingEps)

### 不可信 info.json 字段 (多币种)

```
financialCurrency ≠ USD 时, 以下字段不可信:
  trailingEps, trailingPE, priceToBook, enterpriseToEbitda,
  priceToSalesTrailing12Months, enterpriseValue, bookValue
可信字段 (price 端, 不受币种影响):
  currentPrice, marketCap, sharesOutstanding, fiftyTwoWeekHigh/Low, dividendYield, beta
```

## Edge Cases (指针 — 规则在 owner 节)

| # | 场景 | 处理要点 | owner |
|---|------|---------|-------|
| 1 | 亏损→盈利转换 (CAGR NaN) | Revenue CAGR 不受影响; OpInc/NI/EPS CAGR NaN → 用 Revenue CAGR 或 2yr | §2.2 (Step 2 判据) |
| 2 | 银行股 (JPM/BAC/GS/MS/NU) | 不用 EPS 框架, 用 P/B; Operating Income=$0; Fisher #3/#5 用 NIM 非 GM | §4.1 (P/B<1.0) + §5.2 (用⑥P/B 不用①②) |
| 3 | 半年报公司 (0700.HK/BABA/PDD) | 季度 CSV 多为零 → v3.1 detector 2a 假阳性; 半年报复查 | §1.3 |
| 4 | 收购驱动 g (CAGR 含 step-up) | YoY 跳变 >30% 且非有机 → 剔除该 CAGR, 用 OpInc/有机 YoY | §2.2 (Step 2) |
| 5 | 多币种 ADR | EPS_USD = CSV EPS / FX; P/E = price/EPS_USD; EV 统一币种 | §4.1 (EV 陷阱) + 上方 FX 表 |
| 6 | P/E 分位短历史 (PLTR 2020 上市) | 5yr 数据点 <15 → 分位不可信 → 用公式+DCF; 或本地算真实低 (price×TTM EPS) | §4.2 / §4.3 |
| 7 | CapEx 超级周期 (ORCL/MSFT) | CapEx/OCF>30% → DCF 低估; EPS 不受影响 (D&A 分摊) → 合理价用 EPS | §5.2 / §5.4 |
| 8 | SBC + 回购判断 | 回购>SBC→⑧DCF base+合理价用 EPS; 回购≤SBC→⑦+合理价用⑦ | §5.2 / §5.3 |
