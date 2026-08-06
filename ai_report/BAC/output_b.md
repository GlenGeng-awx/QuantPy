# BAC — Task B：财务健康  ⚠️ 银行口径
> 更新: 2026-08-06（财报 FY26 Q1，2026-04 发；下次 Q2 ~2026-07）

## B.1 SCORECARD 九宫格

| 维度 | 3yr | TTM | 5Q |
|------|-----|-----|-----|
| Income | 100 | 100 | 100 |
| CF | 38 | 35 | 50 |
| BS | 73 | 0 | 54 |

权重: Income 25% / CF 35% / BS 40%

### 背离检验

| 维度×窗口 | SCORECARD 说 | 原始财报 | 方向 |
|------|------|------|------|
| Income 全满分 | 营收/EPS 全线增长 | **证实**：FY22-25 Revenue +6.8% CAGR、EPS +18.7% CAGR | **同向 = 已定价** |
| CF TTM=35 | OCF 负 −$22.68B、FCF 负 | **银行结构扭曲**：OCF 含贷款流动（origination/repayment）、交易资产变动 → 银行 FCF 不适用 | **噪声误伤**（银行 FCF ≠ 经营恶化） |
| BS TTM=0 | AR +20% vs Rev +7% | **轻度误伤**：银行 AR 含交易应收，非经营恶化 | **噪声** |

伤口模式: **无经营伤口**。Income 满分 = 盈利健康。CF 低分是银行结构（FCF 不适用）。BS 3yr=73 尚可。

## B.2 利润表逐季

```
         Rev      NI       EPS     SGA      IntExp   NM%
Q1'25  28.25B   7.36B    —       13.37B   19.62B   26.1%
Q2'25  26.46B   7.12B    0.90    12.89B   20.20B   26.9%
Q3'25  28.09B   8.47B    1.06    13.03B   20.13B   30.2%
Q4'25  31.18B   7.53B    0.98    12.96B   18.51B   24.1%
Q1'26  30.27B   8.58B    1.11    14.03B   17.61B   28.4%   ← 最新
```

- **营收 FY25 $113.10B +6.8% 3yr CAGR**——利息收入（降息环境但量增）+ 非利息收入
- **EPS FY25 $3.81 +18.7% 3yr CAGR**（含回购缩股 −8.2%/3yr）
- **NM 27.8%**（高——银行 SGA/Rev 47% 主要是人工/合规成本）
- **Interest Expense FY25 $78.47B**（存款利率 ~2-3% × 存款 $1T+）
- 银行无 GM/OpInc/EBITDA（结构不同，用 P/B 替代）

## B.3 现金流（⚠ 银行 FCF 不适用）

| 项目 | TTM | 说明 |
|------|-----|------|
| OCF | −$22.68B | **银行 FCF 扭曲**：含贷款 origination/repayment + 交易资产变动 |
| FCF | −$22.68B | = OCF（CapEx = $0，银行无传统 CapEx） |
| SBC | $3.74B（3.1% Rev） | 中等 |
| 回购 | $22.96B | 强（3yr −8.2% 缩股） |
| Net Return | $19.22B | 回购 $22.96B − SBC $3.74B = 正（银行 FCF 扭曲但 Net Return 正） |

⚠ **FCF − SBC = −$22.68B − $3.74B = −$26.41B < 0**

> **银行 FCF−SBC ≠ ×0.40 硬规则**：FCF 负因贷款流动（origination/repayment）扭曲，非经营亏损。银行用 P/B 估值（per normalize_eps.md "银行不适用"）。NI $33.66B 正、ROE 11.2% 正常 → 盈利健康。Net Return +$19.22B（回购−SBC）= 真实股东回报正。

## B.4 资产负债表（bs_quarterly 2026-03-31）

| 项目 | 值 | 说明 |
|------|-----|------|
| Cash + Short Investments | $618.83B | 现金 $249.87B + 短投 $368.96B |
| Total Debt | $383.59B | 长期 $300.76B + 短期 $82.84B |
| Total Assets | $3,496.19B | 全球第二大银行 |
| **BV/share** | **$39.34** | Equity $300.67B / 7.50B diluted shares（≈ info.json $39.34） |
| Equity | $300.67B | 稳定增长（FY22 $273.2B → $300.7B） |
| D/E | 1.28 | $383.59B / $300.67B（银行杠杆正常） |
| Cash/Debt | 1.61x | $618.83B / $383.59B |
| Goodwill | $69.02B | 2.0% Assets（低，稳定） |
| Ordinary Shares | 7.13B | 3yr 8.17B→7.13B（−12.7% 缩股） |

## B.5 正常化 EPS Chain（⚠ 银行仅参考，不用 min(8.5+g,30)）

| 口径 | EPS | 来源 |
|------|-----|------|
| GAAP | $4.33 | Diluted EPS (TTM, info.json trailingEps) |
| 工具 | $4.33 | Normalized Income / Shares（无 Unusual） |
| v3.1 | $4.33 | 无 detector 触发（银行 OtherInc = 0） |
| **FINAL** | **$4.33** | **银行仅参考（不进 PE 公式）** |

> ⚠ **银行口径**：EPS 仅供参考，估值用 P/B（per batches.md "银行 → P/B 不用 EPS"）。合理价 = 合理 P/B × BV/share（见 output_d）。

## B.6 质量地板（银行适配）

| 指标 | 值 | ✓/✗ |
|------|-----|-----|
| GM >60% 稳 | N/A（银行无 GM） | ✗ |
| NM >20% | 27.8% | ✓ |
| FCF yield >5% | 负（银行 FCF 扭曲） | ✗ |
| FCF−SBC >0 | −$26.41B（银行不适用 ×0.40） | ✗ |
| 真缩股 | 8.17B→7.50B（3yr −8.2%） | ✓ |
| ROIC >15% 或 ROE >15% | ROIC n/m / ROE 11.2% | ✗ |

本地评分: 2/6（NM ✓ + 真缩股 ✓）+ 护城河宽（SIFI + 存款特许经营）= 3/7 = **好公司**（低端）

> BAC ROE 11.2% 对大型银行可接受（BAC 历史中枢 ~10-12%），但低于 JPM ~17% 和 15% 硬阈值。NM 27.8% 高、真缩股 −8.2%/3yr 正向。FCF−SBC < 0 是银行结构扭曲（非经营恶化），不适用 ×0.40 硬规则。估值用 P/B（1.3x × $39.34 = $51.14），不用 EPS×PE。
