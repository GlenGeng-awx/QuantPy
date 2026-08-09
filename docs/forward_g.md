# 前瞻 g Checklist v1.0

> 被引用自 `docs/task_c.md`。前瞻 g 的计算方法独立封装于此。

## 原理

g 是**前瞻可持续增速**——不是历史外推，不是分析师乐观值，是穿越周期中枢的保守估计。

```
合理 PE = min(8.5 + g, 30)
```

g 越高 → PE 越高 → 合理价越高。因此 **g 偏保守 = 合理价偏低 = 需要更便宜才出手**。

与 EPS 的 min 原则一致：**哪怕错过，不要做错**。

> 估值三要素关系见 `analysis_framework.md`。

---

## 数据源

| # | 源 | 数据 | 成本 | key / 计算方式 |
|---|------|------|------|--------------|
| 1 | 营收 3yr CAGR | income_annual CSV | 免费 | `Total Revenue` 列0 vs 列2，CAGR 3 年 |
| 2 | OpInc 3yr CAGR | income_annual CSV | 免费 | `Operating Income` 同上 |
| 3 | EPS 3yr CAGR | income_annual CSV | 免费 | `Diluted EPS` 同上（⚠ 受回购/一次性扭曲） |
| 4 | 近期季度 YoY | income_quarterly CSV | 免费 | 最新季 `Total Revenue` vs 同季去年（列0 vs 列4） |
| 5 | PEG 隐含 g | info.json | 免费 | g = `trailingPE` / `pegRatio`（市场预期） |
| 6 | info.json 增长率 | info.json | 免费 | `earningsGrowth`（YoY）、`revenueGrowth` |
| 7 | 分析师 3-5yr 共识 | web search | 贵 | 分析师长期 CAGR 共识 |
| 8 | 管理层指引 | web search | 贵 | FY 指引 / 长期目标 |

### CSV 计算公式

```
文件: income_annual.csv  列0=最新年（新→旧）

⚠ 列号 ≠ 固定年数。col2 常仅 2 年前（非 3 年前）——须 PRINT header 验证 year_gap。
   旧公式写死 "col2=3年前 + ^1/3"，但 CSV col2 常仅 2 年前 → ^1/3 系统性低估增速。
   此陷阱已记录 mistakes.md #4/#11，但须在此 inline 修正，否则下次还踩。

Step 1: PRINT income_annual.csv header row → 读各列日期
Step 2: 找 colN 使 year_gap = col0_year − colN_year = 3（优先）
        若无 3yr 数据 → 用 year_gap = 2（fallback，注明）
        ⚠ 选 colN 时注意基数是否异常（如 FY23 低基数会扭曲 3yr CAGR，见下方 WMT 例）
Step 3: CAGR = (Value[0] / Value[N]) ^ (1 / year_gap) - 1

  营收 CAGR = (Revenue[0] / Revenue[N]) ^ (1/year_gap) - 1
  OpInc CAGR = (OpInc[0] / OpInc[N]) ^ (1/year_gap) - 1
  EPS CAGR  = (DilutedEPS[0] / DilutedEPS[N]) ^ (1/year_gap) - 1   ← ⚠ 受回购/一次性扭曲，仅参考
```

验证示例（WMT FY27 Q1 分析）:
```
header: ['', '2026-01-31', '2025-01-31', '2024-01-31', '2023-01-31']
col0=FY26, col2=FY24 → year_gap=2 → 用 ^1/2
  营收 2yr CAGR = (713.16/648.12)^(1/2)-1 = 4.90%
col0=FY26, col3=FY23 → year_gap=3 → 用 ^1/3，但 FY23 OpInc $20.4B 是低基数
  → OpInc 3yr CAGR = 13.45% 被 FY23 扭曲（虚高），2yr CAGR 5.08% 更代表正常增长
  → G-3 Step 2 剔除 3yr OpInc CAGR（基数异常）
```

```
文件: income_quarterly.csv  列0=最新季，列4=一年前同季

营收 YoY = Revenue[0] / Revenue[4] - 1
```

```
文件: financial_data/{STOCK}/info.json

PEG 隐含 g = trailingPE / pegRatio
earningsGrowth = info.json 里的 YoY 盈利增长率（小数，0.82 = 82%）
revenueGrowth = info.json 里的 YoY 营收增长率
```

---

## Checklist

### G-1: 计算本地 g（免费，Task B 可并行）

```
文件: income_annual.csv + income_quarterly.csv + info.json

1a. 营收 3yr CAGR       ← 基线（最可靠，不易被操纵）
1b. OpInc 3yr CAGR     ← 经营增长（剔非经营项）
1c. EPS 3yr CAGR       ← ⚠ 受回购/一次性扭曲，仅参考
1d. 近期季度 YoY        ← 看加速/放缓趋势
1e. PEG 隐含 g          ← 市场预期参照（不是我们的估计）
1f. info.json 增长率    ← 工具给的 YoY（可能是季度或年度）
```

> ⚠ **CAGR 须先 PRINT header 验证 year_gap**（见上方"CSV 计算公式"）。col2 常仅 2 年前，用 ^1/3 会系统性低估增速。选 colN 后还需查基数是否异常（如 FY23 低基数扭曲 3yr OpInc CAGR）→ G-3 Step 2 剔除。

### G-2: 获取外部 g（web search，Task C）

```
2a. 分析师 3-5yr 营收/EPS CAGR 共识
    来源: Simply Wall St / Yahoo / Seeking Alpha
    ⚠ 分析师可能偏乐观

2b. 管理层指引（注明口径：季度/年度/长期）
    来源: 财报电话会议 / IR
    ⚠ 可能 sandbag（故意低指引 beat 概率高）
    ⚠ 季度指引含季节性/短期因素，不等同长期 g
```

### G-3: 综合判断（产出 g）

```
1. 列出所有 g 源（G-1 本地 + G-2 外部）
2. 剔除明显不可靠的源（judgment，参考下方判据）
3. 剔除剩余中最高的 1 个（保守偏置）
4. 对剩余取算术平均 → g
5. 若有结构性因素（监管/竞争/技术替代）→ 手动定性调整并注明
```

Step 2 剔除判据（非穷举，靠分析者判断）:
- PEG 当 EPS 从近零起步 → 分母极小导致 g 虚高
- CAGR 跨增长阶段（hypergrowth → 成熟）→ 历史不可外推
- 单季 YoY 有并购/一次性扭曲 → 不代表经营增长
- 管理层指引太模糊无法量化 → 不纳入

特殊情况:
  - 剩余源 ≤ 1 个 → 直接用该值，不做平均
  - g < 0（萎缩）→ g = 0%（不给负 PE，封底 8.5x）
  - g ≥ 22% → 封顶 30x（min(8.5+g,30) = 30）
  - PEG < 0.5 → 市场 pricing 极高增长，需验证可持续性

### G-4: g 质量护栏

```
4a. FCF − SBC > 0
    文件: income_ttm/cf_ttm.csv
    `Free Cash Flow` − `Stock Based Compensation` > 0
    ✗ < 0 → 重麻烦 → ×0.40（不否决，合理价照算，详见 discount_coefficient.md）

4b. 回购不进 g
    g 用业务/净利润增长，不含缩股驱动的 EPS 增长
    回购价值体现在"低价回购=安全边际"+"缩股逐年抬升 EPS 基数"，不抬高合理 PE

4c. 增长持续性判断
    - 护城河能否支撑？（宽护城河 → g 可信；窄/无 → g 降档）
    - 竞争是否侵蚀？（份额下降 → g 降档）
    - 增长来源是一次性（基数/恢复/并购）还是可持续？
    - TAM 是否足够大？（成熟市场 → g 天花板低）

4d. 周期股特殊处理（fallback，非默认）
    - 默认：所有标的先用 min(8.5+g, 30) 估值，含 batches.md 标"周期"的标的
    - 仅当 EPS 大幅波动/为负/处周期极端位置时 fall back：
      用中周期正常化盈利 + 中周期 PE（见 `task_a.md` 周期股特殊处理）
    - EPS 稳定正的周期股（如 TSM）不 fall back，用标准公式 + 敏感性表覆盖周期风险
```

---

## g 源诊断

```
本地 g（1a-1d）: 历史已发生，可信但可能不持续
市场 g（1e PEG）: 市场已定价的增长预期，验证"市场对不对"
外部 g（2a-2b）: 前瞻判断，最准但也最贵

诊断:
  本地 g ≈ 外部 g → 增长可信，市场定价合理
  本地 g >> 外部 g → 增长放缓，CAGR 不可外推（G-3 Step 2 候选剔除）
  本地 g << 外部 g → 市场过于乐观（或基数效应）→ 外部偏高可能被 Step 3 剔除
  PEG g >> 其他源 → 市场 pricing 了高增长 → 安全边际更薄
```

---

## 实际例子

| 标的 | CAGR | Q YoY | PEG g | 分析师 | 管理层 | Step2 剔除 | Step3 剔除 | 剩余 | 最终g | 理由 |
|------|------|-------|-------|--------|--------|-----------|-----------|------|-------|------|
| NVDA | 52.5% | +85% | 56.7% | 26-29% | FY26 +71% | PEG(失真) | 85%(最高) | 52.5,28,71 | >>22%封顶 | 所有源 >22%，封顶 30x |
| GOOG | 9.4% | +22% | 19.0% | ~15% | — | — | 22%(最高) | 9.4,19,15 | 15% | avg=14.5≈15% |
| ADBE | 7.0% | +12.7% | 22.2% | ~8.5% | FY26 ~10% | PEG(失真)+EPS CAGR(回购扭曲) | 12.7%(最高) | 7,9.4,7.9,8.5,10 | 9% | avg=8.6≈9% |
| TTD | 22.4% | +11.8% | 23% | 8-12% | Q2 +8%(季度) | PEG(失真) | CAGR(hyper) | 11.8,10,8 | 10% | avg=9.9≈10% |
| PDD | 20.4% | +11% | 11.4% | — | — | CAGR(hyper) | 11.4%(最高) | 20.4,11 | 11%* | 营收 11%，但净利在降 → Step5 定性调至 5% |
| NVO | 10.0% | +24% | 3.2% | ~3.6% | 模糊(不纳入) | Q YoY(Catalent) | CAGR(最高) | 3.2,3.6 | 3% | avg=3.4≈3% |
| UBER | 11.8% | +14.5% | 2.2% | ~10% | — | PEG(刚转正) | 14.5%(最高) | 11.8,10 | 11% | avg=10.9≈11% |
| TCOM | 11.9% | +17% | 3.3% | — | — | — | 17%(最高) | 11.9,3.3 | 8% | avg=7.6≈8%；PEG 3.3% 拉低反映 SAMR 预期 |

> UBER 旧值 g=14%（旧算法取 mid-teens 与长期 10% 中值），新算法降至 11%。同时修正 CAGR：原 output_c 标 18.3% 系 2yr CAGR 误标 3yr（mistakes.md #5），实际 3yr CAGR = (52.02/37.28)^(1/3)−1 = 11.8%。

---

## 与正常化 EPS 的配合

```
合理价   = min(GAAP, tool, v3.1) EPS × min(8.5 + g, 30)
满仓目标 = 合理价 × 折扣系数

EPS 保守（min 三者）+ g 保守（剔高+均值）+ 折扣保守（×0.60~0.75）= 三重保守
```

三重保守叠加 → 合理价偏低 → 需要更便宜才出手 → **哪怕错过，不要做错**

## 实装

```
本地 g 计算可自动化（G-1，从 CSV 算 CAGR + YoY + PEG）
外部 g 需 web search（G-2，分析师共识 + 管理层指引）
综合判断需人工（G-3，剔源判断 + 定性调整）
```
