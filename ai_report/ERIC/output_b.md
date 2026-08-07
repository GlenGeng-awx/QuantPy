# ERIC — Task B：财务健康 + 正常化 EPS
> 更新: 2026-08-07（TTM 2026-06，财报 Q2 FY2026）
> ⚠️ **多币种**：财报 SEK，ADR 价 USD。FX = 9.58 SEK/USD（反推：GAAP EPS SEK 7.38 ÷ trailingEps USD $0.77）
> ⚠️ **强周期股**：OpInc 3yr 4.9x 摆动（26.76B→6.24B→30.39B），盈利随 RAN capex 周期剧烈波动

## B.1 SCORECARD 九宫格

| 维度 | 3yr | TTM | 5Q |
|------|------|-----|-----|
| Income | 40 | 15 | 40 |
| CF | 47 | 76 | 60 |
| BS | 100 | 45 | 80 |

### 背离检验

| 维度 | SCORECARD 说 | 原始财报 | 方向 |
|------|-------------|---------|------|
| Income 3yr | 低分 40（营收 −4.5%/yr） | GM 47% 恢复中、OpInc 从谷底反弹 | 周期底部反弹非真成长 |
| CF TTM | 76（FCF 29.79B SEK 强） | OCF/NI 1.37 干净 | 周期高点 FCF 不可外推 |
| BS 3yr | 100（D/E 0.30 低杠杆） | 净现金、Goodwill 减值后缩水 | BS 最强项，但 goodwill 仍有 49B |

伤口模式: 3yr 低分（Income 40）= 从 2023 谷底（Vonage 减值 −33B）反弹的低基数放大 + TTM/5Q 转弱（营收 −6%、Q2'26 OpInc −4% YoY）。属**周期性伤口**——会随下一轮 RAN capex 周期恢复，但非"一次性一次过"。

## B.2 利润表逐季（SEK billions）

```
        Rev      GM%    OpInc   OpM%    NI      dilEPS  OtherInc  备注
Q2'26  52.69B  45.8%   6.12B   11.6%   4.05B    1.22   -429M     organic -1% (ex-IPR)
Q1'26  49.33B  47.2%   1.70B    3.4%   0.89B    0.27   -439M     北美去库+季节性
Q4'25  69.28B  47.2%   3.11B    4.5%   8.56B    2.57   +8.07B    ⚠ Iconectiv 出售
Q3'25  56.24B  47.6%  15.07B   26.8%  11.15B    3.33    -57M     OpM 异常高
Q2'25  56.13B  47.5%   6.37B   11.3%   4.57B    1.37   +403M     —
```

- **GM 47% 恢复中**（2023 谷底 38.6% → 2025 47.6% → TTM 47.0%），随价格/mix 波动
- **OpInc 剧烈摆动**：Q1'26 OpM 3.4% → Q3'25 26.8% → Q4'25 4.5%——强周期特征，单季不可外推
- **Q4'25 OtherInc +8.07B SEK**（Iconectiv 出售等处置收益）→ GAAP NI 8.56B 被垫高，正常化需剥离
- **营收下滑持续**：TTM −3.9% vs LY，Q2'26 −6% reported / −1% organic（ex-IPR licensing comp）

## B.3 现金流（TTM，SEK billions）

| 项目 | TTM | 说明 |
|------|-----|------|
| OCF | 33.78B | OCF/NI=1.37 |
| FCF | 29.79B | → $3.11B（÷9.58），yield 9.4% |
| SBC | 0 | ⚠ 瑞典 GAAP 未单列，可能内嵌于其他费用 |
| CapEx | 4.00B | CapEx/OCF=12%，轻资产 |
| 回购 | 3.22B（Q2'26 新启） | SEK 15B 程序 2026-04-23 启动 |
| 分红 | 5.0B（Q2'26） | DPS 3.00 SEK/年，2.05% yield |

FCF − SBC = **+29.79B SEK > 0** ✓（但 SBC=0 可能低估真实人力成本）

⚠ FCF 3yr 波动大：1.71B（'23 谷底）→ 42.62B（'24）→ 29.19B（'25）——周期高点 FCF 不可外推。
股东回报合计 ~6-7% yield（2% 股息 + ~4.7% 回购），但回购刚启动。

## B.4 资产负债表（Q2'06，SEK billions）

| 项目 | 值 | 说明 |
|------|-----|------|
| Cash & ST Inv | 55.76B | → $5.82B |
| Total Debt | 39.48B | → $4.12B |
| **净现金** | **16.28B** | **→ $1.70B（5.1% MCap）** |
| D/E | 0.30 | 低杠杆 |
| **利息覆盖** | **11.8x** | **>5x ✓** |
| Goodwill | 49.37B | Assets 20%，Vonage 减值后缩（2022 84.6B→49.4B） |
| Equity | 104.05B | BV/share SEK 31.4 → $3.28 |
| **P/B（手算/MacroTrends）** | **3.00x** | ⚠ info.json 0.3x **错误**（混 USD 价/SEK 权益） |

> 公司自报净现金 SEK 59.8B（含客户融资资产等广义口径），按框架定义（Cash−Total Debt）仅 16.28B。

## B.5 正常化 EPS Chain

> **周期股用 mid-cycle 正常化 EPS**（不用 TTM GAAP，含一次性处置收益）

### TTM EPS Chain（SEK → USD）

| 口径 | EPS (SEK) | EPS (USD) | 来源 |
|------|----------|----------|------|
| GAAP | 7.38 | $0.770 | Diluted EPS（含 Q4'25 Iconectiv +8.07B） |
| 工具 | 5.87 | $0.612 | Normalized Income 19.60B / 3.34B |
| v3.1 | 5.93 | $0.619 | detector 2a 剥 OtherInc 6.56B |
| **min(TTM)** | **5.87** | **$0.612** | **Tool（最低）** |

- detectors: OtherInc（detector 2a：OtherInc 6.56B，含 Iconectiv 出售收益，季度波动极大）
- FX = 9.58 SEK/USD（反推：GAAP SEK 7.38 ÷ info.json USD $0.77）

### Mid-cycle 正常化 EPS（周期股口径）

| 年 | Normalized NI (SEK) | Shares (B) | Norm EPS (SEK) |
|----|-------------------|-----------|----------------|
| 2022 | 19.62B | 3.33 | 5.89 |
| 2023 | 0.064B | 3.33 | 0.02（谷底，Vonage 减值） |
| 2024 | 1.53B | 3.33 | 0.46（谷底） |
| 2025 | 22.01B | 3.33 | 6.61 |
| TTM | 19.60B | 3.34 | 5.87 |

Mid-cycle EPS = **SEK 6.0**（正常年 2022/2025/TTM 均值 6.12，取保守 6.0）
→ **$0.626 USD**（SEK 6.0 ÷ 9.58）

> TTM min($0.612) 与 mid-cycle $0.626 接近——当前利润率尚未到中周期中枢（adj EBITA 18% 滚动已达标，但 Q2'26 单季 13.1% 仍偏低）。

## B.6 质量地板（给 Task D 预判）

| 指标 | 值 | ✓/✗ |
|------|-----|-----|
| GM >60% 稳 | 47%（3yr 38.6→44.1→47.6，恢复中但 <60%） | ✗ |
| NM >20% | 10.8% | ✗ |
| FCF yield >5% | 9.4%（$3.11B / $33B） | ✓ |
| FCF−SBC >0 | +SEK 29.79B（SBC=0，可能低估） | ✓ |
| 真缩股 | 3.33B→3.31B（−0.6%/3yr，刚启动回购） | ✗ |
| ROIC >15% | 22.8% | ✓ |
| 护城河宽 | 中（RAN duopoly，非宽） | ✗ |

本地评分: 2/7 → **平庸**（周期好公司，非伟大）。C 确认护城河中等 → 仍 2/7。
