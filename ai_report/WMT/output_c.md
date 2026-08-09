# WMT — Task C：增长前瞻 + 护城河 + 管理层 + 消息面
> 更新: 2026-08-09

## C.1 增长前瞻（产出 g）

### 本地基线（G-1，免费）

| # | 数据 | 值 | 来源 |
|---|------|-----|------|
| 1 | 营收 3yr CAGR | 5.27% | income_annual（FY23→FY26, ^1/3） |
| 2 | OpInc 3yr CAGR | 13.45% | income_annual（⚠ FY23 低基数扭曲，剔除） |
| 3 | EPS 3yr CAGR | 24.21% | ⚠ 回购 + FY23 双重扭曲，剔除（回购不进 g） |
| 4 | 营收 2yr CAGR | 4.90% | income_annual（FY24→FY26, ^1/2） |
| 5 | OpInc 2yr CAGR | 5.08% | income_annual（FY24→FY26, ^1/2，恢复后正常增长） |
| 6 | 近期季度 YoY Revenue | +7.3% | Q1'27 vs Q1'26（income_quarterly col0 vs col4） |
| 7 | NI 3yr CAGR | 23.30% | ⚠ FY23 扭曲，剔除 |
| 8 | NI 2yr CAGR | 18.80% | FY24→FY26，仍含恢复溢价 |
| 9 | NI YoY (FY25→FY26) | 12.64% | 单年，业务增长参考 |
| 10 | PEG 隐含 g | 9.25% | trailingPE 39.5 / pegRatio 4.27（市场预期 EPS 增速，含回购） |
| 11 | info.json earningsGrowth | 19.4% | YoY 盈利增速（含一次性/回购） |

### 外部判断（G-2，web search，Q1 FY27 财报 May 21 2026）

| # | 数据 | 值 | 来源 |
|---|------|-----|------|
| 12 | Q1 FY27 Revenue YoY | +7.3%（+5.9% constant currency） | Walmart IR Q1 FY27 earnings release |
| 13 | Q1 FY27 Operating Income YoY | +5.0%（adjusted CC +5.1%） | 同上 |
| 14 | Q1 FY27 Global eCommerce | +26% | 同上 |
| 15 | Q1 FY27 Global advertising | +37%（Walmart Connect US +44% ex-VIZIO） | 同上 |
| 16 | Q1 FY27 Global membership fee | +17.4% | 同上 |
| 17 | Q1 FY27 Comp sales (ex fuel) | +4.1% | 同上 |
| 18 | 分析师 1Y target mean | $137.98（40 分析师，Buy 1.6） | Yahoo Finance |
| 19 | forwardPE / forward EPS | 38.17x / $3.28（隐含 EPS +15.5% YoY） | info.json |

### 综合判断（G-3）

**Step 2 剔除不可靠源:**
- 剔 #3 EPS 3yr CAGR 24.21%（回购 + FY23 双重扭曲，违反"回购不进 g"）
- 剔 #2 OpInc 3yr CAGR 13.45%（FY23 $20.43B 低基数，3yr 起点失真）
- 剔 #7 NI 3yr CAGR 23.30%（同 FY23 扭曲）
- 剔 #10 PEG 隐含 g 9.25%（EPS 基础，含回购；且 PEG 4.27 极高 = 市场乐观预期，非我方估计）

**Step 3 剔最高（保守偏置）:**
- 剔 #6 Q YoY Revenue +7.3%（单季，可能含一次性/季节性，不可外推）

**剩余源:**
- Revenue 3yr CAGR 5.27%
- Revenue 2yr CAGR 4.90%
- OpInc 2yr CAGR 5.08%
- NI YoY 12.64%（业务 NI 增长，含 margin expansion）

算术平均 = (5.27 + 4.90 + 5.08 + 12.64) / 4 = 27.89 / 4 = 6.97%

**Step 5 定性调整:**
- 广告（+37-44%）+ 会员（+17.4%）高 margin 引擎驱动 margin mix 上行 → NI 增长 > Revenue 增长
- 但 CapEx 重投入（自动化/电商）压制 OpInc 增长（Q1 OpInc 仅 +5.0%）
- 通胀环境 + 低价定位受益消费降级 → Revenue 增速稳健 5-7%
- 综合判断：业务 g 略高于平均，因 margin expansion 趋势明确，但保守取整

**g = 6%**（业务增长，剔回购；Revenue ~5-6% + margin expansion 1-2pp，保守下限）

- 近期 vs 3yr: Revenue 加速（5.27% → Q1 +7.3%），margin 引擎发力
- 管理层 vs 分析师: 管理层未给 FY27 明确长期 g 指引（季度口径），分析师隐含 EPS +9-15%（含回购），业务口径 ~6-7%
- **g = 6%**（剔回购，与 Revenue CAGR + margin expansion 一致，保守偏置）

### g 质量护栏（G-4）

- [✓] FCF − SBC > 0：$12.55B − $0 = $12.55B 正
- [✓] 回购不进 g：g=6% 用业务增长（广告/电商/会员 + margin mix），回购另计不抬 PE
- [✓] 增长持续性：宽护城河（规模 + EDLP + 供应链）支撑，广告/会员高 margin 引擎可持续
- [✓] g ≥ 22% → 封顶 30x：g=6% < 22%，合理 PE = 14.5x（不封顶）

## C.2 护城河

- **壁垒类型**: 规模/成本（全球最大零售商，~10,750 店，采购规模压低成本）+ 品牌/心智（EDLP "Everyday Low Price" 心智，Sam Walton 品牌）+ 规模/网络（密集门店 + 配送网 + 自动化供应链，当日达/3 小时达）+ 切换成本（会员锁定，Walmart+/Sam's Club）
- **份额趋势**: 扩张（Q1'27 "gained share across business"，grocery + general merchandise，upper-income households 流入）
- **威胁**: 
  - 新进入者: 无（规模壁垒极高）
  - 技术替代: Amazon 电商竞争（但 WMT 全渠道 + 店配优势）
  - 监管: 反垄断潜在风险（但非即时威胁）
  - 客户垂直整合: 无
- **新高 margin 护城河**: Walmart Connect 广告网络（Q1 +44%，high margin）+ 会员费（+17.4%）+ marketplace → 从低 margin 零售向高 margin 平台/广告转型
- **宽度: 宽** → 质量评分 +1（D-1 第 7 分）

## C.3 管理层

| 项目 | 事实 |
|------|------|
| CEO | **John Furner**（2026-02-01 起，56 岁；前任 Walmart U.S. President & CEO，内部培养 30 年） |
| **继任/退休** | **已发生交接**: Doug McMillon 2026-01-31 退休（59 岁，任 CEO 11 年 2014-2026），**Furner 2026-02-01 接任**（2025-11-14 公告）。McMillon 留任 Board。**计划交接，内部培养**（麻烦定性: 一般，非 overhang） |
| 内部人 | Walton 家族持股 ~44.85%（heldPercentInsiders 0.4485，创始人家族稳定持仓，非短期信号） |
| 资本配置 | 48 年股息贵族（payoutRatio 33.5%）、真缩股（3yr -2.2%）、CapEx 重投自动化/电商、VIZIO 收购（广告 stack）、Vibe.co 收购（retail media ad-tech） |
| 指引 vs 实际 | Q1 FY27 Revenue +7.3% vs FY26 +4.7% 加速，连续 beat；但 Q2 FY27 UBS 预警增速放缓（mix/comparisons） |
| 治理风险 | 无 VIE/双层股权；董事会独立；auditRisk 5 / boardRisk 8 / overallRisk 3（低） |

> ⚠ 已查 CEO 交接公告（corporate.walmart.com/news/2025/11/14）。McMillon 退休 + Furner 内部接班 = 计划交接，非突发离职。按 `discount_coefficient.md` 管理层更替分档: "计划交接（有继任人选+时间表）| 一般 | 创始人→内部培养接班"。

## C.4 消息面（近 3 月）

- **2026-08-08**: Walmart Faces Oppenheimer Downgrade (to Perform)，"short-term outperformance less compelling"（Simply Wall St / MT Newswires）
- **2026-08-08**: UBS note: "Walmart's Q2 Growth Could Slow Down due to function of mix, comparisons"（MT Newswires）
- **2026-08-07**: Walmart (WMT) Faces An Oppenheimer Downgrade, Is A 28% Undervalued View Still Credible?（Simply Wall St）
- **2026-08**: DoorDash Gets FAA Green Light for Commercial Drone Deliveries（WMT 配送扩张）
- **2026-07**: Vibe.co Acquisition Aims to Streamline Retail Media Ad-Tech Stack（Morningstar，广告业务整合）
- **2026-08-20**: **Q2 FY27 财报日**（upcoming，关键催化）
- **Pharmacy headwinds**: 准备 Q2 财报时关注

Delta vs 上次分析（2026-07-04 base）: 
- CEO 交接已落地（Furner 2-1 接任，base 时尚在过渡期，现确认完成）
- 新增 Oppenheimer 降级 + UBS Q2 放缓预警（短期逆风）
- Vibe.co 收购（广告 ad-tech 整合，强化 Walmart Connect）
- 结论未变（买贵了），但短期催化偏负（降级 + Q2 放缓预期）

## C.5 熊市逻辑

1. **估值极贵**: P/E 39.4x（5yr 60th 分位，高于历史 median 35.1x），对 6% 增长 + 3.1% NM 的零售商极高；EV/EBITDA 21.4x、P/B 9.4x、PEG 4.27 均高位
2. **增长放缓风险**: UBS 预警 Q2 FY27 增速放缓（mix + 比较基数），OpIncome Q1 仅 +5.0%（reinvestment 拖累）；广告增速若回落（+44% → +20%），re-rate 叙事逆转
3. **资本结构压力**: 净债 $63.45B 无净现金托底、D/E 0.79、FCF yield 1.41%（CapEx 28.34B 吞 FCF，CapEx/OCF 69%）；加息周期利息覆盖压力（当前 10.5x 尚稳）
4. **防御溢价脆弱性**: 39x 含"防御 + 广告/AI re-rate"溢价，一旦 macro risk-on 轮动（资金从防御转向成长），WMT 相对 S&P 滞后（YTD +1.56% vs S&P +13.40%）
5. **CEO 新任期不确定性**: Furner 新任（2-1 起半年），战略连续性尚可但执行待验；Q2 FY27 为其首份完整半年报

## C.6 牛市逻辑

1. **估值（相对）**: P/S 1.2x（粗筛唯一 ✓，零售薄利结构性低，非贵信号）；相对 COST ~50x，WMT 39x 略低
2. **增长加速 + margin mix 上行**: Q1'27 Revenue +7.3%（3yr CAGR 5.27% 加速）、广告 +44%（ex-VIZIO）、会员 +17.4%、eCommerce +26%；高 margin 引擎占比升 → NI 增速 > Revenue 增速（NI YoY 12.6%）
3. **护城河最宽**: 全球最大零售商（270M 客户/周）、规模 + EDLP + 供应链 + 会员锁定；广告网络成新高 margin 护城河；upper-income 客户流入（份额扩张）
4. **资本回报 + 防御**: 48 年股息贵族、真缩股（3yr -2.2%）、Net Return $13.21B（yield ~1.5%）；beta 0.605 防御属性，经济下行抗跌；低价定位受益消费降级/通胀
5. **催化**: Q2 FY27 财报（8-20）若 beat 广告/会员增速 → re-rate 延续；自动化 CapEx 规模化后 FCF 释放（CapEx 增长投资 → 维护投资切换）
