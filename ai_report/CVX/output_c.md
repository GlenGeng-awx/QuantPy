# CVX — Task C：增长前瞻 + 护城河 + 管理层 + 消息面
> 更新: 2026-08-07  ⚠️ 周期股（g 仅参考不进 PE 公式）

## C.1 增长前瞻（产出 g — 周期股仅参考，不进 PE 公式）

### 本地基线

| # | 数据 | 值 | 来源 |
|---|------|-----|------|
| 1 | 营收 3yr CAGR | −2.2% | income_annual col0(FY2025 $184.43B) / col3(FY2022 $235.72B)，^(1/3)−1 |
| 2 | OpInc 3yr CAGR | −26.0% | FY2022 $39.95B → FY2025 $16.67B（油价回落） |
| 3 | EPS 3yr CAGR | −28.1% | FY2022 $18.28 → FY2025 $6.63（油价 + Hess 摊薄） |
| 4 | 近期季度 YoY | +3.2% | Q1'26 $47.56B vs Q1'25 $46.10B |
| 5 | PEG 隐含 g | 6.0% | trailingPE 18.3 / pegRatio 0.78（info.json，但 EPS stale $10.18） |
| 6 | info.json 增长率 | revenueGrowth +0.5% / earningsGrowth +3.2% | info.json |

> ⚠ **CAGR 全负**（油价从 2022 峰回落），不代表前瞻。g 用**业务量增**（Hess/Guyana/Permian 产量增长），非油价驱动。

### G-3 综合判断

```
Step 1 列全部 g 源: -2.2, -26.0, -28.1, 3.2, 6.0, 3.2
Step 2 剔除: #2 OpInc（周期下行不可外推）、#3 EPS（回购+Hess 摊薄扭曲）、#5 PEG（EPS stale）
Step 3 剔最高: #4 Q YoY 3.2% vs #6 earningsGrowth 3.2%（同值，剔任一）
Step 4: 剩余 #1(-2.2%) #6(3.2%) → avg = 0.5%
Step 5 定性调整: Hess/Guyana 产量 +15% YoY → 业务量增 ~5-6%（非营收增速，因油价下行抵消）
  g ≈ 5.5%（业务量增长口径）
```

**g = 5.5%（参考值，周期股不进 min(8.5+g,30) 公式）**

> per forward_g.md G-4d: "周期股不用 g 套 min(8.5+g,30)，用中周期正常化盈利 + 中周期 PE"

### g 质量护栏

- [✓] **FCF − SBC = +$13.78B > 0**（SBC=$0，不触发 ×0.40）
- [✓] 回购不进 g：g 用业务量增长（Hess/Guyana/Permian 产量）
- [△] 增长持续性：Hess/Guyana 储量寿命多十年，但油价主导每股盈利
- [✓] g = 5.5% < 22% → 不封顶（但周期股不套此公式）

## C.2 护城河

- **壁垒类型**: **规模/成本**（Guyana Stabroek 全球成本曲线最左端之一 + Permian 龙头 >100 万桶/日 + 一体化产业链）+ **品牌/纪律**（38 年连增股息）
- **份额趋势**: Hess 并表后 Guyana 权益 + Permian 双引擎，储量寿命延长；产量创纪录 3.86 MMboe/d
- **威胁**: (1) 能源转型长期需求顶；(2) 油价外生（无定价权 = price-taker）；(3) Hess 整合执行 + 杠杆消化；(4) OPEC+ 政策
- **宽度: 中-宽**（储量成本低 + 一体化 + 股息纪律，但无定价权）→ 质量评分 +1

> **本质 price-taker**：护城河 = 低桶成本 + 储量寿命，非定价权 → "好公司"非"伟大"

## C.3 管理层

| 项目 | 事实 |
|------|------|
| CEO | Mike Wirth（per base.md；主导 Hess 收购，历经与 XOM 的 Guyana 仲裁后完成） |
| **继任/退休** | **无公告** |
| 内部人 | —（未查 SEC Form 4） |
| 资本配置 | 38 年连增股息（$1.71/季 = $6.84/年）；2026 回购指引 $2.5-3B/季；FCF 不足以覆盖总回报 $24B → 举债 |
| 指引 vs 实际 | Q1'26 adj EPS $1.41 大超共识 $0.97（系列最大 beat）；产量创纪录 |
| 治理风险 | 无 VIE/双层股权；Hess 仲裁已解决 |

## C.4 消息面（近 3 月）

- **2026-05-01**: Q1'26 adj EPS $1.41 超共识 $0.97（系列最大 beat），GAAP $1.11 受 $2.9B 衍生品 MTM 损失拖累，产量创纪录 3.86 MMboe/d（[Chevron IR](https://chevroncorp.gcs-web.com/news-releases/news-release-details/chevron-reports-first-quarter-2026-results)）
- **Hess 收购完成并全面并表**：Guyana Stabroek 长期增长，发股对价推高股数 +14%
- **股息率 4.0%**，38 年连增；2026 回购指引 $2.5-3B/季
- **油价**: WTI ~$68/bbl、Brent ~$71/bbl（中-低区间，偏软）

Delta: vs base（7/4），无新增重大消息。核心 thesis 无变化。

## C.5 熊市逻辑

1. **油价偏软**：WTI ~$68、Brent ~$71（中-低区间），盈利承压
2. **Hess 并表推高杠杆**：LT 债 $19.6B→$39.6B（翻倍），DD&A 拖累 EPS
3. **FCF 不足以覆盖总回报**：FCF $13.8B < 股息 $13.3B + 回购 $10.7B = $24B → 举债
4. **股息覆盖率 1.04x**（偏紧，比 XOM 更紧）→ 股息安全性是核心盯点
5. **Q1'26 FCF 转负** −$1.55B（衍生品 margin posting + CapEx 时点性）
6. **P/B 2.0x**（5yr 84th 分位，中高位，非周期底）
7. **能源转型长期需求顶**

## C.6 牛市逻辑

1. **股息率 4.0%**（>XOM 100bp）、38 年连增
2. **adj EPS $1.41 大超共识 $0.97**（系列最大 beat）
3. **产量创纪录 3.86 MMboe/d**（+15% YoY，Hess + Permian）
4. **Guyana Stabroek** 全球成本曲线最左端，多十年储量潜力
5. **P/B 2.0x 比 XOM ~2.4x 便宜 20%**
6. **2026 adj EPS 共识回升 +30%**（[Simply Wall St](https://simplywall.st/stocks/us/energy/nyse-cvx/chevron/future)）
7. **Q1'26 $2.9B 衍生品 MTM 损失下季回补**

> 周期股以 P/B 为主口径。P/B 2.0x = 5yr 84th 分位（非周期底，中高位）。中周期合理价 $123.60 → 安全边际 −50.8%（现价 $186 > 合理价 $124）→ 买贵了。
