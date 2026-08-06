# CRM — Task C：增长前瞻 + 护城河 + 管理层 + 消息面
> 更新: 2026-08-06

## C.1 增长前瞻（产出 g）

### 本地基线

| # | 数据 | 值 | 来源 |
|---|------|-----|------|
| 1 | 营收 3yr CAGR | 9.82% | (41.52/31.35)^(1/3)-1, income_annual col0/col3（FY26/FY23） |
| 2 | OpInc 3yr CAGR | 68.68% | (8.92/1.86)^(1/3)-1, col0/col3；⚠ 失真：FY23 OpInc $1.86B 低基数（Slack 收购+重组） |
| 3 | EPS 3yr CAGR | 233.65% | (7.80/0.21)^(1/3)-1；⚠ 失真：FY23 EPS $0.21 低基数 + 回购扭曲 |
| 4 | 近期季度 YoY | +13.3% | Q1'27 $11.13B vs Q1'26 $9.83B |
| 5 | PEG 隐含 g | 29.1% | P/E 22.13 / PEG 0.76, info.json |
| 6 | info.json revenueGrowth | 13.3% | Q1 YoY（同 #4，重复） |
| 6 | info.json earningsGrowth | 52.2% | EPS YoY（含回购+低基数扭曲） |

### 外部判断

| # | 数据 | 值 | 来源 |
|---|------|-----|------|
| 7 | 分析师共识 3-5yr 营收 CAGR | ~11% | targetMeanPrice $241.72（53 analysts, rating Buy 1.66） |
| 8 | 管理层 FY30 目标 | $63B（FY26 $41.5B → 4yr CAGR 11.0%） | Q1 FY27 财报 |
| 9 | Agentforce ARR | $1.2B（+205% YoY） | Q1 FY27 财报 |
| 10 | Agentforce+Data360 ARR | $2.9B（+200%） | Q1 FY27 财报 |

### G-3 综合判断

```
Step 1 列全部 g 源（8 个）:
  9.82, 68.68, 233.65, 13.3, 29.1, 13.3(dup), 52.2, 11.0, 11.0

Step 2 剔除不可靠源（judgment）:
  ✗ #2 OpInc CAGR 68.68%  — 跨增长阶段（FY23 低基数 $1.86B → hypergrowth → mature）
  ✗ #3 EPS CAGR 233.65%   — 同上 + 回购扭曲（G-4b "回购不进 g"）
  ✗ #6 earningsGrowth 52.2% — 回购+低基数扭曲
  ✗ #6 revenueGrowth 13.3% — 重复 #4

Step 3 剔最高 1 个（机械保守偏置）:
  ✗ #5 PEG g 29.1% — 最高

Step 4 均值:
  剩余 [9.82, 13.3, 11.0, 11.0] → avg = 45.12 / 4 = 11.28%

Step 5 定性调整: 无
  （Agentforce +205% 作上行期权不计入基线；增速降级已反映在历史 CAGR）
```

**g = 11%**

> g=11% 高于旧值 10%（旧用"保守交集"非 G-3 "剔高+均值"）。G-3 均值含管理层 FY30 目标 11% + 分析师共识 11% + Q YoY 13.3% + 营收 CAGR 9.82%，剔 PEG 29.1%（最高）后均值 = 11.28% → 11%。

### g 质量护栏

- [✓] FCF − SBC = $11.11B > 0（cf_ttm 2026-04-30）
- [✓] 回购不进 g（g=11% 用营收 CAGR + 前瞻共识 + 管理层目标，不含缩股 EPS 增长）
- [✓] 增长持续性（CRM 市占第一 + Agentforce 生态 + 切换成本）
- [✓] g = 11% < 22% → 不封顶

## C.2 护城河

- **壁垒类型**: 切换成本 + 规模 + 生态
  - CRM 市占第一（全球 #1 CRM 平台）
  - 极高切换成本（企业核心数据+流程锁定）
  - Data Cloud + Agentforce 生态（29,000+ 客户交易）
  - Slack + Informatica 数据底座（并购整合强化）
- **份额趋势**: 核心 CRM 稳固；Agentforce 抢 AI 工作流
- **核心威胁（关键未决）**: AI agent 是否颠覆 **seat-based（按席位收费）** 模式?
  - 若 AI 减少人工席位 → 利空
  - 若 Agentforce 让 CRM 按"AI 消耗/成果"变现 → 利好
  - **新进展（7/2026）**: Agentforce Help Agent 推出 **pay-per-resolution 定价**——直接回应 seat-based 颠覆疑虑
  - $1.6B 联邦合同验证企业价值
  - 这是 CRM 估值的核心多空分歧（决定折扣 ×0.60 存疑档）
- **宽度: 宽** → 质量评分 +1（但 AI 范式问号是真实威胁）

## C.3 管理层

| 项目 | 事实 |
|------|------|
| CEO | Marc Benioff（联合创始人，61 岁，生 1964-09-25） |
| **继任/退休** | **无**（创始人 CEO，无退休公告） |
| COF/CFO | Robin Washington（President, COO & CFO） |
| 内部人 | Benioff exercised $17.6M 期权（弱看空，可能税务规划）；heldPercentInsiders 2.99% |
| 资本配置 | **激进债务融资低位回购**（Q1'27 单季缩股 12%）+ 分红 $1.76/yr + Informatica 收购；转型"利润率优先" |
| 指引 vs 实际 | Q1 FY27 beat（$11.13B +13%），但全年指引偏软 → 股价承压 |
| 治理 | 干净；无 VIE / 无双层股权；杠杆陡升是新风险 |

## C.4 消息面（近 3 月）

- 2026.07.27: **$1.6B 联邦合同**——退伍军人事务部 3 年 Agentforce 合约（[Motley Fool](https://www.fool.com/investing/2026/07/27/salesforce-won-a-16-billion-federal-ai-contract-on/)）
- 2026.07.09: **KeyBanc 降级**至 Sector Weight——"Agentforce as a product just isn't there"（[Sirocco Group](https://www.siroccogroup.com/salesforce-got-downgraded-over-agentforce-the-real-story-is-your-data/)）
- 2026.07.06: Agentforce Commerce 大版本发布（Shopper/Buyer/Merchant Agent GA，ChatGPT 集成）（[Salesforce](https://www.salesforce.com/ap/news/press-releases/2026/07/06/)）
- 2026.07.07: $1B 瑞士投资（5 年 AI 技能）（[Salesforce](https://www.salesforce.com/news/press-releases/2026/07/07/1-billion-ai-transformation-investment-switzerland/)）
- 2026.06.29: **Agentforce Help Agent + pay-per-resolution 定价** GA（[Salesforce](https://www.salesforce.com/news/stories/agentforce-help-agent-announcement/)）
- 2026.04.30: Q1 FY27 营收 $11.13B +13%、GAAP EPS $2.42 +52%、Agentforce ARR 破 $1.2B

Delta vs 上次分析（2026-07-28）: 无新增（9 天前已分析）。结论不变：g=11%（G-3 修正，旧 10%）、存疑档。

## C.5 熊市逻辑

1. **估值**: 正常化 P/E 24.8x（$192.98/$7.77），GAAP P/E 22.4x；合理价 $151.52 < 现价 → 安全边际 −27.4%
2. **增长**: 增速结构性降至 ~11%（已远离 25-30% 超高速期）——估值降级的根因
3. **竞争**: AI agent 可能颠覆 seat-based 收费模式（核心风险）；KeyBanc 称"Agentforce product isn't there"
4. **资本**: 杠杆从净现金陡升至净债 ~$30B + GW 占 62%；投资收益虚增 GAAP NI；SBC 8.3%
5. **管理层**: 全年指引偏软 → 股价 YTD −27%

## C.6 牛市逻辑

1. **估值**: P/E 5yr 分位 0.6th（5yr 最低端）；P/S 3.7x（历史低位 6-10x）、FCF yield 9.3%（历史高位 2-4%）；企业软件第二便宜（仅次于 ADBE 14.8x）
2. **增长**: Q1'27 +13.3% 加速；Agentforce ARR $1.2B（+205%）+ Data360 $2.9B（+200%）；**$1.6B 联邦合约**验证企业价值
3. **护城河**: 78% GM 稳；CRM 市占第一；**pay-per-resolution 定价**= 从 seat-based → outcome-based 转型；29,000+ Agentforce 客户
4. **资本**: FCF $14.66B（利润率 34%）；**单季缩股 12%**（管理层用 $25B 发债回购表态"股价便宜"）；利润率扩张（OpM 20%→22-24%）
5. **催化**: Agentforce ARR 续翻倍 → 整体重加速回 ≥15% → 存疑升档 ×0.67；去杠杆 → BS 修复
