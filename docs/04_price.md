# Task 4: 价格层

> **产出**: 粗筛命中 (N/8) + 分位门 (P/E+P/S 都 ≤30%?) + derating 判断 + 总结。
> 
> **依赖**: output_1 (v3.1 EPS + FCF) + output_2 (g 多档位 → derating) + stock_data CSV + info.json + MacroTrends (web)。
> 
> 两套分析: 1→2→3 = 基本面 (财务+增长+质量); **4 = 市场价格 (分位数 vs 自身历史)**; 5 = 估值 (合并 1+2+3+4); E = 决策 (合并 4+5 交叉验, 读全量 output)。
> 
> **output_4.md 结构 = 本文档节序 (§4.1→§4.2→§4.3→§4.4); 各 § 节的表格式即 output 格式, 不另设模板。**

### 串行输入 (读前序 output)

- **output_1 v3.1 EPS**: 正常化 P/E 分位 (§4.2); FCF yield (§4.1 #5)
- **output_2 g 多档位**: derating 判断 (§4.3, 当前 g vs 历史 g)
- **stock_data CSV + info.json**: 粗筛 + P/S P/B 本地分位
- **MacroTrends (web)**: P/E 5yr 历史

## §4.1 价格粗筛 (8 项, 满足任意 1 条入池)

| # | 条件 | 阈值 | 数据源 | key |
|---|------|------|--------|-----|
| 1 | 1Y 回撤 | >40% | stock_data CSV 近 252 日 | close 最高 vs 最低 |
| 2 | 2Y 回撤 | >60% | 同上, 504 日 | |
| 3 | 距 52W 低 | ≤15% | CSV | 现价 vs 252 日最低 |
| 4 | P/E TTM | <15x | info.json | `trailingPE` (GAAP; 正常化 P/E 见 §4.2) |
| 5 | FCF yield | >5% | FCF (cf_ttm) / MCap (info.json) | output_1 FCF / info.json MCap |
| 6 | EV/EBITDA | <10x | info.json | `enterpriseToEbitda` |
| 7 | P/B | <1.0 (金融) / <1.5 (周期) | info.json | `priceToBook` |
| 8 | P/S | <2.0x | info.json | `priceToSalesTrailing12Months` |

### 特殊口径

```
金融股: P/B <1.0 替代 EV/EBITDA
周期股: 正常化 P/E <12x / P/B <1.5x / 净现金/市值 >30% / 股息率 >5%
轻资产 (GM>60% 或 CapEx/Rev<5%): P/B 不适用 → 标"—"，不算 ✗
NM>25%: P/S 阈值 2.0x → 4.0x
```

### ⚠ 多币种 ADR 陷阱

```
EV/EBITDA 在多币种股上失真 (MCap 用股价币种, EBITDA 用财报币种)
→ 必须手算 EV = MCap + 总债 − 现金 (统一币种)
→ 见 08_reference.md 多币种处理
```

### 工具

```bash
python3 -m fundamental.cheap STOCK    # 价格回撤筛选: 6 信号 ranking + TA + 估值 display
```

output 格式:

| # | 条件 | 阈值 | 实际值 | ✓/✗ |
|---|------|------|--------|-----|
| 1 | 1Y 回撤 | >40% | ...% | ✓/✗ |
| ... | ... | ... | ... | ... |

命中: **{N}/8**

## §4.2 估值分位 (web + 本地)

### 分位表 (4 口径)

| 口径 | 当前 | 5yr 高 | 5yr 低 | 分位 | 来源 |
|------|------|--------|--------|------|------|
| GAAP P/E | 现价 / GAAP EPS | MacroTrends | MacroTrends | (当前−低)/(高−低) | web |
| 正常化 P/E | 现价 / **output_1 v3.1 EPS** | MacroTrends (共用) | 同 | 同 | web + output_1 |
| P/S | MCap / TTM Rev | 本地/MacroTrends | 同 | 同 | price CSV × shares / rev |
| P/B | MCap / Equity | 本地/MacroTrends | 同 | 同 | price CSV × shares / equity |

**P/E + P/S 分位都须 ≤30%** 才算便宜 (P/B 仅参考, 轻资产不适用)。查不到则暂停, 严禁估算。

> **P/S P/B 本地计算**: 用 stock_data CSV (日 close) × annual shares / annual revenue (P/S) 或 annual equity (P/B) → 算每日 P/S P/B → 5yr range = last 1260 交易日 min/max/percentile。不需要 web。

> 正常化 P/E 分位复用 GAAP P/E 的 5yr 范围 (MacroTrends 只有 GAAP)。
> GAAP EPS 从 `income_ttm.csv` `Diluted EPS` 直接读。**v3.1 EPS from output_1**。

### 同业对比

列可比同业当前 P/E + 性质, 算折/溢价%。剔除性质不可比者。

output 格式:

| 同业 | P/E | 性质 | vs 标的 |
|------|-----|------|---------|
| (公司) | ...x | (可比/不可比) | 折/溢价 N% |

### 工具

```bash
# MacroTrends via playwright
# 分位公式: (current - low) / (high - low)
```

## §4.3 de-rating 陷阱

```
5yr P/E 范围如果跨越了两个增长范式:
  高端 = 旧范式溢价 (如 COVID 期 g=30% 的成长溢价)
  低端 = 新范式 (增速降到 13%)
  → 低分位 = de-rating 假象, 不是真便宜

检查:
  1. 5yr 范围是否跨不同增长范式?
  2. 当前 g (from output_2) vs 历史 g 是否大幅不同?
  3. YoY 在降 + 5yr avg >> current g → derating_flag = True
  → derating 时分位门标"不可信"
```

output 格式:

| 检查项 | 结果 |
|--------|------|
| 5yr 跨范式? | 是/否 (说明) |
| 当前 g vs 历史 g | output_2 调整 g vs 历史 CAGR (gap Npp) |
| YoY 方向 | 加速/减速/稳定 (from output_1 趋势表) |
| derating_flag | True/False |

> derating_flag = True → §4.2 分位标"不可信"; Task E 用 output_5 公式价交叉验

---

## §4.4 总结 (→ Task E 快速消费)

| 项 | 内容 |
|----|------|
| 一句话定性 | (便宜/不便宜/不可判断) + 核心原因 |
| 粗筛命中 | N/8 (哪几条) |
| 分位结论 | P/E Nth + P/S Nth (≤30%?); derating_flag? |
| Top risk | 分位是否可信? derating? 多币种? 数据不足? |
