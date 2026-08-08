# TTD — Task C：增长前瞻 + 护城河 + 管理层 + 消息面
> 更新: 2026-08-08（**Q2'26 财报 8/6 报告后**，CSV + web search 更新）

## C.1 增长前瞻（产出 g）

### 本地基线（CSV income_annual + income_quarterly + info.json）

| # | 数据 | 值 | 来源 |
|---|------|-----|------|
| 1 | 营收 3yr CAGR | 22.4% | ($2.90B/$1.58B)^(1/3)−1, 2022→2025（**hypergrowth 不可外推**） |
| 2 | OpInc 3yr CAGR | 73.4% | ($589M/$113M)^(1/3)−1（**hypergrowth**） |
| 3 | EPS 3yr CAGR | 101.5% | ($0.90/$0.11)^(1/3)−1（**hypergrowth + 回购扭曲**） |
| 4 | Q2'26 YoY | **+3.0%** | $715M vs $694M（CSV） |
| 5 | PEG 隐含 g | stale | info.json pegRatio 0.84, trailingEps $0.66（stale pre-Q2）→ EXCLUDE |
| 6 | info.json | revenueGrowth 11.8%, earningsGrowth −20% | stale pre-Q2 → EXCLUDE |

### 外部判断

| # | 数据 | 值 | 来源 |
|---|------|-----|------|
| 7 | 分析师 FY26 共识 | +9.8% avg（range 5.4%–11.0%）→ **$3.18B** | [StockAnalysis.com](https://stockanalysis.com/stocks/ttd/forecast/)（36 分析师, HOLD, Aug 7 更新） |
| 8 | 分析师 FY27 共识 | +9.6% → $3.48B | 同上 |
| 9 | Q3'26 管理层指引 | Rev ≥$650M → **−12.0% YoY**（$650M vs $739M Q3'25） | [ADWEEK](https://www.adweek.com/programmatic/the-trade-desk-ceo-jeff-green-says-sluggish-3-revenue-growth-not-a-reflection-of-the-company/) |
| 10 | Q3'26 EBITDA 指引 | ~$160M（margin ~25% vs 39% LY） | 同上 |
| 11 | H1'26 实际 | +7%（$1.40B vs $1.31B） | CSV Q2'26+Q1'26 vs Q2'25+Q1'25 |

### 综合判断

- **增速断崖**: 22%→19%→15%→3%（Q2'26）→ **−12%**（Q3 guide）→ 从高增长骤降至**营收收缩**
- **旧分析错误修正**: 旧 output_c 标 Q3'26 guide "+3.5% YoY" — **实际 −12.0%**（$650M vs Q3'25 $739M，CSV 确认）。旧分析用错误基期（可能用 Q3'25 = $628M 而非实际 $739M）。
- 管理层归因: ① macro（CPG+Auto 关税冲击，占 25% 业务）② 执行（Kokai 滚出问题、品牌转向低价 fixed-price/programmatic guaranteed）
- 但 Meta 同期 +24% → macro 解释力弱 → 有结构性成分（Amazon 竞争 + DSP 分裂）
- CFO Olmstead: "visibility somewhat more limited than in recent history"，guide 假设 "no meaningful improvement in Q3"

### G-3 计算

```
Step 2 剔除不可靠源:
  1a/1b/1c → hypergrowth CAGR，不外推
  1e PEG → stale
  1f info.json → stale
  2a 分析师 FY26 +9.8% → stale（H1 $1.40B + Q3 $650M guide → FY26 max ~$2.82B = −3%，+9.8% 不可能）

Step 3 剔除剩余最高:
  剩余: Q2'26 +3.0%、Q3 guide −12.0%、FY27 +9.6%
  剔最高 +9.6%（FY27 stale）

Step 4 均值:
  剩余: +3.0%, −12.0%
  avg = (3.0 + (−12.0)) / 2 = −4.5%

Step 5 定性调整 +7%:
  +3% JBP 6x 增速 + 国际 +30% + top 100 double-digit（结构性增长引擎仍在）
  +2% Zuma 升级（8月）+ 新 CFO/C-suite 落定 + Google 反垄断 tailwind
  −1% Amazon 结构性压力（可补贴定价）+ margin 塌陷（Q3 25% vs 39%）
  −1% OpenPath 反弹 + Publicis 信任受损
  净: +3%

g = −4.5% + 3% = −1.5% → 封底 0% → 但考虑 JBP/intl 结构性增长
最终 g = 3%（保守估计：低于市场 5-10% 增速反映 Amazon 份额侵蚀风险，
        但高于 0% 反映 TAM 增长 + JBP/international 支撑）
```

> **旧 g=5% → 新 g=3%**（Q3'26 guide −12% 修正 + 结构性压力，部分被 JBP/intl 抵消）

> ⚠ 分析师 FY26 +9.8% 明显 stale：H1 $1.40B + Q3 $650M = $2.05B → Q4 需 $1.13B（+33% vs Q4'25 $846M）→ 不现实。即使低估计 +5.4% → Q4 需 $1.01B（+19%）→ 仍激进。

### g 质量护栏

- [✓] FCF − SBC > 0（TTM +$396M、H1'26 +$193M）
- [✓] 回购不进 g（g 用营收增速，$974M 回购是安全边际）
- [△] 增长持续性（JBP +6x、intl +30% 支撑；但 Amazon + margin 塌陷侵蚀）
- [✓] g < 22% → 无封顶

## C.2 护城河

- 壁垒类型: **独立性（唯一规模化 DSP 无自有广告库存）+ 规模/数据飞轮 + UID2 身份图**
  - 独立性 vs Google/Amazon 自有库存偏向 → 客观性优势
  - 20M ad ops/秒、AI 决策、95%+ 客户留存 10 年+
  - Netflix 库存整合 + Samsung 智能电视首页广告（[ADWEEK](https://www.adweek.com/programmatic/the-trade-desk-ceo-jeff-green-says-sluggish-3-revenue-growth-not-a-reflection-of-the-company/)）
- 份额趋势: **收窄**——Amazon DSP 零售媒体抢份额（Amazon 广告收入 TTM $76B）、Meta +24% vs TTD +3%（Q4'25）、DSP 市场分裂
- 威胁: **Amazon DSP**（可补贴定价 across retail/AWS/Prime 经济）、Google DV360（整合 Gemini AI）、OpenPath 反弹（代理商撤资）、Kokai 执行问题、Publicis 纠纷（信任受损）
- **宽度: 中**（独立性论点成立 + AI/Google 反垄断 tailwind，但定价权受压 + 执行失误 + Amazon 压力） → 不 +1

## C.3 管理层

| 项目 | 事实 |
|------|------|
| CEO | **Jeff Green**（联合创始人/CEO/President/Chairman，仍在任） |
| **继任** | **无公告** |
| CFO | **Nate Olmstead**（2026-07 新任；前 Penguin Solutions CFO）→ **解决了 interim CFO 问题**（前 CFO Alex Kayyal 离职） |
| C-suite 重建 | 2026 全新: COO Vivek Kundra、CMO Sarah Gavin、CCO Kristi Argyilan、董事会 Penry Price（ex-Google/LinkedIn）→ **整个商业团队换血** |
| 高管离职潮 | 前任: CCO Tim Sims、CRO Jed Dederick + 继任 Anders Mortensen（7 个月离职）、CSO Samantha Jacobson、CFO Alex Kayyal、CMO Ian Colley、3 名董事会成员 |
| 内部人 | Green 持股 ~10.77%（创始人 heavy）；无重大减持 flagged |
| 资本配置 | $974M 回购 TTM（aggressive）；无分红；SBC 15.1% 极高 |
| 指引 vs 实际 | Q2'26 miss（$715M vs 共识 $752M，−4.9%）；Q3 guide $650M vs 共识 $804M（−19.2%）；Adj EPS $0.34 vs 共识 $0.41（−17.1%） |
| 治理 | Publicis 纠纷（Green: "behind us"但信任受损）；CFO 一年四换（已落定）；新团队"early in learning process" |

> CEO Green: "These numbers are not a reflection of our company or the long-term opportunity in front of us. We underperformed our own expectations."（[ADWEEK](https://www.adweek.com/programmatic/the-trade-desk-ceo-jeff-green-says-sluggish-3-revenue-growth-not-a-reflection-of-the-company/)）

> Green on AI: "A DSP is a platform built to decide which of those ad impressions you buy and which you don't, and of course, that is enhanced by AI… I wouldn't say that the DSP model is going to be disrupted by AI. It is AI."

## C.4 消息面（近 3 月）

- **2026-08-06**: **Q2'26 财报**: Rev $715M（+3%，miss −4.9%）、Adj EPS $0.34（miss −17.1%）、Adj EBITDA $241M（margin 34% vs 39%）；**Q3 guide Rev ≥$650M（−12% YoY!）、EBITDA ~$160M（margin ~25%）** → 股价 −27% 至 $12.87 盘前 → $13.80 收盘（−21.9%）（[ADWEEK](https://www.adweek.com/programmatic/the-trade-desk-ceo-jeff-green-says-sluggish-3-revenue-growth-not-a-reflection-of-the-company/), [Zacks/Yahoo](https://finance.yahoo.com/markets/stocks/articles/ttd-q2-earnings-call-flags-140000761.html)）
- **2026-08-07**: 分析师评级大幅下调: Strong Buy 15→6、Hold 17→22、Strong Sell 2→5；目标价均值 $17.55（中位 $16），范围 $9–$32（[StockAnalysis.com](https://stockanalysis.com/stocks/ttd/forecast/)）
  - D.A. Davidson: $29→$16 Hold
  - Cantor Fitzgerald: $20→$14 Hold
  - Benchmark: $30→$20 Buy
- **2026-08**: Zuma（Kokai 升级版）即将发布 — 改善导航 + AI 自动化工作流
- **2026-07**: 新 CFO Nate Olmstead 到任 + 新 C-suite 团队
- **2026-06**: Amazon DSP 竞争加剧（TTD 发文 likening Amazon to Google antitrust）；Amazon 广告 TTM $76B
- **2026-05**: OpenPath 反弹（代理商撤资）；Kokai 执行问题
- **2026-04**: TTD 向代理商示好（Green: "We want to help"），修复 Publicis/WPP/Dentsu 关系
- **2025-04**: Google adtech 反垄断裁决（Judge Brinkema: 非法垄断）→ DOJ 寻求拆分 → TTD 结构性 tailwind（缓慢）

Delta: vs 旧 output（8/7），**CSV 更新确认 Q2'26 实际数据 + Q3'26 guide YoY 修正 −12%（旧 +3.5% 错误）+ 分析师评级大幅下调**

## C.5 熊市逻辑

1. **增速塌陷+营收收缩**: Q2'26 +3%（15 年最低）、Q3 guide **−12%**（营收收缩！）→ 增长引擎熄火
2. **margin 塌陷**: Q3 guide EBITDA margin ~25% vs 39% LY → opex +6% vs rev +3%（cloud→自有数据中心 + AI 投入）
3. **Amazon 结构性**: Amazon DSP 可补贴定价（retail+AWS+Prime 经济）→ TTD take rate 受永久压力；Amazon 广告 $76B TTM
4. **执行失误**: Kokai 滚出问题 + OpenPath 代理商反弹 + Publicis 纠纷 → 自身产品 bet 踉跄
5. **高管离职潮**: CCO/CRO/CSO/CFO/CMO 全换 → 新团队"early in learning process" → 执行风险
6. **Meta 对比**: Meta Q4'25 +24% vs TTD +14%（同期 macro）→ macro 解释力弱 → 公司特有/结构性
7. **SBC 15.1%**: 吃 53.3% FCF；GAAP EPS 被 SBC 压低；回购仅部分对冲

## C.6 牛市逻辑

1. **估值**: P/E 5yr 0.0th（最低）、EV/EBITDA 7.8x（@ $13.80）、FCF yield 12.8%、EV/FCF ~6.6x
2. **FCF 强**: TTM $848M（+8.5% YoY）、H1'26 $412M（+19%）、无债净现金 $1.06B、OCF/NI 2.66
3. **JBP**: 217 clients（+38% YoY）、JBP 营收增速 6x overall → 合同性 recurring
4. **国际**: EMEA+APAC ~+30% YTD、CTV +50% YoY both regions
5. **Top 100 accounts**: 多数 double-digit 增长；top 500 外客户 >+50% YTD
6. **Google 反垄断**: 非法垄断裁决 + DOJ 拆分 → TTD 独立性价值提升（缓慢 tailwind）
7. **新团队 + Zuma**: CFO 落定 + C-suite 重建 + Zuma（8月 usability 升级）+ Audience Unlimited（open beta）→ 执行修复催化
8. **AI 定位**: 测试 Anthropic Claude AI campaign creation + Stagwell Koa agents + agent-to-agent 交易标准化 → DSP = AI 论点
9. **$1T TAM ~1%**: 市场仍大，TTD 渗透率低
