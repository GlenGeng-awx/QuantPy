# DIS — Task B：财务健康 + 正常化 EPS
> 更新: 2026-08-07（财报 FY26 Q2，TTM 2026-06）⚠️ TTM CSV COGS 数据质量问题（见 B.5）

## B.1 SCORECARD 九宫格

| 维度 | 3yr | TTM | 5Q |
|------|-----|-----|-----|
| Income | 100 | 65 | 74 |
| CF | 80 | 75 | 88 |
| BS | 65 | 32 | 25 |

权重: Income 25% / CF 35% / BS 40%

### 背离检验

| 维度×窗口 | SCORECARD 说 | 原始财报 | 方向 |
|------|------|------|------|
| Income 3yr=100 | 营收/OpInc/EPS/GM 全线 ✓ | **证实**：从 COVID 谷底恢复 + streaming 减亏 + parks 复苏 | **同向 = 复苏** |
| Income TTM=65 | EPS −29.2% YoY、GM 21.1%（TTM CSV）、NM 8.7% | **数据问题**：TTM CSV COGS $78B 异常偏高（quarterly sum $61B），GM 21.1% 失真；实际 GM ~37%（quarterly） | **TTM CSV 误伤** |
| CF TTM=75 | OCF −6.1% YoY、FCF $8.29B 正 | **同向**：CapEx $8.7B 重（parks 扩建 + cruise 船队）→ FCF 被吞 | **同向 = CapEx 重** |
| BS 5Q=25 | Cash/Debt 0.12x、CR 0.68（<1）、GW 42% Assets | **证实**：负营运资本 + 高杠杆 + Goodwill $85B（21CFox 遗产） | **同向 = BS 弱** |

伤口模式: BS 5Q=25 是伤口——负营运资本（Working Capital −$11.6B）、Cash/Debt 0.12x、Goodwill 42% Assets。但 Income 3yr=100 + CF 3yr=80 = 从 COVID 谷底强劲复苏。

## B.2 利润表逐季

```
          Rev      GM%    OpInc   OpM%    NI       dilEPS  dilShares
Q1'25  23.62B  37.3%  3.51B   14.9%   3.27B    —       —
Q2'25  23.65B  38.6%  3.65B   15.4%   5.26B    2.92    1.80B  ← tax benefit −$2.73B
Q3'25  22.46B  37.6%  2.60B   11.6%   1.31B    0.73    1.81B
Q4'25  25.98B  35.8%  3.88B   14.9%   2.40B    1.34    1.79B
Q1'26  25.17B  36.8%  3.79B   15.1%   2.25B    1.27    1.77B
```

- **GM ~37% 稳定**（quarterly 数据；TTM CSV 的 21.1% 是 COGS 数据错误，见 B.5）
- **Q2'25 NI $5.26B 含 tax benefit −$2.73B**（递延税调整，一次性）→ 正常化需剔除
- **OpM 12-15%**（parks 高利润率 + streaming 改善）
- **营收 +6.5% YoY Q1'26**（parks + streaming 双增长）
- **缩股**：dil shares 1.83B→1.77B（3yr −3.3%，真回购 $8.25B TTM）

## B.3 现金流

| 项目 | TTM | 说明 |
|------|-----|------|
| OCF | $16.99B（−6.1% YoY） | OCF/NI 1.98（含金量高，DD&A $5.53B 大） |
| FCF | $8.29B | CapEx $8.70B 重（parks 扩建 + cruise 新船 + ESPN/流媒体投入） |
| SBC | $1.52B（1.5% Rev） | 偏高（媒体行业常态） |
| 回购 | $8.25B | 真缩股（dil shares 1.83B→1.77B） |
| 股息 | $2.23B | 首次派息（FY2025 起，$1.00/半年级别） |
| Net Return | $8.25B + $2.23B − $1.52B = $8.96B | 正 |

**FCF − SBC = $8.29B − $1.52B = +$6.77B > 0 ✓**（不触发 ×0.40）

> ⚠ **CapEx 重**：$8.70B = 51% of OCF。parks 扩建 + cruise 船队 + 流媒体内容投入 → FCF 被吞。FCF $8.29B 仍正但 CapEx 若继续升 → FCF 压力。
>
> ⚠ **负营运资本**：Working Capital −$11.6B（AP $0 + Current Debt $8.89B vs AR $14.39B）。但 OCF 正因 DD&A $5.53B 大（非现金折旧回加）。

## B.4 资产负债表（Q1'26, bs_quarterly 2026-03-31）

| 项目 | 值 | 说明 |
|------|-----|-----|
| Cash+STI | $5.68B | — |
| 总债 | $47.36B | LT $38.47B + Current $8.89B |
| **净债** | **$41.68B** | $5.68B − $47.36B = −$41.68B（净负债） |
| D/E | 0.44 | $47.36B / $108.71B Equity |
| Cash/Debt | 0.12x | $5.68B / $47.36B（低） |
| 利息覆盖 | 12.2x | TTM OpInc $15.03B / Interest $1.23B |
| Goodwill | $84.74B | 41.3% Assets（21CFox + Pixar + Lucasfilm + Marvel 累积） |
| BV/share | $62.30 | P/B 1.6x |
| Net PPE | $44.26B | parks/ride 设施 + cruise 船队 |
| 留存收益 | $62.39B | 厚（从 COVID 谷底 $43.64B 恢复） |

> BS 弱点：负营运资本（CR 0.68）、Cash/Debt 0.12x、Goodwill 41% Assets。但利息覆盖 12.2x 强 + 留存收益 $62B 厚 → 非 BS 危机，只是杠杆偏高。

## B.5 正常化 EPS Chain

| 口径 | EPS (USD) | 来源 |
|------|----------|------|
| GAAP (TTM CSV) | **$4.85** | TTM Diluted EPS（TTM ending Jun 2026，不含 Q2'25 tax benefit） |
| 工具 | **$5.45** | Normalized Income $9.70B / 1.78B（剥离 Unusual −$1.52B） |
| v3.1 | **−$0.66** | **假阳性 — 排除**（见下） |
| **FINAL** | **$4.85** | **min(GAAP, tool) = $4.85**（v3.1 排除） |

> ⚠ **TTM CSV COGS 数据质量问题**：TTM COGS $77.99B vs quarterly sum $61.12B（差 $16.87B），导致 TTM GM 21.1%（失真，实际 ~37%）。detector 2e GMDrop 因 TTM GM 21.1% vs hist 35.6% 触发，剥离 $14.4B "excess gross profit" → v3.1 EPS = −$0.66（**假阳性，排除**）。
>
> ⚠ **info.json trailingEps $6.25** vs TTM CSV $4.85：差异因不同 TTM 时点（info.json = TTM ending Mar 2026 含 Q2'25 tax benefit $2.73B；TTM CSV = TTM ending Jun 2026 不含 tax benefit）。TTM CSV $4.85 更"干净"（无 tax benefit）。
>
> GAAP $4.85 = MacroTrends TTM ending Jun 2026 EPS $4.84 ✓（交叉验证）
>
> 工具 $5.45 剥离 Unusual −$1.52B（restructuring + 其他损失），但仍含 tax benefit 影响（TTM ending Jun 已无 tax benefit）。

### Detector 详情（normalize_eps.py 实跑）

| Detector | 信心 | 金额 | 性质 |
|----------|------|------|------|
| 2a: OtherInc(MTM) | high | −$1.20B（pre-tax） | 负值→不剥离 |
| 2b: Restructuring | low | $811M（pre-tax） | flag only（费用不剥离） |
| 2d: OpIncDrop | low | —（flag only） | QoQ 数据问题 |
| 2e: GMDrop | medium | +$14.4B（pre-tax） | **假阳性**（TTM CSV COGS 错误 → GM 21.1% vs hist 35.6%，差 14.5pp） |
| 2x: Unusual(tool) | high | −$1.52B（pre-tax） | 工具归类 Unusual |

## B.6 质量地板（给 Task D 预判）

| 指标 | 值 | ✓/✗ |
|------|-----|-----|
| GM >60% 稳 | ~37%（稳定，非 60%+） | ✗ |
| NM >20% | 8.7% | ✗ |
| FCF−SBC >0 | +$6.77B | ✓ |
| 真缩股 | 1.83B→1.77B 3yr −3.3% | ✓ |
| ROIC >15% 或 ROE >15% | ROIC 7.2% / ROE 11.0% | ✗ |

本地评分: 2/5（FCF−SBC ✓ + 真缩股 ✓；GM ✗ + NM ✗ + ROIC ✗）+ 护城河（C 确认中-宽，+1）= **3/6 = 好公司**

> 旧 output 用 v3.1 $5.60（现已失效）→ FINAL 降至 $4.85。质量评分不变（3/6 好公司）。
>
> FCF yield 不在质量评分（在 A.1 粗筛 #5）。B 只存 FCF 金额。
