# NVO — Task C：增长前瞻 + 护城河 + 管理层 + 消息面
> 更新: 2026-08-02（FY26 Q1 @ 2026-05-06 已发；Q2 ~2026-08 待发）

## C.1 增长前瞻（产出 g）

### 本地基线（免费，income CSV + info.json）

| # | 数据 | 值 | 来源 |
|---|------|-----|------|
| 1 | 营收 3yr CAGR | **10.0%** | income_annual：309.06B/232.26B ^(1/3)−1 |
| 2 | OpInc 3yr CAGR | 7.6% | 127.66B/102.57B ^(1/3)−1（3yr 近乎停滞，−0.5% 绝对） |
| 3 | EPS 3yr CAGR | 7.3% | 23.03/18.62 ^(1/3)−1（⚠ 受回购/一次性扭曲） |
| 4 | 近期季度 YoY | **+24.0%**（Q1'26 vs Q1'25，但 vs 弱基数） | income_quarterly |
| 5 | PEG 隐含 g | 3.2% | trailingPE 11.26 / pegRatio 3.49 |
| 6 | info.json 增长率 | earningsGrowth 67.1% / revenueGrowth 24%（Q1 单季 YoY） | info.json |

### 外部判断（web search）

| # | 数据 | 值 | 来源 |
|---|------|-----|------|
| 7 | 分析师 3-5yr 共识 | 长期营收 +3.6%/EPS +0.5% p.a.（保守派 SimplyWall）；2027 起恢复双位数（多数派） | web |
| 8 | 管理层指引 | 2026 营收/利润 **−4~−12%**（原 −5~−13%，Q1 后上调）；2027 恢复双位数 | Q1'26 电话会 |

### 综合判断（G-3 Step 1234）

**Step 2: 剔除明显不可靠**

| # | 源 | 值 | 剔/留 | 理由 |
|---|------|-----|-------|------|
| 1a | 营收 3yr CAGR | 10.0% | 留 | 营收最可靠，不易被操纵 |
| 1b | OpInc 3yr CAGR | 7.6% | 剔 | TTM 含强 Q1'26 拉高；B.1 SCORECARD 3yr OpInc −0.5%（FY25 口径）→ CAGR 跨增长阶段不可外推（G-3 Step 2 判据） |
| 1c | EPS 3yr CAGR | 7.3% | 剔 | ⚠ 受回购/一次性扭曲，仅参考（G-1 1c 本身标注） |
| 1d | 季度 YoY | 24.0% | 剔 | 单季 YoY 有并购扭曲（Catalent 并购 + 弱基数），不代表经营增长（G-3 Step 2 判据） |
| 1e | PEG 隐含 g | 3.2% | 留 | 市场预期参照，EPS 非近零起步 → PEG 无失真 |
| 1f | info.json | 67.1% | 剔 | Q1 单季 YoY，非长期 g |
| 2a | 分析师 3-5yr | 3.6% | 留 | 保守派 SimplyWall 长期共识 |
| 2b | 管理层指引 | −4~−12% | 不纳入 | 2026 全年指引，口径不对（年度非长期 g） |

**Step 3: 剔除剩余最高 1 个（保守偏置）**

剩余: 1a 营收 CAGR 10.0%, 1e PEG 3.2%, 2a 分析师 3.6%
剔除: 1a 营收 CAGR 10.0%（最高 → 保守偏置）
剩余: 1e PEG 3.2%, 2a 分析师 3.6%

**Step 4: 算术平均**

g = (3.2 + 3.6) / 2 = 3.4% ≈ **3%**

**Step 5: 定性调整**

无额外调整。穿越中枢即便乐观假设 2027 恢复也只 ~5%（2026 −8% + 2027 +13% + 2028 +12% → 3yr CAGR ≈5%），3% 不假设份额稳住/恢复双位数（LLY 在抢份额、CagriSema 输、GM 侵蚀）。原 g=8% 把历史 10% 狂热期 CAGR 折不够 + 假设存疑恢复 → 违反 lean conservative，且与 de-rating 判断"40x→11x 大部分合理范式切换"自相矛盾。

> 敏感性: g=0%（结构崩/LLY 赢家通吃）/ g=3%（基准保守）/ g=5%（2027 恢复）/ g=8%（恢复+份额稳，旧乐观口径）

### g 质量护栏

- [✓] FCF − SBC > 0（+28.6B DKK，一票否决未触发）
- [✓] 回购不进 g（NVO 回购温和 ~1%，g 用业务增长）
- [△] 增长持续性：护城河宽但被侵蚀（LLY 抢份额、GM 下滑），g 可信度打折
- [✓] g = 3% < 22%，PE 不封顶 30x

## C.2 护城河

- 壁垒类型: semaglutide 品牌（Ozempic/Wegovy 全球认知）+ 肽类生物制药**生产工艺 + 产能壁垒**（GLP-1 产能全球瓶颈，NVO+LLY 双寡头）+ 专利 + 监管审批
- 份额趋势: ⚠ **正在流失**——LLY 占美国 GLP-1 组合 **60.1%** vs NVO **39.4%**；LLY 在美国外也已反超；tirzepatide（Zepbound）减重效力 25.5% > CagriSema 23%
- 威胁: LLY orforglipron 口服 GLP-1（Phase 3 达标、全球提交中，直接威胁 NVO 口服 Wegovy）；semaglutide 化合物专利 ~2031-2032 悬崖；美国 MFN 降价；compounding 复方药灰色竞争
- **宽度: 宽（双寡头之一 + 产能壁垒 + TAM 巨大）但正在被侵蚀** → 质量评分 +1（区别 ADBE"纹丝不动不可撼动"，NVO 是"两强分食且对手在领先"的动态战场）

## C.3 管理层

| 项目 | 事实 |
|------|------|
| CEO | **Mike Doustdar，2025-08-07 上任**（原 International Ops EVP，10 年把国际业务翻倍至 DKK 112B），接替 Jorgensen（因股价暴跌 + CagriSema 失望被换） |
| **继任/退休** | **已完成换帅**（Jorgensen 被换下，Doustdar 接任）——换帅本身是"承认危机"信号，新 CEO 主打 semaglutide + 国际扩张 |
| 组织 | R&D 合并为统一单元，Martin Holst Lange 任 CSO（2025-08） |
| 内部人 | Novo Nordisk Foundation 控股（长期稳定大股东，正面） |
| 资本配置 | 2026 CapEx 指引 DKK 55B（从 2025 60B 回落，产能投资见顶）；DKK 15B/年回购（~1% 市值，2026-02 起已回购 2,096 万股 @ 均价 DKK 266）；持续派息（增速 ~7.5%/年至 2030） |
| 指引 vs 实际 | Q1'26 beat（+32% cc，口服 Wegovy 翻倍），但全年指引仍下滑 |
| 治理 | Novo Nordisk Foundation 控股（双层股权，但 Foundation 长期主义，非负） |

## C.4 消息面（近 3-6 月）

- **2026-05-06 Q1'26 财报**: 营收 +32% cc、口服 Wegovy 首季 $354M（翻倍超预期）、上调全年指引至 −4~−12%（[CNBC](https://www.cnbc.com/2026/05/06/wegovy-glp1-weight-loss-novo-nordisk-earnings-stock-nvo-ozempic.html)、[BioPharma Dive](https://www.biopharmadive.com/news/novo-nordisk-wegovy-pill-sales-prescriptions-q1-2026/819418/)))
- **2026-03-19**: FDA 批准高剂量 Wegovy（[CNBC](https://www.cnbc.com/2026/03/19/fda-approves-high-dose-version-of-novo-nordisks-obesity-drug-wegovy.html))
- **2026-02-24**: CagriSema REDEFINE 4 头对头输给 tirzepatide（23% vs 25.5% 减重），股价重挫（[CNBC](https://www.cnbc.com/2026/02/24/healthy-returns-whats-next-for-novo-nordisks-obesity-drug-cagrisema.html))
- **2025-11**: 与 Trump 政府 MFN 降价协议（NVO+LLY 均降价，低-中双位数%）
- **LLY 2026 反超**: 美国份额 60% + orforglipron Phase 3 达标 + 上调 EPS 指引至 $35.5-37（[CNBC](https://www.cnbc.com/2026/02/04/eli-lilly-novo-nordisk-earnings-glp1-market.html)、[GxP News](https://gxpnews.net/en/2026/05/eli-lilly-overtakes-novo-nordisk-in-glp-1-market-share-outside-us/))

Delta: Q2'26 财报待发（~2026-08-05），前无新重大事件；消息面截至 2026-07-04 仍当前。

## C.5 熊市逻辑

1. **竞争**: LLY 全面领先（美国份额 60% vs NVO 39%、orforglipron 口服 Phase 3 达标、Zepbound 效力 25.5% > CagriSema 23%）份额持续流失
2. **利润**: 美国 MFN 降价 + 中/巴/加专利到期压 GM（84.6%→81.0%）；2026 负增长年（指引 −4~−12%）
3. **专利**: semaglutide 化合物专利 ~2031-2032 悬崖
4. **资本**: FCF 被产能 CapEx 吞噬 −58%（70B→31B）、净负债 104B DKK 无托底
5. **估值**: de-rating 大部分合理（40x→11x 是范式切换非错杀）；CagriSema next-gen 落后

## C.6 牛市逻辑

1. **估值**: P/E 11.3x（5yr 6.5th 分位）买全球 GLP-1 双寡头之一、GM 81%+、NM 37%、ROE 71%
2. **增长**: 减重 TAM $100B/2030 仍在扩张（"水涨船高"两强都能赢）；2027 起指引恢复双位数
3. **护城河**: 双寡头 + 产能壁垒 + 品牌（宽，虽被侵蚀）
4. **催化**: 口服 Wegovy 首季 $354M 翻倍超预期 + Medicare 新覆盖 + 高剂量 Wegovy 获批；产能 CapEx 2026 见顶回落 → FCF 有望恢复；新 CEO 主打国际扩张（其强项）；分红+回购持续
