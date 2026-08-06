# AFRM — Task C：增长前瞻 + 护城河 + 管理层 + 消息面
> 更新: 2026-08-06

## C.1 增长前瞻（产出 g）

### 本地基线

| # | 数据 | 值 | 来源 |
|---|------|-----|------|
| 1 | 营收 3yr CAGR | 33.7% | (3.22/1.35)^(1/3)-1, income_annual col0/col3（FY25/FY22） |
| 2 | OpInc 3yr CAGR | N/A | FY22 −$796M → FY25 +$338M（负→正，无法算 CAGR） |
| 3 | EPS 3yr CAGR | N/A | FY22 −$2.51 → FY25 +$0.15（负→正，无法算 CAGR） |
| 4 | 近期季度 YoY | +32.6% | Q1'27 $1.04B vs Q1'26 $783M |
| 5 | PEG 隐含 g | 99% | P/E 71.3 / PEG 0.72, info.json；⚠ 失真（刚转正、基数极低） |
| 6 | info.json earningsGrowth | 3529% | EPS YoY（含低基数扭曲） |
| 6 | info.json revenueGrowth | 32.6% | Q1 YoY（同 #4，重复） |

### 外部判断

| # | 数据 | 值 | 来源 |
|---|------|-----|------|
| 7 | 管理层 FY26 营收指引 | $4.18-4.21B（vs FY25 $3.22B = +30-31% YoY） | [StockTitan](https://www.stocktitan.net/sec-filings/AFRM/8-k-affirm-holdings-inc-reports-material-event-9ba73cefcecb.html) |
| 8 | 分析师共识 | Buy，target $83.89（31 分析师） | [public.com](https://public.com/stocks/afrm/forecast-price-target) |
| 9 | GMV YoY | +35%（$11.6B FQ3'26） | [Investing.com](https://ca.investing.com/news/company-news/affirm-q3-2026-slides-35-gmv-growth-gaap-profitability-achieved-93CH-4620726) |
| 10 | FY26 GMV 指引 | $49.3-49.6B | 同 #7 |

### G-3 综合判断

```
Step 1 列全部 g 源:
  33.7, N/A, N/A, 32.6, 99, 3529, 32.6(dup), 30.5, 35(GMV)

Step 2 剔除不可靠源:
  ✗ #2 OpInc CAGR — N/A（负→正）
  ✗ #3 EPS CAGR — N/A（负→正）
  ✗ #5 PEG g 99% — 失真（刚转正、EPS 近零基数 → g 虚高）
  ✗ #6 earningsGrowth 3529% — 失真（低基数）
  ✗ #6 revenueGrowth 32.6% — 重复 #4
  ✗ #9 GMV +35% — GMV ≠ 营收增长（take rate 变动），不直接作 g 源

Step 3 剔最高 1 个:
  ✗ #1 营收 CAGR 33.7% — 最高

Step 4 均值:
  剩余 [32.6, 30.5] → avg = 31.55%

Step 5 定性调整: 无
  （高增长但信用周期未经验证；增速在减速 FY23→24 +45.9% → FY24→25 +38.8% → Q1'27 +32.6%）
```

**g = 32%**（≥22% → PE 封顶 30x）

> g=32% 基于营收 Q YoY 32.6% + 管理层 FY26 指引 30.5%，剔营收 CAGR 33.7%（最高）。增速减速中（+45.9%→+38.8%→+32.6%），但 g≥22% 一律封顶 30x，精确值不影响 PE。

### g 质量护栏

- [✓] FCF − SBC = +$484M > 0（cf_ttm 2026-03-31）
- [✓] 回购不进 g（g 用营收增长）
- [△] 增长持续性：GMV 高增长但信用周期未经验证；BNPL 竞争激烈
- [✓] g = 32% ≥ 22% → 封顶 30x

## C.2 护城河

- **壁垒类型**: 双边网络（商户+消费者）+ 自有承保数据/风控模型 + Shopify/Amazon 集成
- **份额趋势**: GMV 高增长（+35% YoY），但 BNPL 赛道低切换成本、消费者多平台并用
- **威胁**: **Apple Pay Later、PayPal Pay in 4、Klarna、Afterpay（Block 旗下）** 均有巨大既有用户基与深口袋——AFRM 的承保模型是差异点但**持续被测试**
- **宽度: 窄** → 质量评分不加 +1

## C.3 管理层

| 项目 | 事实 |
|------|------|
| CEO | Max Levchin（创始人，PayPal 联创，2012 创立 AFRM） |
| **继任/退休** | **无**（创始人 CEO） |
| 资本配置 | **零回购、零分红**，SBC 净稀释（Net Return −$302M）；靠发债/证券化为放贷融资 |
| 争议策略 | Levchin 押注 0% APR 贷款（Pay in X），2025 致股价单日 −13%（[CNBC](https://www.cnbc.com/2025/05/09/affirm-drops-13percent-on-weak-forecast-skepticism-of-ceos-bet-on-0percent-loans.html)） |
| 指引 vs 实际 | FY26 兑现 GAAP 盈利里程碑（Q4 FY25 首次 GAAP 经营盈利） |
| 治理 | 干净；无 VIE / 无双层股权 |

## C.4 消息面（近 3 月）

- 2026.05.07: FQ3'26 GMV +35%、达成 GAAP 盈利里程碑（[Investing.com](https://ca.investing.com/news/company-news/affirm-q3-2026-slides-35-gmv-growth-gaap-profitability-achieved-93CH-4620726)）
- 2026.07.01: Citi 上调目标至 $115（[public.com](https://public.com/stocks/afrm/forecast-price-target)）
- Card 业务 +159% YoY（Q2'26）= 新增长引擎
- 拨备率升至 6.0% of loans（5.4%→5.7%→6.0%）= 信用边际趋紧
- 股价从 52W 低 $42.5 反弹至 $78.5（+85%）

Delta: vs 旧 stub（8/01）无新增实质变化。

## C.5 熊市逻辑

1. **估值**: P/E 70x、P/B 7.0x（放贷机构极端泡沫——银行 1-2x、最优 fintech 3-4x）；EV/EBITDA 53x；安全边际 −147%
2. **杠杆放贷本质**: D/E 2.4x、$9.1B 债、interest coverage **1.7x**（脆弱）；拨备升至 6.0%（信用恶化边际）；cohort NCO ~3.5% of GMV
3. **信用周期**: 刚转正一个完整年度，**未经衰退检验**；失业率上升 → 违约升 + GMV 降双杀
4. **零回报**: 零回购、零分红、SBC 净稀释（Net Return −$302M）；股数 3 年 +28%（281M→361M）
5. **竞争**: BNPL 红海——Apple/PayPal/Klarna/Afterpay 深口袋围剿

## C.6 牛市逻辑

1. **高增长**: GMV +35%、营收 +33%；Card 业务 +159% 新引擎
2. **GAAP 转正**: 首次完整年度盈利（FY25 EPS $0.15→TTM $1.10）
3. **承保模型**: 自有风控数据差异化（宣称优于 FICO）
4. **Amazon/Shopify**: 深度集成大商户
5. **分析师**: Buy 共识，Citi 目标 $115
