# SNOW — Task C：增长前瞻 + 护城河 + 管理层 + 消息面
> 更新: 2026-08-08

## C.1 增长前瞻（产出 g）

### 本地基线

| # | 数据 | 值 | 来源 |
|---|------|-----|------|
| 1 | 营收 3yr CAGR | 31.4% | income_annual FY2026 $4.68B vs FY2023 $2.07B, ^(1/3)−1 |
| 2 | OpInc 3yr CAGR | N/A | 负→更负（−$842M→−$1,440M），CAGR 无意义 |
| 3 | EPS 3yr CAGR | N/A | 负→更负（−$2.50→−$3.95），CAGR 无意义 |
| 4 | 近期季度 YoY | +33.5% | income_quarterly Q1'27 $1.39B vs Q1'26 $1.04B |
| 5 | PEG 隐含 g | N/A | 亏损 → trailingPE 负 → PEG 失真（pegRatio 8.0 基于非 GAAP forward EPS）|
| 6 | info.json revenueGrowth | 33.5% | YoY 营收增长 |

### 外部判断

| # | 数据 | 值 | 来源 |
|---|------|-----|------|
| 7 | 分析师共识 | FY27 +29.9%, FY28 +25.7%, 长期 ~26.5% | [Yahoo Finance analysis](https://finance.yahoo.com/quote/SNOW/analysis/)（FY27 Rev $6.08B vs $4.68B, FY28 $7.65B vs $6.08B）|
| 8 | 管理层指引 | FY27 产品收入 +31%（从 27% 上调至 31%）| [Snowflake Q1 FY27 IR](https://www.snowflake.com/en/news/press-releases/)（2026-05 财报）|

### 综合判断

- 近期 vs 3yr: Q YoY +33.5% vs 3yr CAGR 31.3% → **加速/平稳**（增速未减速）
- 管理层 vs 分析师: 管理层 +31% > 分析师 +29.9%（一致区间，管理层略乐观）
- 分析师 FY27→FY28: +29.9%→+25.7%（减速趋势，长期 ~26.5%）

**g 源处理**:
- Step 2 剔除: OpInc CAGR（N/A）、EPS CAGR（N/A）、PEG（失真，亏损+非GAAP）
- Step 2 候选: 3yr Rev CAGR（hypergrowth→maturity 不可外推，但当前增速仍 30%+，保留但降权）
- Step 3 剔最高: Q YoY 33.5%（单季波动，与 info.json 33.5% 重复）
- 剩余: 3yr CAGR 31.4%, 分析师 FY27 29.9%, FY28 25.7%, 长期 26.5%, 管理层 31%
- 平均 = (31.4+29.9+25.7+26.5+31)/5 = 28.9% ≈ 29%

Step 5 定性调整: **g = 20%**（从 29% 降至 20%）
- 营收增长 30%+ 不转化为 GAAP 利润（亏损扩大中）
- FCF−SBC < 0（烧钱式增长，增长靠稀释融资）
- Databricks 以 65% 增速抢食（run-rate $6.9B 已超 SNOW $5.03B）
- NRR 逐季下滑（客户留存/扩张恶化）
- SBC 32%/Rev = 增长用股权稀释购买，非有机价值创造
- 即便 g=20%，仍 ≥22% 的封顶阈值不适用（20% < 22%），PE = 28.5x

### g 质量护栏

- [✗] FCF − SBC > 0 → **-$456M < 0 → 重麻烦 ×0.40**（硬规则触发）
- [✓] 回购不进 g: g 用业务/营收增长，不含缩股 EPS 增长（SNOW 本就在稀释，无缩股）
- [✗] 增长持续性: 护城河真实但被侵蚀（Databricks 65% 增速），NRR 下滑
- [✓] g = 20% < 22% → 不封顶 30x（但 DCF 中 g > r=11% → P/FCF 封顶 30x）

## C.2 护城河

- 壁垒类型: **数据云平台 + Marketplace 数据网络效应**（数据集/应用越多越黏）+ 存储迁移成本 + 多云中立
- 份额趋势: 数据仓库仍最大，但 **Databricks（Lakehouse + AI/ML）以 65% 增速快速逼近**（run-rate $6.9B 已超 SNOW $5.03B TTM），技术差距缩小
- 威胁:
  1. Databricks 正面竞争（增长 2x 于 SNOW）
  2. 云厂商原生方案（BigQuery/Redshift/Fabric）
  3. 开源格式（Iceberg）降低锁定
  4. 客户垂直整合风险
- **宽度: 中** → 质量评分不 +1（护城河真实但被侵蚀中，非宽）

护城河真实（这是"好公司"的一面），但**正被增长更快的对手边缘化**——非纯情绪伤口，有结构性竞争侵蚀成分。

## C.3 管理层

| 项目 | 事实 |
|------|------|
| CEO | Sridhar Ramaswamy（58 岁，前 Google 广告/Neeva 创始人，2024 接替 Frank Slootman）|
| **继任/退休** | **无公告**（2026-08 web search 无退休/交接新闻）|
| 内部人 | CEO 2026-07 获 **$448M 绩效 RSU**（1M 股，绑定股价目标）→ 额外 SBC 稀释（[Reuters](https://www.reuters.com/technology/snowflake-unveils-448-million-pay-plan-ceo-tied-ambitious-stock-targets-2026-07-16/)）|
| 资本配置 | 发 $2.3B 零息可转债回购堵 SBC 稀释；零分红；Goodwill $2.05B（并购扩张）|
| SBC 趋势 | SBC/Rev 从 41.6%(FY2023) 降至 32.2%(TTM) → 在降但仍极高 |
| 指引 vs 实际 | 连续 beat + 上调 FY27 指引（27%→31%）→ 执行力强 |
| 治理风险 | SBC 稀释持续股东价值转移；$11.1B 未归属 RSU 洪水；双层股权 |

> CEO $448M RSU 赏赐（2026-07）= 新增 SBC 洪水，绑股价目标 = CEO 有强动机推高股价但代价是进一步稀释。

## C.4 消息面（近 3 月）

- 2026-08-03: SNOW 将在投资者会议上展示；Q2 FY27 财报定于 9 月 2 日发布（[Snowflake IR](https://www.snowflake.com/en/news/press-releases/snowflake-to-announce-financial-results-for-the-second-quarter-of-fiscal-2027/)）
- 2026-07-28: Snowflake 推出 Agentic Enterprise 监控和成本管理产品（[Snowflake PR](https://www.snowflake.com/en/news/press-releases/snowflake-advances-the-trusted-agentic-enterprise-era-with-unified-monitoring-and-cost-management/)）
- 2026-07-16: **CEO $448M 绩效 RSU 薪酬计划**，绑定股价目标（[Reuters](https://www.reuters.com/technology/snowflake-unveils-448-million-pay-plan-ceo-tied-ambitious-stock-targets-2026-07-16/)）
- 2026-06-02: **Snowflake Summit 2026** — 重大产品发布: CoCo（AI 编码代理）、CoWork（知识工作者 AI 代理）、Horizon Catalog（治理）、Interoperable Lakehouse（开放框架）（[Snowflake PR](https://www.snowflake.com/en/news/press-releases/)）
- 2026-06-02: 客户合作: Thomson Reuters、Sanofi 选择 SNOW 加速 AI（[Snowflake PR](https://www.snowflake.com/en/news/press-releases/thomson-reuters-powers-trusted-enterprise-ai-at-scale-on-snowflake/)）
- 2026-05: Q1 FY27 财报: 产品收入 +34% YoY，上调 FY27 指引至 31%，$6B AWS 采购承诺（已反映在 TTM CSV 中）
- 股价从 2026-04 低点 ~$121 反弹至 2026-08 的 $330（+173%），受 AI 叙事 + Q1 强业绩驱动

Delta: vs 上次分析（2026-07-04 base），新增: CEO $448M RSU（重大治理事件）、Summit 产品发布（AI 转型深化）、股价翻倍以上。核心问题（FCF−SBC<0、GAAP 亏损、SBC 稀释）未改变。

## C.5 熊市逻辑

1. **估值极贵**: P/S 22.3x（软件最贵档之一），GAAP 无 P/E（亏损），非 GAAP P/E ~170x，距 52W 低 +173% 近高位无安全边际
2. **GAAP 从未盈利**: NM −23.8%，5 季 EPS 全负，留存收益 −$10.09B（累计巨亏）
3. **FCF−SBC = −$456M < 0**: 真实现金创造为负，SBC $1.62B > FCF $1.17B，SBC/Rev 32.2%
4. **SBC 稀释洪水**: $11.1B 未归属 RSU = 6.8x 年 SBC；CEO 新获 $448M RSU；3yr 股数 +7.2%（持续稀释）；回购靠发 $2.3B 债堵 = 财技非真缩股
5. **Databricks 侵蚀**: 65% 增速 vs SNOW 31%，run-rate $6.9B 已超 SNOW $5.03B，技术差距缩小
6. **NRR 逐季下滑**: 净收入留存持续恶化（客户扩张减速）
7. **OCF 增速塌方**: 3yr +27% → TTM +1.2%

## C.6 牛市逻辑

1. **数据云护城河真实**: Marketplace 网络效应 + 迁移成本 + 多云中立，数据仓库仍最大
2. **营收 +33.5% 加速**: Q1'27 $1.39B，FY27 指引 +31%（从 27% 上调），增长引擎完好
3. **AI 叙事强劲**: Cortex/CoCo/CoWork 产品矩阵，Summit 2026 重大发布，OpenAI 合作
4. **CapEx 极轻**: $70M / OCF 6%，轻资产模式
5. **管理层执行力**: 连续 beat + 上调指引，SBC/Rev 从 41.6% 降至 32.2%（改善中）
6. **净现金正**: $0.18B（虽薄但非净负债）
