# AMD — Task C：增长前瞻 + 护城河 + 管理层 + 消息面
> 更新: 2026-08-06  ⚠️ 周期股（半导体）

## C.1 增长前瞻（产出 g — 周期股仅参考，不进 PE 公式）

### 本地基线

| # | 数据 | 值 | 来源 |
|---|------|-----|------|
| 1 | 营收 3yr CAGR | 13.64% | (34.64/23.60)^(1/3)-1, income_annual col0/col3（FY25/FY22） |
| 2 | OpInc 3yr CAGR | 42.97% | (3.69/1.26)^(1/3)-1；⚠ 失真：FY23 OpInc $401M 低基数 |
| 3 | EPS 3yr CAGR | 46.66% | (2.65/0.84)^(1/3)-1；⚠ 失真 + 回购扭曲 |
| 4 | 近期季度 YoY | +37.8% | Q1'27 $10.25B vs Q1'26 $7.44B |
| 5 | PEG 隐含 g | 151% | P/E 172.2 / PEG 1.14, info.json；⚠ 失真（P/E 172x 极高基数） |
| 6 | info.json earningsGrowth | 91.2% | EPS YoY（含回购扭曲） |
| 6 | info.json revenueGrowth | 37.8% | Q1 YoY（同 #4，重复） |

### 外部判断

| # | 数据 | 值 | 来源 |
|---|------|-----|------|
| 7 | 管理层长期指引 | 公司 CAGR >35%、数据中心 CAGR >60%、AI CAGR >80% | [AMD IR](https://ir.amd.com/news-events/press-releases/detail/1266/amd-unveils-strategy-to-lead-the-1-trillion-compute-market-and-accelerate-next-phase-of-growth) |
| 8 | Q2'26 指引 | 营收 $11.2B（+46% YoY） | [CNBC](https://www.cnbc.com/2026/05/05/amd-q1-2026-earnings-report.html) |
| 9 | 分析师共识 2026 | +~30% 营收 | [Seeking Alpha](https://seekingalpha.com/news/4546760) |

### G-3 综合判断

```
Step 1 列全部 g 源:
  13.64, 42.97, 46.66, 37.8, 151, 91.2, 37.8(dup), 35, 46, 30

Step 2 剔除不可靠源:
  ✗ #2 OpInc CAGR 42.97% — 跨增长阶段（FY23 低基数 $401M）
  ✗ #3 EPS CAGR 46.66% — 同上 + 回购扭曲
  ✗ #5 PEG g 151% — 失真（P/E 172x 极端基数）
  ✗ #6 earningsGrowth 91.2% — 回购扭曲
  ✗ #6 revenueGrowth 37.8% — 重复 #4
  ✗ #8 Q2'26 指引 46% — 季度指引，非长期 g

Step 3 剔最高 1 个:
  ✗ #4 Q YoY 37.8% — 最高

Step 4 均值:
  剩余 [13.64, 35, 30] → avg = 26.21%

Step 5 定性调整: 无
```

**g = 26%**（≥22%，但**周期股不进 PE 公式**——g 仅作参考）

> ⚠ 周期股特殊处理：per forward_g.md G-4d "周期股不用 g 套 min(8.5+g,30) 公式，用中周期正常化盈利 + 中周期 PE，g 仅作参考不进公式"。g=26% 不影响合理价计算（见 output_d 周期口径）。

### g 质量护栏

- [✓] FCF − SBC = +$6.81B > 0
- [✓] 回购不进 g（g 用营收 CAGR + 管理层指引 + 分析师共识）
- [△] 增长持续性：AI 数据中心需求强但**未经完整周期检验**；ROCm 弱于 CUDA
- [✓] g = 26% ≥ 22% → 若非周期股应封顶 30x（但周期股不用此公式）

## C.2 护城河

- **壁垒类型**: x86 CPU 双寡头（与 Intel）+ GPU/AI 加速器（挑战 NVDA）+ Xilinx FPGA
- **份额趋势**: 服务器 CPU 从 Intel 抢份额（EPYC 强）；**AI GPU 份额 <20%**，NVDA CUDA 软件生态是 AMD 最大短板（ROCm 弱于 CUDA）
- **威胁**: NVDA 生态锁定极强；超大规模厂商自研 ASIC（含 AVGO/Marvell 定制）；Intel 代工/产品回血
- **宽度: 中等（老二困境）** → 质量评分不加 +1

## C.3 管理层

| 项目 | 事实 |
|------|------|
| CEO | Lisa Su（2014 至今，业界顶级 turnaround CEO） |
| **继任/退休** | **无公告** |
| 内部人 | Lisa Su 2026-06 卖 12.5 万股；过去一年累计卖 81 万股、**零买入** = 弱看空信号（[GuruFocus](https://www.gurufocus.com/news/8914834)） |
| 资本配置 | 回购 $1.50B（仅对冲 SBC，未真缩股）；零分红；现金优先内生 + 并购 |
| 指引 vs 实际 | 连续超预期 + 上调指引，执行力强 |
| 治理 | 干净；无 VIE / 无双层股权 |

## C.4 消息面（近 3 月）

- 2026.05.05: Q1'26 数据中心 $5.8B、营收/指引超预期，股价单日 +14-16%（[CNBC](https://www.cnbc.com/2026/05/05/amd-q1-2026-earnings-report.html)）
- MI450/Helios 机架级 2026 Q3 起量，MI500 2027
- **YTD +152%，2026-06-30 ATH $584.73**——AI 狂热追高
- MI308 对华禁运曾致 Q2'25 ~$800M 减值（一次性）
- Lisa Su 6/10 卖 12.5 万股（弱看空）

Delta: Q2 FY26 ~8 月才发。无新消息面变化。

## C.5 熊市逻辑

1. **估值**: GAAP P/E 158x（$482/$3.05）、forward P/E 31x（市场预期 EPS 5x 增长）；P/B 12.2x；EV/EBITDA 105x
2. **GM 50.3%**: GAAP 远低于 NVDA 75%；Xilinx 摊销 ~$4B/yr 压低 GAAP 利润
3. **ROCm 弱于 CUDA**: AI GPU 生态最大短板，份额 <20%
4. **FCF yield 1.1%**: 好价格证据完全缺失
5. **Lisa Su 减持**: 81 万股零买入 = 弱看空
6. **不缩股**: 回购仅对冲 SBC；dil shares 1.57B→1.64B（+4.5%/3yr）
7. **周期风险**: AI 资本开支若见顶 → 估值剧烈收缩；半导体周期下行

## C.6 牛市逻辑

1. **营收 +37.8% 加速**: 数据中心引擎猛；Q2'26 指引 +46% YoY
2. **MI400/MI450 系列**: 2026 Q3 起量，Helios 机架级
3. **管理层 CAGR >35%**: 长期指引，数据中心 CAGR >60%
4. **Lisa Su 执行力**: 连续超预期
5. **FCF $8.57B**: 3yr +180% 真实改善
6. **净现金 $8.48B**: 温和

**但——好公司不假，问题是价格（GAAP P/E 158x）+ AI 狂热追高 + 周期股不该用成长公式。**
