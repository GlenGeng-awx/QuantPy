# MSFT — Task B：财务健康 + 正常化 EPS
> 更新: 2026-08-01（财报 FY26 Q4/全年，2026-07-29 发；下次 Q1 FY27 ~2026-10）
> ⚠️ CSV 缺 Diluted EPS + Diluted Average Shares 字段（nan），EPS 手算 NI/shares

## B.1 SCORECARD 九宫格

| 维度 | 3yr | TTM | 5Q |
|------|-----|-----|-----|
| Income | 90 | 100 | 92 |
| CF | 90 | 100 | 85 |
| BS | 82 | 68 | 80 |

权重: Income 25% / CF 35% / BS 40%

### 背离检验

| 维度×窗口 | SCORECARD 说 | 原始财报 | 方向 |
|------|------|------|------|
| CF 3yr=90→5Q=85 | FCF 3yr −3.3%、5Q YoY −22% | **证实**：capex 两年翻倍 $44B→$116B（FY24→FY26 2.6x），FCF 停滞。但 OCF +34% 强 | **同向 = capex 吞噬 FCF 真瑕疵** |
| BS 3yr=82→TTM=68 | PPE 暴增 + capex 推高杠杆 | **证实**：Net PPE $154B→$308B（2 年翻倍）；但净现金 $21B、D/E 0.10 | **同向 = 主动加杠杆建数据中心** |
| Income 5Q=92 | GM Q YoY 微降 68.6%→67.2% | **轻度误伤**：GM 稳 67-69%，波动 <1.5pp | **噪声** |

伤口模式: 无经营伤口（OpInc +17-20%/yr）。"伤口" = FCF 被 capex 压制 = 消化期，非基本面恶化。

## B.2 利润表逐季

```
          Rev      GM%    OpInc   OpM%    NI       EPS     备注
Q3 FY25  70.07B  68.7%  32.00B  45.7%  25.82B
Q4 FY25  76.44B  68.6%  34.32B  44.9%  27.23B
Q1 FY26  77.67B  69.0%  37.96B  48.9%  27.75B          OpenAI 权益亏拖累
Q2 FY26  81.27B  68.0%  38.27B  47.1%  38.46B          ★含 OpenAI 一次性重估 +$7.6B
Q3 FY26  82.89B  67.6%  38.40B  46.3%  31.78B
Q4 FY26  90.01B  67.2%  40.60B  45.1%  ~30.2B   ~$4.81  ← 最新（7/29 发）
```

- **OpInc 32.0→34.3→38.0→38.3→38.4→40.6B，稳步 +17-20% YoY**——干净经营信号
- **GM 稳定 67.2-69.0%**（5 季波动 <1.8pp）——定价权与盈利能力顶级
- **NI 被 OpenAI 权益法剧烈扰动**：Q2 FY26 +$7.6B 一次性重估（OpenAI 转制 PBC）
- **背离方向 = 低估贵**：GAAP NI 含 $7.6B 一次性收益 → 正常化后更贵

## B.3 现金流

| 项目 | TTM | 说明 |
|------|-----|------|
| OCF | $182.94B（+34.3% YoY vs FY25 $136.16B） | 极强 |
| CapEx | $115.95B（CapEx/OCF 63%） | AI 数据中心 ~$116B/年 run-rate（FY24 $44B→FY26 $116B，2.6x） |
| FCF | $66.99B（3yr −3.3%） | 被 capex 压制；yield 见 A（price-dependent） |
| OCF/NI | 1.37 | 利润含金量高 |
| SBC | $12.41B（SBC/Rev 3.7%） | 低、节制 |
| 回购 | $22.27B + 分红 $26.45B | Net Return +$36.31B |

`FCF − SBC = 66.99 − 12.41 = +$54.58B > 0`（cf_ttm 2026-06-30），但 FCF 3yr 见顶停滞（capex 吞噬，FY24 $74B→FY26 $67B）

## B.4 资产负债表

| 项目 | 值 | 说明 |
|------|-----|------|
| 现金+短投 | $76.65B | — |
| 总债 | $56.83B | **净现金 ~$20B** |
| D/E | 0.10（3yr 0.23→0.13→0.10 下降） | 极低杠杆 |
| Net PPE | $154B→$308B（2 年翻倍） | AI 数据中心 capex 资本化 |
| Goodwill | $119.66B（含 Activision） | 无减值信号 |
| **利息覆盖** | **50.9x** | $155.24B OpInc / $3.05B Interest |

## B.5 正常化 EPS Chain

| 口径 | EPS | 来源 |
|------|-----|------|
| GAAP | $17.95 | income_annual Diluted EPS（FY26 = TTM，2026-06-30；income_ttm Diluted EPS=nan 用 annual 兜底） |
| 工具 | $17.33 | Normalized Income $129.135B / 7.453B shares |
| v3.1 | $16.20 | v3.1 NI $120.72B / 7.453B shares（剥 OtherInc $10.447B + Unusual $5.725B，diff 45.2%>20% 判独立） |
| **FINAL** | **$16.20** | **min(三者) = v3.1** |

> ⚠️ income_ttm.csv Diluted EPS + Diluted Average Shares 均为 nan（数据下载问题）。GAAP EPS 取 income_annual col0（FY26）Diluted EPS $17.95（FY26 = TTM，同截至 2026-06-30）。shares 7.453B 取 income_annual Diluted Average Shares。v3.1 手工计算（normalize_eps.py 因 TTM 缺 shares 返 $0.00）。
> ⚠️ v3.1 剥 $16.172B pre-tax 中含 OpenAI $7.6B 一次性（正确）+ Gain On Sale $5.9B + 其他 $2.6B（可能含经常性利息收入 → v3.1 可能过度保守，normalize_eps.md 已知问题 #2）。但 per 框架硬规则 FINAL = min(GAAP, tool, v3.1) = $16.20，**不许取 GAAP 上界**（`mistakes.md` 二）。

- winner: v3.1
- adj: −9.7%（$16.172B pre-tax 剥离）
- detectors: 2a OtherInc(MTM) $10.447B（vol 3.4x，range -3.94B~9.87B）+ 2x Unusual(tool) $5.725B（diff 45.2%，判独立）

### Detector 2a: OtherInc（OpenAI 投资收益）

OtherInc $10.447B 含 Q2 FY26 OpenAI 一次性重估 $7.6B + Gain On Sale Of Security $5.9B + 其他投资收益。vol 3.4x 触发（投资 MTM 波动）。

### Detector 2x: Unusual

工具 Unusual $5.725B 与 OtherInc $10.447B diff 45.2% → 判独立，都剥离。可能含部分重叠（OpenAI 收益同时在 OtherInc 和 Unusual 中）→ **疑似过度保守**。

### 评估

v3.1 剥 $16.172B pre-tax 中含 OpenAI $7.6B 一次性（正确剥离）+ Gain On Sale $5.9B + 其他投资收益 $2.6B（可能含经常性投资收益 → **过度保守**，normalize_eps.md 已知问题 #2）。**补偿路径**：per 框架硬规则仍取 min = $16.20（不许取 GAAP 上界，`mistakes.md` 二/TME 案例）。两路殊途：v3.1 $16.20 → 合理价 $348（g=13%）；GAAP $17.95 → 合理价 $386。两者均 < 现价 $500 → 买贵了结论稳健。

## B.6 质量地板（给 Task D 预判）

| 指标 | 值 | ✓/✗ |
|------|-----|-----|
| GM >60% 稳 | 67.9%（5 季波动 <1.8pp） | ✓ |
| NM >20% | 40.3% | ✓ |
| FCF−SBC >0 | $54.58B | ✓ |
| 真缩股 | 7.472B→7.453B（3yr，微缩 −0.25%） | ✓* |
| ROIC >15% | 29.6% | ✓ |

本地评分: 5/5（全 ✓）+ 护城河极宽 ✓ = **6/6 = 伟大**（CapEx $116B 吞噬 FCF 是主动投入非恶化）

> FCF yield 不在质量评分（在 A.1 粗筛 #5）。B 只存 FCF 金额。
> 伟大 + 无麻烦 → ×1.0（discount_coefficient.md 主表无麻烦列；巴菲特"合理价买伟大公司"——合理价三重保守即边际，无需额外折扣）。
