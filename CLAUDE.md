# 选股分析框架

## 投资哲学

| 哲学家 | 原则 | 对应 Task |
|--------|------|-----------|
| 格雷厄姆 | 好价格（安全边际） | A + D |
| 费雪 | 好公司（GM/FCF/护城河） | B + C |
| 巴菲特 | 一次性麻烦（暂时困境） | C + D |

三者缺一不可：只有好价格=价值陷阱 | 只有好公司=买贵了 | 好公司+好价格但麻烦非一次性=结构性恶化 | 三者齐备=**最佳买点**

## 三核心公式

```
# EPS 模型（保守下限）
合理价 = 正常化 EPS × min(8.5 + g, 30)
满仓目标 = 合理价 × 折扣系数

# DCF 交叉验（并列，非替代）
DCF per share = base × (1+g)/(r−g) + net_cash/shares
  base = FCF/sh 或 (FCF−SBC)/sh
  r = 质量调整：伟大 9% / 好公司 10% / 平庸 11%
  P/FCF₀ = min((1+g)/(r−g), 30)  ← g 接近 r 时封顶 30x
```

EPS 模型是保守下限，DCF 是内在价值定义。两者并列展示，当 FCF ≈ NI 时一致，高 SBC / 高 CapEx 时背离。详见 `docs/dcf.md`。

## ABCD 工作流

| Task | 内容 | 数据源 |
|------|------|--------|
| A | 价格层（daily）— 粗筛 + FCF yield + 分位 + 安全边际 | 本地 CSV + web |
| B | 财务健康 + 正常化 EPS | 本地 CSV |
| C | 增长前瞻 + 护城河 + 消息面 | web search |
| D | 估值汇聚 + 仓位定档 | A+B+C 输出 |

A/B/C 独立可并行，D 等三者完成后汇聚。

## 分析预检（每次分析股票 / 汇总 / 校验前必须完成）

⚠️ 收到任何股票分析请求、或"汇总/校验"请求时，先用 read 工具加载以下 `docs/*.md`，全部读完才开始（不论分析一只还是汇总所有标的）：

1. `docs/analysis_framework.md` — 框架全景 + 公式 + FX + 数据源
2. `docs/task_a.md` — 价格粗筛方法
3. `docs/task_b.md` — 财务健康方法
4. `docs/normalize_eps.md` — EPS 检查清单（8 检测器）
5. `docs/task_c.md` — 增长/护城河/管理层/消息面方法
6. `docs/forward_g.md` — g 检查清单（8 源）
7. `docs/task_d.md` — 估值汇聚方法
8. `docs/discount_coefficient.md` — 折扣系数清单（7 分+5 档，含无麻烦列）
9. `docs/dcf.md` — DCF 交叉验（Gordon 单阶段 + 质量调整 r + 封顶）
10. `docs/local_data_tools.md` — 工具用法 + 数据格式速查
11. `docs/output_format.md` — 输出格式 + 存档规则
12. `docs/batches.md` — 查标的所在批次 + 元标记
13. `docs/mistakes.md` — 历史复查发现的常见错误 + 提交前自检清单

全部读完后 context 里有完整方法论 + 已知错误，再开始 ABCD 分析或汇总校验。

> ⚠️ 写完 `output_d.md` 后，**必须过一遍 `docs/mistakes.md` 第九节"提交前自检清单"**，逐项打勾再提交。任一项 ✗ = 未完成。

> **`docs/*.md`（框架文本）vs `docs/*.py`（工具）**：框架 .md 必须读（是分析/汇总/校验的 lens，不论一只还是全部）；工具 .py（normalize_eps / dcf / gen_comparison）直接调用，出问题再看源码。

## 硬规则（不读 doc 也不能违反）

- **FCF − SBC < 0 → 重麻烦 → ×0.40**，不否决、总是估值
- **g ≥ 22% → 合理 PE 封顶 30x**，不追高增长
- **合理价 = 正常化 EPS × min(8.5+g, 30)**，折扣只在满仓目标层，不进合理价
- **DCF 交叉验 = base × (1+g)/(r−g) + net_cash/sh**，与 EPS 模型并列展示，非替代
- **5 年估值分位须 ≤30%**，查不到则暂停，严禁估算
- **正常化 EPS = min(GAAP, tool, v3.1)**，只剔收益不加回亏损；EPS 负值时用恢复 EPS（剥一次性后估正常化盈利）
- **回购不进 g**，g 用业务/净利润增长

## web 数据抓取（Task A.2 分位 / Task C 同业·消息面）

- **优先用 playwright 浏览器**（`playwright_browser_navigate` + `playwright_browser_evaluate`）抓 web 数据
- **`webfetch` 易被反爬**：MacroTrends / GuruFocus / stockanalysis / Simply Wall St / Yahoo Finance 子页 等常返 Cloudflare 403（"Just a moment..."）或 403 Forbidden，webfetch 直拿会失败
- playwright 首次导航若遇 Cloudflare 挑战页，**等 5 秒**（`playwright_browser_wait_for time=5`）再读，真浏览器能过
- **拿不到则按硬规则标"暂停"**（"查不到则暂停，严禁估算"），绝不编造、绝不用旧值冒充
- 5yr 分位常用源：[MacroTrends](https://www.macrotrends.net) P/E (`/pe-ratio`) 或 P/B (`/price-book`) 页，季度历史表用 evaluate 提取，公式 `(current−low)/(high−low)` 算分位

## 分析报告（迁移期）

- **新版产出**：`ai_report/{STOCK}/output_a.md` ~ `output_d.md`
- **旧版文件**：`ai_report/{STOCK}/analysis.base.md` + `analysis.price.md`
  - 未迁移的标的：读旧文件获取历史结论（合理价/满仓/质量判定）
  - 完成 ABCD 后写 `output_*.md`，即完成迁移
- 迁移完成后旧文件手动删除

## 每日汇总 + 校验（gen_comparison）

> 触发"汇总/校验"同样按"分析预检"先读全部 `docs/*.md`（框架是 lens，汇总也需在 context），再跑下面命令。

刷完 Task A 后跑汇总+校验（一条命令，verify 是汇总前置步骤，自动跑）：

```
python3 docs/gen_comparison.py --date {YYYY-MM-DD}
```

产出（`ai_report/` 下并列两文件）：
- `comparison.{date}.md` — 决策汇总（8 章节：① 决策摘要 ② 买点详情 ③ 三 Top 10（EPS/DCF FCF/回撤信号）④ 隐藏机会 ⑤ 全量主表 ⑥ 特殊档 ⑦ DCF 信号分组 ⑧ 数据质量）
- `verify.{date}.md` — 数据校验日志（Phase 1：5 项 a+d 检查，自动化 `docs/mistakes.md` §9）

verify 规则（Flag 不阻断）：
- 违规标的主表标 `⚠` 仍保留，决策不阻断
- ⚠ 标的需重跑 Task A/D 修复源数据，再重跑 gen_comparison 至 verify 归零
- 5 检查：① 安全边际符号（1−现价/合理价 符号）② 满仓=合理价×系数 ③ 合理 PE=min(8.5+g,30) ④ g≥22 封顶（折叠进③）⑤ 伟大+无trouble→×1.0

纯 join，不重算 price-derived 量（现价/安全边际/P/E 是 Task A 的活）；唯一派生：DCF 信号标签、DCF FCF 安全边际、隐藏机会筛选。

## 代码风格

- 不用列表推导式 — 用显式 for 循环 + append
- 紧凑作用域用短变量名（sr/su/sf）
- 不写过长单行表达式 — 拆多行
- 极少注释，仅在 WHY 不明显时写
