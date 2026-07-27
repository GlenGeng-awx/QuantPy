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
文件: income_annual.csv  列0=最新年，列2=3年前

营收 CAGR = (Revenue[0] / Revenue[2]) ^ (1/3) - 1
OpInc CAGR = (OpInc[0] / OpInc[2]) ^ (1/3) - 1
EPS CAGR  = (DilutedEPS[0] / DilutedEPS[2]) ^ (1/3) - 1
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

### G-2: 获取外部 g（web search，Task C）

```
2a. 分析师 3-5yr 营收/EPS CAGR 共识
    来源: Simply Wall St / Yahoo / Seeking Alpha
    ⚠ 分析师可能偏乐观

2b. 管理层 FY 指引
    来源: 财报电话会议 / IR
    ⚠ 可能 sandbag（故意低指引 beat 概率高）
```

### G-3: 综合判断（产出 g）

```
规则:
  1. 若近期 YoY < 3yr CAGR（放缓）→ 用近期（不外推高增长）
  2. 若管理层指引 < 分析师共识 → 用管理层（保守）
  3. 若管理层指引 > 分析师共识 → 用分析师（管理层可能过于乐观）
  4. g = 历史与前瞻的保守交集（不是简单 min，但偏向低值）

特殊情况:
  - g < 0（萎缩）→ g = 0%（不给负 PE，封底 8.5x）
  - g ≥ 22% → 封顶 30x（min(8.5+g,30) = 30）
  - PEG < 0.5 → 市场 pricing 极高增长，需验证可持续性
```

### G-4: g 质量护栏

```
4a. FCF − SBC > 0
    文件: income_ttm/cf_ttm.csv
    `Free Cash Flow` − `Stock Based Compensation` > 0
    ✗ 烧钱式增长（FCF 负）→ 不配用成长估值 → g 降至 0%

4b. 回购不进 g
    g 用业务/净利润增长，不含缩股驱动的 EPS 增长
    回购价值体现在"低价回购=安全边际"+"缩股逐年抬升 EPS 基数"，不抬高合理 PE

4c. 增长持续性判断
    - 护城河能否支撑？（宽护城河 → g 可信；窄/无 → g 降档）
    - 竞争是否侵蚀？（份额下降 → g 降档）
    - 增长来源是一次性（基数/恢复/并购）还是可持续？
    - TAM 是否足够大？（成熟市场 → g 天花板低）

4d. 周期股特殊处理
    - 周期股不用 g 套 min(8.5+g,30) 公式
    - 用中周期正常化盈利 + 中周期 PE（见 `task_a.md` 周期股特殊处理）
    - g 仅作参考，不进公式
```

---

## 三个 g 源的交叉验

```
本地 g（1a-1d）: 历史已发生，可信但可能不持续
市场 g（1e PEG）: 市场已定价的增长预期，验证"市场对不对"
外部 g（2a-2b）: 前瞻判断，最准但也最贵

三角验证:
  本地 g ≈ 外部 g → 增长可信，市场定价合理
  本地 g >> 外部 g → 增长放缓，历史不可外推 → 用外部
  本地 g << 外部 g → 市场过于乐观（或基数效应）→ 用本地
  PEG g >> 我们的 g → 市场 pricing 了高增长 → 安全边际更薄
```

---

## 实际例子

| 标的 | 营收CAGR | 季度YoY | PEG隐含g | 分析师共识 | 管理层指引 | 最终g | 理由 |
|------|---------|---------|---------|-----------|-----------|-------|------|
| NVDA | 52.5% | +85% | 56.7% | 26-29% | FY26 +71% | >>22%封顶 | 历史不可持续，但前瞻仍 >22% → 30x 封顶 |
| GOOG | 9.4% | +22% | 19.0% | ~15% | — | 15% | 近期加速(AI)，取前瞻共识 |
| ADBE | 7.0% | +13% | 20.9% | ~12% | FY26 +10% | 8.5% | 历史放缓，取保守 |
| PDD | 20.4% | +11% | 11.4% | — | — | 5%/0% | 营收放缓+净利在降，双口径 |
| NVO | 10.0% | +24% | 3.2% | ~3.6% | 2027恢复双位数 | 8% | 2026谷底年穿越中枢 |
| UBER | 11.7% | +15% | 3.0% | — | — | 14% | PEG 偏低（盈利刚转正），取营收+OpInc |
| TCOM | 11.9% | +17% | 3.3% | — | — | 8% | 季度加速，取营收 CAGR 保守 |

---

## 与正常化 EPS 的配合

```
合理价   = min(GAAP, tool, v3.1) EPS × min(8.5 + g, 30)
满仓目标 = 合理价 × 折扣系数

EPS 保守（min 三者）+ g 保守（取低值）+ 折扣保守（×0.60~0.75）= 三重保守
```

三重保守叠加 → 合理价偏低 → 需要更便宜才出手 → **哪怕错过，不要做错**

## 实装

```
本地 g 计算可自动化（G-1，从 CSV 算 CAGR + YoY + PEG）
外部 g 需 web search（G-2，分析师共识 + 管理层指引）
综合判断需人工（G-3，含护城河/持续性判断）
```
