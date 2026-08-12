# GILD — Task B：财务健康 + 正常化 EPS
> 更新: 2026-08-07（TTM 2026-06，财报 Q2 FY2026）
> ⚠️ **亏损年**：TTM GAAP EPS = −$2.65（Q2'26 ~$12.5B IPR&D + 减值）→ 用**恢复 EPS**

## B.1 SCORECARD 九宫格

| 维度 | 3yr | TTM | 5Q |
|------|------|-----|-----|
| Income | 80 | 60 | 100 |
| CF | 68 | — | 100 |
| BS | 82 | 47 | 68 |

### 背离检验

| 维度 | SCORECARD 说 | 原始财报 | 方向 |
|------|-------------|---------|------|
| Income 5Q | 满分 100（营收/OpInc/EBITDA 全正增长） | Q1'26 Rev +4.4%、OpInc +8.1% YoY | 经营完好 |
| Income TTM | 60 分（TTM EPS −$2.65 亏损） | Q2'26 ~$12.5B IPR&D 一次性 → NI 扭曲 | 非经营恶化 |
| BS TTM | 47 分（AR 增 +8%、Cash/Debt 0.34x） | $11.3B 收购消耗现金 + 举债 | M&A 驱动非恶化 |

伤口模式: 无伤口——营收/OpInc 从未下降。TTM 亏损系 Q2'26 一次性 IPR&D + Trodelvy 减值。**经营完好（OpInc flat vs FY2025）**。

## B.2 利润表逐季

```
        Rev     GM%    OpInc   OpM%    NI       dilEPS   OtherInc   备注
Q1'26  6.96B  79.2%   2.69B   38.6%   2.02B    1.61     +33M      —
Q4'25  7.92B  79.6%   2.99B   37.7%   2.18B    1.74     -750M     —
Q3'25  7.77B  79.8%   3.50B   45.0%   3.05B    2.43     +312M     —
Q2'25  7.08B  78.8%   2.72B   38.4%   1.96B    1.56     -115M     —
Q1'25  6.67B  76.9%   2.49B   37.3%   1.31B     —       -675M     —
```

> ⚠ Q2'26 季度数据不在 CSV（TTM 含 Q2'26 但季度 CSV 仅至 Q1'26）。Q2'26 为 ~$12.5B OtherInc 减值（IPR&D + Trodelvy），TTM 覆盖 Q3'25-Q2'26。

- **GM 79.6% 高且稳**（76.9-79.8%）—— Pharma 轻资产
- **OpInc 3yr CAGR +2.2%**（$10.97B→$11.70B）——低速增长但稳定
- **TTM OpInc $11.72B flat vs FY2025**（$11.70B）——经营完好，亏损在 OtherInc
- **Q2'26 ~$12.5B OtherInc 减值**:
  - $11.2B 收购 IPR&D（Arcellx $7.0B + Tubulis $3.1B + Ouro $1.0B）——deal-close 会计，一次性非现金
  - Trodelvy/Immunomedics IPR&D 减值——结构性（EVOKE-03 NSCLC 失败 + Dato-DXd 竞争）

## B.3 现金流（FY2025 annual，HKD billions）

> 季度 CF TTM 无数据，用 FY2025 annual。

| 项目 | FY2025 | 说明 |
|------|--------|------|
| OCF | $10.02B | OCF/NI=1.18（FY2025 GAAP NI $8.51B） |
| FCF | $9.46B | yield = 5.8%（$9.46B / $163.59B MCap） |
| SBC | $894M | SBC/Rev=3.0% |
| CapEx | $563M | CapEx/OCF=6% |
| 回购 | $1.92B | 3yr consistent |
| 分红 | $4.00B | $3.28/yr（2.5% yield） |

FCF − SBC = **+$8.57B > 0** ✓

⚠ H1'26 OCF = $6.1B（Q2 $3.6B），$11.3B 收购消耗现金 → Cash 从 $10.6B（YE2025）降至 $3.2B（Q2'26）。举债 $4.1B 补充。

## B.4 资产负债表（Q1'06）

| 项目 | 值 | 说明 |
|------|-----|------|
| Cash & ST Inv | $7.64B | Q2'26 降至 ~$3.2B（$11.3B 收购消耗） |
| Total Debt | $22.17B | D/E=0.94 |
| 净现金/债 | **−$14.5B** | **净债**（M&A 驱动） |
| Cash/Debt | 0.34x | <1，靠 FCF 覆盖 |
| **利息覆盖** | **11.7x** | **>5x ✓** |
| Goodwill+Intangibles | $24.70B | Assets 44%（IPR&D 减值后缩水） |
| Equity | $23.52B | — |

## B.5 正常化 EPS Chain — **恢复 EPS**（亏损年）

> GAAP EPS = −$2.65 < 0 → 用**恢复 EPS**（详见 normalize_eps.md EPS-4b）

| 口径 | EPS | 说明 |
|------|-----|------|
| GAAP | −$2.65 | TTM 含 Q2'26 ~$12.5B IPR&D + 减值 |
| 工具 | $3.88 | Normalized Income $4.85B / 1.25B（可能低估，Q2'26 normalization 问题） |
| v3.1 | −$2.60 | detector 无法修复亏损（OtherInc + TaxAnomaly + OpIncDrop） |
| **恢复 EPS** | **$7.59** | **framework 公式手算** |

### 恢复 EPS 计算过程

```
TTM Pretax                    −$1.96B
  + 一次性费用加回             $13.48B    ← Total Unusual Items（IPR&D $11.2B + Trodelvy 减值）
  − 一次性收益剥离              $0         ← 无大额一次性收益
  = 恢复 Pretax                $11.52B
  × (1 − 正常税率 17.6%)       ← FY22-25 均值（21.5%/18.2%/13.2%），排除 2024 扭曲
  = 恢复 NI                    $9.49B
  ÷ 稀释股数 1.25B
  = 恢复 EPS                   $7.59
```

### 交叉验

| 口径 | NI | EPS | 说明 |
|------|-----|-----|------|
| FY2025 Normalized | $9.58B | $7.66 | 接近恢复 EPS $7.59 ✓ |
| OpInc-based TTM | $8.83B | $7.07 | OpInc $11.72B − Interest $1.0B × (1−17.6%) |
| 研究 normalized | — | $8.4-8.8 | non-GAAP + IPR&D addback（更高，因 non-GAAP 剥更多） |
| FY2027E 共识 | — | $9.62 | 分析师恢复预期 |

> 恢复 EPS $7.59 与 FY2025 Normalized $7.66 一致 → 可信。Tool $3.88 可能低估（Q2'26 normalization 问题）。

## B.6 质量地板（给 Task D 预判）

| 指标 | 值 | ✓/✗ |
|------|-----|-----|
| GM >60% 稳 | 79.6%（3yr 76.0→78.3→78.8→79.6 TTM） | ✓ |
| NM >20% | −10.6%（TTM GAAP 亏损；恢复 NI NM ~31%） | ✗ |
| FCF−SBC >0 | +$8.57B（FY2025） | ✓ |
| 真缩股 | 1.26B→1.24B（−1.6%/3yr，consistent buyback $1-2B/yr） | ✓ |
| ROIC >15% | 18.5% | ✓ |

本地评分: 4/5（GM ✓ + FCF−SBC ✓ + 真缩股 ✓ + ROIC ✓；NM ✗）+ 护城河中等 ✗ = **4/6 = 好公司**

> ⚠ NM ✗ 系 TTM GAAP 亏损（一次性 IPR&D）。恢复 NI NM = $9.49B/$30.46B = 31.2% ✓。但框架评分用 TTM 口径。
>
> FCF yield 不在质量评分（在 A.1 粗筛 #5）。B 只存 FCF 金额。
