# CVX — Task B：财务健康 + 正常化 EPS
> 更新: 2026-08-07（财报 FY26 Q1）⚠️ 周期股（一体化油企 = commodity price-taker）

## B.1 SCORECARD 九宫格

| 维度 | 3yr | TTM | 5Q |
|------|-----|-----|-----|
| Income | 50 | 0 | 71 |
| CF | 72 | 64 | 52 |
| BS | 65 | 45 | 55 |

权重: Income 25% / CF 35% / BS 40%

### 背离检验

| 维度×窗口 | SCORECARD 说 | 原始财报 | 方向 |
|------|------|------|------|
| Income 3yr=50 | 营收/OpInc/EPS 全线 ⚠ 下滑（油价 + Hess DD&A） | **同向**：油价从 2022 峰回落 + Hess 并表推高 DD&A/股数 | **周期下行 = 已定价** |
| Income TTM=0 | TTM 数据缺失（income_ttm.csv 仅 EPS $10.39 stale） | **数据问题**：TTM CSV 仅含 EPS/shares，无 Rev/OpInc/NI。从 quarterly 重建 TTM | — |
| CF TTM=64 | FCF $16.1B 正但 OCF −5.3% YoY | **部分误伤**：Q1'26 FCF −$1.55B（衍生品 margin posting 时点性），TTM 仍正 | **同向 = 油价下行** |
| BS TTM=45 | AR +29% vs Rev +3%、Cash/Debt 0.12x | **证实**：Hess 并表推高 Total Debt $45.4B（from $29.5B）、AR 跳升 | **同向 = 杠杆升** |

伤口模式: 油价周期下行（2022 峰回落）+ Hess 并表噪音（债务翻倍、DD&A 上升、股数 +14%）。产量创纪录 3.86 MMboe/d。**周期性伤口 + 一次性整合噪音，非结构损伤**。

> ⚠ **income_ttm.csv 数据缺失**：TTM CSV 仅含 Diluted EPS $10.39 + shares，其余字段空白。$10.39 系 mid-2025 TTM（stale），实际 TTM EPS = Q2'25 $1.45 + Q3'25 $1.82 + Q4'25 $1.39 + Q1'26 $1.11 = **$5.77**。周期股用中周期正常化 EPS（见 B.5），不用 TTM。

## B.2 利润表逐季

```
          Rev      GM%    OpInc   OpM%    NI       dilEPS  dilShares
Q1'25  46.10B  29.0%  4.30B    9.3%   3.50B    2.00    1.75B
Q2'25  44.38B  29.7%  4.06B    9.1%   2.49B    1.45    1.72B
Q3'25  48.17B  31.1%  4.30B    8.9%   3.54B    1.82    1.95B（Hess 并表）
Q4'25  45.79B  31.8%  4.02B    8.8%   2.77B    1.39    2.00B
Q1'26  47.56B  28.4%  3.22B    6.8%   2.21B    1.11    1.99B
```

- **GM 28-32% 摆动**（随油价，commodity price-taker，无定价权）
- **Q1'26 GAAP EPS $1.11 vs adj $1.41**：差额 = ~$2.9B 衍生品 MTM 时点损失 + Hess DD&A（一次性，下季反向回补）
- **股数因 Hess 跳升**：1.72B → 2.00B（+16%，发股对价），摊薄 EPS
- **产量创纪录** 3.86 MMboe/d（美国 +24%、全球 +15%）

## B.3 现金流

| 项目 | TTM (quarterly 重建) | 说明 |
|------|---------------------|------|
| OCF | $31.26B | 油价软化，OCF/NI 2.84 极高含金量（DD&A 大） |
| FCF | $13.78B | Q1'26 单季 −$1.55B（衍生品 margin posting 时点性，会回补） |
| SBC | $0（未披露/无） | CVX 不单独披露 SBC |
| 回购 | ~$10.7B（TTM，从 quarterly 估算） | 回购 + 股息 = 总回报 ~$24B |
| 股息 | ~$13.3B | 38 年连增，$1.71/季 |
| Net Return | ~$24B | 回购 + 股息 > FCF $13.8B → 动用举债 |

**FCF − SBC = $13.78B − $0 = +$13.78B > 0 ✓**（SBC=0，不触发 ×0.40）

> ⚠ **FCF 不足以覆盖总回报**：FCF $13.8B < 股息 $13.3B + 回购 $10.7B = $24B → 举债派息回购。股息覆盖率 FCF/股息 ≈ 1.04x（偏紧，比 XOM 更紧）。Q1'26 FCF 转负是时点性（margin posting），但油价再降则回购须收缩。

## B.4 资产负债表（Q1'26, bs_quarterly 2026-03-31）

| 项目 | 值 | 说明 |
|------|-----|------|
| Cash+STI | $5.33B | — |
| 总债 | $45.43B | LT $39.60B + Current $5.83B（Hess 并表后翻倍 from $29.5B） |
| **净债** | **$40.10B** | $5.33B − $45.43B = −$40.10B（净负债，无托底） |
| D/E | 0.25 | $45.43B / $183.72B Equity（仍低，Hess 前仅 0.13） |
| Cash/Debt | 0.12x | $5.33B / $45.43B（低，重资产周期股特征） |
| 利息覆盖 | ~11.6x | TTM OpInc $13.8B（估算）/ Interest $345M（Q1'26 季度 ×4 估算） |
| Goodwill | $4.57B | 1.4% Assets（低，干净） |
| BV/share | $92.91 | P/B 2.0x |
| Net PPE | $218.15B | 重资产（Hess 并表 +$72B） |
| 留存收益 | $204.04B | 厚（38 年连增股息靠留存 + FCF） |

## B.5 正常化 EPS Chain（周期股：中周期正常化 EPS）

| 口径 | EPS (USD) | 来源 |
|------|----------|------|
| GAAP TTM (quarterly 重建) | **$5.77** | Q2'25 $1.45 + Q3'25 $1.82 + Q4'25 $1.39 + Q1'26 $1.11 |
| GAAP TTM (CSV stale) | $10.39 | income_ttm.csv（mid-2025，数据不完整/过期） |
| 工具 | N/A | TTM CSV 无 Normalized Income 字段 |
| v3.1 | N/A | TTM CSV 无 Pretax/OpInc，无法计算 |
| **中周期正常化 EPS** | **$10.3** | **5yr NI 均值 $19.6B ÷ ~1.9B 股**（含 2022 超级周期峰） |

> ⚠ **周期股用中周期正常化 EPS，不用 TTM**：TTM $5.77 含 Q1'26 $2.9B 衍生品时点损失 + Hess DD&A 摊销上升 = 低谷偏低。中周期 $10.3（5yr 均值）跨 2022 峰 $35.5B → 2025 谷 $12.3B。
>
> **保守口径**：Hess 摊薄后股数 ~1.98B → 中周期 EPS $19.6B/1.98B = $9.9。取 $10.3（pre-Hess 基准 + post-Hess 储量增量未兑现）。
>
> **normalize_eps.py 无法运行**（TTM CSV 数据缺失）。gaap_eps=$10.39（stale），norm_eps=0.0，tool_eps=0.0。手工用 quarterly 重建 TTM + 5yr 均值算中周期。

## B.6 质量地板（给 Task D 预判）

| 指标 | 值 | ✓/✗ |
|------|-----|-----|
| GM >60% 稳 | 30.4%（3yr 均值，commodity price-taker） | ✗ |
| NM >20% | ~4.6%（Q1'26，薄利） | ✗ |
| FCF yield >5% | 3.7%（$13.78B/$371.25B） | ✗ |
| FCF−SBC >0 | +$13.78B（SBC=$0） | ✓ |
| 真缩股 | 1.94B(2022)→1.86B(2025) 3yr −4.1%（Hess 推高至 2.0B 但 3yr 仍降） | ✓ |
| ROIC/ROE >15% | ROE 6.6%（$12.3B/$186.5B） | ✗ |

本地评分: 2/6 + 护城河（C 确认中-宽，+1）= **3/7 = 好公司**

> **FCF−SBC > 0 → 不触发 ×0.40**（SBC=$0，周期股 FCF 正）。
> 好公司（非伟大）：一体化 + Guyana/Permian 储量 + 38 年连增股息，但 commodity price-taker 无定价权 + GM 薄 + Hess 推高杠杆。
