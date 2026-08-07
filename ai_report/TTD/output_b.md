# TTD — Task B：财务健康 + 正常化 EPS
> 更新: 2026-08-07（TTM 2026-03 CSV + Q2'26 财报 8/6 报告）
> ⚠️ **Q2'26 财报刚发**：营收 miss、Q3 指引 margin 压缩、股价盘前 -27% 至 $12.87

## B.1 SCORECARD 九宫格

| 维度 | 3yr | TTM | 5Q |
|------|------|-----|-----|
| Income | 90 | 88 | 62 |
| CF | 100 | 85 | 100 |
| BS | 73 | 100 | 100 |

### 背离检验

| 维度 | SCORECARD 说 | 原始财报 | 方向 |
|------|-------------|---------|------|
| Income 3yr | 满分 90（营收/OpInc 3yr 全涨） | 但增速持续降档 22%→12%→8%→3% | 增长在熄火 |
| CF 3yr | 满分 100（OCF/FCF 持续增长） | H1'26 FCF $412M（+19% YoY） | 现金流仍强 |
| BS | 100（无债净现金） | Cash $1.41B、无债 | BS 最强项 |

伤口模式: **增速断崖 + margin 压缩**。3yr 高分（增长基数低）→ TTM/5Q 转弱（Q1'26 GM 73.6%、Q2'26 +3%、Q3'26 guide margin 25% vs 39%）。**增长引擎熄火 + margin 塌陷 = 真实伤口，非情绪**。

## B.2 利润表逐季（CSV 至 Q1'26 + Q2'26 研究）

```
        Rev     GM%    OpInc   OpM%    NI      dilEPS   备注
Q2'26  715M    ~74%*   ~241M*  ~34%*   64M*    0.14*   ⚠ 营收 miss 共识 $752M；Q3 guide margin 25%
Q1'26  688M    73.6%   66M     9.6%    39M     0.08    Q1 淡季 GM 低
Q4'25  846M    80.7%   256M    30.3%   186M    0.39    —
Q3'25  739M    78.1%   161M    21.8%   115M    0.23    —
Q2'25  694M    78.2%   116M    16.7%    90M    0.18    —
```
*Q2'26 数据来自研究（[BusinessWire](https://www.businesswire.com/news/home/20260806055680/en/The-Trade-Desk-Reports-Second-Quarter-2026-Financial-Results)），CSV 尚未更新。

- **GM 78% 但下滑中**（81.2→78.6→77.8 TTM，Q1'26 跌至 73.6%）——take rate 受压
- **增速断崖**: Q1'25 +25% → Q2'25 +19% → Q3'25 +18% → Q4'25 +14% → Q1'26 +12% → **Q2'26 +3%** → Q3'26 guide +3.5%
- **Q2'26 miss**: Rev $715M vs 共识 $752M（−$37M）；YoY 仅 +3%
- **Q3'26 指引 margin 塌陷**: EBITDA ~$160M / Rev ~$650M = ~25% margin（vs 39% LY、34% Q2'26）
- **OpInc 增速 vs 营收**: Q2'26 OpEx +6% vs Rev +3% → OpM 压缩（cloud→自有数据中心 + AI 投入）

## B.3 现金流（TTM CSV + H1'26 研究）

| 项目 | TTM (CSV) | H1'26 (研究) | 说明 |
|------|----------|-------------|------|
| OCF | $1.09B | $545M (+19.5% YoY) | 强——OCF/NI 2.53 |
| FCF | $829M | $412M (+19% YoY) | yield 9.3%（@ CSV price $18.96） |
| SBC | $471M | $219M | SBC/Rev 15.9%（**极高**） |
| CapEx | $263M | $133M | CapEx/OCF 24% |
| 回购 | $1.16B | $241M | aggressive；shares 499→487M |

FCF − SBC = **+$358M > 0** ✓（但 SBC 吃 57% FCF，黄灯）

> H1'26 FCF−SBC = +$193M > 0 ✓（研究确认，不触发 ×0.40）

## B.4 资产负债表（Q1'06 CSV）

| 项目 | 值 | 说明 |
|------|-----|------|
| Cash & ST Inv | $1.41B | H1'26 增至 $1.49B |
| Total Debt | $0.42B | 仅融资租赁，**无实质债务** |
| 净现金 | **$0.99B** | **11.1% MCap** |
| D/E | ~0.17 | 无杠杆 |
| Goodwill | $0 | 无商誉风险 |
| Equity | $2.45B | Retained Earnings −$724M（回购超累积利润） |
| P/B | 3.6x → 轻资产（GM >60%） | — |

## B.5 正常化 EPS Chain

| 口径 | EPS | 来源 |
|------|-----|------|
| GAAP | $0.88 | Diluted EPS TTM（CSV Q1'26） |
| 工具 | $0.89 | Normalized Income |
| v3.1 | $0.89 | detector Unusual（$1M 微额） |
| **FINAL** | **$0.88** | **min = GAAP** |

> Post-Q2'26 TTM EPS = 0.23+0.39+0.08+0.14 = **$0.84**（Q2'26 rolled in）。CSV 尚未更新，用 $0.88。

- detectors: Unusual（$1M 极小）、[OpIncDrop]（Q1'26 OpInc $66M vs Q4'25 $256M，季节性）
- GAAP 干净（Unusual $1M），min = GAAP $0.88

## B.6 质量地板（给 Task D 预判）

| 指标 | 值 | ✓/✗ |
|------|-----|-----|
| GM >60% 稳 | 77.8%（**3yr 下滑 81.2→78.6**） | ✗ |
| NM >20% | 14.6% | ✗ |
| FCF yield >5% | 9.3%（$829M/$8.91B） | ✓ |
| FCF−SBC >0 | +$358M（SBC 吃 57% FCF） | ✓ |
| 真缩股 | 499M→487M（−2.4%） | ✓ |
| ROIC >15% | 26.7% | ✓ |

本地评分: 4/6 → C 确认护城河**中等**（Amazon 侵蚀 + 执行失误 → 中）→ 不 +1 → **4/7 好公司**

> ⚠ Q2'26 后 GM/NM 将进一步恶化（Q3 guide margin 25% vs 39%），质量评分可能降至 3/7 平庸。但 FCF 仍正（H1'26 +$193M）。
