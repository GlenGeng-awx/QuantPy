# CPNG — Task C：增长前瞻 + 护城河 + 管理层 + 消息面
> 更新: 2026-08-07

## C.1 增长前瞻（产出 g）

### 本地基线

| # | 数据 | 值 | 来源 |
|---|------|-----|------|
| 1 | 营收 3yr CAGR | 18.8% | income_annual col0(FY2025 $34.53B) / col3(FY2022 $20.58B)，^(1/3)−1 |
| 2 | OpInc 3yr CAGR | n/m | FY2022 OpInc −$112M（负值，无法算） |
| 3 | EPS 3yr CAGR | n/m | FY2022 EPS −$0.05（负值，无法算） |
| 4 | 近期季度 YoY | +7.5% | Q1'26 $8.50B vs Q1'25 $7.91B |
| 5 | PEG 隐含 g | n/m | P/E N/A（EPS 负），pegRatio 0.45 失真 |
| 6 | info.json 增长率 | revenueGrowth +7.5% | info.json |

> ⚠ **CAGR 列号**：forward_g.md 公式 `(Rev[0]/Rev[2])^(1/3)−1` 标"列2=3年前"，但 CSV 实际 col2=FY2023（仅 2 年前）。正确用 col0/col3（FY2025/FY2022）。per mistakes.md 已知问题。

### 外部判断

| # | 数据 | 值 | 来源 |
|---|------|-----|------|
| 7 | 分析师共识 | 2026 营收 ~$37.8B（+7.5%），15 分析师 | [base.md 引 Seeking Alpha] |
| 8 | 管理层指引 | Product Commerce EBITDA margin 8.4%→目标 10%+ | Q1'26 财报电话会议 |

### G-3 综合判断

```
Step 1 列全部 g 源: 18.8, n/m, n/m, 7.5, n/m, 7.5, 7.5, margin(非量化)
Step 2 剔除: #2 OpInc n/m、#3 EPS n/m、#5 PEG 失真、#6 ≈#4（同值）、#8 非量化 g
Step 3 剔最高: #1 CAGR 18.8%（hypergrowth→成熟，韩国近饱和不可外推）
Step 4 均值: [7.5, 7.5] → avg = 7.5%
Step 5 定性调整: PC EBITDA margin 8.4%→10%+ = 利润率改善 → 盈利增长 > 营收增长 ~1.5pp → g ≈ 8%
```

**g = 8%**（7.5% 营收增速 + 1.5% 利润率改善 = 9% → 保守取 8%）

- 营收从 +19% CAGR 放缓至近期 +7.5%；Product Commerce +4%（成熟低速），Developing +28%（烧钱）
- PC EBITDA margin 7.5%→8.4%→目标 10%+，利润率改善在兑现

### g 质量护栏

- [✗] **FCF − SBC = −$181M < 0 → 重麻烦 → ×0.40**（不否决，合理价照算，per CLAUDE.md 硬规则）
- [✓] 回购不进 g：g 用业务/净利润增长
- [△] 增长持续性：韩国电商近饱和（个位数），Taiwan 未验证
- [✓] g = 8% << 22% → 不封顶

## C.2 护城河

- **壁垒类型**: **全栈自建物流**（Rocket Delivery 次日/当日达覆盖 99% 韩国家庭）+ WOW 会员 14M（切换成本 + 网络效应）+ 韩国电商 ~25% 份额、40% 在线流量
- **份额趋势**: 韩国核心稳固领先（Naver/Kakao 追不上物流）；食品配送 35% 份额
- **威胁**: (1) 韩国电商近饱和（增速降至个位数）；(2) Taiwan 从零建仓护城河未证明可复制；(3) AliExpress/Temu 低价冲击
- **宽度: 中-宽**（韩国宽，Taiwan 未验证）→ 质量评分 +1

## C.3 管理层

| 项目 | 事实 |
|------|------|
| CEO | Kim Bom（Bom Kim），创始人控制，数据泄露后公开道歉 |
| **继任/退休** | **无公告**（创始人仍在任） |
| 内部人 | —（web 未查 SEC Form 4） |
| 资本配置 | 首次回购启动（TTM $634M，含 Q1'26 $391M）；零分红；Taiwan 激进烧钱 |
| 指引 vs 实际 | PC EBITDA margin 7.5%→8.4% 说到做到；数据泄露是重大执行失误 |
| 治理风险 | 数据泄露暴露风控缺陷（3370 万账户，韩国史上最大罚款 $410M） |

> 创始人集中控制 + 数据泄露风控失误 + Taiwan 无纪律烧钱 = 治理与资本配置存疑。

## C.4 消息面（近 3 月）

- **2026-05-05**: Q1'26 营收 $8.5B（+8% cc），PC +4%、Developing +28%；NI −$266M（数据泄露 $1.2B 代金券 + 罚款）（[Motley Fool 转录](https://www.fool.com/earnings/call-transcripts/2026/05/05/coupang-cpng-q1-2026-earnings-transcript/)）
- **数据泄露**: 3370 万账户，$410M（624.7B 韩元）史上最大罚款；$1.18B 代金券补偿（[ts2.tech](https://ts2.tech/en/coupang-stock-pops-in-premarket-after-1-18-billion-voucher-plan-tied-to-data-leak/)）
- **BofA 下调目标价**: 增长放缓 + Taiwan 亏损（[Investing.com](https://uk.investing.com/news/analyst-ratings/bofa-cuts-coupang-stock-price-target-on-slower-growth-taiwan-losses-93CH-4531140)）
- **Nvidia AI 合作**: Coupang Intelligent Cloud + DGX SuperPOD

Delta: vs base（7/4），无新增重大消息。核心 thesis 无变化。

## C.5 熊市逻辑

1. **亏损**（TTM NI −$165M, EPS −$0.10）
2. **FCF−SBC < 0**（−$181M，CapEx 吞噬）→ 重麻烦 ×0.40
3. **GM 28.8% 薄**（电商低毛利）且下滑（29.3%→27.0%）
4. **数据泄露 + 罚款**（风控缺陷）
5. **Taiwan/Eats 持续烧钱**（−$329M/季，主动非一次性）
6. **净现金仅 ~$0.9B**（含租赁后托底薄）
7. **利息覆盖 1.0x**（≤2x fail）

## C.6 牛市逻辑

1. **P/S 0.8x**（全 batch 最低；但薄利换算正常化 P/E ~26x 非真便宜）
2. **1Y 回撤 52% + 距 52W 低 +5.8%**
3. **韩国 #1 电商** + Rocket Delivery 物流护城河宽
4. **PC EBITDA margin 7.5%→8.4%→目标 10%+**（利润率改善在兑现）
5. **WOW 会员 14M** 黏性
6. **数据泄露 $1.2B 是一次性**（会过去）

> 恢复 EPS $0.62 × min(8.5+8, 30) = 16.5x → 合理价 $10.23 → 安全边际 −56.4%（现价 $16 > 合理价）→ 买贵了。FCF−SBC < 0 → 重麻烦 ×0.40 → 满仓 $4.09。韩国护城河真实但薄利 + CapEx 吞 FCF + Taiwan 烧钱 = 麻烦半结构性。
