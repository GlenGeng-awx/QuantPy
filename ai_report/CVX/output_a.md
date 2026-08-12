# CVX — Task A：价格层（daily）  ⚠️ 周期股（一体化油企）
> 更新: 2026-08-07  现价 $186.56

## A.1 价格粗筛 + price-dependent 指标（8 项，满足任意 1 条入池）

| # | 条件 | 阈值 | 实际值 | ✓/✗ |
|---|------|------|--------|-----|
| 1 | 1Y 回撤 | >40% | 11.3%（高 $209.23 → 现 $186.56） | ✗ |
| 2 | 2Y 回撤 | >60% | 11.3% | ✗ |
| 3 | 距 52W 低 | ≤15% | 27.3%（$186.56 vs 低 $146.49） | ✗ |
| 4 | P/E TTM | <15x | 32.3x（$186.56/$5.77 quarterly TTM EPS；info.json 18.2x 用 stale EPS $10.24） | ✗ |
| 5 | FCF yield | >5% | 3.8%（FCF $13.78B quarterly rebuild / MCap $365.96B） | ✗ |
| 6 | EV/EBITDA | <10x | **8.1x**（info.json） | ✓ |
| 7 | P/B | <1.5x（周期） | 2.0x（BV $92.91） | ✗ |
| 8 | P/S | <2.0x | **1.75x**（MCap $365.96B / Rev $209.37B） | ✓ |

命中: **2/8**（EV/EBITDA 8.1x + P/S 1.75x）。弱入池信号。距 52W 低 +27%（非底部）。

> ⚠ **P/E 反读（周期股）**：TTM P/E 32.3x（高 = 低谷盈利 → 周期底信号？但 P/B 2.0x 84th 分位 ≠ 周期底）。info.json trailingEps $10.24（stale mid-2025）。周期股 P/E 反读需配合 P/B <30% = 周期底，CVX P/B 84th → **非周期底**。
>
> ⚠ **income_ttm.csv 数据缺失**：TTM CSV 仅含 Diluted EPS $10.39 + shares，其余字段空白。实际 quarterly TTM EPS = $5.77。normalize_eps 无法运行。用 quarterly 重建 + 中周期正常化。
>
> FCF yield 用 quarterly rebuild FCF $13.78B（cf_ttm.csv stale $16.10B 为 mid-2025）。

## A.2 估值分位（周期股：P/B 为主，P/E 反读）

### 双分位（暂停 — TTM EPS stale/incomplete）

| 口径 | 当前 | 5yr 高 | 5yr 低 | 分位 | 来源 |
|------|------|--------|--------|------|------|
| GAAP P/E TTM | 32.3x（quarterly rebuild $5.77） | — | — | — | TTM CSV stale，无 5yr P/E 区间 |
| 正常化 P/E | 18.1x（中周期 EPS $10.3） | — | — | — | 无 5yr 正常化序列 |

> **双分位暂停**：income_ttm.csv 数据缺失（仅 EPS/shares，无 Rev/OpInc/NI），TTM EPS stale $10.39 vs quarterly rebuild $5.77。无法从 MacroTrends 获取可靠 5yr P/E 区间。用 P/B 分位替代（周期股 fallback）。

### P/B 分位（周期股主口径）

| 口径 | 当前 | 5yr 高 | 5yr 低 | 5yr 中位 | 分位 | 来源 |
|------|------|--------|--------|---------|------|------|
| P/B | 2.0x | 2.16x（2026-03 Hess 并表峰） | 1.18x（2021-09） | ~1.57x | **84th ✗** | [MacroTrends](https://www.macrotrends.net/stocks/charts/CVX/chevron/price-book) |

> P/B 分位 = (2.0−1.18)/(2.16−1.18) = 84th >30% → **✗ 非周期底**。P/B 从 2021 低 1.18x 升至 2.0x = Hess 并表 + 油价偏软但股价未深跌。真正周期底 P/B <1.3x（2020 曾到 0.97x）。当前 2.0x 处中高位。

### P/E 反读（周期股辅助口径）

| 口径 | 当前 | 说明 |
|------|------|------|
| GAAP P/E (quarterly TTM) | 32.3x | TTM EPS $5.77（低谷，含衍生品损失）→ P/E 高 = 周期低信号 |
| GAAP P/E (info.json stale) | 18.3x | trailingEps $10.18（mid-2025，stale） |
| 中周期 P/E | 18.1x | $186.41 / 中周期 EPS $10.3 |

> **周期股 P/E 反读规则**：P/E >70% + P/B <30% = 周期底部。CVX：P/E 32.3x（高）+ P/B 84th（高）→ P/B 未满足 <30% → **非周期底**。P/E 高反映低谷盈利，但 P/B 高反映股价未充分回调。

### 同业对比

| 公司 | P/B | 股息率 | 前瞻 P/E（adj） | 备注 |
|------|-----|--------|-----------------|------|
| **CVX** | **2.0x** | **4.0%** | ~11-13x | P/B 更低、股息率更高（相对 XOM 便宜） |
| XOM | ~2.4x | 3.0% | ~15x | BS 更强、市场给品质溢价 |

CVX 相对 XOM **P/B 折价 ~17%、股息率高 100bp** = 相对便宜，但代价是 Hess 杠杆升 + DD&A 拖累。

### de-rating 判断

1Y 回撤仅 11%（非深度回调）。P/B 2.0x = 5yr 84th 分位（中高位）。油价从 2022 峰回落但股价未深跌 → 市场定价"产量增长 + 股息安全 + Hess 协同"溢价。**非错杀，估值部分合理但缺好价格**。
