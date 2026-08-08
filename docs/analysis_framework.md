# 分析框架：概述

> 框架核心：识别"因暂时困境被市场低估的优质公司"。三位投资哲学家的原则缺一不可。

## 投资哲学（核心）

| 哲学家 | 原则 | 对应 Task |
|--------|------|-----------|
| **格雷厄姆** | 好价格（安全边际） | A（粗筛/分位）+ D（折扣） |
| **费雪** | 好公司（GM/FCF/护城河） | B（SCORECARD）+ C（护城河） |
| **巴菲特** | 一次性麻烦（暂时困境） | C（消息面/增长前瞻）+ D（麻烦定性） |

三者缺一不可：

| 条件 | 归类 |
|------|------|
| 只有好价格 | 价值陷阱（便宜的烂公司） |
| 只有好公司 | 买贵了 |
| 好公司 + 好价格但麻烦非一次性 | 结构性恶化 |
| 三者齐备 | **最佳买点** |

> 三核心要素是哲学的实现公式，ABCD 四任务是执行工作流——下面依次展开。

---

## 三核心要素（实现公式）

```
# EPS 模型（保守下限）
合理价   = 正常化 EPS × min(8.5 + g, 30)
               ↑               ↑
            Task B           Task C
         normalize_eps.md  forward_g.md

满仓目标 = 合理价 × 折扣系数
                      ↑
                    Task D
               discount_coefficient.md

# DCF 交叉验（并列，非替代）
DCF/sh = base × (1+g)/(r−g) + net_cash/shares

  base = FCF/sh 或 (FCF−SBC)/sh              ← dcf.md (from Task B CSV)
  g = 前瞻增速                                ← forward_g.md (from Task C)
  r = 质量调整：伟大 9% / 好公司 10% / 平庸 11%  ← dcf.md
  P/FCF₀ = min((1+g)/(r−g), 30)
```

| 要素 | 性质 | checklist | 原则 |
|------|------|-----------|------|
| **正常化 EPS** | 事实性（财报算） | `normalize_eps.md` | min(GAAP, tool, v3.1) — 三者取最低 |
| **前瞻 g** | 半预测（历史+共识+指引） | `forward_g.md` | 剔高+均值，不外推高增长 |
| **折扣系数** | 判断性（质量×麻烦） | `discount_coefficient.md` | 7分评分+4档定性→交叉查表 |
| **DCF 交叉验** | 现金流估值（内在价值定义） | `dcf.md` | base × (1+g)/(r−g)，与 EPS 模型并列 |

EPS 模型是保守下限（隐含 r≈12-15%），DCF 是内在价值定义（r=9-11%）。两者并列展示：
- FCF ≈ NI 时一致
- 高 SBC（TTD/CRM）→ DCF > EPS 模型，揭示 EPS 低估
- 高 CapEx（GOOG/NVDA）→ DCF < EPS 模型，揭示 EPS 高估

三重保守（EPS min + g 保守 + 折扣保守）→ 合理价偏低 → 需要更便宜才出手 → **哪怕错过，不要做错**

---

## ABCD 四任务

```
Task A: 价格层（daily）            ← price-dependent：P/E, P/B, EV/EBITDA, FCF yield, 安全边际（join D 锚）
Task B: 财务层（low-freq）         ← 纯财报数据：EPS, SCORECARD, FCF 金额, SBC — price 无关
Task C: 增长层（low-freq）         ← g, 护城河, 管理层, 消息面 — price 无关
Task D: 估值锚（low-freq）         ← 合理价, 满仓, 折扣系数 — price 无关
汇总:   join A(price) + D(锚)      ← 安全边际 + 操作建议（通用逻辑，每次汇总现算）
```

### 依赖关系

```
B (财务) ──→ A (FCF, EPS)
B (财务) ──→ D (EPS, 质量)
C (g/护城河) ─→ D (g, 麻烦)
D (锚)   ──→ A (合理价, 满仓)
```

- **B 和 C 并行**（都读 CSV，互不依赖）
- **D 依赖 B + C**（EPS, g, 折扣），**不依赖 A**（price 无关）
- **A 依赖 B + D**（FCF from B，合理价 from D）
- **A.1/A.2 独立于 D**（只需 CSV + web），A.3 依赖 D

> 低频和日频解耦：D 在财报后算一次（锚），日频只刷 price + 算安全边际。

| D 的公式 | B 提供 | C 提供 |
|----------|--------|--------|
| 合理价 = EPS × PE(g) | EPS | g |
| 满仓目标 = 合理价 × 折扣 | 质量 | 麻烦 |

> 安全边际 = 1 − A.现价 / D.合理价 — join A + D 算，不在 D 里。

B 可给 D 一个**预判**（EPS 已定，折扣地板可估），C 完成后更新。

### 各任务详细文档

| 任务 | 详细文档 | 内容 |
|------|---------|------|
| A | `task_a.md` | 价格层（daily）：粗筛 7 项 + FCF yield + 估值分位 + 安全边际（join D 锚） |
| B | `task_b.md` | SCORECARD 9 宫格 + 财报 heuristic + 正常化 EPS（引用 `normalize_eps.md`） |
| C | `task_c.md` | 增长前瞻 g（引用 `forward_g.md`）+ 护城河 + 管理层 + 消息面 + 熊牛逻辑 |
| D | `task_d.md` | 估值锚（low-freq）：合理价 + 满仓 + 折扣系数（引用 `discount_coefficient.md`） |

---

## FX 汇率

> 多币种股（ADR/港股）做 EPS 转换时，用当前汇率，不抄旧报告。
>
> **更新日期：2026-08-02** | 每 3-5 天更新一次下表数值。

| 币种对 | 近似值 | 涉及标的 |
|--------|--------|---------|
| CNY/USD | ~6.8 | BABA PDD JD TCOM BIDU BILI FUTU TME BEKE LI XPEV NIO |
| CNY/HKD | ~1.1 | 0700.HK |
| TWD/USD | ~32 | TSM |
| EUR/USD | ~1.15 | ASML BNTX SPOT |
| DKK/USD | ~6.48 | NVO |
| SEK/USD | ~10.5 | ERIC |
| KRW/USD | ~1350 | CPNG |
| SGD/USD | ~1.35 | SE |

> ⚠ 上表为近似值，会变。看更新日期判断是否过期。也可从 info.json 反推：`FX = EPS_财报币种 ÷ trailingEps_USD`（如 NVO：DKK 27.41 ÷ $4.18 = 6.56，与 spot 6.48 差 ~1.2%，EPS 转换用反推值更与 ADR 报告口径一致）。

---

## 数据源与成本

| 任务 | 数据源 | 成本 | 更新频率 |
|------|--------|------|---------|
| A.1 价格粗筛 | `stock_data/` CSV + `info.json` | 免费 | 每次分析 |
| A.2 估值分位 | web search | 中 | 月度 |
| B 财务+EPS | `financial_data/` CSVs | 免费 | 财报后 |
| C.1 g | web search（分析师共识+指引） | 高 | 财报后 |
| C.2 消息面 | web search（RSS） | 中 | 周度 |
| C.3 护城河/管理层 | web search | 高 | 半年度 |
| D 估值汇聚 | A+B+C 输出 | 免费 | 每次分析 |

本地工具用法详见 `local_data_tools.md`。

```
每次分析（daily/weekly）:
  → A.1 价格粗筛（免费，本地）+ D 汇聚（用已有 B/C）

周度:
  → C.2 消息面 RSS 扫描

月度:
  → A.2 估值分位更新

财报后（quarterly, per stock）:
  → download + B（免费）+ C.1 g 更新

半年度:
  → C.3 护城河/管理层深度 review
```

---

## Subagent 分工

低频批（财报/消息面后）：
- **Agent 1**: Task B（财务+EPS）— 可批量跑全部标的，CSV only，免费
- **Agent 2**: Task C（g + 护城河 + 消息面）— **最贵，需 focus，逐只精做**
- → Task D（锚）— 等 B+C 完成后算，**不等 A**

日频批（每交易日）：
- 读 CSV price → A.1 粗筛刷新 → A.3 = 1 − price/D.合理价 → 汇总
- **trivial，不需要 agent**

C 是瓶颈和成本中心——最先启动、最后完成。
B 和 C 并行（都读 CSV，互不依赖）。
D 在 B+C 完成后立即可算（不等 A）。
A 依赖 B + D（FCF from B，合理价 from D）；A.1/A.2 可与 B/C 并行（CSV + web）。
