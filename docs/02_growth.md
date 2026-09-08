# Task 2: g 计算

> **产出**: g 多档位 (熊/基准/牛/调整) + 交叉验 + 总结。
> 
> **依赖**: Task 1 的 4 年趋势表 + web (#7 分析师共识 + #8 管理层指引)。
> 
> g 偏保守 = 合理价偏低 = 需要更便宜才出手 = 哪怕错过不做错。
>
> **output_2.md 结构 = 本文档节序 (§2.1→§2.2→§2.3→§2.4→§2.5→§2.6); 各 § 节的表格式即 output 格式, 不另设模板。**

## §2.1 数据源 (8 源)

> Revenue/GM/NM/OCF/FCF/SBC 趋势数据来自 Task 1 的 4 年趋势表。

| # | 源 | 数据 | 成本 | key |
|---|------|------|------|-----|
| 1 | Revenue 3yr CAGR | income_annual CSV | 免费 | `Total Revenue` col0 vs colN, year_gap=3 |
| 2 | OpInc 3yr CAGR | income_annual CSV | 免费 | `Operating Income` 同上 (辅助) |
| 3 | NI 3yr CAGR | income_annual CSV | 免费 | `Net Income` 同上 (不受回购影响) |
| 4 | Revenue Q YoY (latest Q) | income_quarterly CSV | 免费 | `Total Revenue` col0 vs col4 |
| 5 | PEG 隐含 g | info.json | 免费 | trailingPE / pegRatio |
| 6 | NI YoY (annual) | income_annual CSV | 免费 | `Normalized Income` col0 / col1 - 1 (剔 unusual items) |
| 7 | 分析师共识 | web search | 贵 | 分析师 3-5yr 营收 CAGR |
| 8 | 管理层指引 | web search | 贵 | FY 指引 / 长期目标 |

### CSV CAGR 计算公式

```
⚠ PRINT header 验证 year_gap — col2 常仅 2 年前, 不是 3 年前
  → 必须找到 colN 使 year_gap = col0_year - colN_year = 3
  → 3yr 数据不可用 OR 3yr CAGR 因峰/谷基数失真 → 用 year_gap = 2 (fallback, 注明)
CAGR = (Value[0] / Value[N]) ^ (1/year_gap) - 1
```

### EPS CAGR → 背离信号 (不进 g)

```
EPS CAGR 不进 g, 仅作背离信号:
  EPS CAGR >> NI CAGR → 回购驱动 (缩股 → EPS 涨但 NI 没涨)
  EPS CAGR ≈ NI CAGR → EPS 增长是真实的
  EPS CAGR << NI CAGR → 稀释 (发股 → NI 涨但 EPS 没涨)
可靠度: Revenue > OpInc > NI > EPS
```

output 格式 (g 源 8 源):

| # | 数据 | 值 | 来源 |
|---|------|-----|------|
| 1a | Revenue 3yr CAGR | ...% | income_annual CSV ($X→$Y, year_gap=N) |
| 1b | OpInc 3yr CAGR | ...% | 同上 |
| 1c | NI 3yr CAGR | ...% | 同上 |
| 1d | Revenue Q YoY (latest Q) | ...% | income_quarterly CSV ($X vs $Y) |
| 1e | PEG 隐含 g | ...% | info.json (trailingPE / pegRatio) |
| 1f | NI YoY (annual) | ...% | income_annual CSV ($X / $Y - 1) |
| 1g | 分析师共识 | ...% | web: (来源) |
| 1h | 管理层指引 | ...% | web: (来源) |

> EPS CAGR vs NI CAGR → gap Npp = 回购驱动/稀释 (背离信号)
> → EPS CAGR 不进 g

---

## §2.2 g-baseline 算法

> ⚠ **必须跑完全部 8 源, 包括 web search (#7 + #8)。**
> 没有 web search 的 g 不可靠 — ADBE/AVGO/PLTR 三次教训 (漏共识/指引 → g 偏)。
> web 源不可获 (paywall/Cloudflare) → 标"未获取", 用已有源算 g, 注明可信度低。

### Step 1: 剔除不可靠

判据 (judgment, 非穷举):
- PEG 当 trailing EPS 被压低 (重组/税异常/近零起步) → g 虚高; 或 PE 极端 (hypergrowth → PEG 不适用)
- CAGR 跨增长阶段 (hypergrowth → 成熟) → 历史不可外推
- CAGR 跨重大并购 → 含一次性 step-up → 不可外推 (判据: 营收 YoY 某年跳变 >30% 且非有机)
- CAGR base 为负 (亏损→盈利转换) → CAGR NaN → 用 Revenue CAGR 或 2yr
- hypergrowth + 负基数 (如 PLTR: NI 从亏→盈, Revenue +56%) → 历史源 1-6 多数不可靠 → g 依赖前瞻源 7-8 + §2.3 LLM 判断
- 单季 YoY 有并购/一次性扭曲 → 不代表经营增长
- 管理层指引太模糊 → 不纳入

output 格式:

| 剔除 | 值 | 理由 |
|------|-----|------|
| (源) | ...% | (理由) |

> After Step 1 sorted: [g1, g2, ..., gN]

### Step 2: 剔最高 1 个

```
剩余源中剔除最高的 1 个 (保守偏置)
```

output 格式:

| 剔除 | 值 | 理由 |
|------|-----|------|
| (源) | ...% | (理由) |

> After Step 2: [g1, ..., gN-1]

### Step 3: 均值

```
对剩余取算术平均 → g_baseline (基准档)
特殊情况: 剩余源 ≤ 1 → 直接用该值; g < 0 → g = 0% (封底 8.5x)
```

output: g_baseline = (g1 + ... + gN-1) / (N-1) = **...%**

---

## §2.3 LLM 定性调整 → 调整 g

```
LLM 看 g 源分布 + YoY 方向, 判断是否需要调整:
  历史源 >> 前瞻源 (margin expansion 拉高历史?) → 调低
  历史源 << 前瞻源 (基数效应压低历史?) → 调高
  收购 step-up 残留 → 调低
  监管/竞争结构性因素 → 调低
  YoY 在加速 → 可调高 (Fisher #1-4 待 Task 3 确认)

调整必须透明 (调整前/调整后/理由); 不调整也 OK (标 "不调整" + 理由)

→ §2.3 产出 = "调整 g", 独立列, **不覆盖基准档** (见 §2.5)
```

output 格式:

**(g_baseline) → (g_adjusted)%**

理由:
- (理由 1)
- (理由 2)

---

## §2.4 交叉验

```
源 A — 调整 g (§2.3 输出; 若不调整则 = 基准档 §2.2 Step 3)
源 B — 分析师共识 (web search, 源 1g/1h)

A vs B:  |A - B| < 3pp → 一致, g_final = A
         |A - B| ≥ 3pp → 取低者 (保守); 例外: YoY 加速 → 可取高者
         ⚠ 周期股: 分析师共识可能是单年低谷预测 (非长期 g) → 不盲目取低者, 注明
```

> Fisher #1-4 对 g 的影响通过 §2.3 定性调整处理 (非机械联动); Fisher 对估值的影响通过折扣系数 (§3.2) 处理。

output 格式:

| 源 A (调整 g) | 源 B (分析师共识) | 差距 | 判定 |
|---------------|-------------------|------|------|
| ...% | ...% | Npp | < 3pp → 一致 ✓ / ≥ 3pp → 取低者 |

---

## §2.5 多档位 (单源, 其他文件引用 §2.5)

四档全部来自 Step 2 后的列表 [g1, g2, ..., gM] (M = 剔除不可靠 + 剔最高后的源数):

| 档位 | 取值 | 说明 |
|------|------|------|
| 熊 | g1 (min) | 最悲观: 最低可靠源 |
| 基准 | avg(g1,...,gM) | g-baseline (§2.2 Step 3 输出) |
| 牛 | gM (max) | 最乐观: 最高可靠源 (剔最高后) |
| 调整 | §2.3 输出 | LLM 定性调整 (独立列, 不进三档排序) |

⚠ 顺序: 熊 ≤ 基准 ≤ 牛 (调整 g 不破坏此顺序)
  if 调整 g < 熊 → 调整 g 单列, 不覆盖基准档
  → 决策双看: 基准档 (历史外推) + 调整 g (LLM 保守判断)

源不足时合并:
  M=2: 熊=g1, 基准=avg(g1,g2), 牛=g2
  M=1: 三档全 = g1, 无调整 (源不足, LLM 不调)

output 格式:

| 档位 | g | 来源 |
|------|---|------|
| 熊 | ...% | min = (源名) |
| 基准 | ...% | g-baseline (§2.2 Step 3) |
| 牛 | ...% | max = (源名) |
| 调整 | ...% | LLM 定性调整 (§2.3, 独立列) |

> → 每档独立估值 (Task 5 矩阵 §5.3), 决策看现价落在哪个区间

---

## §2.6 总结 (→ Task 3/5 快速消费)

| 项 | 内容 |
|----|------|
| 一句话定性 | (高增长/稳定增长/周期/收缩) + g 共识范围 |
| 关键 flag | g 源一致性 (历史 vs 前瞻); PEG 是否删; 负基数/税异常/并购扭曲; YoY 方向 (加速/减速) |
| 交叉验结果 | A vs B 一致/分歧; Fisher #1-4 待 Task 3 |
| Top risk | Task 3/5 需关注: g 是否可持续? 一次性 vs 结构性? |

---

## 护栏

```
✓ 回购不进 g (用 Revenue/NI, 不用 EPS)
✓ CAGR 跨增长阶段 → 不可外推 → 用 latest_yoy
✓ CAGR 跨重大并购 → 不可外推 → 剔除该 CAGR
✓ CAGR base 为负 → NaN → 用 Revenue CAGR 或 2yr
✓ CAGR 峰/谷基数失真 → 用 2yr fallback (注明)
✓ g 质量看 Fisher #1-4 (增长可持续性, Task 3)
```
