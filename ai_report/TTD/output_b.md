# TTD — Task B：财务健康 + 正常化 EPS
> 更新: 2026-08-08（TTM 2026-06 CSV，含 Q2'26 实际数据）
> 现价 $13.80（8/7 close）

## B.1 SCORECARD 九宫格

| 维度 | 3yr | TTM | 5Q |
|------|------|-----|-----|
| Income | 90 | 65 | 35 |
| CF | 100 | 85 | 80 |
| BS | 73 | 100 | 100 |

### 背离检验

| 维度 | SCORECARD 说 | 原始财报 | 方向 |
|------|-------------|---------|------|
| Income 3yr | 满分 90（营收/OpInc/EPS 3yr 全涨） | 增速持续降档：22%→19%→15%→**3%** Q2'26 | 增长在熄火 |
| Income TTM | 65（EPS −6.7% YoY、OpInc −0.5%） | TTM OpInc $586M vs LY $589M = 持平/微降 | 经营拐点 |
| Income 5Q | 35（OpInc −13%、EPS −22% QoQ） | Q2'26 OpInc $101M vs Q2'25 $116M = −13% YoY | 恶化中 |
| CF | 100/85/80（OCF +9%、FCF +8.5%） | OCF/NI 2.66（利润含金量高） | 现金流仍强 |
| BS | 100（无债净现金 $1.06B） | Cash $1.49B、Debt $434M（仅融资租赁） | BS 最强项 |

伤口模式: **增速断崖 + margin 压缩**。3yr 高分（增长基数低）→ TTM/5Q 转弱（GM 78.2→74.2% YoY、OpInc −13% YoY）。**增长引擎熄火 + margin 塌陷 = 真实伤口，非情绪**。

## B.2 利润表逐季（CSV income_quarterly，列0=最新季）

```
            Rev     GM%    OpInc   OpM%    NI      dilEPS   备注
Q2'26      715M    74.1%   101M    14.1%   64M     0.14    营收 miss 共识 $752M；YoY +3%（最低增速）
Q1'26      688M    73.5%    66M     9.6%   39M     0.08    Q1 淡季 GM 低
Q4'25      846M    80.7%   256M    30.3%  186M     0.39    季节性高峰
Q3'25      739M    78.1%   161M    21.8%  115M     0.23    —
Q2'25      694M    78.2%   116M    16.7%   90M     0.18    —
```

- **GM 下滑中**: Q2'25 78.2% → Q3'25 78.1% → Q4'25 80.7% → Q1'26 73.5% → Q2'26 74.1%（YoY 78.2→74.1 = −4.1pp）
- **增速断崖**: Q2'25 +25% → Q3'25 +18% → Q4'25 +14% → Q1'26 +12% → Q2'26 +3% → Q3'26 guide **−12%**（$650M vs $739M LY）
- **OpInc YoY 下降**: Q2'26 $101M vs Q2'25 $116M = **−13.0%**（OpEx +6% vs Rev +3% → OpM 14.1% vs 16.7% LY）
- **Q3'26 guide**: Rev ≥$650M（−12% YoY）、Adj EBITDA ~$160M（margin ~25% vs 39% LY）

### 年度趋势（income_annual）

```
            Rev      GM%     OpInc   OpM%    NI      EPS
2025      2.90B    78.6%    589M    20.3%  443M     0.90
2024      2.44B    80.7%    427M    17.5%  393M     0.78
2023      1.95B    81.2%    200M    10.3%  179M     0.36
2022      1.58B    82.2%    114M     7.2%   53M     0.11
```

- GM 3yr 下滑: 82.2→81.2→80.7→78.6（−3.6pp）
- OpM 波动大: 7.2→10.3→17.5→20.3（2025 是周期高点，2026 回落）

## B.3 现金流（cf_ttm CSV，TTM 2026-06）

| 项目 | TTM | 说明 |
|------|-----|------|
| OCF | $1.08B | OCF/NI = 2.66（高含金量） |
| FCF | $848M | yield = 12.8%（@$13.80, MCap $6.63B） |
| SBC | $452M | SBC/Rev = 15.1%（**极高**） |
| CapEx | $233M | CapEx/OCF = 21.5% |
| 回购 | $974M | Net Return = $974M − $452M = $522M > 0 ✓ |
| OCF YoY | +9.0% | vs LY $992M |
| FCF YoY | +8.5% | vs LY $782M |

**FCF − SBC = $848M − $452M = $396M > 0** ✓

> SBC 吃 53.3% FCF（$452M/$848M），黄灯但不触发 ×0.40

### 季度现金流（cf_quarterly）

```
            OCF     FCF     SBC     CapEx   回购
Q2'26      153M    135M    109M     17M     77M
Q1'26      391M    276M    109M    115M    163M
Q4'25      311M    281M    112M     29M    422M
Q3'25      224M    154M    121M     69M    310M
Q2'25      165M    116M    128M     48M    260M
```

H1'26: OCF $544M（+19.5% YoY）、FCF $412M（+19% YoY）、SBC $219M
H1'26 FCF−SBC = $412M − $219M = **$193M > 0** ✓

## B.4 资产负债表（bs_quarterly Q2'26）

| 项目 | 值 | 说明 |
|------|-----|------|
| Cash & ST Inv | $1.49B | Q2'26 增至（from $1.30B Q4'25） |
| Total Debt | $434M | 仅融资租赁，**无实质债务** |
| 净现金 | **$1.06B** | **15.9% MCap**（$1.06B/$6.63B） |
| D/E | 0.169 | 无杠杆 |
| **利息覆盖** | **N/A** | 无利息支出 |
| Goodwill | $0 | 无商誉风险 |
| Equity | $2.57B | Retained Earnings −$719M（回购超累积利润） |
| Current Ratio | 1.73 | $4.82B / $2.79B |
| P/B | —（轻资产 GM 76.9% >60%） | 不适用 |

## B.5 正常化 EPS Chain

| 口径 | EPS | 来源 |
|------|-----|------|
| GAAP | $0.84 | Diluted EPS TTM（CSV 2026-06） |
| 工具 | $0.847 | Normalized Income $407M / 480.6M shares |
| v3.1 | $0.847 | detector Unusual $91K（极小） |
| **FINAL** | **$0.84** | **min = GAAP** |

> TTM EPS = $0.23 + $0.39 + $0.08 + $0.14 = $0.84（Q3'25 + Q4'25 + Q1'26 + Q2'26）
> 旧分析用 $0.88（pre-Q2 TTM），CSV 更新后 $0.84（Q2'26 $0.14 滚入，Q2'25 $0.18 滚出）

### EPS-1: GAAP 基准

```
GAAP NI    = $407M
GAAP EPS   = $0.84
Pretax     = $642M
Tax        = $235M
有效税率    = 36.6%
Revenue    = $2.99B
GrossProfit = $2.30B → GM 76.9%
```

### EPS-2: Detector 扫描

```
2a: OtherInc → $91K（< 0.01% of NI → 跳过，Type A 干净）
2b: Restructuring → $0（无重组）
2c: Tax → TTM 36.6% vs 3yr 均值（2022: 57.5%, 2023: 33.3%, 2024: 22.5%, 2025: 32.7%）→ 波动大但不触发异常
2d: OpInc → Q2'26 $101M vs Q4'25 $256M（季节性，非异常）
2e: GMDrop → TTM GM 76.9% vs 3yr 均值 80.8% = −3.9pp（<5pp 阈值，不触发）
2f: R&D → TTM R&D% 18.1% vs 3yr 均值 17.2% = +0.9pp（<3pp 阈值，不触发）
2g: SGA → TTM SGA% 39.1% vs 3yr 均值 38.5% = +0.6pp（<3pp，不触发）
2h: Discontinued → NI = NI_continuing（无终止经营）
```

### EPS-3: 交叉验

```
Total Unusual Items = $91K（税前）
v3.1 检测到 OtherInc $91K → 与 Unusual 完全重叠
|91K − 91K| / max = 0% → 重叠，取大值 = $91K
剥离后影响 < $0.001 EPS → 可忽略
```

### EPS-4: 计算

```
GAAP EPS   = $0.84
工具 EPS   = $407M / 480.6M = $0.847
v3.1 EPS   = ($642M − $0.091M) × (1 − 36.6%) / 480.6M = $407M / 480.6M = $0.847
正常化 EPS = min($0.84, $0.847, $0.847) = $0.84
```

- winner: GAAP（最低）
- adj: 0%（GAAP 干净，Unusual 仅 $91K）
- detectors: 2a 触发但金额极小（$91K）

### GAAP → v3.1 桥接

```
GAAP 税前                    $642M
  − OtherInc 剥离（税前）      $0.091M    ← detector 2a（极小）
  = 正常化税前               $642M
  × (1 − 税率 36.6%)
  = 正常化净利               $407M
  ÷ 稀释股数 480.6M
  = v3.1 EPS                 $0.847
```

> GAAP 干净（Unusual $91K < 0.01% NI），min = GAAP $0.84

## B.6 质量地板（给 Task D 预判）

| 指标 | 值 | ✓/✗ |
|------|-----|-----|
| GM >60% 稳 | 76.9%（**3yr 下滑 82.2→78.6→76.9**） | ✗ |
| NM >20% | 13.6% | ✗ |
| FCF yield >5% | 12.8%（$848M/$6.63B） | ✓ |
| FCF−SBC >0 | +$396M（SBC 吃 53.3% FCF） | ✓ |
| 真缩股 | 499M→480.6M（−3.7%） | ✓ |
| ROIC >15% | 24.4% | ✓ |

本地评分: 4/6 → C 确认护城河**中**（Amazon 侵蚀 + 执行失误 + Q3 guide −12%）→ 不 +1 → **4/7 好公司**

> ⚠ Q3'26 guide margin ~25%（vs 39% LY）→ NM/FCF 将进一步恶化，质量评分可能降至 3/7 平庸。但 FCF 仍正（H1'26 +$193M）。
