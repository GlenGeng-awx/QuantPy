# SNOW（Snowflake）— 基本面 base

> **静态层**：财报/前瞻 g/护城河/管理层/消息面驱动，季度或重大事件更新。动态的现价、第一步粗筛、安全边际、仓位定档见 `analysis.price.md`。
> **更新: 2026-07-04**（财报 FY27 Q1，2026-05 发；财年截至 1 月）　货币: USD

**质量判定**：**平庸偏好公司**（数据云平台护城河真实——Marketplace 数据网络效应 + 迁移成本高，GM 67% 但对软件偏低且微降、GAAP 巨亏 NM −23.8%、**SBC 占营收 32-41%**、`FCF−SBC = 1.17 − 1.62 = −$0.45B < 0`、$11.1B 未归属 RSU = 7.5x 年费的未来稀释洪水、真实股数不缩仅靠发债回购对冲）× 麻烦 **无麻烦（反而在涨）**　→　**框架外：不适用成长折扣估值，走价值陷阱-on-SBC 判定**

**核心锚（静态）**：**无正常化正 EPS**（GAAP 亏损）。FCF 口径反推的"公允价"约 **$110-140**（见第五步，软估算），现价 $260 显著高于——**买贵了 + SBC 侵蚀（价值陷阱风险）**，不给席位。

---

## 二、估值分位（区间结构 + 同业 + de-rating）

**非周期股**（数据云 SaaS）。**GAAP 无 P/E**（亏损），只能看 P/S。

### SNOW 自身区间（P/S，无 P/E）

| 口径 | 数值 | 来源 |
|------|------|------|
| P/S（TTM） | **17.9x**（MCap $90.2B / Rev $5.03B） | 本地 combine |
| NTM EV/Rev | 从 2025-10 的 17.85x 压缩到 2026-05 的 **7.89x** | [SaaStr](https://www.saastr.com/databricks-vs-snowflake-at-5b-arr-same-revenue-2x-valuation-gap-heres-why/) |
| 远期 P/E（非 GAAP） | ~128-142x | [24/7 Wall St](https://247wallst.com/investing/2026/06/30/mongodb-vs-snowflake-why-one-is-the-better-stock-to-buy-in-2026/) |
| 距 52 周高点 | 曾跌 50%+ 至 $121，现已反弹回 $260（近高位） | [TIKR](https://www.tikr.com/blog/snowflake-stock-has-lost-half-its-value-in-2026-why-analysts-still-say-buy) |

关键：股价 **不在困境低点**——从 $121 低点反弹一倍多回到 $260，1Y 回撤仅 11%，**没有暴跌可捡**。P/S 17.9x 在软件里属最贵一档。

### 同业对比（数据/云平台，估值倍数）

| 公司 | 估值 | 增速 | 备注 |
|------|------|------|------|
| **SNOW** | **P/S 17.9x、非 GAAP P/E ~142x** | 产品 +34% YoY | 最贵 + GAAP 亏损 |
| MongoDB | 非 GAAP P/E ~76x、RPO +88% | 高 | OpM 18%，盈利更干净 |
| Datadog | 非 GAAP P/E ~64x、NTM EV/Rev 11.4x | +27.7% | 已 GAAP 盈利 |
| Databricks（未上市） | 私募估值 ~$134B（P/S ~25x） | +65% | 直接竞对，增长更快 |

SNOW 是同组里 **估值最高**（142x 非 GAAP 利润 vs MDB 76x、DDOG 64x），却是唯一 **GAAP 亏损** 者，且被增长快一倍的 Databricks 侵蚀。**无相对价值可言。**

⚠️ **de-rating 陷阱反向**：SNOW 的问题不是被错杀 de-rating，而是**估值仍在成长泡沫溢价区**（P/S 17.9x）。市场为 34% 产品增速 + AI 叙事付满价，一旦增速滑向 Databricks 抢食的 20% 区间，17.9x → 8x 的 de-rating 空间巨大（NTM EV/Rev 已从 17.85x 砸到 7.89x 印证过一轮）。

## 三、财务健康 — GAAP 巨亏 + SBC 洪水（逐表走查）

SCORECARD 九宫格（USD）：

| 维度 | 3yr | TTM | 5Q | 解读 |
|------|-----|-----|-----|------|
| Income | 30 | 90 | 78 | 3yr=30 因 OpInc/EPS 全负；TTM/5Q 高分是"亏损收窄"的改善，非盈利 |
| CF | 100 | 60 | 95 | OCF/FCF 3 年 +26% 真增长；TTM=60 因 SBC 占营收 32% + Net Return −$939M 扣分 |
| BS | 23 | 100 | 70 | 3yr=23 因流动比率下滑 + 举债；净现金薄 |

### 利润表 — 逐季拆解

```
        Rev     GM%    OpInc   OpM%    NI      dilEPS  dilShares  SBC
Q1'26  1.04B  66.6%  -447M  -43.0%  -430M   -1.29    332M      379M
Q2'26  1.14B  67.8%  -340M  -29.8%  -298M   -0.89    335M      404M
Q3'26  1.21B  67.9%  -329M  -27.2%  -293M   -0.87    339M      412M
Q4'26  1.28B  67.0%  -318M  -24.8%  -309M   -0.90    342M      403M
Q1'27  1.39B  66.6%  -326M  -23.5%  -295M   -0.86    345M      402M
```

- **营收强劲加速**：Q1'27 $1.39B、**+33.5% YoY**，产品收入 +34%——增长引擎完好，这是好公司的一面
- **GM 67% 但对软件偏低且微降**（66.6-67.9%）——数据云是"转售算力"模式（底层跑在 AWS/Azure），GM 结构性低于 ADBE 89%、纯 SaaS 80%+；且承压于 AWS $6B 采购承诺
- **GAAP 从未盈利**：OpM 虽从 −43% 改善到 −23.5%，**仍深度为负**；OpInc 5 季全负；改善靠营收摊薄固定费用（爬坡），非真盈利
- **SBC 是黑洞**：每季 SBC ~$400M ≈ 营收 **29-38%**，TTM SBC $1.62B / Rev $5.03B = **32.2%**（[GuruFocus](https://www.gurufocus.com/term/stock-based-compensation/SNOW)）。SBC 加回是"OpInc −23.5% 但非 GAAP +11%"的 34pct 缺口来源
- 正常化：GAAP 亏损，无正常化正 EPS 可套公式

### 现金流 — FCF 正但被 SBC 吞噬

| 项目 | TTM | 说明 |
|------|-----|------|
| OCF | 1.24B（+1.2% YoY） | 增速已大幅放缓（3yr +27% → TTM +1.2%） |
| FCF | 1.17B | CapEx 极轻（$70M），FCF 主要靠 SBC 加回 + 递延收入浮存 |
| **SBC** | **1.62B** | **> FCF**：SBC 占营收 32%（[valuesense](https://valuesense.io/ticker/snow/sbc)） |
| **`FCF − SBC`** | **1.17 − 1.62 = −0.45B < 0** | **真实现金创造为负** ✗ |
| 股东回报 Net Return | **−939M** | 回购 $682M + 分红 0 − SBC $1.62B = 净流出 |

**这是本案核心裁决**：FCF $1.17B 看似正，但全部（且不止）来自 SBC 加回。`FCF − SBC = −$0.45B` → 剔除股权稀释成本后，Snowflake **不创造真实现金**。此为 SNAP/ORCL 出局的同一标准（`FCF−SBC<0` → 无成长估值资格）。

⚠️ **$11.1B 未归属 RSU**（= 7.5x 年 SBC 费用，[hightechinvesting](https://hightechinvesting.substack.com/p/what-you-as-a-shareholder-should)）= 未来数年持续稀释洪水。当前 dil shares 靠**发 $2.3B 零息可转债回购**对冲才勉强不涨（9 个月净稀释仍 +8.1M 股），**并非真缩股**——是"发债买股堵稀释"的财技，非留存收益回购。

### 资产负债表

| 项目 | 值 | 解读 |
|------|-----|------|
| 现金 + 投资 | 2.95B（Q1'27）；含 LT ~$4.8B | 净现金薄（总债 $2.77B）→ **净现金仅 ~$0.2-2B** |
| 总债 | 2.77B（含 $2.3B 可转债 + 租赁） | 为回购而发的债 |
| 递延收入（流动） | 2.85B | 预收订阅，负营运资本浮存（模式优点，但撑起部分 FCF，作锚打折） |
| 留存收益 | **−$10.09B** | 累计巨亏，从未真赚过钱 |
| Goodwill | 1.54B | 并购累积（增长部分靠买） |

净现金薄（≈$2B / MCap $90B = 2%），**无资产托底**——不像 LI（净现金 88% MCap）那种下行锁死的期权结构。

### 伤口模式

**非伤口——SNOW 没有困境**。营收 +33% 加速、股价从 $121 反弹回 $260。这不是"暂时麻烦被错杀"的猎物，而是"高增长高估值 SaaS，市场付满价"。麻烦（Databricks 侵蚀 + NRR 下滑 + SBC 稀释）是**结构性的、且未反映在价格里**。

## 四、增长前瞻 / 护城河 / 管理层 / 消息面

### 增长前瞻（本应产出 g，但估值不适用）

| 口径 | 数值 | 说明 |
|------|------|------|
| 历史 3 年营收 CAGR | ~34%（2.07B→4.68B） | 高 |
| 近期季度 YoY | Q1'27 产品 +34%（加速） | 强 |
| FY27 产品指引 | +31%（从 27% 上调），$5.84B | 管理层上调 |
| 前瞻共识 3-5 年 CAGR | ~26.5%（[public.com](https://public.com/stocks/snow/forecast-price-target)） | 长期减速中 |

质量：增长真实且 AI（Cortex/CoCo）在加速消费。但 **g≥22% 一律封顶 30x**（价值框架不追高增长）——即便按 30x 估，也需要**正的正常化 EPS**，SNOW 没有。且增长质量存疑：Databricks 以 65% 增速抢食、NRR（净收入留存）逐季下滑（"best-in-class metric declining every quarter" [Runchey](https://www.runcheyresearch.com/blog/snow-q4-fy2026-earnings-preview)）。

### 护城河 — 真实但被侵蚀

- 壁垒类型：**数据云平台 + Marketplace 数据网络效应**（数据集/应用越多越黏）+ 存储迁移成本 + 多云中立
- 份额趋势：数据仓库仍最大，但 **Databricks（Lakehouse + AI/ML）以 65% 增速快速逼近**（run-rate $6.9B 已超 SNOW），技术差距缩小
- 威胁：Databricks 正面竞争、云厂商原生方案（BigQuery/Redshift/Fabric）、开源格式（Iceberg）降低锁定

护城河真实（这是"好公司"的一面），但**正被增长更快的对手边缘化**——非纯情绪伤口，有结构性竞争侵蚀成分。

### 管理层

| 项目 | 事实 |
|------|------|
| CEO | Sridhar Ramaswamy（前 Neeva/Google 广告，2024 接任），AI-first 转型主导者 |
| 资本配置 | **发 $2.3B 零息可转债回购**堵 SBC 稀释；零分红；并购扩张（Goodwill 增） |
| SBC 趋势 | 占营收从 41% 降至 32%（在降但仍极高） |
| 说到做到 | 连续 beat + 上调 FY27 指引（27%→31%）——执行力强 |
| 治理风险 | SBC 稀释是持续股东价值转移；$11.1B 未归属 RSU 洪水 |

### 消息面

- Q1 FY27（2026-05）：产品收入 +34% YoY 加速、上调 FY27 指引至 31%、$6B AWS 采购承诺（[Snowflake IR](https://www.snowflake.com/en/news/press-releases/snowflake-reports-financial-results-for-the-fourth-quarter-and-full-year-of-fiscal-2026/)）
- 分析师普涨目标价至 $270-370（UBS/Citi/WF/MS/GS），共识 ~$288-297，Strong Buy（[public.com](https://public.com/stocks/snow/forecast-price-target)）——但均基于非 GAAP/DCF，未罚 SBC 稀释
- 股价 2026 先跌 50% 至 $121 再反弹回 $260

### 熊 / 牛逻辑

**熊市逻辑**：GAAP 从未盈利、`FCF−SBC<0`、SBC 占营收 32%、$11.1B 未归属 RSU 稀释洪水、P/S 17.9x（软件最贵档）、Databricks 65% 增速侵蚀 + NRR 逐季下滑、OCF 增速从 27% 塌到 1.2%、股价已从底反弹一倍无安全边际。

**牛市逻辑**：数据云平台 + Marketplace 网络效应真实、产品收入 +34% 加速、AI（Cortex/CoCo）变现起势、非 GAAP OpM 升至 13.5%、管理层执行力强连续 beat 上调指引、CapEx 极轻。

## 五、安全边际 — 框架外（无正常化正 EPS）

**公式不适用**：`合理价 = 正常化 EPS × min(8.5+g,30)` 需要**正的正常化 EPS**，SNOW GAAP 亏损、`FCF−SBC<0`，**成长估值资格不合格**（护栏：烧钱式增长 / SBC 伪 FCF 不配用成长估值）。

**只能软估**（FCF 口径反推，标注为软估算）：

```
真实自由现金流（罚 SBC）= FCF − SBC = −$0.45B < 0   → 无正现金锚
非 GAAP FCF（不罚 SBC，市场口径）= $1.17B
若给成熟 SaaS 25-30x FCF（宽容口径，不罚 SBC）
  公允 MCap = 1.17B × 25~30 = $29-35B
  对应股价 = 29~35B / 346M 股 = $84-101（软·未罚 SBC）
若罚 SBC（FCF−SBC<0）→ 无正锚，趋近 0
```

即使用**最宽容的不罚 SBC 口径**（25-30x FCF），公允价也仅 **$84-101**——现价 $260 是其 2.6-3.1 倍。若按框架标准罚 SBC，则无正锚。

**保守给个"框架外软锚"区间 $110-140**（在 $84-101 宽容 FCF 口径上再给一些数据云稀缺性溢价），现价 $260 仍高出 **~85-135%**。

护栏检查：
- **`FCF − SBC = −$0.45B < 0`** → 成长估值不合格 ✗（同 SNAP/ORCL 出局标准）
- **高增长封顶**：g~26% 本应封顶 30x，但需正常化正 EPS，无 → 无法套用 ✗
- **无净现金托底**：净现金仅 ~$2B（2% MCap），非 LI 式期权结构 ✗
- **回购非真缩股**：靠发债堵稀释，$11.1B 未归属 RSU 待稀释 ✗

## 综合判定（静态两行）

| 要素 | 证据 | 判定 |
|------|------|------|
| 好公司 | 数据云护城河真实（Marketplace 网络效应）+ 产品 +34% 加速；但 GM 67% 偏低、GAAP 从未盈利、`FCF−SBC<0`、SBC 32%、被 Databricks 侵蚀 | 半✓（护城河真实但盈利质量差 + 竞争侵蚀） |
| 一次性麻烦 | **无麻烦**——股价从底反弹一倍、无困境。SBC 稀释 + 竞争是结构性且未反映在价格 | ✗（无困境可捡，且结构问题未定价） |

（"好价格"行 + 安全边际% + 最终定档见 `analysis.price.md`）

归类：**买贵了 + 价值陷阱-on-SBC 双重不合格**——
- 缺好价格：P/S 17.9x（软件最贵档）、非 GAAP 142x、股价近高位无回撤、公允价软估 $110-140 vs 现价 $260（高出 ~85-135%）→ **买贵了**
- 价值陷阱特征：`FCF−SBC<0`、GAAP 从未盈利、$11.1B RSU 稀释洪水、回购靠发债堵——**SBC 伪 FCF**，即使便宜也是价值陷阱

**不给席位**（既贵又有 SBC 侵蚀结构问题）。与 SNAP/ORCL 同一出局标准（`FCF−SBC<0`）；但护城河比 SNAP 强，故不完全等同价值陷阱，归"框架外·买贵了为主"。

**关注信号（转正需同时满足）**：① GAAP 转正盈利（非仅非 GAAP）；② `FCF−SBC > 0` 且真实缩股（停止发债堵稀释）；③ 股价大幅回落至 $110-140 软锚区；④ NRR 企稳、抵御住 Databricks。四者不齐不入池。
**降级信号**：产品增速跌破 25% / NRR 续降 / Databricks IPO 后加速抢份额 / SBC 占营收回升。
