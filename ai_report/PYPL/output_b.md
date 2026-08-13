# PYPL — Task B：财务健康 + 正常化 EPS
> 更新: 2026-08-08（财报 Q2'26 FY26，2026-07-28 发；TTM 戳 2026-06）

## B.1 SCORECARD 九宫格

| 维度 | 3yr | TTM | 5Q |
|------|-----|-----|-----|
| Income | 92 | 57 | 50 |
| CF | 78 | 100 | 100 |
| BS | 65 | 100 | 100 |

权重: Income 25% / CF 35% / BS 40%

### 背离检验

| 维度×窗口 | SCORECARD 说 | 原始财报 | 方向 |
|------|------|------|------|
| Income TTM=57/5Q=50 | OpInc −1.8%、EBITDA −5.3%、EPS −2.2% YoY | **证实（真恶化）**: GM 5 季 −140bps（take-rate 被 Stripe/Adyen/Apple Pay 挤压），OpInc 停滞 = take rate 吃掉增长 | **同向 = 已正确定价（陷阱侧）** |
| CF TTM/5Q=100 | FCF $6.59B、OCF Q +120.8%、FCF Q +156.5% YoY | **证实（改善！）**: FCF 从 $5.56B→$6.59B 大幅改善，重组见效 | **同向但方向反转 = 重组见效** |
| BS 全满分 | Net Debt $2.14B、GW 13%、D/E 0.68 | **证实**: BS 无瑕 | **同向 = 已正确定价** |

伤口模式: **半结构性伤口**——GM 下滑 140bps 是真实 take-rate 侵蚀（非情绪）；但 FCF 大幅改善 = 重组（20% 裁员 + Venmo 独立）见效。PYPL "好公司 × 半结构"（非"伟大 × 一次性"）的量化依据。

## B.2 利润表逐季

```
          Rev     GM%    OpInc   OpM%    NI      EPS     Shares
Q2'25  8.29B   46.3%  1.62B   19.5%  1.26B   1.29    977M
Q3'25  8.42B   46.0%  1.59B   18.9%  1.25B   1.30    960M
Q4'25  8.68B   46.4%  1.59B   18.3%  1.44B   1.53    939M
Q1'26  8.35B   45.6%  1.56B   18.7%  1.11B   1.21    920M
Q2'26  8.68B   44.9%  1.54B   17.7%  1.10B   1.25    882M  ← 最新
```

- **GM 阶梯下滑 46.3%→44.9%**（−140bps/5Q）——take-rate 结构性侵蚀
- **OpInc 停滞**: 1.62→1.54B，营收 +4.8% 但利润不增（−4.9% YoY）
- **EPS 全靠缩股撑**: 977M→882M（−9.7%/5Q），但 Q2'26 EPS 1.25 < Q2'25 1.29（−3.1% YoY）
- **重组费持续**: TTM ~$336M

## B.3 现金流

| 项目 | TTM | 旧值 | 变化 |
|------|-----|------|------|
| OCF | $7.47B（+16.5% YoY） | $6.42B | ↑↑ 改善！ |
| FCF | **$6.59B** | $5.56B | **↑↑ 大幅改善！** |
| SBC | $1.00B（2.9% Rev） | 3.0% | 降 |
| `FCF−SBC` | **$5.59B** | $4.56B | ↑↑ |
| 回购 | $6.05B + 分红 $382M | — | Net Return $5.43B（真缩股 9.7%/yr） |

> **重大变化**：FCF 从 $5.56B→$6.59B（+18%），FCF−SBC 从 $4.56B→$5.59B（+23%）。重组见效，现金流大幅改善。回购 $6.05B >> SBC $1.00B → 净缩股 → SBC 被回购对冲。

## B.4 资产负债表

| 项目 | 值 | 说明 |
|------|-----|------|
| 现金 + ST Inv | $11.26B | 2026-06 季度 |
| 总债 | $13.40B（含 current debt $2.50B） | Net Debt $2.14B（≈MCap 4.2%） |
| D/E | 0.68 | 稳定 |
| Goodwill | 13.4% Assets | 干净 |
| Treasury Stock | $36.16B | 持续回购沉淀 |
| **利息覆盖** | **13.6x** | $6.28B OpInc / $461M Interest |

> Net Debt $2.14B（非"≈0"，最新季度 current debt $2.50B 拉高总债）。Annual 2025-12 曾为 Net Cash +$0.43B。

## B.5 正常化 EPS Chain

| 口径 | EPS | 来源 |
|------|-----|------|
| GAAP | $5.29 | Diluted EPS（TTM 2026-06） |
| 工具 | $5.67 | Normalized Income $5.24B / 924M shares |
| v3.1 | $5.30 | detector 计算（total_adj=$0） |
| **FINAL** | **$5.29** | **min(三者) = GAAP** |

- winner: GAAP
- adj: 0%（v3.1 = GAAP，无 gain 需剥离）
- detectors: 2a OtherInc（−$408M loss，不剥离）+ 2b Restructuring（$336M 费用，只标记不剥离）

### GAAP → v3.1 桥接

```
GAAP 税前                    $5.86B
  − OtherInc 剥离（税前）      $0      ← detector 2a: amount=−$408M（loss, max(0,−408)=0）
  − Unusual 剥离（税前）       $0      ← 工具 Unusual=−$408M（loss, 不剥离）
  − Restructuring             $0      ← 2b confidence=low，只标记
  = 正常化税前               $5.86B
  × (1 − 税率 16.4%)
  = 正常化净利               $4.90B
  ÷ 稀释股数 924M
  = v3.1 EPS                 $5.30
```

### Detector 2a: OtherInc（非利息其他收入）

非利息 Other = Other Income Expense = −$406M（TTM）

子项拆解（从 TTM CSV）:

| 子项 | 金额 | 性质 |
|------|------|------|
| Other Income Expense | −$406M | 含投资 MTM + Gain On Sale |
| Gain On Sale Of Security | −$72M | 投资 MTM |
| **合计** | −$406M | 损失（负值） |

> OtherInc 为负（损失），按"只剔收益不加回亏损"原则不剥离 → v3.1 = GAAP。季度波动率 vol_ratio=2.1x（>2 触发），但 amount 为负 → max(0, −408)=0，不进 total_adj。

### Unusual 重叠检查

```
|OtherInc −408M − Unusual −408M| / max = 0.5%
→ <20% 重叠（同向负值）→ 不重复剥离（均为 loss，本就不剥离）
```

### 三口径对比

| 口径 | 剥离额 | Normalized NI | EPS |
|------|--------|--------------|-----|
| GAAP | 0 | $4.90B | $5.29 |
| 工具 | $341M | $5.24B | $5.67 |
| v3.1 | $0 | $4.90B | $5.30 |

> 工具剥离 $341M（Unusual loss 加回）→ 工具 EPS $5.67 > GAAP。min() 取 GAAP $5.29 保守。v3.1 = GAAP（无 gain 剥离）。

## B.6 质量地板（给 Task D 预判）

| 指标 | 值 | ✓/✗ |
|------|-----|-----|
| GM >60% 稳 | 45.8%（且下滑 −140bps） | ✗ |
| NM >20% | 14.4% | ✗ |
| FCF−SBC >0 | $5.59B | ✓ |
| 真缩股 | 977M→882M（−9.7%/yr） | ✓ |
| ROIC >15% 或 ROE >15% | ROE 24.5% > 15%（ROIC n/m 金融） | ✓ |

本地评分: **3/5 local** + 护城河 ✗（中等收窄，不加分）= **3/6 = 好公司**（FCF 强 + 真缩股 + ROE 高，但 GM 下滑 + NM 薄）
