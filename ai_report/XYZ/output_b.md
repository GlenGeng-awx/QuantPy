# XYZ — Task B：财务健康 + 正常化 EPS
> 更新: 2026-08-09（财报 FY26 Q2，2026-08-05 发，日历季 2026-06）货币: USD，财年=日历年

## B.1 SCORECARD 九宫格

| 维度 | 3yr | TTM | 5Q |
|------|------|-----|-----|
| Income | 88 | 65 | 70 |
| CF | 80 | 100 | 100 |
| BS | 82 | 95 | 90 |

### 背离检验

| 维度 | SCORECARD 说 | 原始财报 | 方向 |
|------|-------------|---------|------|
| Income | 3yr=88 强（OpInc 381M→3.05B +80.6%）但 TTM/5Q 低（65/70，EPS −73% YoY） | GAAP NI 被 BTC MTM −$2.22B + 重组 $1.96B 压低；adj OpM record 27% | **机会**（情绪/非经营伤口，非结构性恶化） |
| CF | 100/100 满分 | FCF $3.88B（+56% YoY）、OCF $4.06B（+57%）、FCF−SBC +$2.68B | **已定价偏正面**（CF 不受非现金项影响，印钞机） |
| BS | 82/95/90 | 净现金 $5.10B、GW 33.6% risk flag | **中性**（资产质量稳，GW 占比偏高但 Afterpay 并购累积，无减值） |

伤口模式: 3yr 高 + TTM 低 = 典型"非经营项砸单季"（BTC 持仓减值 + 重组费用），CF 反而满分 → **非结构性恶化，情绪/非经营伤口**。区别于 ADBE（情绪伤口、基本面完好）：XYZ 是**真困境反转**（2022-23 真亏过），如今 OpInc 转正 + GP 加速（+24.8% YoY Q2'26）。

## B.2 利润表逐季拆解

```
File: income_quarterly.csv  列0=最新季（新→旧）

         Rev     GP     GM%    OpInc   OpM%    NI(GAAP)  Norm NI   dilEPS  dilShares
Q2'26  6.62B  3.17B  47.8%   1.03B   15.6%     88M      600M     0.15    608M
Q1'26  6.06B  2.91B  48.0%    328M    5.4%   -308M      189M    -0.52    597M
Q4'25  6.25B  2.87B  45.9%    995M   15.9%    115M      703M      —       —     ← CSV EPS/shares gap
Q3'25  6.11B  2.66B  43.5%    772M   12.6%    461M      692M     0.74    621M
Q2'25  6.05B  2.54B  42.0%    778M   12.9%    538M      605M     0.87    618M
```

- **GP 稳步加速**：GM% 42.0%→47.8%（5 季 +5.8pct），GP 绝对额 $2.54B→$3.17B（+24.8% YoY Q2'26）→ **业务真实向上**
- **GAAP NI 与 Normalized NI 剧烈背离**：Q1'26 GAAP −$308M vs Normalized +$189M（差额 −$672M Unusual = BTC 减值 + 重组）；Q2'26 GAAP $88M vs Normalized $600M → **OpInc 与 NI 背离 = 非经营项主导，必须正常化**
- **OpM 波动大**（5.4%-15.9%）：重组费用 TTM $1.96B 在吞噬 OpInc，属 Dorsey 裁员 40% 的一次性台阶；但 adj OpM（% of GP）达 record 27%（Q2'26）
- **缩股真实**：dil shares 621M(Q3'25)→608M(Q2'26)，TTM 回购 $1.89B > SBC $1.20B = 真缩股
- Q4'25 dilEPS/dilShares 为 CSV 数据空白（年报合并口径），NI 从 TTM 反推验证 = $115M ✓

## B.3 现金流

| 项目 | TTM | 说明 |
|------|-----|------|
| OCF | $4.06B（+57.3% YoY） | OCF/NI=11.36（虚高——因 GAAP NI 被一次性项压低；正常化后 ~2.3，仍健康） |
| FCF | $3.88B（+56% YoY） | CapEx 仅 $175M（轻资产），yield=8.2%（FCF/MCap $47.46B） |
| SBC | $1.20B | SBC/Rev=4.8%（下降中，软件业偏低） |
| 回购 | $1.89B | Net Return=+$0.69B（回购>SBC=真缩股） |

**FCF − SBC = 3.88 − 1.20 = +$2.68B > 0** ✓ 且 3 年增长（2022 $5M→2025 $2.42B→TTM $3.88B）。成长估值合格。

## B.4 资产负债表

| 项目 | 值 | 说明 |
|------|-----|------|
| 净现金/债 | +$5.10B（Cash $12.27B − Total Debt $7.17B） | 有托底（占 MCap ~11%）；RE 转正（3.45B，2023 还是 −528M）= 真赚 ✓ |
| D/E | 0.33（$7.17B / $22.05B） | 低 |
| **利息覆盖** | **N/A** | Interest Expense 近季无数据（Q1'26 $53M，其余零/空白）；FY25 Interest Paid $246M |
| Goodwill | $13.17B（Assets $39.16B 的 33.6%） | Afterpay($29B 2022)+其他并购累积，risk flag >33%，无减值 |

## B.5 正常化 EPS Chain

| 口径 | EPS | 来源 |
|------|-----|------|
| GAAP | $0.56 | Diluted EPS（income_ttm） |
| 工具 | $2.95 | Normalized Income $1.79B / Diluted Shares 608M |
| v3.1 | $0.58 | detector 计算（无收益剥离，税率为 TTM 50%） |
| **FINAL** | **$0.56** | **min(三者) = GAAP** |

- winner: **GAAP**（$0.56 是三者最低）
- adj vs GAAP: tool $2.95 比 GAAP 高 $2.39 → tool 加回了 −$2.40B Total Unusual Items（BTC MTM + 重组**损失**），框架"只剔收益不加回亏损"→ 取 GAAP 兜底
- detectors 触发: **OtherInc, TaxAnomaly, [Restructuring], [SGASpike]**（实跑 `normalize_eps.py` 验证）

### GAAP → v3.1 桥接

```
GAAP 税前 (Pretax)                    $712M
  非利息 OtherInc = Pretax − OpInc − NetInt
                     = 712 − 3130 − 0 = −$2,418M  ← BTC 持仓 MTM 亏损（detector 2a）
  amount = −$2,418M（损失）→ 不剥离（"只剔收益不加回亏损"）   ← 0
  Restructuring $1.96B                  ← detector 2b，[只标记]（费用非收益 + 连续 5 年增长=经常性）
  SGA spike                             ← detector 2g，[只标记]（低信心）
  TaxAnomaly: TTM 50% vs 3yr 均值（2024 DTA 释放扭曲→负）  ← 触发，但 v3.1 ≈ GAAP（税率调整微小）
  = 正常化税前                          $712M（无剥离）
  × (1 − TTM 税率 50%)
  = 正常化净利                          $356M
  ÷ 稀释股数 608M
  = v3.1 EPS                            $0.58
```

### Detector 2a: OtherInc（非利息其他收入）

**定义**：非利息 Other = Pretax − Operating Income − Net Interest = 712 − 3130 − 0 = −$2,418M

子项拆解（从 TTM CSV 逐行读）：

| 子项 | 金额 | 性质 |
|------|------|------|
| Gain On Sale Of Security | −$436M（TTM） | 投资 MTM（BTC 持仓 + 证券） |
| 未列缺口 | ~−$1,982M | BTC 持仓减值 + 其他投资损益 |
| **合计** | −$2,418M | 全部为**损失/费用**（负值） |

> 季度波动率：5 季全为负（Q2'26 −$675M, Q1'26 −$667M, Q4'25 −$739M, Q3'25 −$136M, Q2'25 −$95M），波动来自 BTC 价格波动 → 真 MTM 波动。但 amount < 0（损失）→ **不剥离**（per "只剔收益不加回亏损"）。

### Detector 触发原因分析

- **OtherInc (2a)**：真波动触发（季度全负，BTC MTM），但 amount < 0 = 损失 → 不剥离
- **TaxAnomaly (2c)**：TTM 50% vs 3yr 均值（2024 DTA 释放 −111% 扭曲均值）→ 触发，但 v3.1 ≈ GAAP
- **[Restructuring] (2b)**：$1.96B TTM，连续 5 年增长（$550M→$660M→$794M→$1.34B→$1.96B）= 经常性非一次性 → 只标记
- **[SGASpike] (2g)**：SGA/Rev 跳升（法律应计 $526M DOJ + $45M 州和解）→ 只标记

### Unusual 重叠检查

```
|OtherInc −$2,418M| vs |Total Unusual −$2,40B|
→ 两者均为负（损失），detector 不剥离（不加回亏损）
→ tool 加回全部 Unusual → $2.95；v3.1 不加回 → $0.58
→ min(GAAP $0.56, tool $2.95, v3.1 $0.58) = $0.56
```

### 三口径对比

| 口径 | 剥离额 | Normalized NI | EPS |
|------|--------|--------------|-----|
| GAAP | 0 | $357M | $0.56 |
| 工具 | +$2.40B（加回 Unusual 损失） | $1.79B | $2.95 |
| v3.1 | 0（不加回损失） | $356M | $0.58 |

> 工具剥离额 vs v3.1 差距 = tool 加回 −$2.40B Unusual 损失（BTC + 重组），v3.1 按"不加回亏损"保留 GAAP。
> **旧分析用 $3.54（adj/毛利润口径，回加 SBC + 摊销）→ 非框架口径**。框架不回加 SBC/摊销 → FINAL $0.56。差异 530%。
> **XYZ 属"低 GAAP 盈利 + 强 FCF"类（同 COIN）**：GAAP NI 被非现金 BTC MTM（−$2.22B）+ 重组（$1.96B）严重压低，但 FCF $3.88B 不受影响 → EPS 模型过度保守，DCF 交叉验更准确（见 Task D D.2b）。

## B.6 质量地板（给 Task D 预判）

| 指标 | 值 | ✓/✗ |
|------|-----|-----|
| GM >60% 稳 | 46.4%（TTM） | ✗（注：Revenue 含 BTC 毛记账拉低 GM；GP/Rev 46.4% 对支付/金融科技算正常，但框架阈值 60% 硬线 ✗） |
| NM >20% | 1.4%（TTM） | ✗（极薄，GAAP NI 被压低；adj NM ~8% 更代表性但仍 <20%） |
| FCF yield >5% | 8.2%（$3.88B / $47.46B） | ✓ |
| FCF−SBC >0 | +$2.68B | ✓ |
| 真缩股 | 636M→608M（3yr −4.6%，TTM 回购 $1.89B > SBC $1.20B） | ✓ |
| ROIC >15% 或 ROE >15% | ROIC 11.1%、ROE 1.6% | ✗（ROE 被 GAAP NI 压低；ROIC 11.1% < 15%） |

本地评分: **3/6** → 至少"好公司 ×0.67"，待 C 确认护城河（中→不加分 → 3/7 好公司）
