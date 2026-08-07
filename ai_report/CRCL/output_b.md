# CRCL — Task B：财务健康 + 正常化 EPS
> 更新: 2026-08-07（财报 FY26 Q1，TTM 2026-03）⚠️ 新近 IPO（2025-06），<1yr 公开数据

## B.1 SCORECARD 九宫格

| 维度 | 3yr | TTM | 5Q |
|------|-----|-----|-----|
| Income | 20 | 45 | 32 |
| CF | 70 | 25 | 30 |
| BS | 82 | 61 | 60 |

权重: Income 25% / CF 35% / BS 40%

### 背离检验

| 维度×窗口 | SCORECARD 说 | 原始财报 | 方向 |
|------|------|------|------|
| Income 3yr=20 | OpInc −155.9%、GM 29.4%→8.7% 崩塌 | **证实**：营收增长但 GM 压缩 + SBC 暴增 → OpInc 转负 | **同向 = 恶化** |
| Income TTM=45 | 3/4 季盈利（Q2'25 IPO 巨亏拖累 TTM） | **误伤**：Q2'25 −$482M = IPO 一次性（SBC 加速 + 亏损） | **错杀 = 恢复机会** |
| CF TTM=25 | FCF $446M 正但 SBC $601M 吞噬 | **证实**：FCF−SBC = −$155M < 0（IPO SBC spike 拖累） | **同向 = 隐忧** |
| BS 3yr=82 | D/E 0.01（几乎无债） | **证实**：Total Debt ~$0，干净 BS | **同向 = 亮点** |

伤口模式: 3yr Income 20（IPO 后 GM 崩塌 + SBC 暴增）+ TTM/5Q 45/32（Q2'25 IPO 一次性巨亏）= 新近 IPO + 业务模型转型期。Q3'25-Q1'26 3 季已恢复正盈利。

## B.2 利润表逐季

```
          Rev     GM%    OpInc   OpM%    NI       dilEPS  SBC     一次性
Q1'25  578M  26.8%   99M   17.1%    64M    0.00    12M     —（pre-IPO）
Q2'25  658M  -38.3% -326M  -49.5%  -482M   -4.48   431M    IPO SBC 加速 + COGS 异常
Q3'25  739M  21.9%   79M   10.7%   214M    0.64     59M    tax benefit -$61M
Q4'25  770M  22.4%   56M    7.3%   133M    0.43     59M    —
Q1'26  694M  21.5%   45M    6.5%    55M    0.21     51M    —
```

- **GM TTM 8.1%（TTM 被 Q2'25 负 GM 拉低）；正常化 GM ~21-22%**（Q3'25-Q1'26 稳定）
- **Q2'25 GM −38.3%**：COGS $910M >> Revenue $658M = IPO 一次性（SBC 加速 + 重组费用嵌入 COGS）
- **SBC Q2'25 $431M（IPO 加速）vs 正常 ~$55M/季**：TTM $601M 含 ~$376M 一次性 IPO SBC
- **OpM 正常化 ~6-11%**（Q3'25 10.7% → Q1'26 6.5%，下行趋势）
- **Revenue QoQ 下降**（$770M Q4 → $694M Q1）= 利率下行开始压缩储备利息收入

> ⚠ **旧 base.md GM ~90%+ 估算错误**：误将"利息收入 ≈ 全部毛利"当 GM。实算 TTM GM 8.1%（COGS $2.63B 含 Coinbase 分成 + 分销成本）。正常化 GM ~21-22%（post-IPO 稳定期）。

## B.3 现金流

| 项目 | TTM | 说明 |
|------|-----|------|
| OCF | $506M | 正（含 SBC 加回 $601M） |
| FCF | $446M | 正（CapEx $60M 低，轻资产） |
| SBC | $601M（21.0% Rev） | ⚠ 极高（含 IPO $431M 一次性；正常化 ~$225M = 7.9% Rev） |
| 回购 | $0 | 零回购 |
| Net Return | −$601M | 负（零回购 − SBC $601M） |

**FCF − SBC = $446M − $601M = −$155M < 0 → 重麻烦 → ×0.40**

> ⚠ **FCF−SBC < 0 由 IPO SBC spike 驱动**：Q2'25 SBC $431M（IPO 加速 vesting）vs 正常 ~$55M/季。正常化 FCF−SBC ≈ $446M − $225M = +$221M > 0。但硬规则用 TTM → ×0.40。
>
> 旧 base.md "FCF −$141M" 错误（实算 FCF = $446M）；"SBC 未披露"错误（TTM SBC = $601M）。

## B.4 资产负债表（Q1'26, bs_quarterly 2026-03-31）

| 项目 | 值 | 说明 |
|------|-----|------|
| Cash+STI | $1.52B | Cash $1.52B + STI $1M |
| 限制性现金 | $77.69B | ⚠ USDC 储备资产（**非公司现金**，客户资金） |
| 总债 | ~$0 | 无 Current Debt，无 Long Term Debt |
| **净现金** | **$1.52B** | MCap ~9%（中等托底） |
| D/E | ~0 | 几乎无债（干净 BS） |
| Cash/Debt | n/m（无债） | — |
| Goodwill | $265M | 3.3% Assets（低，干净） |
| 留存收益 | −$1.24B | 累计亏损（pre-IPO），NOL 可抵税 |
| BV/share | $13.84 | P/B 4.6x |
| Equity | $3.43B | IPO 后 APIC $4.66B 撑起 |

> ⚠ **限制性现金 $77.69B ≠ 公司资产**：USDC 稳定币储备（T-Bill + Cash），对应 USDC 发行负债。不进净现金计算。公司净现金 = Cash $1.52B − Debt $0 = $1.52B。

## B.5 正常化 EPS Chain（恢复 EPS — EPS-4b）

| 口径 | EPS (USD) | 来源 |
|------|----------|------|
| GAAP | **−$0.23** | TTM Diluted EPS（负值！Q2'25 IPO 巨亏） |
| 工具 | **−$0.38** | Normalized Income −$94M / 247M |
| v3.1 | **−$1.69** | detector 2e GMDrop +$356M 剥离（**假阳性**，见下） |
| **恢复 EPS** | **$1.20** | **EPS-4b**（见下） |

> ⚠ **三口径全负 → 用恢复 EPS（EPS-4b）**：TTM 含 Q2'25 IPO 巨亏（−$482M NI）。剥离后用 post-IPO 稳定季（Q3'25-Q1'26）年化。

### 恢复 EPS 推导（EPS-4b）

```
Post-IPO 稳定期 3 季（Q3'25 + Q4'25 + Q1'26）:
  Pretax = $153M + $140M + $56M = $349M
  Annualized Pretax = $349M × 4/3 = $465M
  正常税率 20%（hist 19%，含 NOL 耗尽后 normal）
  Annualized NI = $465M × (1-0.20) = $372M
  Diluted shares = 266M（Q1'26 post-IPO 稳定）
  恢复 EPS = $372M / 266M = $1.40

保守调整至 $1.20（利率下行风险 + GM 下行趋势 + IPO <1yr 数据有限）
```

> ⚠ **v3.1 −$1.69 假阳性**：detector 2e GMDrop 剥离 $356M（TTM GM 8.1% vs hist 20.6%，差 12.5pp × Revenue $2.86B = $356M）。但 GM 变化是**业务模型转型**（IPO 后分销成本上升），非一次性。v3.1 过度剥离。取 GAAP 兜底 → 负 → 用恢复 EPS。
>
> ⚠ **工具 EPS −$0.38** vs GAAP −$0.23：工具 Normalized Income −$94M（含 Total Unusual Items $25M 剥离），比 GAAP NI −$79M 更负。两者均负 → 用恢复 EPS。

### Detector 详情（normalize_eps.py 实跑）

| Detector | 信心 | 金额 | 性质 |
|----------|------|------|------|
| 2a: OtherInc(MTM) | high | −$44M（pre-tax） | 负值→不剥离（只剔收益不加回亏损） |
| 2c: TaxAnomaly | medium | −$31M（after-tax） | TTM 41.9% vs hist 19.0%（差 22.9pp） |
| 2e: GMDrop | medium | +$356M（pre-tax） | **假阳性**：GM 变化是业务模型转型非一次性 |
| 2x: Unusual(tool) | high | +$25M（pre-tax） | 工具归类 Unusual $25M |

## B.6 质量地板（给 Task D 预判）

| 指标 | 值 | ✓/✗ |
|------|-----|-----|
| GM >60% 稳 | 8.1% TTM / ~21% 正常化 | ✗ |
| NM >20% | −2.8% TTM / ~8% 正常化 | ✗ |
| FCF yield >5% | 2.6%（$446M/$16.91B） | ✗ |
| FCF−SBC >0 | **−$155M** | ✗（→ 重麻烦 ×0.40） |
| 真缩股 | 222M→247M（+11% dilution，IPO 发股） | ✗ |
| ROIC/ROE >15% | ROE −3.0% / ROIC n/m | ✗ |

本地评分: 0/6 + 护城河（C 确认中，+1）= **1/7 = 平庸**

> **FCF − SBC < 0 → 重麻烦 → ×0.40**（per CLAUDE.md 硬规则："不否决、总是估值"）。
> 旧 output 标"框架外/一票否决"——违反硬规则。已修正：总是估值，×0.40，恢复 EPS $1.20。
> SBC $601M TTM 含 IPO $431M 一次性 spike；正常化 SBC ~$225M（7.9% Rev）。
