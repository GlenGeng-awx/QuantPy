# EBAY — Task B：财务健康 + 正常化 EPS
> 更新: 2026-08-07（TTM 2026-03，财报 Q1 FY2026）

## B.1 SCORECARD 九宫格

| 维度 | 3yr | TTM | 5Q |
|------|------|-----|-----|
| Income | 60 | 90 | 88 |
| CF | 78 | 100 | 75 |
| BS | 18 | 100 | 90 |

### 背离检验

| 维度 | SCORECARD 说 | 原始财报 | 方向 |
|------|-------------|---------|------|
| Income 3yr | 低分 60（OpInc/EPS 3yr 零增长） | GM 72% 稳、营收 +4.3%/yr | 引擎停滞但底盘稳 |
| CF TTM | 满分 100 | OCF/NI 1.06、FCF $1.69B | 干净，但 FCF 3yr −14% 萎缩 |
| BS 3yr | 极低 18（D/E 升、CR 降、GW/Assets 升） | 回购举债推高 D/E，非经营恶化 | 资本配置选择非陷阱 |

伤口模式: 3yr 低分（BS 18、Income 60）+ TTM/5Q 高分（90-100）= **非困境反转**——是成熟停滞公司的常态，3yr 趋势性低分反映引擎熄火，TTM/5Q 反映 FCF 仍强。无"情绪伤口"机会。

## B.2 利润表逐季

```
        Rev     GM%    OpInc   OpM%    NI      dilEPS  税率
Q1'26  3.09B  74.0%   611M   19.8%   512M    1.12    17.2%
Q4'25  2.96B  71.6%   601M   20.3%   528M    1.15    15.7%
Q3'25  2.82B  70.9%   576M   20.4%   632M    1.35   -4.2%   ⚠税收利好
Q2'25  2.73B  71.4%   484M   17.7%   368M    0.79    22.6%
Q1'25  2.58B  73.3%   611M   23.7%   499M    1.06    20.4%
```

- **GM 71.8% 高且稳**（70.9-74.0%，marketplace take-rate 模式毛利天然高）——好公司特征
- **OpInc 3yr 零增长**：$2.35B（'22）→ $1.94B（'23）→ $2.32B（'24）→ $2.28B（'25），TTM $2.28B——引擎停滞，营收增长被 SGA 涨幅吞噬
- **Q3'25 税率 −4.2%（税收利好）虚增 NI 至 $632M**——TTM EPS $4.41 含此一次性利好；但 TTM 税率 12.6% vs 3yr 均值 17.2%，差 4.6pp < 10pp 阈值 → TaxAnomaly 未触发
- **Q1'26 GM 74.0% 跳升**：focus categories（收藏品/TCG）高 take rate 集中确认 + Depop 未并表

> ⚠ Q2'26 已于 2026-08-05 报告（Revenue $3.13B +15%、GAAP EPS $1.21、non-GAAP EPS $1.60），但 CSV 尚未更新。TTM 戳为 2026-03（Q1 FY2026），价格已反映 Q2 信息。

## B.3 现金流

| 项目 | TTM | 说明 |
|------|-----|------|
| OCF | $2.17B | OCF/NI=1.06 |
| FCF | $1.69B | yield=3.4% |
| SBC | $627M | SBC/Rev=5.4% |
| 回购 | $2.37B | Net Return=$2.28B（回购+分红−SBC） |
| 分红 | $536M | $0.31/季，稳定 |
| CapEx | $486M | CapEx/OCF=22% |

FCF − SBC = **+$1.06B** > 0 ✓

⚠ FCF 3yr 萎缩：$1.97B（'23）→ $1.96B（'24）→ $1.43B（'25），−27%。回购 $2.37B > FCF $1.69B，举债维持。

## B.4 资产负债表

| 项目 | 值 | 说明 |
|------|-----|------|
| 净现金/债 | −$3.34B | 净债（举债回购），无托底 |
| D/E | 1.63 | 高，回购缩股本+举债推高 |
| **利息覆盖** | **9.3x** | **>5x ✓** |
| Goodwill | $4.46B | Assets 25%，历史并购+Depop |
| Treasury Stock | $54.31B | 累计回购巨量，股本大幅缩减 |
| Cash/Debt | 0.54x | <1，靠 FCF 覆盖 |
| Working Capital | $1.12B | 正，较 '23 $6.50B 大幅收窄 |

BS 3yr=18 是回购举债推高 D/E + 缩股本使权益变薄——**资本配置选择**，非经营恶化。

## B.5 正常化 EPS Chain

| 口径 | EPS | 来源 |
|------|-----|------|
| GAAP | $4.41 | Diluted EPS |
| 工具 | $4.29 | Normalized Income $1.990B / 463.5M |
| v3.1 | $4.21 | detector 计算 |
| **FINAL** | **$4.21** | **min(三者)** |

- winner: v3.1
- adj: −4.5% vs GAAP
- detectors: Discontinued（2h）、Unusual（EPS-3 交叉验）

### GAAP → v3.1 桥接

```
GAAP 税前（continuing）          $2.296B
  − Unusual 剥离（税前）          $19M      ← EPS-3 交叉验（Gain On Sale of Security）
  = 正常化税前                   $2.277B
  × (1 − 税率 12.59%)
  = 正常化净利（continuing）     $1.990B
  − Discontinued 剥离（税后）     $37M      ← detector 2h
  = v3.1 净利                    $1.953B
  ÷ 稀释股数 463.5M
  = v3.1 EPS                     $4.21
```

### Detector 2h: Discontinued Operations

| 子项 | 金额 | 性质 |
|------|------|------|
| NI total | $2.044B | 含终止经营 |
| NI continuing | $2.007B | 持续经营 |
| Discontinued（税后） | $37M | 一次性 |

### Detector 触发原因分析

- **Unusual $19M**：Gain On Sale of Security，TTM 小额（<1% NI），季度波动稳定 → EPS-3 交叉验捕获，detector 2a 因 <1% NI 阈值跳过
- **Discontinued $37M**：终止经营收益，2h 高信心自动剥离
- ⚠ **v3.1 可能过度保守**：Pretax $2.296B 为 continuing-only 口径（Discontinued $37M 为税后项，不在 Pretax 中），v3.1 公式从 continuing NI 中再剥 Discontinued = 可能双重扣减。Tool NI $1.990B 未双重剥。差异 $0.08/股。但按框架 min(三者) = $4.21，保守优先

### 三口径对比

| 口径 | 剥离额 | Normalized NI | EPS |
|------|--------|--------------|-----|
| GAAP | 0 | $2.044B | $4.41 |
| 工具 | $54M（Unusual $17M + Disc $37M） | $1.990B | $4.29 |
| v3.1 | $56M（Unusual $19M pre-tax + Disc $37M） | $1.953B | $4.21 |

> 工具 vs v3.1 差距 = $37M Discontinued 双重扣减。v3.1 更保守但 min 原则优先。

## B.6 质量地板（给 Task D 预判）

| 指标 | 值 | ✓/✗ |
|------|-----|-----|
| GM >60% 稳 | 71.8%（3yr 72.7→72.0→71.5→71.8 TTM，微降但 TTM 回升） | ✓ |
| NM >20% | 17.6% | ✗ |
| FCF yield >5% | 3.4% | ✗ |
| FCF−SBC >0 | +$1.06B | ✓ |
| 真缩股 | 558M→463.5M（−16.9%/3yr） | ✓ |
| ROIC >15% | 25.7%（ROE 42.9%） | ✓ |

本地评分: 4/6 → 至少"好公司 ×0.67"，待 C 确认护城河（中等 → 非宽 → 不加分 → 4/7 好公司）
