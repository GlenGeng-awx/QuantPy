# HOOD — Task B：财务健康 + 正常化 EPS
> 更新: 2026-08-07（TTM 2026-06，Q2'26 财报 7/29 报告）
> ⚠️ batches.md 标记**周期**（券商），但 2024+ 营收从未下降 → 用标准框架 + 周期风险注释
> ⚠️ **FCF−SBC < 0**（TTM）：FCF 被客户资金流扭曲，触发 ×0.40 硬规则（但标注失真）

## B.1 SCORECARD 九宫格

| 维度 | 3yr | TTM | 5Q |
|------|------|-----|-----|
| Income | 20 | 95 | 100 |
| CF | 40 | 60 | 15 |
| BS | 15 | 44 | 40 |

### 背离检验

| 维度 | SCORECARD 说 | 原始财报 | 方向 |
|------|-------------|---------|------|
| Income 3yr | 低分 20（OpInc 从亏损到盈利 = 趋势 ✗ 但绝对改善） | 2022−$966M → TTM $2.27B = 从巨亏到暴利 | 周期反转 |
| CF TTM/5Q | 低分 60/15（OCF 暴跌 85%） | WC 变化 −$2.48B（客户资金流）扭曲 | 非经营恶化 |
| BS 3yr | 极低 15（D/E 升、CR 降） | 2022 亏损致 Retained Earnings −$4.9B | 周期修复中 |

## B.2 利润表逐季

```
        Rev     GM%    OpInc   OpM%    NI      dilEPS   备注
Q2'26  1.31B  82.0%   574M   43.8%   561M    0.62     RECORD Rev +32%、Gold 4.8M
Q1'26  1.07B  80.4%   411M   38.4%   350M    0.38     —
Q4'25  1.28B  76.7%   650M   50.8%   605M    0.66     —
Q3'25  1.27B  86.6%   635M   50.0%   556M    0.61     —
Q2'25  0.99B  81.8%   439M   44.4%   386M    0.42     —
```

- **GM 82.9% TTM**（高，券商轻资产），但 3yr 下滑 92.2→79.4→83.3 → 周期波动
- **营收 Q2'26 +32% YoY RECORD**：event contracts $156M（>10x）、options $342M（+29%）、equities $129M（+95%）
- **crypto −38% YoY**（$100M vs $161M）→ 周期性疲软（Bitcoin 回调）
- **Gold 4.8M subscribers**（+39% YoY）、AUC $369B（+32%）、net deposits $21.7B
- **2022-2023 连亏**（−$1.03B、−$541M）→ 2024+ 转正 = 周期反转
- **营收 2022 同比下降**（$1.82B→$1.36B = −25%，研究确认）→ 确有周期性

## B.3 现金流（TTM）

| 项目 | TTM | FY2025 | 说明 |
|------|------|--------|------|
| OCF | $245M | $1.64B | ⚠ **暴跌 85%**——客户资金流扭曲（WC −$2.48B） |
| FCF | $178M | $1.58B | yield 0.2%（$178M/$83.4B） |
| SBC | $351M | $305M | SBC/Rev 7.1%（↓ from 46.7% in 2023 = 大幅改善） |
| CapEx | $67M | $54M | 轻资产 |
| 回购 | $871M | $653M | aggressive，但 2026-06 发 $2.2B 可转债补充 |

FCF − SBC = **−$173M < 0** → 触发 ×0.40 硬规则

> ⚠ **FCF 失真分析**: TTM OCF $245M 包含 WC 变化 −$2.48B（客户资金 receivables/payables）。剔除客户资金流后：
> - 真实 OCF ≈ $245M + $2.48B = $2.73B
> - 真实 FCF ≈ $2.73B − $67M = $2.66B
> - 真实 FCF−SBC ≈ $2.66B − $351M = **$2.31B > 0**
>
> 但 HOOD 非银行（B5 Fintech 非 B6 Banks），银行例外（"FCF因贷款流动扭曲, 不适用×0.40"）不直接适用。**按硬规则 ×0.40，但标注失真。**

## B.4 资产负债表（Q2'06）

| 项目 | 值 | 说明 |
|------|-----|------|
| Cash & ST Inv | $16.16B | 含 $2.2B 可转债净收入 |
| Restricted Cash | $13.26B | 客户资金（非公司资产） |
| Total Debt | $22.71B | 含 $2.17B LT Debt（2026 新增） |
| Net cash/(debt) | −$6.55B | **净债**（可转债驱动） |
| D/E | 2.40 | 高（杠杆上升） |
| Goodwill | $762M | Assets 1.3%（Bitstamp/WonderFi/TradePMR） |
| Equity | $9.48B | BV/share $10.55 |
| P/B | 8.8x → 轻资产（GM >60%） | — |
| Retained Earnings | −$1.24B | 累计亏损修复中（2022 −$4.9B → −$1.2B） |

## B.5 正常化 EPS Chain

| 口径 | EPS | 来源 |
|------|-----|------|
| GAAP | $2.26 | Diluted EPS TTM |
| 工具 | $2.25 | Normalized Income |
| v3.1 | $2.09 | detector 2a OtherInc + 2c TaxAnomaly |
| **FINAL** | **$2.09** | **min = v3.1** |

- detectors: OtherInc（TTM OtherInc $145M，含投资收益 $135M Q2'26 RVI deconsolidation gain）、TaxAnomaly（TTM tax 14% vs 3yr 均值 ~0% 含亏损年退税 → 差 >10pp 触发）
- adj: −7.5% vs GAAP

## B.6 质量地板（给 Task D 预判）

| 指标 | 值 | ✓/✗ |
|------|-----|-----|
| GM >60% 稳 | 82.9%（**3yr 下滑 92→83**） | ✗ |
| NM >20% | 42.0% | ✓ |
| FCF yield >5% | 0.2%（$178M/$83.4B） | ✗ |
| FCF−SBC >0 | −$173M < 0（**触发 ×0.40**；FCF 失真） | ✗ |
| 真缩股 | 878M→919M（**+4.7% dilutive**） | ✗ |
| ROE >15% | 23.6% | ✓ |
| 护城河宽 | 中（narrow，Schwab 30x 规模；但 gaining share） | ✗ |

本地评分: 2/7 → **平庸**。FCF−SBC < 0 → **重麻烦 → ×0.40**
