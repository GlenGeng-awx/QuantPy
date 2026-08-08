# SNAP — Task C：增长前瞻 + 护城河 + 管理层 + 消息面
> 更新: 2026-08-08（财报 Q2'26 = 2026-08-03 发布）

## C.1 增长前瞻（产出 g）

### 本地基基线（G-1，免费 CSV + info.json）

| # | 数据 | 值 | 来源 |
|---|------|-----|------|
| 1 | 营收 3yr CAGR | **8.83%** | income_annual `(5.93B/4.60B)^(1/3)−1`（2022→2025） |
| 2 | OpInc 3yr CAGR | N/A | OpInc 3yr 全负（−1.40B→−787M→−532M），CAGR 不适用 |
| 3 | EPS 3yr CAGR | N/A | EPS 3yr 全负（−0.89→−0.42→−0.27），CAGR 不适用 |
| 4 | 近期季度 YoY（Q2'26 vs Q2'25） | **+19.0%** | income_quarterly `1.60B/1.34B−1` |
| 5 | PEG 隐含 g | N/A | trailingEps 负（−$0.18）→ PEG 失真（info.json pegRatio 508.87 无意义） |
| 6 | info.json revenueGrowth | 18.9% | 与 #4 重叠（Q2 YoY），不重复纳入 |

### 外部判断（G-2，web search）

| # | 数据 | 值 | 来源 |
|---|------|-----|------|
| 7 | 分析师 FY26/27 营收增速共识 | **+12.5%**（FY26 +12.54%、FY27 +12.49%） | [Yahoo Finance SNAP/analysis](https://finance.yahoo.com/quote/SNAP/analysis/)（FY26 $6.67B / FY27 $7.51B） |
| 8a | 管理层 Q3'26 营收指引 | $1.70–1.74B（midpoint +14% YoY） | [Q2'26 Investor Letter](https://s25.q4cdn.com/442043304/files/doc_financials/2026/q2/Q2-2026-Prepared-Remarks.pdf)、[Snap IR Q2'26 PR](https://investor.snap.com/news/news-details/2026/Snap-Inc--Announces-Second-Quarter-2026-Financial-Results/default.aspx) |
| 8b | 管理层 Q3'26 Adj EBITDA 指引 | $300–350M（YoY ~+100%，vs Q3'25 ~$100M） | 同上 |
| 8c | FY26 基建成本指引上调 | $1.65–1.70B（AI/ML 投入） | 同上 |

> 分析师 EPS 共识（Yahoo）：FY26 −$0.07、FY27 **+$0.12**（首次全年 GAAP 转正）。info.json forwardEps $0.77 系调整口径（non-GAAP），GAAP 共识 $0.12 更保守。

### 综合判断（G-3）

- **近期 vs 3yr**: 加速（Q2 +19% vs 3yr CAGR 8.83%）。但加速主因 = Snapchat+ +85% 订阅 + 世界杯广告 spend + Ad tech 改善；3yr CAGR 包含 hypergrowth 早期不可外推
- **管理层 vs 分析师**: Q3 指引 +14% YoY（世界杯后正常化）/ FY26-27 共识 +12.5% — 两者一致，Q2 +19% 为短期峰值
- **长期可持续性**: 广告市场长期增速 ~5-8%、订阅渗透 <3% → 头空间至 7-12%（行业基准）、Specs AR 眼镜非 2030 前不指望；长期 g 合理 8-12%
- **结构性拖累**: NA DAU 持平（92M）、广告仅 +9%（vs 总营收 +19%）— 增长靠订阅/低变现地区，非核心广告

**G-3 Step 2 剔除（不可靠）**:
- #5 PEG（亏损，失真）
- #4 Q YoY（订阅+世界杯扭曲，非经营增长斜率）
- #6 与 #4 重复
- #8a Q3 指引（单季，含季节性；forward_g.md 明文："季度指引含季节性/短期因素，不等同长期 g"）

**G-3 Step 3 剔除最高**: 剩余源 = 3yr CAGR (8.83%) + 分析师共识 (12.5%)。剔除最高 (12.5%)。

**G-3 剩余**: 3yr CAGR 8.83% 单源 → 剩余源 ≤ 1，直接用该值（per forward_g.md 特殊情况）

**g = 9%**（8.83% 上调整至 9%，反映 NA DAU 持稳 + Ad tech 改善 + 订阅头空间；仍低于分析师共识 12.5% 与指引 +14%）

### g 质量护栏（G-4）

- [✗] **FCF − SBC > 0**：−$325M < 0 → **重麻烦 ×0.40 硬规则触发**（不否决，合理价照算）
- [✓] 回购不进 g：g 用营收/经营增长（不含缩股驱动 EPS 增长，且 SNAP 3yr 仍在稀释）
- [⚠] 增长持续性：护城河窄（TikTok/Meta 三面夹击）、核心北美 DAU 持平（不再流失但未恢复）、广告 +9% 与总营收 +19% 背离 = 增长靠订阅而非核心广告
- [✓] g ≥ 22% → 封顶 30x：g=9% 不触发

## C.2 护城河

- **壁垒类型**: 网络效应（年轻用户社交）+ 品牌（AR/相机差异化）
- **份额趋势**: 北美 92M DAU **持平**（Q2'26，vs 之前 YoY −7% 已止跌）；MAU 971M 增长；Spotlight 美国发帖用户 +115% YoY、DAV +20% — 用户参与度回升
- **威胁**:
  - **Meta（IG/Reels）+ TikTok + YouTube** 三面夹击，差异化（AR/相机）被更强资源复制
  - 监管风险：青少年安全/隐私/年龄验证诉讼待审
  - Specs AR 眼镜 $2,195 高定价，量产普及预计 2030 前
- **宽度: 窄** → 质量评分护城河项 ✗（不加 1 分）

护城河宽度 = **Task D 折扣系数的质量评分第 7 分**（+1 = 宽）→ ✗ 不加分

## C.3 管理层

| 项目 | 事实 |
|------|------|
| CEO | Evan Spiegel（联创，34 岁；2011 创立至今 15 年） |
| **继任/退休** | **无**（联创 CEO，未宣布交接计划）|
| 内部人增减持 | 2026-01-02: Spiegel 售 1.26M 股 @$8.001 (~$10.1M) — **Rule 10b5-1 预设计划**（2025-09-04 采纳），非即时决策；2026-05-19: GC Briers 售 71,745 股 (~$0.41M)。**无公开市场增持**。insiderscreener 统计近 12 月 ~$64.6M 卖出（全部 10b5-1）— 弱看空但程序化（[secform4.com](https://www.secform4.com/insider-trading/1699293.htm)、[stocktitan](https://www.stocktitan.net/sec-filings/SNAP/form-4-snap-inc-insider-trading-activity-90b5ac5c824d.html)、[quiverquant](https://www.quiverquant.com/news/Insider+Sale:+General+Counsel+of+$SNAP+Sells+71,745+Shares)） |
| 资本配置 | TTM 回购 $851M 被 SBC $1.03B 吞噬，Net Return −$179M（股东价值净流出）；**2027 起实施多年回购计划**（CFO Hott 在 Q2 电话会议承诺），主要用 FCF 资助 "稳定股本" — 资本配置转向积极 |
| 指引 vs 实际 | Q2'26 EPS −$0.10 实际 vs 共识 −$0.12（**连续 4 季 beat**，surprise +18-189%）；营收 Q2'26 $1.60B vs $1.55B 共识（beat 3%） |
| 治理风险 | 双层股权（Spiegel/Murphy 超级投票权 ~99% 控制）；青少年安全/隐私诉讼待审（state AG 调查中）；SBC 全标的最高 |

### 红线检查

- 零分红 + TTM Net Return 负 → 重大负面（但 2027 起承诺改变）
- CEO 联创在位、无继任计划 → 不影响
- 无 VIE（美股本土）、无双层股权除超级投票权外无重大治理瑕疵
- 创始人 10b5-1 程序化减持 → 弱看空（非即时决策，且仍持 22.4% insiders 总持仓）

## C.4 消息面（近 3 月）

- **2026-08-03**: Q2'26 财报发布（[Snap IR](https://investor.snap.com/news/news-details/2026/Snap-Inc--Announces-Second-Quarter-2026-Financial-Results/default.aspx)）— 营收 $1.60B +19% YoY、Adj EBITDA $250M（+ $208M YoY）、净亏 −$164M（YoY 改善 $99M）、FCF $121M（TTM $706M）、DAU 493M、NA DAU 92M 持平、Q3 指引 $1.70–1.74B（+14% YoY）+ Adj EBITDA $300–350M
- **2026-08-04**: Q2 电话会议（[Yahoo/GuruFocus](https://finance.yahoo.com/markets/stocks/articles/snap-inc-snap-q2-2026-050622199.html)）— 多元营收引擎（Snapchat+/Memory/Lens+）、Specs 9-16 发布会、FY26 基建指引上调至 $1.65–1.70B（AI/ML）、2027 起多年回购计划
- **2026-05-19**: GC Briers 售 71,745 股 ~$0.41M（10b5-1）
- **2026-01-02**: CEO Spiegel 售 1.26M 股 ~$10.1M @ $8.001（10b5-1）
- **2025-09-04**: Spiegel 采纳 10b5-1 卖出计划（后续执行上述销售）
- 即将 2026-09-16: Specs AR 眼镜发布（定价 $2,195，量产普及预计 2030 前）

**Delta vs 上次分析（2026-08-01 stub）**: **重大变化** — Q2'26 财报（5 天前发布）显示：(1) NA DAU 从 −7% YoY 改善至持平；(2) 广告增速从 +3% 加速至 +9%；(3) FCF 连续 8 季为正；(4) 管理层承诺 2027 起多年回购稳定股本。**结构性熊点（NA DAU 流失、回购被 SBC 吞噬）部分缓解**，但 FCF−SBC<0 与 GAAP 持续亏损未变 → 重麻烦档不变。

## C.5 熊市逻辑

1. **估值**: EPS 负 → EPS 模型 N/A；唯一估值口径 DCF FCF（乐观上限）= $11.6（base g=10% capped）；FCF−SBC<0 → 主口径应取 FCF−SBC 但其 N/A；P/B 4.3x 对亏损公司偏贵；有形净资产 $0.06B 几乎为零
2. **增长**: 3yr 营收 CAGR 8.83% 仍亏损 → 增长不经济；广告仅 +9% vs 总营收 +19%（增长靠订阅，非核心）；Q3 指引 +14% 已从 Q2 +19% 放缓
3. **竞争**: NA DAU 92M 持平（不流失但未恢复）；TikTok/Meta/YouTube 三面夹击；广告业务规模不经济（GM 57% <60% 阈值，vs META 82%）
4. **资本**: FCF−SBC = −$325M（烧钱式增长）；3yr 股数 1.61B→1.69B（+5% 稀释）；Net Return −$179M；SBC 16.2%/Rev（全标的最高之一）；累计亏损 −$14.8B
5. **管理层**: Spiegel 10b5-1 程序化减持 ~$10M（2026-01）；治理双层股权超级投票权；青少年安全诉讼待审

## C.6 牛市逻辑

1. **估值**: P/S 1.42x（vs 历史 >20x，深跌 94% 自 $83 ATH）；P/FCF 12.7x（如果信 FCF 真实）；分析师目标均价 $7.28（vs 现价 $5.33 隐含 +37%）
2. **增长**: Q2'26 +19% YoY 加速；Snapchat+ +85% 订阅增长（<3% 渗透 → 行业基准 7-12% 头空间）；AI 驱动广告效率（cost per purchase −18%、app purchase volume +128%、Sponsored Snaps CTR +226%）；Spotlight 美国发帖用户 +115% YoY
3. **资本**: 8 连季 FCF 为正（TTM $706M）；CFO Hott 承诺 2027 起多年回购稳定股本；SBC/Rev 从 28.7% (2023) 降至 16.2% (TTM) — 纪律改善
4. **催化**: Specs AR 眼镜 2026-09-16 发布（首发优势）；FY27 GAAP EPS 首次转正 +$0.12 共识；多元营收（订阅+硬件）减少广告依赖；FCF 拐点 → 可同时投资 Specs/回购/降杠杆
5. **质量**: Adj EBITDA TTM 9M vs 3yr 前 −$1.1B（巨幅改善）；Q3 指引 Adj EBITDA $300–350M（YoY +200%+）；NA DAU 持平（vs 之前 −7%）= 核心市场止跌

## C.7 与上次结论对比

上次（2026-08-01 stub）: "框架外（亏损+FCF−SBC<0）→ 不纳入"。但该结论违反 `CLAUDE.md` 硬规则: **"FCF−SBC<0 → 重麻烦 → ×0.40，不否决、总是估值"**。本次按硬规则重新估值。

主要变化: Q2'26 财报后，结构性熊点部分缓解（NA DAU 止跌、广告增速回升、回购承诺稳定股本），但 FCF−SBC<0 未变（仍重麻烦 ×0.40）。
