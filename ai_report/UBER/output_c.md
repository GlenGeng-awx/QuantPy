# UBER — Task C：增长前瞻 + 护城河 + 管理层 + 消息面
> 更新: 2026-08-09（Q2'26 财报后）

## C.1 增长前瞻（产出 g）

### 本地基线
| # | 数据 | 值 | 来源 |
|---|------|-----|------|
| 1 | 营收 3yr CAGR | 11.8% | income_annual（$52.02B/$37.28B）^(1/3)−1（framework col0/col2；注：col2=2023 实为 2yr 跨度，true 3yr vs 2022 = 17.7%，但 forward_g.md UBER 范例即用 11.8%） |
| 2 | OpInc 3yr CAGR | 71.4% | $5.57B/$1.11B ^1/3 — hypergrowth 低基数，不可外推 |
| 3 | EPS 3yr CAGR | ~75% | $4.73/$0.87 ^1/3 — 受递延税/MTM 严重扭曲，仅参考 |
| 4 | Q2'26 Rev YoY | +12.2% | $14.19B vs $12.65B（减速：Q1 +14.5% → Q2 +12.2%） |
| 5 | PEG 隐含 g | 2.05% | trailingPE 15.47 / pegRatio 7.55（EPS 被递延税垫高，PEG 失真） |
| 6 | info.json earningsGrowth | +85.5% | GAAP EPS YoY，递延税扭曲 |
| 7 | info.json revenueGrowth | +12.2% | YoY 营收 |

### 外部判断
| # | 数据 | 值 | 来源 |
|---|------|-----|------|
| 8 | 分析师长期共识 | ~10-12%（营收） | Yahoo Growth Estimates：Current Year EPS +36%（递延税扭曲）、营收 +12%；旧 TIKR 长期 ~10% |
| 9 | 管理层 Q3'26 指引 | gross bookings +18-22% YoY cc（$58.25-60.25B） | Uber IR 2026-08-05；revenue 增速因 take rate 压缩低于 bookings |

### 综合判断（G-3 Step 1234）

```
g 源:
  营收 3yr CAGR 11.8%      col2=2023 实为 2yr 跨度，forward_g 范例即用此值
  OpInc 3yr CAGR 71.4%     hypergrowth 低基数 $1.11B→$5.57B
  EPS 3yr CAGR ~75%        递延税/MTM 严重扭曲
  Q2'26 Rev YoY 12.2%      减速 Q1 14.5%→Q2 12.2%
  PEG 2.05%               GAAP P/E 含递延税收益垫高，失真
  earningsGrowth 85.5%     GAAP EPS YoY，递延税扭曲
  分析师长期 ~10-12%       Yahoo 长期营收共识
  mgmt Q3 bookings 18-22%  bookings ≠ revenue（take rate 压缩），口径不对

Step 2 剔除:
  OpInc CAGR 71.4%         hypergrowth 低基数，不可外推
  EPS CAGR ~75%            递延税/MTM 扭曲
  PEG 2.05%               EPS 被递延税垫高 → PEG 失真
  earningsGrowth 85.5%    递延税扭曲
  mgmt bookings 18-22%    口径不对（bookings ≠ revenue）

Step 3 剔除:
  Q2 YoY 12.2%            最高剩余，保守偏置

Step 4:
  avg(11.8, 11) = 11.4% ≈ 11%
```

- **g = 11%**（营收 3yr CAGR 11.8% + 分析师长期 11% 均值；旧值 14% 已在 v2 降至 11%）
- g 区间宽（5-14%）反映 AV 去中介化 + take rate 压缩的不确定性
- take rate 压缩: bookings +22% vs revenue +12% → revenue g 低于 bookings g
- AV 威胁（2028-01 Waymo 自有 App）→ 长期 g 有下行风险，11% 未充分反映

### g 质量护栏
- [✓] FCF − SBC = +$8.18B > 0
- [✓] 回购不进 g（g 用营收/净利润增长，不含缩股）
- [✓] 增长持续性（双边网络 + 外卖，但 AV 结构性威胁 + take rate 压缩）
- [✓] g = 11% < 22% → 不封顶

## C.2 护城河

- **壁垒类型**: 双边网络效应（司机↔乘客密度）+ 外卖/出行超级 App 交叉补贴 + Uber One 会员切换成本（会员 → 频次↑ → 留存↑）
- **份额趋势**: 北美出行龙头（vs Lyft ~75% 份额）；外卖与 DoorDash 双寡头
- **威胁（核心）**: **AV 去中介化** — Waymo 通知 Uber 将于 **2027-01** 结束独占、在 Austin/Atlanta 推出自有 App（Bloomberg 2026-07-24）。证明 AV 运营商可绕过 Uber 直接触达需求 → 平台去中介化。**Take rate 压缩**：gross bookings +22% 但 revenue 仅 +12%（低 take rate 业务如 grocery/AV 占比升）
- **Uber 反制**: 投 **$10B+** 自建 AV 网络，多伙伴布局：Zoox（Las Vegas）、Avride（Dallas）、Wayve（London）、Lucid+Nuro（Bay Area/LA）、WeRide+Baidu（中东）。Khosrowshahi：2026 年底 15 城部署、2028 年 28 城（Automotive World 2026-08-06）
- **宽度: 宽但正被 AV 侵蚀** → 质量评分 +1

## C.3 管理层

| 项目 | 事实 |
|------|------|
| CEO | Dara Khosrowshahi（2017 至今，~55 岁，从巨亏到 FCF $10B+） |
| **继任/退休** | **无公告**（web search 确认） |
| CFO | Balaji Krishnamurthy（~40 岁，相对新任） |
| 内部人 | heldPercentInsiders 0.196%（低）；无重大公开市场增持 |
| 资本配置 | $6.90B 回购 TTM（真缩股 2.13B→2.05B）+ $10B+ AV 投资；零分红 |
| 指引 vs 实际 | Q2'26 gross bookings $58B 超 guidance 高端（+22% cc，连续 4 季加速）；Q3 指引 +18-22% |
| 治理风险 | 普通硅谷公司，无 VIE/双层股权；auditRisk 2（低） |

## C.4 消息面（近 3 月）

- **2026-08-05**: Q2'26 财报 — gross bookings $58.0B（+24% reported / +22% cc，连续 4 季加速）、revenue $14.2B（+12%）、trips 3.9B（+18%）、EPS $1.17 beat（Uber IR / Nasdaq）
- **2026-08-06**: Uber 承诺 $10B+ robotaxi，Khosrowshahi：年底 15 城部署、2028 年 28 城；称 Waymo 仍"important"（Automotive World）
- **2026-08-01**: TechCrunch — Uber 构建 AV 帝国（多伙伴：Zoox/Avride/Wayve/Nuro/Baidu）
- **2026-07-24**: Bloomberg — **Waymo 计划结束 Uber robotaxi 合作**，Austin/Atlanta 推出自有 App（2028-01 起），加剧竞争
- （旧）2026-06-29: Waymo 退出凤凰城合作

Delta: vs 上次分析（Aug 1），新增 Q2 财报 + Waymo 结束合作具体时间表（2028-01）+ Uber $10B AV 反制细节。**AV 威胁从"隐忧"升级为"有时间表的结构性挑战"**。

## C.5 熊市逻辑

1. **EPS 含水分**: 正常化 EPS $4.56 含 Q3'25 递延税收益 ~$2.2/sh（DTA 一次性释放）；分析师 2026 共识 EPS $3.21 → normalized P/E = $75/$3.21 = 23.4x，对 11% 增速偏贵
2. **AV 结构性威胁**: Waymo 去中介化（2028-01 自有 App），平台价值被侵蚀；$10B+ 反制未验证
3. **Take rate 压缩**: gross bookings +22% 但 revenue 仅 +12%，结构性 mix shift（grocery/AV 低 take rate 占比升）
4. GM 42% 薄（非软件级，<60%）；NM 17%（<20%）
5. 净债 $9.34B（含租赁），Cash/Debt 0.42x

## C.6 牛市逻辑

1. FCF $10.12B（yield 6.6%）+ FCF−SBC $8.18B = 最硬证据，3 年从 $3.36B → $10.12B
2. 真缩股 2.13B→2.05B（5Q −3.8%），回购 $6.90B >> SBC $1.94B
3. OpM 改善 8.2%→13.3%，GM 升至 45%（Q2'26）
4. Gross bookings 加速 +22% cc（连续 4 季），Q3 指引 +18-22%
5. 双边网络效应护城河 + Uber One 会员（切换成本）
6. $10B+ AV 反制（多伙伴），15 城年底 / 28 城 2028
7. P/E 5yr 分位 3.5th（框架口径，但高分位为近零 EPS 假象）
