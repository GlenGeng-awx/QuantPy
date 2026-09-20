# 分析框架 v2 — 全景

> 好价格 + 好公司 + 一次性麻烦 = 击球区
>
> 三者缺一不可：只有好价格 = 价值陷阱；只有好公司 = 买贵了；好公司+好价格但麻烦非一次性 = 结构性恶化
>
> **本文档是 lens（分析/汇总/校验前必读）。** 规则只在 owner 节定义一次（见 §-ID），其他文件用 §-ID 引用、不复述。

## §0.1 核心公式 (EPS + DCF + gap)

```
# EPS 模型（保守下限）→ 合理价
合理价 = 正常化 EPS × PE(g)        # PE = 8.5+g (Graham, 入场基准) 或 8.5+2g (Fisher, 出场基准) — §5.1
入场价 (满仓) = 合理价 × 折扣系数    # 折扣 = Fisher 15 2D 表 (§3.2); 应用在 Task E Step 3 (§6.1)

# DCF（内在价值, 与 EPS 并列）
DCF/sh = 一阶段/两阶段 + net_cash/sh   # g≤3% Gordon Growth; g>3% 两阶段 (N=5) — §5.1
                                     # base: 回购≤SBC → ⑦FCF-SBC; 回购>SBC → ⑧FCF — §5.2
回购≤SBC 时: 
合理价 = ⑦; 
入场价 (满仓) = ⑦ × 折扣系数 (同 EPS 路径, §6.1 Step 3)

# gap = 置信度信号 (§5.2 置信度 + §5.3 gap 诊断)
EPS vs DCF gap → 哪个更可信 → 看 gap 来源 → 决定合理价口径 (§5.3 机械规则)
```

## §0.2 依赖图

```
用户手动选标的
  ↓
  Task 1 (财务) — 读 financial_data CSV
  ↓
  Task 2 (g) — 读 output_1 (SCORECARD 损伤 + 趋势表 + EPS)
  ↓
  Task 3 (Fisher 15) — 读 output_1 (定量损伤 → #追查) + output_2 (g 多档位 → #1 可持续性)
  ↓
  Task 4 (价格层) — 读 output_1 (v3.1 EPS/FCF) + output_2 (g/derating) + stock CSV + MacroTrends
  ↓
  Task 5 (估值) — 读 output_1 (EPS/per-share) + output_2 (g 多档位) + output_3 (折扣/r) + output_4 (分位 ④⑤⑥)
    ├── 纯估值引擎: 算全部方法 (①②⑦⑧ 公式 + ④⑤⑥ 分位) → 矩阵 → gap → 置信度
    └── output_5 = 合理价 + 全方法值 + 范围 + 置信度 (不做决策, 无 flag)
  ↓
  Task E (决策) — 读 output_1 (BS/EPS) + output_2 (g 档位) + output_3 (折扣/质量) + output_4 (分位/derating) + output_5 (合理价/gap) + stock CSV (最新 EOD)
    ├── Step 1: BS 生存力 + 估值能力判断 (能/能力圈外/价值陷阱, 自产 flag — §6.1)
    ├── Step 2-4: 选可信方法 → 入场价/出场价 → 安全边际
    ├── 公式价 vs 分位价 交叉验 (output_5 ①②⑦⑧ vs output_4 ④⑤⑥)
    └── 场景叙事 + 入场策略 + 归类
```

> 串行 pipeline: 1→2→3→4→5→E; 每个 task 只读前序 output, 不回指
> 
> 估值能力判断 (旧 "估值门口") = Task E Step 1 自产 flag; ×0.40 硬规则 = "不否决, 总是估值"
> 
> 交叉验 (公式价 vs 分位价) 在 Task E: output_5 (①②⑦⑧) vs output_4 (④⑤⑥)

## §0.3 设计原则

| 原则 | 含义 |
|------|------|
| g = 最佳估计 | g-baseline 算法产出 (§2.2), 不打折。保守由折扣系数处理, 不在 g 层打折 |
| 多档位 g | 熊/基准/牛/调整, 从 g 源取 min/avg/max, 不编数 (§2.5) |
| gap = 置信度 | 方法间 gap 大小 = 置信度 (§5.2), gap 来源 = 哪个口径更可信 (§5.3) |
| 周期股默认标准 | 所有标的用标准 Task 5, 仅明显不合理才 fallback 到中周期 (§5.4) |
| 折扣 = Fisher 15 | 质量(10条) × 麻烦(5条) 数 PASS → 2D 表, 不用旧 6/6 评分 (§3.2) |

## §0.4 旧框架退役清单

| 旧概念 | 状态 | 替代 |
|--------|------|------|
| 30x PE 封顶 | 移除 | 多方法去极值 + Task E 估值能力判断 + BS 生存力 (§6.1) |
| 6/6 质量评分 | 退役 | Fisher 15 固定映射 (§3.2) |
| Path 51/52/53 分叉 | 统一 | Task 5 统一估值 |
| trajectory × 0.8 公式 | 已删除 | LLM 定性调整替代 (§2.3) |
| 旧折扣系数表 (伟大×麻烦) | 替代 | Fisher 15 质量×麻烦 2D 表 (§3.2) |
| EPS CAGR 进 g | 替代 | NI CAGR (不受回购影响), EPS CAGR 作背离信号 |
| 麻烦维度数 FAIL | 替代 | 两维度对称数 PASS (borderline 不计 = 有 cost → 隐性降档) (§3.2) |
| 强牛档 (第 5 档) | 删除 | 4 档: 熊/基准/牛/调整 (§2.5) |
| 估值门口 (Task 5 Step 0) | 移交 | Task E Step 1 估值能力判断 (§6.1) |
| "Fisher < 8" | 退役 | 质量 ≤5/10 PASS (平庸档) (§6.1) |
| "主口径" 一词 | 退役 | 拆成 **DCF base** (⑦ vs ⑧) + **合理价口径** (EPS vs DCF) — 见 §0.6 |
| 唯一保留硬规则 | — | FCF-SBC < 0 → ×0.40 (不否决, 总是估值) (§3.2) |

## §0.5 文件导航 + 目录结构

| 文件 | 产出 | 依赖 | LLM 读取时机 |
|------|------|------|-------------|
| 00_framework | 全景 + 术语 + 退役清单 + 目录结构 | — | 分析预检, 必读 |
| 01_financials | SCORECARD + 正常化 EPS + per-share 估值输入 | financial_data CSV | Task 1 |
| 02_growth | g 多档位 (熊/基准/牛/调整) | output_1 + web | Task 2 |
| 03_fisher15 | 质量档 + 麻烦档 + 折扣系数 + r | output_1 (SCORECARD 损伤 + 趋势表) + output_2 (g 多档位) + web | Task 3 |
| 04_price | 粗筛命中 + 分位门 + derating | output_1 (v3.1 EPS/FCF) + output_2 (g/derating) + stock CSV + MacroTrends | Task 4 |
| 05_valuation | 合理价 + 全方法值 + 范围 + 置信度 + gap | output_1 + output_2 + output_3 + output_4 | Task 5 |
| 06_decision | 估值能力 + 入场/出场 + 安全边际 + 场景 + 策略 + 归类 | output_1 + output_2 + output_3 + output_4 + output_5 + stock CSV | Task E |
| 07_checklist | 提交前自检清单 (指针式) | 全部 | 写报告后提交前 |
| 08_reference | 固定参数 + FX + edge cases (纯查表, 不含规则) | — | 按需查表 |

### 目录结构 (产出文件)

```
ai_report/{STOCK}/
├── output_1.md    Task 1: 财务健康 (SCORECARD + EPS + FCF + BS)
├── output_2.md    Task 2: g 计算 (8源 + g-baseline + 多档位)
├── output_3.md    Task 3: Fisher 15 (15条 + 2D折扣 + r)
├── output_4.md    Task 4: 价格层 (粗筛 + 分位门 + derating)
├── output_5.md    Task 5: 估值 (多档位×方法矩阵 + gap)
└── output_e.md    Task E: 决策 (安全边际 + 入场策略 + 归类)
```

> 全局约定: **output_N.md 结构 = 对应 task doc 节序** (如 output_5 = §5.1→§5.5); 各 § 节的表格式即 output 格式, 不另设模板。
> 例外: **output_3 (Fisher 15) = 认知顺序** (调查→判定→计分→总结), 章节用语义名 (§ 指针标规则归属) — 计算 task 边算边写表格即内容, 调查 task 判定从证据长出来, 先叙事后计分 (规则 owner: 03_fisher15 §3.3 报告结构)。
> 
> 文件名与 docs Task 编号一一对应。gen_comparison 只读 output_e。

### 报告时效 (重跑触发)

产出后发生任一事件 → **全链路重跑** (旧 output 作废, 不打增量补丁):
- 财报 / 10-Q / 10-K (数据层: Task 1-2 输入变化)
- C-level 变动 / SEC / DOJ 级法律事件 (Task 3 输入变化)
- Task E 重取最新 EOD 只覆盖价格层; 上述事件动的是 1-5 的数据层

> ADBE 教训 (2026-09): 9/6 报告基于 Q2 数据, 漏 9/10 Q3 财报 (FY26 OpM 指引 35%) + 9/3 CEO 官宣 + 3/13 DOJ $150M 和解 → 三处结论级差异

## §0.6 术语表 (glossary)

> 每术语定义一次 + owner §-ID。退役词标"已退役"。改规则只动 owner 节, 引用不破。

| 术语 | 定义 | owner |
|------|------|-------|
| **合理价** | 标的内在价值的保守估计；默认 = EPS 模型 (①/②), 回购≤SBC 时 = DCF ⑦ | §5.3 |
| **满仓 / 入场价** | full-size 入场价 = 合理价 × 折扣系数 | §6.1 (Step 3) |
| **出场价** | 乐观档方法值 (EPS 路径 = ②Fisher; DCF 路径 = ⑧FCF), 无折扣 | §6.1 (Step 3) |
| **安全边际** | 1 − 现价 / 合理价 (正=便宜) | §6.1 |
| **DCF base** | DCF 的 base 口径：回购>SBC → ⑧FCF；回购≤SBC → ⑦FCF-SBC | §5.2 |
| **合理价口径** | 合理价用哪个方法：回购>SBC → EPS 模型；回购≤SBC → DCF ⑦；CapEx 超级周期 → EPS | §5.3 |
| **一阶段 / 两阶段 DCF** | g ≤3% → Gordon Growth 一阶段; g >3% → 两阶段 (N=5, g_terminal=3%) | §5.1 |
| **调整 g** | LLM 定性调整后的 g, 独立列, 不覆盖基准档; Task E 场景叙事默认用它 | §2.3 |
| **基准档** | g-baseline 均值 (§2.2 Step 3), 多档位之一 | §2.5 |
| **多档位** | 熊/基准/牛 + 调整, 从 g 源取, 不坍缩单点 | §2.5 |
| **数 PASS** | Fisher 15 计分: 质量/麻烦两维度对称数 PASS; borderline 不计 = 有 cost → 隐性降档 | §3.2 |
| **borderline** | Fisher 15 第三态 = neutral, 两维度都不计 PASS | §3.1 |
| **derating** | 5yr P/E 跨增长范式 → 低分位是假便宜, 排除分位法 | §4.3 |
| **正常化 EPS** | min(GAAP, 工具, v3.1), 保守下限 | §1.3 |
| **估值能力判断** | Task E Step 1 自产 flag: 能 / 能力圈外 / 价值陷阱 (旧 "估值门口") | §6.1 |
| **主口径** | ❌ 已退役 (一词两义致误用)。拆成 DCF base + 合理价口径 | — |
| **组合估值** | ❌ 已退役 → 合理价 (方法 gap 大时不强行合并, 见 §5.3) | — |

## §-ID 约定

- 命名: `§<文件号>.<节号>`, 如 `§5.3` = 05_valuation 第 3 节。
- 规则只在 owner 节定义一次；其他文件引用用 `§X.Y` 指针, **不复述规则**。
- 改一条规则 = 改 owner 节一处；引用方不破 → 爆炸半径小。
