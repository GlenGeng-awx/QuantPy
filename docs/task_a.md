# Task A：价格层（daily）

> 所有 price-dependent 指标。日级别更新（读 CSV 刷 price/P/E/FCF yield/分位）。
> A 不依赖 D（安全边际 → Task E）。A 读 B 的 v3.1 EPS 算正常化 P/E 分位。

## 目标

判断"这个标的是否因暂时困境**下跌**到值得看的程度"。

---

## A.1 价格粗筛 + price-dependent 指标（daily，本地 CSV + info.json + cf_ttm）

### 8 项粗筛信号

满足任意 1 条即入池。门槛宽——漏斗入口，不是最终判断。

| # | 条件 | 阈值 | 数据源 | key |
|---|------|------|--------|-----|
| 1 | 1Y 回撤 | >40% | `stock_data/` CSV 近 252 日 | close 最高 vs 最低 |
| 2 | 2Y 回撤 | >60% | 同上，504 日 | |
| 3 | 距 52 周低点 | ≤15% | CSV | 现价 vs 252 日最低 |
| 4 | P/E TTM | <15x | `info.json` | `trailingPE` |
| 5 | FCF yield | >5% | FCF(from `cf_ttm.csv`) / MCap(from `info.json`) | cheap 工具自动算 |
| 6 | EV/EBITDA | <10x | `info.json` | `enterpriseToEbitda` |
| 7 | P/B | <1.0x（金融股）/ <1.5x（周期股） | `info.json` | `priceToBook` |
| 8 | P/S | <2.0x | `info.json` | `priceToSalesTrailing12Months` |

> FCF yield 是估值指标（同 P/E），衡量"便不便宜"（P/E 用 NI，FCF yield 用真实现金），不衡量"公司好不好"。已从 `discount_coefficient.md` 质量评分移出（质量评分改 6/6）。

### 特殊口径

```
金融股: P/B <1.0 替代 EV/EBITDA
周期股: 正常化 P/E <12x / P/B <1.5x / 净现金/市值 >30% / 股息率 >5%
轻资产（GM >60% 或 CapEx/Rev <5%）: P/B 不适用——book value 不含品牌/IP/网络效应，高 P/B 是资本效率高的体现非贵。标"—（轻资产）"，不算 ✗
NM >25% 放宽: P/S 阈值 2.0x → 4.0x
```

> 标记说明（银行/周期/多币种/VIE）见 `batches.md`。

### ⚠ 多币种 ADR 陷阱

`EV/EBITDA` 在多币种股上失真（MCap 用股价币种，EBITDA 用财报币种）。
BABA = 股 USD / 财报 CNY，0700.HK = 股 HKD / 财报 CNY。
**必须手算 EV** = MCap + 总债 − 现金（统一币种）。

### 工具

```bash
python3 -m fundamental.cheap STOCK    # 自动跑 8 项（含 FCF yield #5）
```

详见 `local_data_tools.md` 的 cheap 章节。

---

## A.2 估值分位（web search + B v3.1，月度）

### 双分位

| 口径 | 当前 | 5yr 高 | 5yr 低 | 5yr 中位 | 分位 | 来源 |
|------|------|--------|--------|---------|------|------|
| GAAP P/E TTM | 现价 / GAAP EPS | MacroTrends | MacroTrends | MacroTrends | (当前−低)/(高−低) | web |
| 正常化 P/E | 现价 / v3.1 EPS（from B） | MacroTrends（共用 GAAP 范围） | 同 | 同 | (正常化P/E−低)/(高−低) | web 范围 + B v3.1 |

**两个分位都须 ≤30%**才算便宜。查询失败则暂停，严禁估算。

> **正常化 P/E 分位复用 GAAP P/E 的 5yr 范围当标尺**：MacroTrends 只有 GAAP P/E 历史，没有 v3.1 正常化 P/E 序列。用 GAAP 范围当标尺，插正常化 P/E 当当前值 → 分位。例：TME GAAP P/E <10x（分位极低 → 看着严重低估），正常化 P/E 14-15x（分位正常 → 其实不便宜）。

> GAAP EPS 从 `income_ttm.csv` `Diluted EPS` 字段直接读（原始 CSV，非 B 的 output）。v3.1 EPS 从 B 的 output 读（B 跑 `normalize_eps.py` 算出）。

### 周期股特殊处理（fallback，非默认）

**默认：所有标的（含周期股）先用 `EPS × min(8.5+g, 30)` 估值。** 周期股仅当 EPS 大幅波动或为负、无法用公式时，才 fall back 到以下方法：

**何时 fall back**：
- EPS 跨周期摆动大（峰谷差 >2x，如 MU 内存周期）
- EPS 为负（亏损股 → 用恢复 EPS，见 `normalize_eps.md` EPS-4b）
- 当前 EPS 处周期极端位置（峰/谷），直接套会严重高估/低估

**Fall back 方法**：
- 中周期正常化 P/E（盈利取跨周期中枢，非当前峰/谷）
- P/B 分位（P/E >70% + P/B <30% = 周期底部信号）
- 净现金 / 清算价值

**不 fall back 的周期股**（EPS 稳定正 → 用标准公式）：
- GM 稳定 >50% + EPS 连续正（如 TSM 先进制程准垄断、GM 64%+）
- 用标准 `EPS × min(8.5+g, 30)`，在敏感性表加 GM 正常化下行情景即可

### 同业对比表

列可比同业当前或前瞻倍数 + 性质，算折/溢价%。
剔除性质不可比者（如卡组织 vs 支付处理商）。

### de-rating 陷阱

历史高分位若来自成长泡沫期溢价，低分位有一部分是范式切换，不全是错杀，需打折看。

### 展开要求

不许只写"≈Xth 通过"。必须给：
- **双分位区间表**：GAAP + 正常化 P/E 的 当前/高/低/中位/分位 + 来源 URL
- **同业对比表**：可比同业倍数 + 折/溢价%
- **de-rating 判断**：便宜成因是错杀还是真实恶化

---

## 与其他 Task 的关系

| 输入 | 来源 |
|------|------|
| GAAP EPS（算 GAAP P/E） | `income_ttm.csv` `Diluted EPS`（直接读源 CSV） |
| v3.1 正常化 EPS（算正常化 P/E 分位） | Task B（`normalize_eps.py` 产出） |
| FCF（算 FCF yield #5） | `cf_ttm.csv` `Free Cash Flow`（cheap 工具直接读） |
| 现价 | 本地 CSV |

| 输出 | 去向 |
|------|------|
| 8 项粗筛 pass/fail + FCF yield | Task E |
| 双分位（GAAP + 正常化 P/E）+ 同业 + de-rating | Task E + Task C（便宜成因呼应竞争/财报） |

A.1 可独立跑（只需 CSV + info.json + cf_ttm.csv）。
A.2 需 web search（月度）+ B v3.1 EPS（算正常化 P/E 分位）。
A 不依赖 D（安全边际 → Task E）。
