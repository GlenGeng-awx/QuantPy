# 本地数据工具箱

> combine / cheap / health / statements 的输入输出和用法。

## 概述

四个本地工具，全部基于 `financial_data/` 和 `stock_data/` 下的 CSV/JSON，无需联网。

```bash
python3 -m fundamental.combine STOCK [STOCK ...]    # 全量（推荐）
python3 -m fundamental.cheap STOCK                  # 仅价格粗筛
python3 -m fundamental.statements STOCK             # 仅三张财报
python3 -m fundamental.health STOCK                 # 仅 SCORECARD
python3 -m fundamental.download STOCK               # 仅下载/更新数据
python3 docs/normalize_eps.py STOCK                 # 正常化 EPS（详见 docs/normalize_eps.md）
python3 docs/dcf.py STOCK G QUALITY [EPS]            # DCF 交叉验（详见 docs/dcf.md）
```

---

## combine — 全量分析（主力工具）

**代码**: `fundamental/combine.py`

**输入**:
- `stock_data/{STOCK}_1d.csv` — 日 K 线（价格、回撤）
- `financial_data/{STOCK}/income_*.csv` — 利润表（annual/quarterly/ttm）
- `financial_data/{STOCK}/cf_*.csv` — 现金流表
- `financial_data/{STOCK}/bs_*.csv` — 资产负债表
- `financial_data/{STOCK}/info.json` — 估值倍数、MCap、sector 等

**输出**（按顺序打印）:
1. **三张财报**（statements）— annual + quarterly + TTM，按 template 排列
2. **价格粗筛**（cheap）— 8 项信号 + 4 项技术提示，每项给 pass/fail + 实际值 + 详情
3. **SCORECARD**（health）— 9 宫格（Income/CF/BS × 3yr/TTM/5Q）+ ROIC/ROE/ROA + Risk Flags
4. **排名表**（多只时）— 按 cheap count 降序，一览所有标的的粗筛命中 + 九宫格分数

**与四任务框架的映射**:
- → Task A（价格粗筛）: cheap 的 8 项信号（含 FCF yield #5）
- → Task B（财务健康）: health 的 9 宫格 + statements 的原始数据
- → Task B（正常化 EPS）: statements 的 income CSV（`docs/normalize_eps.md` v3.1 checklist）
- 不覆盖 Task C（增长/消息面，需 web search）
- 不覆盖 Task D（估值汇聚，需 A+B+C 合并）

**关键**: combine 是**报案人不是评委**——SCORECARD 高分/低分、粗筛命中只是机械信号，结论永远来自读原始 CSV。

---

## cheap — 价格粗筛（Task A.1）

**代码**: `fundamental/cheap/scoring.py` + `signals.py` + `hints.py`

**输入**: `stock_data/{STOCK}_1d.csv` + `financial_data/{STOCK}/info.json`

### 8 项信号（signals.py）

信号定义和阈值详见 `task_a.md` A.1。工具输出顺序：1Y回撤 → 2Y回撤 → 距52周低 → P/E → FCF yield → EV/EBITDA → P/B → P/S。

**返回**: `{'signals': [(pass, value, detail), ...], 'count': N}`

### 4 项技术提示（hints.py）

| # | 提示 | 数据源 | 说明 |
|---|------|--------|------|
| 1 | Elliott | preload 的 Elliott 日期 | 近 5 日收盘价接近 Elliott 拐点价 |
| 2 | Neck Line | preload 的颈线 | 近 5 日触及颈线 |
| 3 | Trend Line | preload 的趋势线 | 近 5 日触及趋势线 |
| 4 | MinMax 4th | price CSV 的 LOCAL_MAX/MIN_4TH 标记 | 近 5 日接近 4 阶极值 |

**注意**: hints 需要 `preload.py` 预处理过的 Elliott/颈线/趋势线数据。若未 preload，hints 全为空。

---

## health — SCORECARD（Task B 的一部分）

**代码**: `fundamental/health/scoring.py` + `income.py` + `cashflow.py` + `balance_sheet.py`

**输入**: `financial_data/{STOCK}/` 下全部 CSV + `info.json`

### 9 宫格结构

结构（3yr/TTM/5Q × Income/CF/BS，权重 25%/35%/40%）和背离检验方法论详见 `task_b.md` B.1。
下面列出工具实际检查的**字段和判定规则**（实现细节）。

### Income 检查项

| 周期 | 检查项 | 字段 | 判定 |
|------|--------|------|------|
| 3yr | Revenue Trend | `Total Revenue` annual | 连续 3 年增长 + 正值 = pass |
| 3yr | EPS Trend | `Diluted EPS` annual | 同上 |
| 3yr | GM Trend | `Gross Profit` / `Total Revenue` | GM 不下滑 = pass |
| TTM | Revenue vs LY | `Total Revenue` TTM vs annual LY | YoY 正增长 = pass |
| TTM | EPS vs LY | `Diluted EPS` TTM vs annual LY | YoY 正增长 = pass |
| TTM | Margins | `Gross Profit`/`Net Income` | GM、NM 非零 = pass |
| TTM | Interest Coverage | `Operating Income` / `Interest Expense` | >5x = pass / 2-5x = warn / ≤2x = fail |
| 5Q | Revenue Q YoY | quarterly 最新季 vs 同季去年 | 正增长 = pass |
| 5Q | EPS Q YoY | quarterly EPS | 正增长 = pass |
| 5Q | Revenue 4Q+ | 近 4 季全正 | 4/4 正 = pass |
| 5Q | GM/NM Q YoY | 同季 GM/NM 同比趋势 | 不下滑 = pass |

### CF 检查项

| 周期 | 检查项 | 字段 | 判定 |
|------|--------|------|------|
| 3yr | OCF Trend | `Operating Cash Flow` annual | 连续增长 |
| 3yr | FCF Trend | `Free Cash Flow` annual | 连续增长 |
| 3yr | OCF/NI | OCF / `Net Income` | >1 = pass |
| 3yr | Buyback/Div | `Repurchase Of Capital Stock` + `Common Stock Dividend Paid` | 3yr 有回购或分红 = pass |
| 3yr | SBC/Rev | `Stock Based Compensation` / `Total Revenue` | 下降趋势 = pass |
| TTM | OCF vs LY | TTM vs annual | 正增长 |
| TTM | FCF > 0 | `Free Cash Flow` TTM | >0 = pass |
| TTM | OCF/NI | TTM OCF / `Net Income` TTM | >1 = pass |
| TTM | Net Return | 回购 + 分红 − SBC | >0 = pass |
| 5Q | OCF 4Q+ | 近 4 季全正 | 4/4 正 |
| 5Q | OCF Q YoY | 最新季 vs 同季去年 | 正增长 |
| 5Q | FCF 4Q+ | 近 4 季全正 | 4/4 正 |
| 5Q | FCF Q YoY | 最新季 vs 同季去年 | 正增长 |
| 5Q | Buyback 4Q | 近 4 季有回购 | 有 = pass |

### BS 检查项

| 周期 | 检查项 | 字段 | 判定 |
|------|--------|------|------|
| 3yr | D/E Trend | `Total Debt` / `Stockholders Equity` | 下降 = pass |
| 3yr | CR Trend | `Current Assets` / `Current Liabilities` | 上升 = pass |
| 3yr | GW/Assets | `Goodwill And Other Intangible Assets` / `Total Assets` | 下降 = pass |
| TTM | AR vs Revenue | `Accounts Receivable` TTM vs annual | AR 增速 ≤ 营收增速 = pass |
| TTM | AP vs Revenue | `Accounts Payable` TTM vs annual | AP 增速 ≤ 营收增速 = pass |
| TTM | Inventory vs Rev | `Inventory` TTM vs annual | 存货增速 ≤ 营收增速 = pass |
| TTM | CapEx/OCF | `Capital Expenditure` / `Operating Cash Flow` | <100% = pass |
| 5Q | Cash/Debt | `Cash Cash Equivalents And Short Term Investments` / `Total Debt` | >1x = pass |
| 5Q | D/E | 同 3yr 但季度 | ≤1 = pass |
| 5Q | Current Ratio | `Current Assets` / `Current Liabilities` | >1 = pass |
| 5Q | AR YoY | AR 增速 vs 营收增速 | ≤ = pass |
| 5Q | AP YoY | AP 增速 | 合理 = pass |

### Risk Flags

| 检查 | 触发 | 影响 |
|------|------|------|
| Goodwill 占比 >33% | `Goodwill And Other Intangible Assets` / `Total Assets` > 0.33 | BS 5Q 扣 10 分 |
| NI 下降 | TTM NI < 上年 | 标记 |

### 额外计算

| 指标 | 公式 | 数据源 |
|------|------|--------|
| ROIC | NOPAT / (债+权益−现金) | income `Operating Income` + BS + `Tax Rate For Calcs` |
| ROE | `Net Income` / `Stockholders Equity` | info.json `returnOnEquity` |
| ROA | `Net Income` / `Total Assets` | info.json `returnOnAssets` |
| P/E | `currentPrice` / TTM EPS | info.json `trailingPE` |
| P/B | `currentPrice` / `bookValue` | info.json `priceToBook` |

**金融股 ROIC 返回 n/m**（无意义），看 ROA/ROE + P/B。

---

## statements — 三张财报打印

**代码**: `fundamental/statements/__main__.py` + `templates.py`

**输入**: `financial_data/{STOCK}/income_*.csv` + `cf_*.csv` + `bs_*.csv`

**输出**: 按 template 排列的 annual + quarterly + TTM 报表

### Template 字段（见 `fundamental/statements/templates.py`）

- **INCOME_FIELDS**: 35 字段，7 步 multi-step 格式
  - EPS-1~7: Revenue→Gross→OpInc→Non-Op→Tax→NI→Normalization→EPS→EBITDA
- **BS_FIELDS**: 28 字段
  - 流动资产→PPE→Goodwill→总资产→流动负债→长期负债→总负债→权益→营运资本
- **CF_FIELDS**: 18 字段
  - OCF→CapEx→投资→融资→FCF

### 数据加载函数（`fundamental/data.py`）

| 函数 | 输入 | 输出 | 说明 |
|------|------|------|------|
| `load_statement(stock, filename)` | stock名+文件名 | pandas DataFrame | index=字段名，columns=期间，**自动 filter_incomplete** |
| `load_info(stock)` | stock名 | dict | 从 info.json 加载 |
| `load_price(stock)` | stock名 | DataFrame | 从 stock_data CSV 加载 |
| `get_val(df, field, col)` | DataFrame+字段+列名 | float | 取指定字段在指定列的值 |
| `get_series(df, field)` | DataFrame+字段 | list of (col, value) | 取指定字段的所有期间值（新→旧） |
| `get_last_close(stock)` | stock名 | float | 最新收盘价 |
| `format_value(v)` | 数值 | string | 格式化（B/M/K） |
| `get_info_val(info, key)` | info dict + key | float | 取 info.json 值，含 BABA FX 修正 |

### CSV 口径速查

- **行 = 指标名（index），列 = 期间，列从左到右 = 新→旧**
- `df.columns[0]` 是最新期，`get_val(df, field, 0)` 取最新值
- 同比用 `iloc[0]` vs `iloc[4]`（最新季 vs 一年前同季）
- `filter_incomplete` 丢掉缺失率 >50% 的列
- **BS 无 TTM**——snapshot 口径

---

## preload — 数据预处理

**代码**: `preload.py`

为 cheap/hints 预处理技术分析数据：Elliott 波浪日期、颈线、趋势线、4 阶极值标记。需要在 cheap 之前运行。

```bash
python3 preload.py STOCK    # 单只
python3 preload.py          # 全部
```

---

## normalize_eps — 正常化 EPS（Task B 的 EPS 部分）

**代码**: `docs/normalize_eps.py`

详见 `docs/normalize_eps.md`（v3.1 checklist）。

```bash
python3 -m docs.normalize_eps           # 跑全部 78 只
```

---

## dcf — DCF 交叉验（Task D 的 D.2b 部分）

**代码**: `docs/dcf.py`

详见 `docs/dcf.md`（Gordon 单阶段 + 质量调整 r + 封顶 30x）。

```bash
python3 docs/dcf.py WMT 6 好公司 2.609       # STOCK G(%) QUALITY [EPS for gap]
python3 docs/dcf.py NVDA 15 伟大 10.03        # g≥r 封顶演示
python3 docs/dcf.py TTD 3 好公司 0.84          # 高 SBC 演示（DCF>EPS）
```

输入：cf_ttm（FCF/SBC/回购）、income_ttm（shares/EPS）、bs_quarterly（Cash/Total Debt）。g/quality/EPS 来自 Task C/D（非自动）。输出：完整 DCF 表（两口径）+ gap 分析 + 三口径排序。

---

## 数据更新

```bash
python3 -m fundamental.download STOCK   # 下载/更新单只数据
```

更新后重新跑 `combine` 或各子模块即可获得最新结果。

---

## 与分析框架的映射

| 框架 Task | 本地工具 | 补充 |
|-----------|---------|------|
| A.1 价格粗筛 | `cheap`（8 项信号，含 FCF yield） | 免费，每次分析 |
| A.2 估值分位 | — | 需 web search（月度） |
| B 财务健康 | `health`（9 宫格）+ `statements`（原始数据） | 免费，财报后更新 |
| B 正常化 EPS | `normalize_eps`（v3.1 checklist） | 免费，财报后更新 |
| C 增长/消息面 | — | 需 web search（最贵） |
| D 估值锚 | `dcf`（DCF 交叉验）+ 手工算（合理价/满仓/系数） | DCF 自动，EPS 模型手工 |
| E 决策 | — | join A(price) + D(anchor)，daily 刷新 |

**combine = A.1 + B 的合体**——一次跑完价格粗筛 + 财务健康 + 原始报表，是日常分析的主力入口。

---

## 多币种 ADR 数据质量

> 多币种股（`financialCurrency` ≠ USD）的 info.json 多个字段不可信——股价 USD 与财报币种混合导致失真。**combine 工具直接继承这些错误**，须手算修正。

### 不可信字段

| info.json 字段 | 问题 | 正确做法 |
|---|---|---|
| `trailingEps` | 用非 spot FX 转换，可能 stale | CSV `Diluted EPS` ÷ spot FX |
| `trailingPE` | 基于上面 stale EPS | `currentPrice` ÷ CSV EPS（÷ FX） |
| `priceToBook` | USD price ÷ TWD book value | 手算 price ÷ (Equity ÷ shares ÷ FX) |
| `enterpriseToEbitda` | EV 字段单位/口径混乱 | 手算 (MCap + Debt÷FX − Cash÷FX) ÷ (EBITDA÷FX) |
| `priceToSalesTrailing12Months` | USD MCap ÷ TWD revenue | MCap ÷ (Revenue ÷ FX) |
| `enterpriseValue` | 单位/口径混乱 | MCap + 净债（统一币种） |
| `bookValue` | 财报币种 book value ÷ shares | BS Equity ÷ shares ÷ FX |

### 可信字段（price 端，不受币种影响）

`currentPrice`, `marketCap`, `sharesOutstanding`, `fiftyTwoWeekHigh`, `fiftyTwoWeekLow`, `dividendYield`, `dividendRate`, `beta`

### FX 验证 decision tree

```
financialCurrency ≠ USD ?
├─ 否 → info.json 字段可信，正常用
└─ 是 → 不信 trailingEps / trailingPE / priceToBook / enterpriseToEbitda / priceToSales / enterpriseValue
   │
   ├─ FX 来源优先级：
   │   ① Google Finance spot（playwright 抓）← 最准
   │   ② 框架表 ≈ 值（analysis_framework.md，3-5 天更新）
   │   ③ 反推值 = CSV EPS_TWD ÷ info.json trailingEps_USD ← 仅交叉验，可能 stale
   │
   ├─ EPS_USD = CSV Diluted EPS ÷ spot FX
   ├─ P/E = currentPrice ÷ EPS_USD
   ├─ P/B = currentPrice ÷ (BS Equity ÷ shares ÷ FX)
   ├─ EV/EBITDA = (MCap + Debt÷FX − Cash÷FX) ÷ (EBITDA÷FX)
   ├─ P/S = MCap ÷ (Revenue ÷ FX)
   │
   └─ 交叉验：MacroTrends P/E（web），偏差 >5% → 用 CSV + spot，标 info.json stale
```

> ⚠️ **反推 FX 降级**：`analysis_framework.md` 原写"FX = EPS_财报币种 ÷ trailingEps_USD，反推值更与 ADR 报告口径一致"——当 info.json trailingEps stale 时反推值也错。TSM 案例：反推 37.56 vs spot 32.26，差 17%。**spot FX 为准，反推值仅交叉验。**

### 涉及标的

| 币种 | 标的 |
|------|------|
| TWD | TSM |
| EUR | ASML BNTX SPOT |
| DKK | NVO |
| SEK | ERIC |
| KRW | — |
| SGD | SE |
| CNY | BABA PDD JD TCOM BIDU BEKE BILI FUTU TME 0700.HK |
| HKD | 0700.HK FUTU |

> 详见 `batches.md`"多币种"标记。
