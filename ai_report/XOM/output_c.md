# XOM — Task C：增长前瞻 + 护城河 + 管理层 + 消息面
> 更新: 2026-08-09　⚠️ 周期股（g 用业务量增，价格周期不进 g）

## C.1 增长前瞻（产出 g）

### 本地基线（income_annual CSV，col0=FY25, col3=FY22, year_gap=3）

> PRINT header 验证: `['2025-12-31','2024-12-31','2023-12-31','2022-12-31','2021-12-31']` → col0=FY25, col3=FY22, year_gap=3 ✓

| # | 数据 | 值 | 来源 |
|---|------|-----|------|
| 1 | 营收 3yr CAGR | **-6.4%** | (323.9/398.7)^(1/3)-1 — 油价周期下行，**不可靠剔除** |
| 2 | OpInc 3yr CAGR | **-18.9%** | (33.94/64.03)^(1/3)-1 — 油价峰回落，**不可靠剔除** |
| 3 | EPS 3yr CAGR | **-19.7%** | (6.70/13.26)^(1/3)-1 — 油价+回购扭曲，**不可靠剔除** |
| 4 | 近期季度 YoY | Q1'26 -43.2% / Q2'26 +112% | Q1'26 $1.00 vs $1.76；Q2'26 $3.48 vs $1.64 — 周期摆动，**不可靠剔除** |
| 5 | PEG 隐含 g | 21.5% | trailingPE 26.0 / pegRatio 1.21 — TTM EPS 低谷扭曲，**不可靠剔除** |

> 周期股 g 源诊断：本地 g 全部由油价周期主导（2022 峰→2025 谷），不代表可持续增速。PEG 用低谷 EPS 算出 21.5% 虚高。全剔除。

### 外部判断（web search）

| # | 数据 | 值 | 来源 |
|---|------|-----|------|
| 6 | 分析师 3-5yr LTG | **4.15%** | [Chartmill](https://www.chartmill.com/stock/quote/XOM/analyst-ratings) |
| 7 | 管理层指引 | Permian **9% volume CAGR 至 2030**；Guyana 5th FPSO 4Q26 启产 | [Exxon IR Q2'26 PR](https://investor.exxonmobil.com/company-information/press-releases/detail/1208/exxonmobil-announces-second-quarter-2026-results) |
| 8 | 2026 EPS 共识 | $9.21（vs FY25 $6.70 = +37% YoY 恢复）| [Simply Wall St](https://simplywall.st/stocks/us/energy/nyse-xom/exxonmobil-holdings)（via Google snippet）|
| 9 | 2026 分析师目标价 | $165.58 共识 / BofA $158 | [public.com](https://public.com/stocks/xom/forecast-price-target)；[BofA via TheStreet](https://www.thestreet.com/investing/bofa-just-turned-on-exxon-in-favor-of-chevron) |

### 综合判断（G-3 Step 1234）

```
g 源:
  营收 3yr CAGR -6.4%      油价周期下行，不可靠
  OpInc 3yr CAGR -18.9%    油价峰回落，不可靠
  EPS 3yr CAGR -19.7%      油价+回购扭曲，不可靠
  Q YoY -43%/+112%         周期摆动，不可靠
  PEG 21.5%               TTM 低谷 EPS 扭曲，不可靠
  分析师 LTG 4.15%         长期共识
  mgmt Permian 9%          仅上游子业务量增，非全公司

Step 2 剔除:
  营收 CAGR -6.4%          油价周期扭曲（CAGR 跨峰谷）
  OpInc CAGR -18.9%        油价周期扭曲
  EPS CAGR -19.7%          油价+回购扭曲
  Q YoY -43%/+112%         周期摆动
  PEG 21.5%               低谷 EPS 扭曲
  mgmt Permian 9%          口径过窄（仅上游子业务量增）

Step 3 剔除:
  （仅剩 1 源，不需剔最高）

Step 4:
  仅剩 1 源 → 直接用: 4.15% ≈ 4%
```

- **g = 4%**（分析师 LTG 4.15% 取整保守；本地 g 全剔除——油价周期扭曲 CAGR 不可外推）
- g 用业务量增（Guyana/Permian 低成本桶 + 结构性成本节约 $16.3B 累计），不含缩股。油价是外生周期变量，不进 g。

### g 质量护栏
- [✓] FCF − SBC > 0（$18.79B - $0 = $18.79B）
- [✓] 回购不进 g（g 用业务量增，不含缩股）
- [✓] 增长持续性（Guyana Stabroek 全球成本曲线最左端 + Permian 核心区 + 一体化平滑周期 → 量增可持续）
- [✓] g < 22%（4% 远低于封顶，PE = 8.5+4 = 12.5x）

## C.2 护城河

- **壁垒类型**: 低成本储量（Guyana Stabroek 全球成本曲线最左端之一、Permian >1.8 Moebd 记录）+ 一体化（上游+炼化+化工平滑周期）+ 规模 + 43 年股息记录（资本纪律信誉）
- **份额趋势**: 稳固（Guyana 权益 45% Stabroek、Permian 龙头；5th FPSO 4Q26 +250 Kbd 产能；储量寿命长）
- **威胁**: 能源转型长期需求见顶风险、油价周期外生不可控、OPEC+ 供给政策、**无定价权**（commodity price-taker）
- **本质**: price-taker — 护城河体现在"比同行更低的桶成本 + 更强的资产负债表扛周期"，**不是定价权** → 只配"好公司"，非"伟大"
- **宽度: 中等** → 质量评分 +0（不宽，不达 +1 阈值）

## C.3 管理层

| 项目 | 事实 |
|------|------|
| CEO | Darren Woods（2017-01 至今，~9.5yr；生于 1965-12-16 = 60 岁；内部晋升，前任 Rex Tillerson 退休交接）|
| **继任/退休** | **无公告**（web search 无退休/继任/过渡信号；60 岁未到 Exxon 强制退休年龄 65）|
| 内部人 | 未查到 Form 4 异常增持/减持（未深查，非主要催化）|
| 资本配置 | TTM 回购 $20.34B + 分红 $17.23B = $37.57B；43 年连增股息（Q3'26 $1.03/季 = $4.12/年已宣布）；CapEx $28.93B 投 Guyana/Permian；H1'26 股东回报 $9.4B |
| 指引 vs 实际 | Q2'26 adj EPS $3.52 vs 共识 $3.56 = slight miss（-1.1%）；Q1'26 EPS $1.00 大幅低于共识（underlying earnings $8.77B YTD 口径仍强）|
| 治理 | 2026-07-01 Texas 重组（redomiciliation merger，charter/by-laws 全面修订）；无 VIE、无双层股权 |

> 红线检查: 无零回购+零分红（43 年连增）✓；无 CEO 突发离职/空缺 ✓；无创始人售股异常 ✓。

## C.4 消息面（近 3 月）

- **2026-07-31**: Q2'26 财报 EPS $3.48 GAAP / $3.52 adj（YoY +112%，H1'26 EPS $4.47 vs H1'25 $3.40 = +31.5%）；OCF $23.6B、FCF $17.2B、股东回报 $9.4B；Permian 9% CAGR 至 2030 重申；5th Guyana FPSO 启航 4Q26 启产（[Exxon IR](https://investor.exxonmobil.com/company-information/press-releases/detail/1208/exxonmobil-announces-second-quarter-2026-results)）
- **2026-07-28**: BofA 降级 Buy→Neutral，PT $154→$158（ cited limited upside + oil price decline risks）（[TheStreet](https://www.thestreet.com/investing/bofa-just-turned-on-exxon-in-favor-of-chevron)）
- **2026-07-01**: Texas redomiciliation merger 生效（charter/by-laws 修订；NYSE 交易 7/1 暂停后恢复）（[Yahoo Finance](https://finance.yahoo.com/energy/articles/exxonmobil-xom-texas-move-governance-191244612.html)）
- **2026-08-06**: MarketBeat 共识 Hold（Q2'26 EPS miss $0.04；BS 支撑长期）（[MarketBeat](https://www.marketbeat.com/instant-alerts/exxonmobil-corporation-nysexom-receives-consensus-recommendation-of-hold-from-analysts-2026-08-06/)）
- California 诉讼：trial date Oct 2026（[StocksToday](https://stockstoday.com/exxon-mobil-navigates-legal-and-operational-challenges/)）
- 证券欺诈集体诉讼：Exxon 胜诉（jury trial）（[Compass Lexecon](https://www.compasslexecon.com/cases/exxon-mobil-prevails-in-rare-securities-fraud-class-action-jury-trial)）

Delta: vs 旧 base（2026-07-04）— 新增 Q2'26 财报（强劲反弹）、BofA 降级、Texas 重组生效。thesis 不变（周期下行 + 好公司 + 等好价格）。

## C.5 熊市逻辑

1. **估值贵**：P/B 2.43x 处 5yr 82nd 分位（vs 5yr 高 2.68、低 1.26）= 市场并未把它当低谷贱卖；P/E 26x 反读但非周期底（P/E 分位 60th 未 >70%、P/B 分位 82th 未 <30% = **非周期底部信号**）；中周期合理价 ~$106 vs 现价 $153 = 安全边际 -44%
2. **油价软**：TTM EPS $5.94 是周期低谷（Q1'26 $1.00 季度最低），WTI ~$68、JPM 见 2026 Brent ~$60；GM 从 22.8% → 16.7%（-6.1pct/5Q）
3. **FCF 紧**：TTM FCF $18.79B 仅覆盖股息 $17.23B 1.09x；Net Return $37.57B > FCF = 动用 BS + 举债（TTM 发债净 +$8.77B）；CapEx/OCF 61% 重
4. **行业**：能源转型长期需求见顶；commodity 无定价权；OPEC+ 供给政策外生
5. **ROE 低**：ROIC 7.2%、ROE 12.6%（周期低谷，资本回报不达 15% 优秀线）

## C.6 牛市逻辑

1. **全行业最强 BS**：D/E 0.19、利息覆盖 42.5x = 周期下行扛得住；股息覆盖油价 <$40（管理层承诺）；43 年连增不断
2. **增长兑现**：Guyana 5th FPSO 4Q26 启产（+250 Kbd 产能）；Permian >1.8 Moebd 记录、9% CAGR 至 2030 重申；Q2'26 EPS $3.48 YoY +112%（周期回升已启动）；结构性成本节约累计 $16.3B（行业最高）
3. **估值锚**：中周期正常化 EPS $8.5 × 12.5x（8.5+g=4）= $106 合理价；满仓 $71（×0.67，= P/B 1.16x + 股息率 5.8%）；分析师目标 $165-170（隐含 +8-11%）
4. **催化**：油价若回升（Brent $80+）则 EPS + FCF 双弹；Guyana 满产 + Permian 量增持续兑现
