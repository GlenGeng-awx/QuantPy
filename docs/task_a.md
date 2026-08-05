# Task A：价格层（daily）

> 所有 price-dependent 指标。日级别更新（读 CSV 刷 price/P/E/FCF yield/安全边际）。
> B/C/D 不受 price 影响，仅财报/消息面时动。

## 目标

判断"这个标的是否因暂时困境**下跌**到值得看的程度"。

---

## A.1 价格粗筛 + price-dependent 指标（daily，本地 CSV + info.json）

### 7 项粗筛信号

满足任意 1 条即入池。门槛宽——漏斗入口，不是最终判断。

| # | 条件 | 阈值 | 数据源 | key |
|---|------|------|--------|-----|
| 1 | 1Y 回撤 | >40% | `stock_data/` CSV 近 252 日 | close 最高 vs 最低 |
| 2 | 2Y 回撤 | >60% | 同上，504 日 | |
| 3 | 距 52 周低点 | ≤15% | CSV | 现价 vs 252 日最低 |
| 4 | P/E TTM | <15x | `info.json` | `trailingPE` |
| 5 | EV/EBITDA | <10x | `info.json` | `enterpriseToEbitda` |
| 6 | P/B | <1.0x（金融股）/ <1.5x（周期股） | `info.json` | `priceToBook` |
| 7 | P/S | <2.0x | `info.json` | `priceToSalesTrailing12Months` |

### 其他 price-dependent 指标（从 B 吸收）

| 指标 | 计算 | 说明 |
|------|------|------|
| FCF yield | FCF(from B) / MCap(from price) | 随 price 变，B 只存 FCF 金额 |

### 特殊口径

```
金融股: P/B <1.0 替代 EV/EBITDA
周期股: 正常化 P/E <12x / P/B <1.5x / 净现金/市值 >30% / 股息率 >5%
NM >25% 放宽: P/S 阈值 2.0x → 4.0x
```

> 标记说明（银行/周期/多币种/VIE）见 `batches.md`。

### ⚠ 多币种 ADR 陷阱

`EV/EBITDA` 在多币种股上失真（MCap 用股价币种，EBITDA 用财报币种）。
BABA = 股 USD / 财报 CNY，0700.HK = 股 HKD / 财报 CNY。
**必须手算 EV** = MCap + 总债 − 现金（统一币种）。

### 工具

```bash
python3 -m fundamental.cheap STOCK    # 自动跑 7 项（含 P/B）
```

详见 `local_data_tools.md` 的 cheap 章节。

---

## A.2 估值分位（web search，月度）

### 自身 P/E 区间表

| 口径 | 数值 | 来源 |
|------|------|------|
| 正常化 P/E | 现价 ÷ 正常化 EPS（从 Task B 引） | 本地算 |
| 5 年高 | MacroTrends / GuruFocus | web |
| 5 年低 | 同上 | web |
| 5 年中位 | 同上 | web |
| 当前分位 | (当前 − 低) / (高 − 低) | 算 |

**须 ≤30% 分位**才算便宜。查询失败则暂停，严禁估算。

### 周期股特殊处理

P/E 分位对周期股**反读**：
- 周期底：盈利低 → P/E 高 → 看着贵 → 实际是买点
- 周期顶：盈利高 → P/E 低 → 看着便宜 → 实际是卖点

改用：
- 中周期正常化 P/E（盈利取跨周期中枢）
- P/B 分位（P/E >70% + P/B <30% = 周期底部）
- 净现金 / 清算价值

### 同业对比表

列可比同业当前或前瞻倍数 + 性质，算 PYPL 折/溢价%。
剔除性质不可比者（如卡组织 vs 支付处理商）。

### de-rating 陷阱

历史高分位若来自成长泡沫期溢价，低分位有一部分是范式切换，不全是错杀，需打折看。

### 展开要求

不许只写"≈Xth 通过"。必须给：
- **自身区间表**：当前 / 高 / 低 / 中位 / 前瞻 + 分位 + 来源 URL
- **同业对比表**：可比同业倍数 + 折/溢价%
- **de-rating 判断**：便宜成因是错杀还是真实恶化

---

## A.3 安全边际（daily，join D 的锚）

> 从 output_d D.1 读合理价和满仓（不重算），用 A.1 现价算安全边际。

```
安全边际 vs 合理价 = 1 − 现价 / D.合理价
安全边际 vs 满仓目标 = 1 − 现价 / D.满仓目标
```

操作建议（通用逻辑，汇总时算）：

| 安全边际 vs 满仓 | 操作 |
|----------------|------|
| ≥ 0（现价 ≤ 满仓） | 满仓建仓 |
| < 0 但现价 < 合理价 | 小仓/观察 |
| 现价 ≥ 合理价 | 不出手，等 callback |

---

## 与其他 Task 的关系

| 输入 | 来源 |
|------|------|
| 正常化 EPS（算正常化 P/E） | Task B |
| FCF 金额（算 FCF yield） | Task B |
| 合理价 / 满仓目标（算安全边际） | Task D |
| 现价 | 本地 CSV |

| 输出 | 去向 |
|------|------|
| 7 项粗筛 pass/fail + FCF yield + 安全边际 | 汇总表（join D → 操作建议） |
| 估值分位 + 同业 + de-rating | Task C（便宜成因呼应竞争/财报） |

A.1 可独立跑（只需 CSV + info.json）。
A.2 需 web search（月度）。
A.3 需 D 的合理价/满仓（join）。
