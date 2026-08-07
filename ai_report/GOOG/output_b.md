# GOOG — Task B：财务健康 + 正常化 EPS
> 更新: 2026-08-07（TTM 2026-06，财报 Q2 FY2026 7/22 报告）

## B.1 SCORECARD 九宫格

| 维度 | 3yr | TTM | 5Q |
|------|------|-----|-----|
| Income | 90 | 88 | 100 |
| CF | 100 | 85 | 100 |
| BS | 73 | 100 | 100 |

### 背离检验

| 维度 | SCORECARD 说 | 原始财报 | 方向 |
|------|-------------|---------|------|
| Income | 高分（营收/OpInc 3yr 全涨 +12-20%/yr） | Q2'26 Rev +24%、Cloud +82% | 增长加速 |
| CF | TTM 85（FCF 下降因 capex 暴增） | FCF $53.3B TTM（↓ from $73.3B FY25），capex $132.4B | **AI capex 吞噬 FCF** |
| BS | 100（净现金、无债） | Cash $242B、Debt $121B、净现金 $121B | BS 稳健 |

## B.2 利润表逐季

```
        Rev       GM%    OpInc   OpM%    NI        dilEPS   OtherInc    备注
Q2'26  119.80B  61.6%   40.77B  34.0%  112.19B    9.11    97.83B     ⚠ $99B Anthropic/SpaceX 收益
Q1'26  109.90B  62.4%   39.70B  36.1%   62.58B    5.11    36.87B     ⚠ $37B 投资收益
Q4'25  113.83B  59.8%   35.93B  31.6%   34.45B    2.82     2.27B     —
Q3'25  102.35B  59.6%   31.23B  30.5%   34.98B    2.87    11.83B     —
Q2'25   96.43B  59.5%   31.27B  32.4%   28.20B    2.31     1.87B     —
```

- **GM 60.9% TTM**（3yr 上升 55.4→58.2→59.6→60.9），Cloud稀释但 Search/YouTube 80%+ 拉升
- **营收 +24% Q2'26 YoY**（$119.8B vs $96.4B），Cloud +82%（$24.8B，$514B backlog）
- **Q2'26 OtherInc $97.83B** = Anthropic（$965B 估值，Google 持 10%+）+ SpaceX 股权 MTM → **一次性投资收益**
- **TTM OtherInc $148.8B** 垫高 GAAP NI 至 $244.2B → GAAP EPS $19.93 虚高
- **OpInc +30% YoY**（$40.77B vs $31.27B）→ 经营利润强劲增长

## B.3 现金流（TTM）

| 项目 | TTM | FY2025 | 说明 |
|------|------|--------|------|
| OCF | $185.7B | $164.7B | OCF/NI 0.76（NI 含投资收益，OCF 更干净） |
| FCF | **$53.3B** | $73.3B | **↓ 27%（capex 暴增）** |
| SBC | $28.2B | $25.0B | SBC/Rev 6.3% |
| CapEx | **$132.4B** | $91.5B | **AI capex 暴增（60% servers / 40% DC）** |
| 回购 | $17.4B | $45.7B | ↓（capex 挤压回购空间） |
| 分红 | $10.3B | $10.1B | $0.84/yr |

FCF − SBC = **+$25.1B > 0** ✓（但 FCF 从 $73B 降至 $53B，capex 吃掉了 $41B）

⚠ **前瞻风险**: FY26 capex 指引 $195-205B（第三次上调）、FY27E ~$257B → FY26 FCF 预测仅 ~$8.7B → FCF−SBC 可能转负 → ×0.40 风险

## B.4 资产负债表（TTM）

| 项目 | 值 | 说明 |
|------|-----|------|
| Cash & ST Inv | $242B | 极充裕 |
| Total Debt | $121B | D/E ~0.40 |
| 净现金 | **$121B** | **2.8% MCap**（薄 vs 历史标准） |
| Goodwill | — | 无商誉风险 |
| Equity | ~$303B | BV/share $50.9 |
| P/B | 7.1x → 轻资产（GM >60%） | — |

## B.5 正常化 EPS Chain

| 口径 | EPS | 来源 |
|------|-----|------|
| GAAP | $19.93 | Diluted EPS（**含 $148.8B 投资收益 → 虚高**） |
| 工具 | $10.03 | Normalized Income $122.8B / 12.24B |
| v3.1 | $10.03 | detector 2a 剥 OtherInc $148.8B |
| **FINAL** | **$10.03** | **min = v3.1 = Tool** |

> ⚠ **屏幕 P/E 低估贵**: GAAP P/E 18.1x 看似便宜，但 EPS $19.93 含 $148.8B 一次性投资收益。正常化 EPS $10.03 → 真实 P/E = 35.9x。属"屏幕 P/E 低估贵"型背离。

### v3.1 桥接

```
GAAP Pretax               $299.3B
  − OtherInc 剥离（税前）   $148.8B    ← detector 2a（Anthropic/SpaceX MTM）
  = 正常化 Pretax          $150.5B    （= OpInc $147.6B + 利息净收入 $2.8B）
  × (1 − 税率 18.4%)
  = 正常化 NI              $122.8B
  ÷ 稀释股数 12.24B
  = v3.1 EPS               $10.03
```

> OtherInc $148.8B 含 Anthropic（Google 持 10%+，$965B 估值）+ SpaceX 股权 MTM → 真正一次性。Interest income $2.8B 保留（经常性）。

## B.6 质量地板（给 Task D 预判）

| 指标 | 值 | ✓/✗ |
|------|-----|-----|
| GM >60% 稳 | 60.9% TTM（3yr 55.4→59.6→60.9 上升） | ✓ |
| NM >20% | 27.5% normalized（GAAP 54.8% 虚高） | ✓ |
| FCF yield >5% | 1.2%（$53.3B / $4.40T） | ✗ |
| FCF−SBC >0 | +$25.1B | ✓ |
| 真缩股 | 13.16B→12.24B（−7.0%） | ✓ |
| ROIC/ROE >15% | ROE 48.7% | ✓ |

本地评分: 5/6 → C 确认护城河**宽**（Search 垄断 + YouTube 3B 用户 + Cloud +82% + Android）→ +1 → **6/7 = 伟大**
