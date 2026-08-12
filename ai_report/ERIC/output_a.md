# ERIC — Task A：价格层（daily）
> 更新: 2026-08-07  现价 $10.15
> ⚠️ **多币种**（SEK/USD = 9.58）| **强周期股**（P/E 分位反读，用 P/B 分位 + mid-cycle P/E）

## A.1 价格粗筛 + price-dependent 指标（8 项，满足任意 1 条入池）

> ⚠ 多币种陷阱：info.json 的 P/B = 0.3x **错误**（混 USD 价 / SEK 权益）；EV/EBITDA 和 P/S 缺失。FCF yield cheap 工具 89.5% **错误**（SEK FCF / USD MCap 混算）。**全部手算统一币种**。

| # | 条件 | 阈值 | 实际值 | ✓/✗ |
|---|------|------|--------|-----|
| 1 | 1Y 回撤 | >40% | 26.2%（high $13.74 → $10.15） | ✗ |
| 2 | 2Y 回撤 | >60% | 26.2% | ✗ |
| 3 | 距 52W 低 | ≤15% | 35.9%（low $7.47 → $10.15） | ✗ |
| 4 | P/E TTM | <15x | 13.2x（$10.15/$0.77 GAAP；⚠ 正常化 16.6x 含 Iconectiv 剥离） | ✓ |
| 5 | FCF yield | >5% | **9.3%**（FCF SEK 29.79B÷9.58=$3.11B / MCap $33.29B） | ✓ |
| 6 | EV/EBITDA | <10x | **6.9x**（手算：EV $31.3B / EBITDA $4.51B） | ✓ |
| 7 | P/B | <1.5x | **3.07x**（手算 $10.15/BV $3.28；info.json 0.3x **错误**） | ✗ |
| 8 | P/S | <2.0x | **1.39x**（手算：MCap $33.29B / Rev $23.74B） | ✓ |

命中: **4/8**（P/E ✓ + FCF yield ✓ + EV/EBITDA ✓ + P/S ✓）

> ⚠ **FCF yield 手算**：cheap 工具显示 89.5%（SEK FCF 29.79B / USD MCap 33.29B = 混算，多币种陷阱）。正确：FCF SEK 29.79B ÷ 9.58 = $3.11B → $3.11B / $33.29B = 9.3% ✓

FCF yield = $3.11B / $33.0B = **9.4%**

手算明细（SEK ÷ 9.58 = USD）:
- Revenue TTM: SEK 227.55B → $23.74B → P/S = $33/$23.74 = 1.39x
- EBITDA TTM: SEK 43.23B → $4.51B
- Debt: SEK 39.48B → $4.12B；Cash: SEK 55.76B → $5.82B
- EV = $33 + $4.12 − $5.82 = $31.30B → EV/EBITDA = $31.30/$4.51 = 6.94x
- BV/share: SEK 31.4 → $3.28 → P/B = $10.06/$3.28 = 3.07x（MacroTrends 3.00x）

## A.2 估值分位

### 周期股口径：P/E 反读 + P/B 分位

| 口径 | 当前 | 5yr 高 | 5yr 低 | 分位 | 来源 |
|------|------|--------|--------|------|------|
| GAAP P/E | 13.1x | 17.66x（2021-03） | 6.84x（2022-09） | 58.5th | [MacroTrends](https://www.macrotrends.net/stocks/charts/ERIC/ericsson/pe-ratio) |
| 正常化 P/E | 16.4x | 同上 | 同上 | 88.6th | 手算（$10.06/$0.612） |
| **P/B** | **3.00x** | 3.29x（2026-06） | 1.28x（2022-23 谷底） | **85.6th** | [MacroTrends](https://www.macrotrends.net/stocks/charts/ERIC/ericsson/price-book) |

> ⚠ **屏幕 P/E 13.1x 低估贵**：GAAP EPS $0.77 含 Q4'25 Iconectiv 出售收益 +8.07B SEK，正常化后 P/E 16.4x 才是真口径。
>
> 周期股判读: P/E 58.5th（非 >70% 谷底信号）+ P/B 85.6th（非 <30% 谷底信号）→ **不在周期底部**。P/B 3.00x 处 5yr 高位（85.6th），距谷底 1.28x 远。

### 同业对比（RAN / 电信设备）

| 公司 | P/E | P/B | 备注 |
|------|-----|-----|------|
| **ERIC** | **13.1x GAAP / 16.4x norm** | **3.00x** | RAN 龙头、低增长周期 |
| Nokia (NOK) | ~14-16x | ~1.5x | 直接对标，P/B 低得多 |
| Cisco (CSCO) | ~15-17x | ~3-4x | 企业网络，GM 64% 质地更稳 |

ERIC vs NOK：P/E 贴近，但 P/B 3.0x vs NOK ~1.5x → ERIC P/B 偏高（equity 因 Vonage 减值缩水）。质地不如 CSCO（GM 47% vs 64%）。

### de-rating 判断

**非 de-rating 也非 re-rating**——Ericsson 长期就是低倍数周期股（历史中位 ~13-15x 正常化）。屏幕 P/E 13.1x 的"便宜"是 Q4'25 Iconectiv 出售收益制造的假象，正常化 P/E 16.4x 略高于历史中枢。P/B 3.0x 处高位（因减值缩 equity + 价格恢复），非深度折价。
