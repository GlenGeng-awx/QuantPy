# Task E：决策层（daily）

> 被 引用自 `analysis_framework.md`。Task E = join A(price) + D(anchor) → 安全边际 + 操作建议 + 归类。
> 数据源：output_a.md（现价/粗筛/分位）+ output_d.md（合理价/满仓/DCF/质量）。
> price-dependent，daily 刷新。

## 目标

join A(现价) + D(锚) 算安全边际，产出操作建议和归类。E 是 daily 唯一刷新的决策文件，聚合 A 和 D 的关键字段，供 gen_comparison 直接读取。

---

## 依赖关系

```
B (v3.1 EPS + FCF金额 + SCORECARD) ──→ A (粗筛 + 双分位) ──→ E
B, C (g + 护城河 + 麻烦)           ──→ D (合理价 + 满仓 + DCF) ──→ E
```

- A 和 D 并行（都只等 B）
- E 等 A + D 完成
- E 是 A 和 D 的"物化视图"（materialized view）：抄 A 的价格/信号/分位 + 抄 D 的锚/DCF + 自己算安全边际/操作/归类

---

## E.1 粗筛信号（from A）

直接引用 A.1 的 8 项粗筛结果（不重算）：

| # | 条件 | 阈值 | 实际值 | ✓/✗ |
|---|------|------|--------|-----|
| 1-8 | （同 A.1） | ... | ... | ... |

命中: {N}/8

> E 不自己跑粗筛——从 output_a.md 读结果。A 用 info.json + CSV + web 算，E 只抄。

---

## E.2 估值锚（from D）

直接引用 D.2 / D.2b 的锚字段（不重算）：

| 口径 | 值 | 来源 |
|------|-----|------|
| 合理价 | ${val} | from D（EPS × PE） |
| 满仓目标 | ${val} | from D（合理价 × 系数） |
| 系数 | ×{val} | from D（质量×麻烦 → 查表） |
| g | {val}% | from D（from C） |
| 合理 PE | {val}x | from D（min(8.5+g, 30)） |
| 正常化 EPS | ${val} | from D（min(GAAP, tool, v3.1)） |
| GAAP EPS | ${val} | from B |
| FCF/sh | ${val} | from D（from B cf_ttm） |
| FCF−SBC/sh | ${val} | from D（from B cf_ttm） |
| r | {val}% | from D（质量调整） |
| P/FCF₀ | {val}x | from D（min((1+g)/(r−g), 30)） |
| DCF FCF−SBC | ${val} | from D（D.2b） |
| DCF FCF | ${val} | from D（D.2b） |
| 质量×麻烦 | {val}×{val} | from D（D.5） |

> E 不算锚——从 output_d.md 读。D 是 low-freq（财报后才动），E daily 只抄 + 用新现价算安全边际。

---

## E.3 安全边际 + 操作建议（join A price + D anchor）

```
安全边际 = 1 − A.现价 / D.合理价
```

| 口径 | 合理价 | 满仓 | 安全边际 | 操作 |
|------|--------|------|---------|------|
| EPS 模型 | from D | from D | 1 − price/合理价 | f(安全边际, 满仓) |
| DCF FCF | from D | — | 1 − price/DCF FCF | — |
| DCF FCF−SBC | from D | — | 1 − price/DCF FCF−SBC | — |

操作建议（通用逻辑）：

| 现价位置 | 操作 |
|---------|------|
| ≤ 满仓目标 | 满仓建仓 |
| 满仓 < 现价 < 合理价 | 小仓/观察 |
| ≥ 合理价 | 不出手，等回调 |

> 现价从 A 读（daily），合理价/满仓从 D 读（low-freq）。安全边际 = join。

---

## E.4 归类

```
好价格（A: 粗筛命中 + 双分位 ≤30%）+
好公司（B+C: 质量 6/6 + 护城河）+
一次性麻烦（C+D: 麻烦定性）
→ 归类
```

| 条件 | 归类 |
|------|------|
| 三者齐备 | **最佳买点** |
| 只有好价格 | 价值陷阱（便宜的烂公司） |
| 只有好公司 | 买贵了 |
| 好公司 + 好价格但麻烦非一次性 | 结构性恶化 |

> 特殊归类（旧 stub "框架外" 已修正为"总是估值"）：
> - 不对称投机：平庸公司 + 重麻烦（FCF−SBC<0）+ 好价格（净现金托底）→ ≤3% 仓位
> - 接近最佳买点：现价在满仓和合理价之间

---

## E.5 双分位（from A）

A.2 产出双分位，E 抄过来供 gen_comparison 排序：

| 口径 | 当前 | 5yr 高 | 5yr 低 | 分位 | 来源 |
|------|------|--------|--------|------|------|
| GAAP P/E TTM | {val} | {val} | {val} | {N}th | MacroTrends |
| 正常化 P/E (v3.1) | {val} | {val} | {val} | {N}th | MacroTrends 范围 + B v3.1 |

> 两个都 ≤30% 才算便宜。范围共用 GAAP P/E 的（MacroTrends），当前值不同 → 分位不同。
> 正常化 P/E = 现价 / v3.1 EPS（from B），用 GAAP P/E 5yr 范围当标尺算分位。

---

## lazy 更新规则

| 事件 | 改谁 | 不改谁 |
|------|------|--------|
| 价格漂移（trivial） | E（price + 安全边际重算） | A, B, C, D |
| 价格 >3-5% | A（粗筛刷新）→ E（信号 + price + 安全边际） | B, C, D |
| 财报 | B → D → E（锚刷新 + price + 安全边际） | A（除非 P/E 变） |
| 消息面 non-trivial | C → D（若 g/麻烦变）→ E | A, B |

> E 是 daily 唯一必碰的文件。A 在价格 >3-5% 或财报后刷新。B/C/D 是 low-freq 锚。

---

## 与其他 Task 的关系

| 输入 | 来源 |
|------|------|
| 现价 + 粗筛信号 + 双分位 | Task A |
| 合理价 + 满仓 + 系数 + DCF + 质量×麻烦 | Task D |

| 输出 | 去向 |
|------|------|
| 安全边际 + 操作 + 归类 + 全部锚字段 | gen_comparison（只读 E） |

> gen_comparison 不再 join A+D——E 已聚合一切，gen_comparison 变成纯格式化 + 排序。
