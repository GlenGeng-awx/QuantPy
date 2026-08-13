# XYZ — Task C：增长前瞻 + 护城河 + 管理层 + 消息面
> 更新: 2026-08-09（Q2'26 财报后，2026-08-05 发）

## C.1 增长前瞻（产出 g）

⚠️ **营收口径陷阱**：XYZ 营收 $25.04B **含 Bitcoin 交易额毛记账**（Cash App BTC 转售，近零毛利），Revenue CAGR 低估真实业务增长。**必须用毛利润（Gross Profit）口径**衡量增长。下文 g 源同时列 Rev 和 GP。

### 本地 g 基线

| # | 数据 | 值 | 来源 |
|---|------|-----|------|
| 1 | 营收 3yr CAGR（2025 vs 2022，gap=3） | 11.3% | income_annual（BTC 毛记账失真，低估） |
| 1b | **GP 3yr CAGR**（2025 vs 2022） | **20.0%** | income_annual（$5.99B→$10.36B，最 meaningful） |
| 2 | OpInc 3yr CAGR | N/A | 2022 负基数（−$27M），无法算 |
| 3 | EPS 3yr CAGR | N/A | 2022 负基数（−$0.93），无法算 |
| 4 | 近期季度 YoY（Q2'26 vs Q2'25） | Rev +9.4%、**GP +24.8%**、OpInc +32.6% | income_quarterly |
| 5 | PEG 隐含 g | 155%（141/0.91） | info.json — **失真**（EPS near $0.56，P/E 141x 虚高） |
| 6 | info.json 增长率 | earningsGrowth −83.3%（失真）、revenueGrowth +9.3% | info.json |

> CAGR 已 PRINT header 验证 year_gap：income_annual col0=2025, col3=2022, gap=3 ✓

### 外部判断

| # | 数据 | 值 | 来源 |
|---|------|-----|------|
| 7 | **FY2026 GP 指引**（上调） | **$12.51B，+21% YoY** | [Block IR / Zacks](https://finance.yahoo.com/markets/stocks/articles/blocks-q2-earnings-revenues-beat-183900653.html) |
| 8 | **Q4'26 exit rate** | **mid-teens（~15%）** | CFO Ahuja（[TIKR](https://www.tikr.com/blog/block-stock-fell-6-after-its-most-profitable-quarter-ever-heres-where-xyz-could-go-in-2026)） |
| 9 | Q3'26 GP 指引 | $3.13B，+18% YoY | Block IR（同上） |
| 10 | FY2026 adj EPS 指引 | $4.02（+70% YoY） | Block IR — 从 depressed base，非 sustainable |
| 11 | 分析师 consensus（FY26 adj EPS） | $3.90（Zacks） | [Zacks via Yahoo](https://finance.yahoo.com/markets/stocks/articles/blocks-q2-earnings-revenues-beat-183900653.html) |
| 12 | Street price target | ~$93 | [TIKR](https://www.tikr.com/blog/block-stock-fell-6-after-its-most-profitable-quarter-ever-heres-where-xyz-could-go-in-2026) |

### 综合判断（G-3 Step 1234）

```
g 源:
  营收 3yr CAGR 11.3%      BTC 毛记账失真，低估
  GP 3yr CAGR 20.0%        $5.99B→$10.36B，最 meaningful
  OpInc 3yr CAGR N/A        2022 负基数
  EPS 3yr CAGR N/A          2022 负基数
  Q2'26 GP YoY 24.8%       peak，指引减速
  PEG 155%                 EPS near $0.56，失真
  FY26 GP 指引 21%          管理层上调
  Q4 exit mid-teens ~15%   管理层 CFO Ahuja
  Q3'26 GP 指引 18%         减速趋势

Step 2 剔除:
  PEG 155%                 EPS near-zero 失真
  OpInc/EPS 3yr CAGR       负基数
  earningsGrowth -83.3%    一次性项扭曲
  Rev CAGR 11.3%           BTC 毛记账失真

Step 3 剔除:
  Q2'26 GP YoY 24.8%       peak，指引减速

Step 4:
  avg(20.0, 21, 15, 18) = 18.5%
```

**Step 5 定性调整**: 18.5% → **15%**（管理层 Q4 exit mid-teens 从 20% 历史减速；竞争激烈 + Neighborhoods 新引擎未验证）

- **g = 15%**（管理层 exit mid-teens，从 20% 历史减速的保守前瞻；不含回购）
- g 用 GP 增长（非 Revenue，因 BTC 毛记账失真）

### g 质量护栏

- [✓] FCF − SBC > 0（+$2.68B）
- [✓] 回购不进 g（g 用 GP 增长，非 EPS 缩股增长）
- [✓] 增长持续性（护城河中等，GP 加速中但 Q4 减速至 mid-teens；竞争激烈但 Neighborhoods 新引擎）
- [✗] g ≥ 22% → 封顶 30x：**否**（15% < 22%，不触发封顶；PE = 23.5x）

## C.2 护城河

- **壁垒类型**：Square（商户收单，硬件+软件生态、切换成本）+ Cash App（消费金融，59M MAU、9.4M 银行活跃 +17% YoY 的网络效应）双边生态；Afterpay（BNPL）
- **份额趋势**：Cash App MAU +3% YoY（放缓，靠 engagement 非 new users）；Square GPV +13.4%（U.S. +9.8%，2023 Q2 以来最强）；International GPV +28%
- **威胁**：支付红海（Stripe/PayPal/Adyen）、BNPL（Affirm/Klarna/Apple）、消费金融（Chime/Robinhood 银行化）——**无一方向有绝对护城河**，靠生态整合与执行
- **Neighborhoods**（新引擎）：Square→Cash App 桥接，年化 GPV $1B（+220% YoY），新卖家 onboarding 8x March pace → 早期但 promising
- **宽度：中**（无宽护城河，双边生态有网络效应但竞争激烈、无定价权）→ 质量评分不加分

## C.3 管理层

| 项目 | 事实 |
|------|------|
| CEO | **Jack Dorsey**（创始人，Block Head），2026 激进 AI 重组砍 40% 人力（10000→<6000） |
| **继任/退休** | **无宣布**（Dorsey 仍在位，无交接公告 — web search 确认） |
| CFO | Amrita Ahuja（仍在；Q2'26 call 主持） |
| 内部人 | ARK（Cathie Wood）6/17 重新买入 ~237K 股（机构，非内部人）；无内部人大额增持/减持记录 |
| 资本配置 | $1.89B 回购 TTM（>SBC $1.20B=真缩股）；$5.3B 剩余授权；零分红 |
| 重组 | 裁员 40%+，目标人均产出 $2M（重组前 ~$500K）；围绕 AI 重构组织，砍管理层 |
| 指引 vs 实际 | Q2'26 beat（adj EPS $1.02 vs $0.86 est），**连续 3 季上调 FY 指引** |
| 治理 | DOJ 调查（accrued $526M，from $240M Q1）；$45M 46 州 AG 和解（7 月）；SEC 调查 3 月关闭无执法 |

⚠️ Dorsey 的 AI 豪赌（砍半人力）是**高风险高回报**：H1'26 交付 130 features（3x YoY）= 执行证明；但若砸产品/增长=反转夭折。

## C.4 消息面（近 3 月）

- **2026-08-05**：Q2'26 财报 — record adj OpM 27%、GP +24.8%、adj EPS $1.02（beat $0.86）、上调 FY26 GP 至 $12.51B（+21%）、adj EPS $4.02（+70%）；**股价次日跌 6.15% 至 $79.02**（sell the news at 52w high, YTD +21%）[Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/blocks-q2-earnings-revenues-beat-183900653.html) / [TIKR](https://www.tikr.com/blog/block-stock-fell-6-after-its-most-profitable-quarter-ever-heres-where-xyz-could-go-in-2026)
- **2026-08-05**：CFO Ahuja 指 Q4 exit rate "mid-teens" GP 增长 → 减速信号；BTC gross profit −31%（deliberate Cash App fee cuts）；Cash App MAU 仅 +3% YoY [TIKR](https://www.tikr.com/blog/block-stock-fell-6-after-its-most-profitable-quarter-ever-heres-where-xyz-could-go-in-2026)
- **2026-07**：$45M 46 州 AG 和解（Cash App 欺诈保护）[PYMNTS](https://www.pymnts.com/legal/2026/block-pays-45-million-to-settle-46-state-probe-into-cash-app-fraud-protection-and-resolution/)
- **2026-Q2 10-Q**：DOJ accrued loss 升至 $526M（from $240M Q1），正在谈判和解，公司警告 ultimate loss 可能更高 [TIKR](https://www.tikr.com/blog/block-stock-fell-6-after-its-most-profitable-quarter-ever-heres-where-xyz-could-go-in-2026)
- **2026-03**：SEC 调查关闭，无执法行动 [TIKR](https://www.tikr.com/blog/block-stock-fell-6-after-its-most-profitable-quarter-ever-heres-where-xyz-could-go-in-2026)
- **2026-06-17**：ARK 重新买入 ~237K 股 [旧 base]

**Delta vs 旧 base（2026-07-04）**：Q2'26 财报确认 record 盈利 + 上调指引（符合预期）；DOJ accrued 翻倍（$240→$526M，超预期负面）；$45M 州和解落地（已知）；股价 sell-the-news 跌 6%（非旧 base 预期）。**结论方向不变**：好公司但买贵了。

## C.5 熊市逻辑

1. **估值**：GAAP P/E 141x（E=$0.56 被 BTC+重组压低，失真）；即使 adj P/E 19.7x（$79/$4.02 FY26 guide）对 NM 1.4%→adj ~8% 的薄利消费金融业务仍不便宜；FCF yield 8.2% 尚可但非深度价值
2. **增长**：GP 增速从 Q2'26 +24.8% 减速到 Q3 指引 +18% → Q4 exit mid-teens；Cash App MAU 仅 +3% YoY（engagement 非 new users）；BTC gross profit −31%（deliberate fee cuts）
3. **竞争**：支付/BNPL/消费金融全线红海，无宽护城河；Stripe/PayPal/Adyen/Affirm/Klarna/Chime/Robinhood 各方向挤压
4. **资本**：GAAP NM 仅 1.4%；DOJ $526M pending（可能更高）；重组 $1.96B/TTM 连续 5 年增长 = 经常性非一次性
5. **管理层**：Dorsey AI 豪赌（40% 裁员），若砸产品/增长=反转夭折；DOJ matter 持续升级

## C.6 牛市逻辑

1. **估值**：P/GP 4.1x（MCap $47.46B / GP $11.61B）、FCF yield 8.2%、前瞻 adj P/E ~17x NTM（TIKR）、street target $93（+18% upside）
2. **增长**：GP +24.8% Q2'26（record）、adj OpM 27%（record）、adj EBITDA $1.17B（+31%）、adj EPS +65% YoY；FY26 上调至 GP +21%
3. **护城河**：Neighborhoods inflection（$1B GPV +220%、sellers 8x March pace）、Square Financial Services 首笔 in-house acquiring（廉价存款 funding lending book）、AI 交付 130 features H1（3x YoY）
4. **催化**：AI 重组→利润率跃升路径在兑现（27% adj OpM）；Q3'26 GP +18% guidance（11/3 财报验证）；DOJ 和解落地=消除 overhang
